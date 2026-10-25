"""Execute the supplied NB4 workflow in a NEW isolated directory; never alter global Git settings."""
from pathlib import Path
import sys,os,argparse,subprocess,json,hashlib,platform,importlib.util,importlib.metadata as md
import pandas as pd
from sklearn.datasets import load_breast_cancer
import mlflow
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--workspace',required=True);ap.add_argument('--git',default='git');args=ap.parse_args()
    work=Path(args.workspace).resolve()
    if work.exists() and any(work.iterdir()):raise ValueError('Choose a new empty workspace; existing data will not be deleted.')
    work.mkdir(parents=True,exist_ok=True);(work/'data').mkdir();(work/'src').mkdir()
    env=dict(os.environ,PYTHONHASHSEED='0',GIT_PYTHON_REFRESH='quiet',OMP_NUM_THREADS='1')
    def git(*command):return subprocess.run([args.git,*command],cwd=work,env=env,capture_output=True,text=True,check=True).stdout.strip()
    def save(path,text):(work/path).write_text(text,encoding='utf-8')
    def commit(message,*files):
        git('add',*files);git('commit','-m',message)
    git('init','-b','main');git('config','--local','user.name','Course Automation - AI assisted');git('config','--local','user.email','course-automation@invalid')
    save('.gitignore','__pycache__/\n*.db\nmlruns/\n');save('.gitattributes','* text=auto eol=lf\n');save('README.md','# NB4 public-data teaching workflow\n\nPrepared with AI assistance; not company data or prior student development.\n')
    commit('Initialize isolated public teaching project','README.md','.gitignore','.gitattributes')
    load_breast_cancer(as_frame=True).frame.to_csv(work/'data/breast_cancer.csv',index=False,lineterminator='\n')
    commit('Record the public Wisconsin dataset','data/breast_cancer.csv')
    save('src/train.py',(ROOT/'session_05/nb4_results/train.py').read_text(encoding='utf-8'))
    commit('Implement the supplied seeded leakage-free training recipe','src/train.py')
    cmd=[sys.executable,'src/train.py','--seed','42']
    a=subprocess.run(cmd,cwd=work,env=env,capture_output=True,text=True,check=True).stdout.strip()
    b=subprocess.run(cmd,cwd=work,env=env,capture_output=True,text=True,check=True).stdout.strip()
    assert a==b
    repeated={'same_seed_output_identical':True,'output':json.loads(a),'python':platform.python_version(),'launch_hash_seed':'0'}
    save('repeatability.json',json.dumps(repeated,indent=2)+'\n');commit('Verify two fresh-interpreter runs with the same seed','repeatability.json')
    spec=importlib.util.spec_from_file_location('nb4_training',work/'src/train.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    previous=Path.cwd();os.chdir(work)
    try:
        mlflow.set_tracking_uri('sqlite:///'+(work/'mlflow.db').as_posix());mlflow.set_experiment('NB4_public_teaching')
        results=[];code_commit=git('rev-parse','HEAD')
        for seed in [0,1,2,3,42]:
            value=module.main(seed)
            with mlflow.start_run(run_name=f'public-seed-{seed}'):
                mlflow.log_params({'seed':seed,'data_md5':value['data_md5'],'git_commit':code_commit,'model':'logistic_regression','data_origin':'PUBLIC_TEACHING_DATA'})
                mlflow.log_metrics({'accuracy_mean':value['accuracy_mean'],'accuracy_sd':value['accuracy_sd']})
            results.append({**value,'git_commit':code_commit})
        frame=pd.DataFrame(results);frame.to_csv(work/'results_summary.csv',index=False,lineterminator='\n')
    finally:os.chdir(previous)
    commit('Record all five seeds and their code provenance','results_summary.csv')
    deps='\n'.join(p+'=='+md.version(p) for p in ['numpy','pandas','scikit-learn'])+'\n';save('requirements.txt',deps)
    save('README.md','# NB4 public teaching workflow\n\nAI-assisted execution of the supplied workflow; no mining claims.\n\nRun `python src/train.py --seed 42` after installing requirements.txt.\n\nExpected output:\n```json\n'+a+'\n```\n\nAll five seeds are retained in results_summary.csv.\n')
    commit('Document direct dependencies and verified expected output','README.md','requirements.txt')
    evidence=ROOT/'session_05/nb4_results';frame.to_csv(evidence/'results_summary.csv',index=False,lineterminator='\n')
    (evidence/'repeatability.json').write_text(json.dumps(repeated,indent=2)+'\n',encoding='utf-8')
    history=git('log','--reverse','--format=%H|%s')
    (evidence/'actual_git_history.txt').write_text(history+'\n',encoding='utf-8')
    result={'public_data':True,'same_seed_repeat_identical':True,'number_of_seeds':5,'mean_of_seed_cv_means':float(frame.accuracy_mean.mean()),'sample_sd_of_seed_cv_means':float(frame.accuracy_mean.std(ddof=1)),'actual_content_commits':len(history.splitlines()),'note':'These are actual new automated workshop commits, not historical student work.'}
    (evidence/'execution.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    git('bundle','create',str((evidence/'workshop.bundle').resolve()),'--all')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
