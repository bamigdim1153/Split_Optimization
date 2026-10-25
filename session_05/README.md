# Session 5 — Reproducible SYNTHETIC pipeline

The 120 rows are invented mathematical records, not the company's historical blasts. Four abstract indices and an uncalibrated numeric target demonstrate grouped evaluation; there is no conversion to operational charge/layout parameters.

Run `python src/generate_synthetic.py` then `python src/run_experiment.py` from the repository root. Exact package versions are in requirements-lock.txt. Local MLflow/SQLite records parameters, metrics and dataset hash; no remote tracking service is used. SQLite files are excluded from Git; portable CSV/JSON evidence is included.

The experiment uses a fixed 90/30 disjoint-group holdout, three grouped internal folds, training-only preprocessing/tuning, seven estimator seeds, mean and sample SD, paired ablations and an exact same-seed repeatability check. Read results_synthetic/REPORT_SYNTHETIC.md and all runs; do not select a lucky seed or claim that outperforming a deliberately weak baseline establishes a thesis contribution.

Dockerfile is prepared but not executed. DVC remote/clone/pull and running the earlier NB1/NB3/NB4 originals remain separate requirements where applicable. The newly added Sessions 6 and 7 notebooks are now available and executed in English teaching copies; their evidence is in the corresponding session folders.
