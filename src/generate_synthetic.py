"""Generate uncalibrated SYNTHETIC teaching data; never operational blast designs."""
from pathlib import Path
import csv, random, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
def main():
    rng=random.Random(20261024)
    path=ROOT/'data/synthetic/blasts_SYNTHETIC.csv'
    path.parent.mkdir(parents=True,exist_ok=True)
    fields=['data_origin','event_id','stope_id','time_order','geology_index','strength_index','moisture_index','abstract_design_index','p80_demo_mm']
    rows=[]
    for i in range(120):
        g,s,h,d=[rng.uniform(0,1) for _ in range(4)]
        y=150+70*g+45*s+60*(d-.5)**2+30*h+20*g*s+rng.gauss(0,6)
        rows.append(['SYNTHETIC',f'DEMO_{i+1:03}',f'GROUP_{i//10+1:02}',i+1,*[round(x,6) for x in [g,s,h,d]],round(y,6)])
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(fields);w.writerows(rows)
    manifest={'data_origin':'SYNTHETIC','n':120,'generator_seed':20261024,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'formula':'150+70g+45s+60(d-0.5)^2+30h+20gs+N(0,6)','warning':'Invented, uncalibrated values. The abstract design index cannot be converted to operational parameters. No mine P80 or costs are inferred.'}
    (path.parent/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(manifest))
if __name__=='__main__':main()
