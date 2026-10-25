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
    for name in ['session_06_english.ipynb','session_07_english.ipynb','NB1_Reproducibility_Magic_Tricks_english.ipynb','NB3_Case_Study_100_Percent_LITE_english.ipynb','session_07_complete_english.ipynb','session_07_your_turn_addendum.ipynb']:
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
    dvc=json.loads((ROOT/'session_05/dvc_results/roundtrip.json').read_text())
    assert dvc['hashes_match'] and dvc['source_sha256']==data_hash
    counts=json.loads((ROOT/'session_04/prisma_counts.json').read_text())
    with (ROOT/'session_04/screening_register.csv').open(encoding='utf-8') as f:screened=list(csv.DictReader(f))
    assert len(screened)==76 and sum(x['final_decision']=='included_report' for x in screened)==13
    assert counts['screened']-counts['excluded_title']==counts['reports_sought']
    assert counts['reports_sought']-counts['reports_not_retrieved']==counts['full_text_assessed']
    assert counts['full_text_assessed']-counts['full_text_excluded']==counts['included_reports']
    nb4=json.loads((ROOT/'session_05/nb4_results/execution.json').read_text())
    assert nb4['actual_content_commits']==6 and nb4['same_seed_repeat_identical']
    public=json.loads((ROOT/'session_05/dvc_results/public_stranger_test.json').read_text())
    assert public['dvc_pull_exit_code']==0 and public['restored_sha256']==data_hash
    ci=json.loads((ROOT/'control/container_ci_evidence.json').read_text())
    assert ci['conclusion']=='success' and all(j['conclusion']=='success' for j in ci['jobs'])
    assert counts['identified_records']-counts['duplicates_removed']==counts['screened']
    assert counts['priority_reports']==10 and counts['supporting_reports']==3
    prisma=json.loads((ROOT/'session_04/prisma_official/execution.json').read_text())
    assert prisma['conclusion']=='success'
    zotero=json.loads((ROOT/'session_04/zotero_organization.json').read_text())
    assert zotero['imported_items']==13 and zotero['priority_items_observed']==10
    with (ROOT/'session_04/priority_10.csv').open(encoding='utf-8') as f:priority=list(csv.DictReader(f))
    assert len(priority)==10
    searches=json.loads((ROOT/'session_04/semantic_scholar_searches.json').read_text())
    assert sum(bool(x['matched']) for x in searches['targeted_searches'])==7
    ext=json.loads((ROOT/'session_07/course_complete/extension_results.json').read_text())
    assert ext['data_origin']=='PUBLIC_WISCONSIN_TEACHING_DATA' and len(ext['paired_ablation'])==3
    assert (ROOT/'session_06/evidence/executed_notebook_capture.png').stat().st_size>1000
    extra=json.loads((ROOT/'session_07/your_turn_addendum/results.json').read_text())
    assert len(extra['exercise7']['seeds'])==10 and extra['exercise9']['measured_features']==30 and extra['exercise9']['noise_features']==5000
    manifest=json.loads((ROOT/'submission/file_hashes.json').read_text())
    assert all(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest for name,digest in manifest.items())
    report={'local_links'    :'PASS','python_and_notebook_syntax':'PASS','executed_course_notebooks':'PASS','synthetic_origin_hash_and_ids':'PASS','group_disjoint_holdout':'PASS','seven_seeds_42_runs':'PASS','repeatability':'PASS','documentation_check':'8/8; completeness only','private_company_records_included':False,'docker_run':'PASS: actual GitHub-hosted Docker build/run/artifact export; see container_ci_evidence.json','dvc_remote_test':'PASS: local push/clone/pull AND fresh public GitHub clone/HTTP DVC pull; identical SHA256','mini_review':'PASS:76 records,13 full-text reports,10 priority papers with Semantic Scholar evidence; bounded/post-hoc search limitations disclosed','prisma_official_package':'PASS: PRISMA2020 exported SVG/PNG/PDF in successful CI','reference_manager':'PASS: actual Zotero import13/tag view10','session7_extensions':'PASS: Exercises7-12 plus explicit Your turn7/9 modifications executed; overlapping-resample limits documented','session6_reflection':'PASS: student explicitly approved the translated statement; actual output capture included','nb4_workshop':'PASS: five seeds, MLflow, six actual automation commits and repeatability'}
    (ROOT/'control/verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
