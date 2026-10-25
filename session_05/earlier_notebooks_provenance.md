# Earlier notebook provenance

English computational adaptations were prepared from the locally supplied NB1_Reproducibility_Magic_Tricks, NB3_Case_Study_100_Percent_LITE and NB4_Workshop_Reproducible_Pipeline_LITE. Original files remain local. NB1/NB3 outputs were produced by src/execute_notebook.py in Python3.12.14, scikit-learn1.6.1. English prose/plot labels replace bilingual commentary; computations are teaching demonstrations, not mining data.

NB4's local driver retains the supplied training pipeline and five-fold scoring, uses an isolated local workspace, local Git identity and MLflow SQLite, and replaces Colab shell/notebook setup with explicit Python subprocess calls. Its six actual content commits and Git bundle are reviewable. Logs establish automated execution, not the student's personal execution.

NB1 measured accuracy mean0.9727778 with sampleSD0.0071873; pure-noise leaky accuracy0.87 versus clean0.50. NB3's invented instructor paper reached1.0 at seed12 but0.9685315 over20 seeds; the synthetic-patient leakage example has41/143 overlapping test rows. Full comparators and units appear in the executed notebooks/JSON. These new measurements supersede any illustrative numbers in course prose for this execution environment.
