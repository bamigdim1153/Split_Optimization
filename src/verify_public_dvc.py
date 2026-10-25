from pathlib import Path
from dulwich import porcelain
import subprocess,sys,os,json,hashlib
import argparse
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True);a=p.parse_args()
base=Path(a.workspace).resolve();base.mkdir(exist_ok=False)
clone=base/'fresh_clone'
porcelain.clone('https://github.com/bamigdim1153/Split_Optimization.git',str(clone),checkout=True)
data=clone/'data/versioned/blasts_SYNTHETIC.csv';assert not data.exists()
env=dict(os.environ,DVC_NO_ANALYTICS='true',DVC_SITE_CACHE_DIR=str(base/'site-cache'),DVC_SYSTEM_CONFIG_DIR=str(base/'system'),DVC_GLOBAL_CONFIG_DIR=str(base/'global'),PYTHONIOENCODING='utf-8')
r=subprocess.run([sys.executable,'-m','dvc','pull'],cwd=clone,env=env,capture_output=True,text=True)
print(r.stdout,r.stderr)
if r.returncode:raise RuntimeError('DVC pull failed: '+str(r.returncode))
h=hashlib.sha256(data.read_bytes()).hexdigest();assert h=='7ebd3c2edcefc67024d9ab4ca9f09332615573930c6e93e3c70043f43dc97332'
from dulwich.repo import Repo
head=Repo(str(clone)).head().decode()
result={'date':'2026-10-25','repository':'https://github.com/bamigdim1153/Split_Optimization','commit':head,'clone_implementation':'Dulwich pure-Python Git clone','initially_missing_versioned_data':True,'dvc_pull_exit_code':r.returncode,'remote':'public HTTP GitHub raw mirror','restored_sha256':h,'matches_tracked_synthetic_copy':data.read_bytes()==(clone/'data/synthetic/blasts_SYNTHETIC.csv').read_bytes(),'data_origin':'SYNTHETIC','limitation':'Fresh isolated workspace on this machine; not an independent human reproduction.'}
out=Path(__file__).resolve().parents[1]/'session_05/dvc_results/public_stranger_test.json';out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
