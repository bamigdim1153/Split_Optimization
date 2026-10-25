# Model Card

## Model details
- **Name / version:** BreastCancer-GBM v0.1
- **Owner / contact:** Course demonstration; student review pending
- **Date:** 2026-10-24
- **Architecture:** Gradient Boosting (200 trees, depth 3) on standardised features
- **License:** UNKNOWN — to investigate

## Intended use
- **Primary intended uses:** Teaching example for documentation practice ONLY.
- **Out-of-scope / misuse:** NOT for clinical decisions. Trained on one historical dataset; not validated on any hospital population.
- **Intended users:** Doctoral students in this course

## Factors
- **Relevant groups / conditions:** Tumour type (malignant vs benign). Real clinical factors (age, scanner, site) are ABSENT from this dataset.
- **Evaluation factors:** Reported overall and per class.

## Metrics
- **Performance measures:** Accuracy and macro-F1
- **Decision thresholds:** 0.5 default
- **Variation approach:** Mean ± population std over 10 split/model seeds; single-split metrics are labelled separately

## Evaluation data
- **Datasets:** 25% held-out stratified split of the Wisconsin Breast Cancer dataset
- **Preprocessing:** StandardScaler fit on the training split only

## Training data
- **Datasets:** 75% of the Wisconsin Breast Cancer dataset (569 samples total)
- **Known limitations:** Single source, historical, no demographic metadata

## Quantitative analyses
- **Overall results:** accuracy=0.9580, macro-F1=0.9543
- **Disaggregated results:** per-class recall: {np.str_('malignant'): 0.9057, np.str_('benign'): 0.9889}

## Ethical considerations
- **Risks:** False reassurance if mistaken for a clinical tool; dataset lacks demographic diversity.
- **Mitigations:** Clearly marked educational; no deployment.

## Caveats and recommendations
- **Caveats:** Performance will NOT transfer to real clinical imaging or other populations.
- **Recommendations:** External validation required before any real use.
