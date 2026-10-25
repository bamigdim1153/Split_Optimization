# Session 7 — Benchmarking, ablation and documentation

The supplied notebook explicitly requests an own-model Model Card, own-data Datasheet and an 8/8 documentation reading for core Part A. Part B is recommended/extension. The documentation function checks structure/keywords; passing it does not establish accuracy, permission, safety, scientific validity or academic acceptance.

## Public teaching demonstration

[Executed English notebook](../notebooks/session_07_english.ipynb) · [Results](course_demo/results.json).

Core Exercises1–6 were executed. The ablation Your turn was implemented by increasing from five to ten seeds. The public Wisconsin example obtained weak-baseline accuracy0.9161, tuned-baseline0.9790 and gradient-boosting0.9580 on the stated split. Across ten split/model seeds, gradient boosting averaged0.9685 with population SD0.0095. These are public teaching results, not mine findings. The notebook varies both split and estimator seed and uses ddof0; this differs from the fixed-split synthetic mining demonstration.

## Own synthetic-project artifacts

[Model Card](model_card.md) · [Datasheet](datasheet.md) · [Official-function score output](documentation_score.txt) · [Machine-readable check](documentation_score.json).

These cards describe only the synthetic regression exercise, and contain actual measured synthetic results. A separate [real-project status](real_project_status.md) records what remains unknown. The random forest is an ablation demonstration, not a preselected final winner; Ridge can have lower holdout error.

Exercises7–12 and the AnnexIV crosswalk were not executed. No legal applicability or conformity statement is made. The student's acceptance of synthetic work must be confirmed with the instructor.
