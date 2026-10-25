# Synthetic results — no mine findings

The mathematical generator is uncalibrated. No cost savings, causality or field suitability are established.

## Executed protocol
120 fictional events; 90 training / 30 test; disjoint groups; three internal grouped folds; seven estimator seeds and a fixed holdout. Tuning uses training only.

| model | variant | rmse_mean | rmse_sd | mae_mean | r2_mean | n |
|---|---|---|---|---|---|---|
| mean_baseline | full | 22.193811 | 0.000000 | 17.548103 | -0.011057 | 7 |
| rf_tuned | full | 10.666283 | 0.186711 | 9.114162 | 0.766411 | 7 |
| rf_tuned | without_design | 11.127222 | 0.164276 | 9.579261 | 0.745805 | 7 |
| rf_tuned | without_geology | 24.032402 | 0.258192 | 19.524008 | -0.185630 | 7 |
| rf_weak | full | 19.065939 | 0.159526 | 16.157480 | 0.253802 | 7 |
| ridge_tuned | full | 8.859887 | 0.000000 | 7.405560 | 0.838873 | 7 |

## Interpretation
Ridge has lower holdout error here than the tuned random forest; no outcome is forced to favor ML complexity. The weak baseline is deliberately limited and cannot establish a research contribution. Seeds are not independent mining replications. Ablation differences are predictive and synthetic, not physical causal effects.

Same-seed predictions are exactly identical in this environment: True.

Metrics and parameters are logged to local MLflow SQLite. CSVs are portable; database artifact paths may refer to the execution directory. Rerun to create a local database. No remote tracking server is used.

No company data, budget figures, operational design recommendations, p-values or prospective field findings are supplied. Population transfer and deployment remain untested.
