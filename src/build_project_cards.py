"""Build cards for the SYNTHETIC project and run the supplied course completeness check."""
from pathlib import Path
import json,io,contextlib,zipfile
import pandas as pd
from documentation_score import score_documentation
ROOT=Path(__file__).resolve().parents[1]
def render(card,title):
    lines=['# '+title,'','**SYNTHETIC TEACHING EXERCISE — NOT MINING FINDINGS**','']
    for section,fields in card.items():
        lines += ['## '+section]
        for key,value in fields.items():lines.append(f'- **{key}:** {value}')
        lines.append('')
    return '\n'.join(lines)
def main():
    out=ROOT/'session_07';out.mkdir(exist_ok=True)
    summary=pd.read_csv(ROOT/'session_05/results_synthetic/summary_synthetic.csv')
    rf=summary[(summary.model=='rf_tuned')&(summary.variant=='full')].iloc[0]
    ridge=summary[(summary.model=='ridge_tuned')&(summary.variant=='full')].iloc[0]
    preds=pd.read_csv(ROOT/'session_05/results_synthetic/predictions_synthetic.csv')
    preds=preds[(preds.model=='rf_tuned')&(preds.variant=='full')].copy()
    data=pd.read_csv(ROOT/'data/synthetic/blasts_SYNTHETIC.csv')
    preds=preds.merge(data[['event_id','stope_id']],on='event_id',validate='many_to_one')
    preds['squared_error']=(preds.synthetic_prediction-preds.synthetic_observed)**2
    groups=(preds.groupby('stope_id').squared_error.mean()**.5).to_dict()
    per_group={k:round(float(v),6) for k,v in groups.items()}
    pd.DataFrame([{'synthetic_group':k,'rmse_fictional_mm':v} for k,v in per_group.items()]).to_csv(out/'per_group_metrics_synthetic.csv',index=False)
    card={
      'Model details':{'Name / version':'Split Optimization — synthetic RF demonstration v0.2','Owner / contact':'Repository owner: bamigdim1153; academic review/signoff UNKNOWN','Architecture':'RandomForestRegressor, 80 trees; grouped training-only grid search over depth and minimum leaf size; see per-seed parameters','License':'UNKNOWN — repository-owner licensing decision not recorded'},
      'Intended use':{'Primary intended uses':'Research-methods teaching: repeatability, baselines, seeds and ablation','Out-of-scope / misuse':'NOT FOR actual blasting design, charge recommendations, production deployment or claims about mine savings','Intended users':'The student and instructor reviewing this course exercise'},
      'Factors':{'Relevant groups / conditions':'Twelve fictional groups; four uncalibrated abstract indices','Evaluation factors':'Disjoint holdout groups and paired seeds; grouping does not reproduce mine geology'},
      'Metrics':{'Performance measures':'MAE, RMSE and R2 for a fictional target called p80_demo_mm','Decision thresholds':'No operational acceptance threshold or recommended P80','Variation approach':'Mean ± sample SD across seven estimator seeds; fixed holdout; not independent mine replications'},
      'Evaluation data':{'Datasets':'30 fictional rows in the last three groups; no company or prospective observations','Preprocessing':'Held-out data untouched during fitting/tuning; train/test group IDs are disjoint'},
      'Training data':{'Datasets':'90 fictional rows in nine groups from the 120-row generator','Preprocessing':'Imputation fitted in training; three-fold GroupKFold grid search; Ridge comparator additionally scales inside its pipeline'},
      'Quantitative analyses':{'Overall results':f"RF RMSE={rf.rmse_mean:.6f} ± {rf.rmse_sd:.6f}; MAE={rf.mae_mean:.6f}; mean R2={rf.r2_mean:.6f}. All units are fictional.",'Per-group disaggregated results':json.dumps(per_group,sort_keys=True),'Comparator and interpretation':f"Ridge holdout RMSE={ridge.rmse_mean:.6f}; lower than RF here. RF is an ablation demonstration, not a preselected final winner. See all seven seeds and paired deltas."},
      'Ethical considerations':{'Risks':'Misrepresenting synthetic outcomes as empirical mine evidence; treating a completeness score as validation','Mitigations':'Origin labels, separate real-project status, explicit unknowns, no operational parameter conversion'},
      'Caveats and recommendations':{'Caveats':'Invented generator, one holdout, small synthetic sample, no real cost/production/safety validation','Recommendations':'Instructor acceptance and student review required; create a separate authorized real-data evaluation before any mine-use claim'}
    }
    sheet={
      'Motivation':{'Purpose':'Demonstrate research methods without reading or publishing company records','Created by / funded by':'Mathematical generator prepared with AI assistance; no company funding claim'},
      'Composition':{'What instances represent':'120 fictional event records, twelve abstract groups, four indices and one invented target','Labels':'Every row data_origin=SYNTHETIC','Sample vs population':'Not a sample from the mine and not a population estimate','Missing data':'None intentionally generated; this does not describe the company dataset'},
      'Collection process':{'How collected':'No field collection: deterministic pseudorandom generation with seed20261024; formula and hash in data/synthetic/MANIFEST.json','Timeframe':'Simulation generated for this course portfolio; not a six-month field study','Consent / ethics':'No people or company records; permission for any future real-data use remains UNKNOWN'},
      'Preprocessing / cleaning / labeling':{'Steps':'Generator rounds values; fixed90/30 group-disjoint split; learning transformations inside training','Raw data available':'The generated CSV, code and hash are included; no raw mine images exist in this dataset'},
      'Uses':{'Appropriate uses':'Teaching, code verification and labelled methodological demonstrations','Should NOT be used for':'Operational blast decisions, real-mine P80/cost predictions, thesis savings claims or causal physical conclusions'},
      'Distribution':{'How distributed':'This repository contains only synthetic records and public-course result artifacts','License / restrictions':'Repository-owner license decision UNKNOWN; public availability alone is not a company-data license'},
      'Maintenance':{'Maintainer':'Repository owner; institutional endorsement UNKNOWN','Update plan':'Regenerate from code; any generator change requires a new hash/version and evaluation'}
    }
    (out/'model_card.json').write_text(json.dumps(card,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (out/'datasheet.json').write_text(json.dumps(sheet,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (out/'model_card.md').write_text(render(card,'Model Card — synthetic project'),encoding='utf-8')
    (out/'datasheet.md').write_text(render(sheet,'Datasheet — synthetic project'),encoding='utf-8')
    stream=io.StringIO()
    with contextlib.redirect_stdout(stream):passed,total=score_documentation(card,sheet)
    assert (passed,total)==(8,8)
    text=stream.getvalue()+'\nLIMIT: This is the supplied structural/keyword completeness check. It does not validate performance, permissions, originality, safety or assessment acceptance.\n'
    (out/'documentation_score.txt').write_text(text,encoding='utf-8')
    (out/'documentation_score.json').write_text(json.dumps({'passed':passed,'total':total,'check_source':'Session7 Exercise6 supplied function','data_origin':'SYNTHETIC','limitation':'Completeness only, not real-data or field validation'},indent=2)+'\n',encoding='utf-8')
    bundle=out/'session7_deliverable.zip'
    include=[out/'model_card.md',out/'datasheet.md',out/'model_card.json',out/'datasheet.json',out/'documentation_score.txt',out/'documentation_score.json',out/'per_group_metrics_synthetic.csv',ROOT/'requirements.txt',ROOT/'requirements-lock.txt',ROOT/'data/synthetic/blasts_SYNTHETIC.csv',ROOT/'data/synthetic/MANIFEST.json',ROOT/'src/generate_synthetic.py',ROOT/'src/run_experiment.py',ROOT/'src/build_project_cards.py',ROOT/'src/documentation_score.py',ROOT/'session_05/README.md']
    include+=list((ROOT/'session_05/results_synthetic').glob('*.csv'))+list((ROOT/'session_05/results_synthetic').glob('*.png'))+list((ROOT/'session_05/results_synthetic').glob('*.json'))+list((ROOT/'session_05/results_synthetic').glob('*.md'))
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        for p in include:z.write(p,p.relative_to(ROOT))
    print(text.replace('✓','PASS').replace('✗','FAIL'));print('Saved own-project synthetic cards and reproducibility bundle.')
if __name__=='__main__':main()
