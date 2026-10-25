# Session 7 — Benchmarking, ablation and documentation

The supplied notebook explicitly requests an own-model Model Card, own-data Datasheet and an 8/8 documentation reading for core Part A. Part B is recommended/extension. The documentation function checks structure/keywords; passing it does not establish accuracy, permission, safety, scientific validity or academic acceptance.

## Public teaching demonstration

[Executed English notebook](../notebooks/session_07_english.ipynb) · [Results](course_demo/results.json).

Core Exercises1–6 were executed. The ablation Your turn was implemented by increasing from five to ten seeds. The public Wisconsin example obtained weak-baseline accuracy0.9161, tuned-baseline0.9790 and gradient-boosting0.9580 on the stated split. Across ten split/model seeds, gradient boosting averaged0.9685 with population SD0.0095. These are public teaching results, not mine findings. The notebook varies both split and estimator seed and uses ddof0; this differs from the fixed-split synthetic mining demonstration.

## Own synthetic-project artifacts

[Model Card](model_card.md) · [Datasheet](datasheet.md) · [Official-function score output](documentation_score.txt) · [Machine-readable check](documentation_score.json).

These cards describe only the synthetic regression exercise, and contain actual measured synthetic results. A separate [real-project status](real_project_status.md) records what remains unknown. The random forest is an ablation demonstration, not a preselected final winner; Ridge can have lower holdout error.

## Complete course practice and exit ticket

[Complete executed notebook, Exercises1–12](../notebooks/session_07_complete_english.ipynb) · [Extension results](course_complete/extension_results.json) · [Course bundle](course_complete/session7_course_complete.zip) · [Exit ticket](exit_ticket.md).

Extensions7–12 are now executed, in addition to the core exercise already recorded. Baseline tuning is repeated inside each training partition; the budget comparison uses matched seed subsets; ablation bars use paired differences and report sample SD, not a falsely independent confidence interval. Naive paired/adjusted p-values remain teaching illustrations because repeated splits overlap. The educational crosswalk records documentation gaps and makes no legal-applicability/conformity claim.

The cards at this folder root describe the actual executed synthetic project; the public Wisconsin exercise remains separate. Company data and field validation are future thesis conditions, not simulated observations in these cards.

Additional Exercise7/9 Your turn modifications are executed in [the addendum](your_turn_addendum/README.md).
