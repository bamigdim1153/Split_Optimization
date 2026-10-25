from pathlib import Path
import os
os.environ.setdefault('GIT_PYTHON_REFRESH', 'quiet')
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import csv, json, hashlib, platform, importlib.metadata as md
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GroupKFold, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'session_05/results_synthetic'
FEATURES = ['geology_index', 'strength_index', 'moisture_index', 'abstract_design_index']
SEEDS = [7, 13, 21, 42, 67, 89, 101]

def build(kind, seed):
    if kind == 'mean_baseline':
        return Pipeline([('impute', SimpleImputer()), ('model', DummyRegressor(strategy='mean'))])
    if kind == 'ridge_tuned':
        base = Pipeline([('impute', SimpleImputer()), ('scale', StandardScaler()), ('model', Ridge())])
        grid = {'model__alpha': [0.1, 1.0, 10.0, 100.0]}
    elif kind == 'rf_weak':
        return Pipeline([('impute', SimpleImputer()), ('model', RandomForestRegressor(n_estimators=80, max_depth=1, random_state=seed, n_jobs=1))])
    else:
        base = Pipeline([('impute', SimpleImputer()), ('model', RandomForestRegressor(n_estimators=80, random_state=seed, n_jobs=1))])
        grid = {'model__max_depth': [3, None], 'model__min_samples_leaf': [1, 4]}
    return GridSearchCV(base, grid, scoring='neg_root_mean_squared_error', cv=GroupKFold(3), n_jobs=1, refit=True)

def fit(kind, seed, cols, train):
    estimator = build(kind, seed)
    kw = {'groups': train['stope_id']} if isinstance(estimator, GridSearchCV) else {}
    estimator.fit(train[cols], train['p80_demo_mm'], **kw)
    return estimator

def evaluate(est, cols, test):
    y = test['p80_demo_mm']
    p = est.predict(test[cols])
    return (p, {'mae': float(mean_absolute_error(y, p)), 'rmse': float(np.sqrt(mean_squared_error(y, p))), 'r2': float(r2_score(y, p))})

