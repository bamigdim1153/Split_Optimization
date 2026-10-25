from pathlib import Path
import csv,json,re,ast,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    errors=[]
    for p in ROOT.rglob('*.md'):
        if '.git' in p.parts:continue
        for link in re.findall(r'\[[^]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' not in link and not (p.parent/link).exists():errors.append((str(p.relative_to(ROOT)),link))
    assert not errors,errors
    for p in (ROOT/'src').glob('*.py'):ast.parse(p.read_text(encoding='utf-8-sig'))
    for name in ['session_06_english.ipynb','session_07_english.ipynb']:
        nb=json.loads((ROOT/'notebooks'/name).read_text(encoding='utf-8'))
        cells=[c for c in nb['cells'] if c['cell_type']=='code']
        assert all(c['execution_count'] is not None for c in cells)
        assert not any(o.get('output_type')=='error' for c in cells for o in c['outputs'])
        for c in cells:ast.parse(''.join(c['source']))
    with (ROOT/'data/synthetic/blasts_SYNTHETIC.csv').open(encoding='utf-8') as f:rows=list(csv.DictReader(f))
    assert len(rows)==120 and {r['data_origin'] for r in rows}=={'SYNTHETIC'}
    assert len({r['event_id'] for r in rows})==120
    data_hash=hashlib.sha256((ROOT/'data/synthetic/blasts_SYNTHETIC.csv').read_bytes()).hexdigest()
    assert json.loads((ROOT/'data/synthetic/MANIFEST.json').read_text())['sha256']==data_hash
    with (ROOT/'session_05/results_synthetic/split_synthetic.csv').open(encoding='utf-8') as f:split=list(csv.DictReader(f))
    train={r['stope_id'] for r in split if r['partition']=='train'};test={r['stope_id'] for r in split if r['partition']=='test'}
    assert train.isdisjoint(test) and len(train)==9 and len(test)==3
    with (ROOT/'session_05/results_synthetic/runs_synthetic.csv').open(encoding='utf-8') as f:runs=list(csv.DictReader(f))
    assert len(runs)==42 and len({r['seed'] for r in runs})==7
    assert json.loads((ROOT/'session_05/results_synthetic/repeatability.json').read_text())['predictions_identical']
    score=json.loads((ROOT/'session_07/documentation_score.json').read_text());assert(score['passed'],score['total'])==(8,8)
    with zipfile.ZipFile(ROOT/'session_07/session7_deliverable.zip') as z:assert z.testzip() is None
    assert abs(sum(w*s for w,s in zip([30,20,25,15,10],[5,4,3,5,4]))/100-4.2)<1e-9
    report={'local_links':'PASS','python_and_notebook_syntax':'PASS','executed_course_notebooks':'PASS','synthetic_origin_hash_and_ids':'PASS','group_disjoint_holdout':'PASS','seven_seeds_42_runs':'PASS','repeatability':'PASS','documentation_check':'8/8; completeness only','private_company_records_included':False,'docker_run':'NOT PERFORMED','dvc_remote_test':'NOT PERFORMED','systematic_prisma':'PENDING'}
    (ROOT/'control/verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
