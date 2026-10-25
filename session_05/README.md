# Session 5 — Reproducible SYNTHETIC pipeline

The 120 rows are invented mathematical records, not the company's historical blasts. Four abstract indices and an uncalibrated numeric target demonstrate grouped evaluation; there is no conversion to operational charge/layout parameters.

Run `python src/generate_synthetic.py` then `python src/run_experiment.py` from the repository root. Exact package versions are in requirements-lock.txt. Local MLflow/SQLite records parameters, metrics and dataset hash; no remote tracking service is used. SQLite files are excluded from Git; portable CSV/JSON evidence is included.

The experiment uses a fixed 90/30 disjoint-group holdout, three grouped internal folds, training-only preprocessing/tuning, seven estimator seeds, mean and sample SD, paired ablations and an exact same-seed repeatability check. Read results_synthetic/REPORT_SYNTHETIC.md and all runs; do not select a lucky seed or claim that outperforming a deliberately weak baseline establishes a thesis contribution.

## Additional executed course notebooks

- [NB1 English executed notebook](../notebooks/NB1_Reproducibility_Magic_Tricks_english.ipynb): seed variation and noise/leakage demonstration; [results](nb1_results/results.json).
- [NB3 English executed notebook](../notebooks/NB3_Case_Study_100_Percent_LITE_english.ipynb): the instructor's **invented** cancer-paper example, not a real publication; [results](nb3_results/results.json). Seed12 gives 100%, but the 20-seed mean is 0.968531; 41/143 test rows have a patient ID also present in training in the leakage demonstration.
- [NB4 portable driver](../src/run_nb4_workshop.py), adapted from the supplied notebook for a local isolated workspace: actual MLflow five-seed results, exact same-seed repetition, and six actual content-bearing automated commits. [Evidence](nb4_results/execution.json), [history](nb4_results/actual_git_history.txt), [portable Git bundle](nb4_results/workshop.bundle). These commits were made now with an AI-assisted automation identity, not backdated student work. Public Wisconsin teaching data only.

NB4 run (choose a new empty workspace): `python src/run_nb4_workshop.py --workspace ../nb4-demo --git git`. To inspect the actual six-commit mini-project: `git clone session_05/nb4_results/workshop.bundle ../nb4-inspection`. The bundle preserves a separate workshop repository; it is not a claim that this main branch has the student's historical six-commit development.

## Data versioning and container

DVC optional dependencies are separate: `python -m pip install -r requirements-dvc.txt`. Run `python src/verify_dvc_roundtrip.py --workspace ../dvc-demo --git git`. The verified environment used Dulwich for the actual fresh Git clone because Git for Windows shell startup was denied by the sandbox; DVC push/pull ran through its CLI. It creates a real local remote and proves a fresh clone initially lacks the data, then restores it using DVC. See [roundtrip evidence](dvc_results/roundtrip.json). The demo reconstructs its own local remote; a stranger cannot pull from the original machine's local path. This is not a shared production/cloud remote.

The Dockerfile now includes the lockfile and Session5 README needed by the card/bundle builder. A GitHub Actions workflow builds and runs it; inspect the actual run status before claiming container execution passed. Docker is absent on the local machine, so local Docker execution is not claimed. Direct runtime dependencies are pinned in requirements.txt; the full environment is recorded separately in requirements-lock.txt.