def table(df, columns):
    lines = ['| ' + ' | '.join(columns) + ' |', '|' + '|'.join(['---'] * len(columns)) + '|']
    for _, row in df.iterrows():
        vals = [f'{row[c]:.6f}' if isinstance(row[c], (float, np.floating)) else str(row[c]) for c in columns]
        lines.append('| ' + ' | '.join(vals) + ' |')
    return '\n'.join(lines)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    path = ROOT / 'data/synthetic/blasts_SYNTHETIC.csv'
    df = pd.read_csv(path)
    if len(df) != 120 or set(df['data_origin']) != {'SYNTHETIC'} or (not df['event_id'].is_unique):
        raise ValueError('Only the 120-row SYNTHETIC dataset is allowed here; do not pass company data.')
    if df[FEATURES + ['p80_demo_mm']].isna().any().any():
        raise ValueError('The synthetic dataset contains unexpected missing values.')
    data_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    df = df.sort_values('time_order').reset_index(drop=True)
    train = df.iloc[:90].copy()
    test = df.iloc[90:].copy()
    assert set(train.stope_id).isdisjoint(test.stope_id)
    for a, b in GroupKFold(3).split(train, groups=train.stope_id):
        assert set(train.iloc[a].stope_id).isdisjoint(train.iloc[b].stope_id)
    split = df[['event_id', 'stope_id', 'time_order']].copy()
    split['partition'] = ['train'] * 90 + ['test'] * 30
    split.to_csv(OUT / 'split_synthetic.csv', index=False)
    db = OUT / 'mlflow_SYNTHETIC.db'
    mlflow.set_tracking_uri('sqlite:///' + db.as_posix())
    mlflow.set_experiment('SYNTHETIC_Loveleen')
    rows = []
    predictions = []
    cv = []
    variants = {'full': FEATURES, 'without_geology': ['abstract_design_index'], 'without_design': ['geology_index', 'strength_index', 'moisture_index']}
    for seed in SEEDS:
        for kind in ['mean_baseline', 'ridge_tuned', 'rf_weak', 'rf_tuned']:
            for variant, cols in variants.items():
                if kind != 'rf_tuned' and variant != 'full':
                    continue
                est = fit(kind, seed, cols, train)
                pred, metrics = evaluate(est, cols, test)
                params = getattr(est, 'best_params_', {})
                row = {'data_origin': 'SYNTHETIC', 'seed': seed, 'model': kind, 'variant': variant, **metrics, 'parameters': json.dumps(params, sort_keys=True)}
                rows.append(row)
                for event, actual, p in zip(test.event_id, test.p80_demo_mm, pred):
                    predictions.append({'data_origin': 'SYNTHETIC', 'seed': seed, 'model': kind, 'variant': variant, 'event_id': event, 'synthetic_observed': actual, 'synthetic_prediction': p})
                if isinstance(est, GridSearchCV):
                    for j, par in enumerate(est.cv_results_['params']):
                        cv.append({'seed': seed, 'model': kind, 'variant': variant, 'parameters': json.dumps(par, sort_keys=True), 'rmse_cv_train': -float(est.cv_results_['mean_test_score'][j])})
                with mlflow.start_run(run_name=f'SYNTHETIC_{kind}_{variant}_{seed}'):
                    mlflow.set_tags({'data_origin': 'SYNTHETIC', 'intended_use': 'Teaching exercise, not mining findings'})
                    mlflow.log_params({'seed': seed, 'model': kind, 'variant': variant, 'n_train': 90, 'n_test': 30, 'dataset_sha256': data_hash, 'features': ','.join(cols), 'best_parameters': json.dumps(params, sort_keys=True)})
                    mlflow.log_metrics(metrics)
    runs = pd.DataFrame(rows)
    runs.to_csv(OUT / 'runs_synthetic.csv', index=False)
    pd.DataFrame(predictions).to_csv(OUT / 'predictions_synthetic.csv', index=False)
    pd.DataFrame(cv).to_csv(OUT / 'training_only_tuning.csv', index=False)
    summary = runs.groupby(['model', 'variant']).agg(rmse_mean=('rmse', 'mean'), rmse_sd=('rmse', 'std'), mae_mean=('mae', 'mean'), r2_mean=('r2', 'mean'), n=('seed', 'size')).reset_index()
    summary.to_csv(OUT / 'summary_synthetic.csv', index=False)
    ab = runs[runs.model == 'rf_tuned'].pivot(index='seed', columns='variant', values='rmse').reset_index()
    for v in ['without_geology', 'without_design']:
        ab['delta_' + v] = ab[v] - ab['full']
    ab.to_csv(OUT / 'paired_ablation_synthetic.csv', index=False)
    a = fit('rf_tuned', 42, FEATURES, train)
    b = fit('rf_tuned', 42, FEATURES, train)
    pa, ma = evaluate(a, FEATURES, test)
    pb, mb = evaluate(b, FEATURES, test)
    repeat = {'data_origin': 'SYNTHETIC', 'seed': 42, 'predictions_identical': bool(np.array_equal(pa, pb)), 'metrics_identical': ma == mb, 'predictions_sha256_a': hashlib.sha256(pa.tobytes()).hexdigest(), 'predictions_sha256_b': hashlib.sha256(pb.tobytes()).hexdigest()}
    assert repeat['predictions_identical'] and repeat['metrics_identical']
    (OUT / 'repeatability.json').write_text(json.dumps(repeat, indent=2) + '\n', encoding='utf-8')
    env = {'python': platform.python_version(), 'system': platform.system(), 'packages': {p: md.version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'matplotlib', 'mlflow-skinny']}, 'dataset_sha256': data_hash, 'seeds': SEEDS, 'train': 90, 'test': 30, 'training_groups': 9, 'test_groups': 3, 'data_origin': 'SYNTHETIC'}
    (OUT / 'environment.json').write_text(json.dumps(env, indent=2) + '\n', encoding='utf-8')
    models = summary[summary.variant == 'full']
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(models.model, models.rmse_mean, yerr=models.rmse_sd, capsize=5, color='#24566f')
    ax.set_ylabel('RMSE (fictional mm)')
    ax.set_title('SYNTHETIC — comparison; bars: SD across seeds')
    ax.tick_params(axis='x', rotation=15)
    fig.tight_layout()
    fig.savefig(OUT / 'comparison_synthetic.png', dpi=160)
    plt.close(fig)
    full = summary[summary.model == 'rf_tuned']
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(full.variant, full.rmse_mean, yerr=full.rmse_sd, capsize=5, color='#90672b')
    ax.set_ylabel('RMSE (fictional mm)')
    ax.set_title('SYNTHETIC — ablation: refit with the same tuning budget')
    fig.tight_layout()
    fig.savefig(OUT / 'ablation_synthetic.png', dpi=160)
    plt.close(fig)
    report = '# Synthetic results — no mine findings\n\n'
    report += 'The mathematical generator is uncalibrated. No cost savings, causality or field suitability are established.\n\n'
    report += '## Executed protocol\n120 fictional events; 90 training / 30 test; disjoint groups; three internal grouped folds; seven estimator seeds and a fixed holdout. Tuning uses training only.\n\n'
    report += table(summary, ['model', 'variant', 'rmse_mean', 'rmse_sd', 'mae_mean', 'r2_mean', 'n'])
    report += '\n\n## Interpretation\nRidge has lower holdout error here than the tuned random forest; no outcome is forced to favor ML complexity. The weak baseline is deliberately limited and cannot establish a research contribution. Seeds are not independent mining replications. Ablation differences are predictive and synthetic, not physical causal effects.\n'
    report += '\nSame-seed predictions are exactly identical in this environment: ' + str(repeat['predictions_identical']) + '.\n'
    report += '\nMetrics and parameters are logged to local MLflow SQLite. CSVs are portable; database artifact paths may refer to the execution directory. Rerun to create a local database. No remote tracking server is used.\n'
    report += '\nNo company data, budget figures, operational design recommendations, p-values or prospective field findings are supplied. Population transfer and deployment remain untested.\n'
    (OUT / 'REPORT_SYNTHETIC.md').write_text(report, encoding='utf-8')
    print(summary.to_string(index=False))
    print('REPEATABILITY', repeat['predictions_identical'])
    print('SYNTHETIC: no result describes the mine.')
if __name__ == '__main__':
    main()
