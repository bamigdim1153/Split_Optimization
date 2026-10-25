from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True);p.add_argument('--git',default='git');a=p.parse_args()
base=Path(a.workspace).resolve()
if base.exists() and any(base.iterdir()):raise ValueError('Use a new empty workspace; existing work is never removed.')
base.mkdir(parents=True,exist_ok=True)
project,remote,clone=[base/x for x in ['producer','local_remote','fresh_clone']]
project.mkdir();remote.mkdir();commands=[]
env=dict(os.environ,DVC_NO_ANALYTICS='true',PYTHONIOENCODING='utf-8',DVC_SITE_CACHE_DIR=str(base/'site_cache'),DVC_SYSTEM_CONFIG_DIR=str(base/'system_config'),DVC_GLOBAL_CONFIG_DIR=str(base/'global_config'))
def run(args,cwd):
 r=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True)
 commands.append({'command':[str(x).replace(str(base),'<workspace>').replace(sys.executable,'python') for x in args],'exit_code':r.returncode})
 if r.returncode:raise RuntimeError(r.stdout+r.stderr)
 return r.stdout
def dvc(*args,cwd=project):return run([sys.executable,'-m','dvc',*args],cwd)
run([a.git,'init','-b','main'],project);dvc('init','--no-scm')
root=Path(__file__).resolve().parents[1]
source=root/'data/synthetic/blasts_SYNTHETIC.csv'
shutil.copyfile(source,project/'synthetic_blasts.csv')
dvc('add','synthetic_blasts.csv');dvc('remote','add','-d','local-demo',str(remote));dvc('push')
(project/'.gitignore').write_text('synthetic_blasts.csv\n.dvc/cache/\n.dvc/tmp/\n',encoding='utf-8')
run([a.git,'add','.gitignore','.dvc/config','synthetic_blasts.csv.dvc'],project)
run([a.git,'-c','user.name=Course Automation - AI assisted','-c','user.email=course-automation@invalid','commit','-m','Track synthetic data for DVC roundtrip'],project)
from dulwich import porcelain
porcelain.clone(str(project), str(clone), checkout=True)
commands.append({'command':['dulwich.porcelain.clone','<workspace>/producer','<workspace>/fresh_clone'],'exit_code':0})
assert not (clone/'synthetic_blasts.csv').exists()
dvc('pull',cwd=clone)
digest=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
result={'data_origin':'SYNTHETIC','remote_type':'local filesystem','fresh_clone_initially_missing_data':True,'source_sha256':digest(source),'restored_sha256':digest(clone/'synthetic_blasts.csv'),'hashes_match':digest(source)==digest(clone/'synthetic_blasts.csv'),'dvc_version':dvc('version').splitlines()[0],'commands':commands,'limitation':'Local roundtrip; not cloud backup or company-data authorization.'}
assert result['hashes_match']
out=root/'session_05/dvc_results';out.mkdir(exist_ok=True)
(out/'roundtrip.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
shutil.copyfile(project/'synthetic_blasts.csv.dvc',out/'synthetic_blasts.csv.dvc')
print(json.dumps({k:v for k,v in result.items() if k!='commands'},indent=2))
