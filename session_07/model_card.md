# Model Card — synthetic project

**SYNTHETIC TEACHING EXERCISE — NOT MINING FINDINGS**

## Model details
- **Name / version:** Split Optimization — synthetic RF demonstration v0.2
- **Owner / contact:** Repository owner: bamigdim1153; academic review/signoff UNKNOWN
- **Architecture:** RandomForestRegressor, 80 trees; grouped training-only grid search over depth and minimum leaf size; see per-seed parameters
- **License:** UNKNOWN — repository-owner licensing decision not recorded

## Intended use
- **Primary intended uses:** Research-methods teaching: repeatability, baselines, seeds and ablation
- **Out-of-scope / misuse:** NOT FOR actual blasting design, charge recommendations, production deployment or claims about mine savings
- **Intended users:** The student and instructor reviewing this course exercise

## Factors
- **Relevant groups / conditions:** Twelve fictional groups; four uncalibrated abstract indices
- **Evaluation factors:** Disjoint holdout groups and paired seeds; grouping does not reproduce mine geology

## Metrics
- **Performance measures:** MAE, RMSE and R2 for a fictional target called p80_demo_mm
- **Decision thresholds:** No operational acceptance threshold or recommended P80
- **Variation approach:** Mean ± sample SD across seven estimator seeds; fixed holdout; not independent mine replications

## Evaluation data
- **Datasets:** 30 fictional rows in the last three groups; no company or prospective observations
- **Preprocessing:** Held-out data untouched during fitting/tuning; train/test group IDs are disjoint

## Training data
- **Datasets:** 90 fictional rows in nine groups from the 120-row generator
- **Preprocessing:** Imputation fitted in training; three-fold GroupKFold grid search; Ridge comparator additionally scales inside its pipeline

## Quantitative analyses
- **Overall results:** RF RMSE=10.666283 ± 0.186711; MAE=9.114162; mean R2=0.766411. All units are fictional.
- **Per-group disaggregated results:** {"GROUP_10": 9.379696, "GROUP_11": 10.822704, "GROUP_12": 11.674281}
- **Comparator and interpretation:** Ridge holdout RMSE=8.859887; lower than RF here. RF is an ablation demonstration, not a preselected final winner. See all seven seeds and paired deltas.

## Ethical considerations
- **Risks:** Misrepresenting synthetic outcomes as empirical mine evidence; treating a completeness score as validation
- **Mitigations:** Origin labels, separate real-project status, explicit unknowns, no operational parameter conversion

## Caveats and recommendations
- **Caveats:** Invented generator, one holdout, small synthetic sample, no real cost/production/safety validation
- **Recommendations:** Instructor acceptance and student review required; create a separate authorized real-data evaluation before any mine-use claim
