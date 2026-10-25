# Reproducibility Report - Session 7
_Generated 2026-10-25 06:12 UTC_

## Environment
- Python: 3.12.14
- numpy: 2.2.6 | pandas: 2.2.3 | scikit-learn: 1.6.1 | scipy: 1.18.1
- Global RANDOM_STATE: 42
- Dataset: Wisconsin Breast Cancer (569 samples, 30 features)

## Headline results (measured in this run)
- Fancy model, test accuracy: 0.9580
- Tuned baseline, test accuracy: 0.9790
- Paired t-test over 10 seeds (fancy vs tuned baseline): p = 0.1530
- McNemar exact p (single test set): 0.3750
- Fancy bootstrap 95% CI: [0.9231, 0.9860]

## Artifacts in this bundle
- model_card.md - 9-section Model Card (Mitchell et al., 2019)
- datasheet.md - 7-section Datasheet (Gebru et al., 2021)
- annex_iv_crosswalk.md - EU AI Act Annex IV gap analysis
- fig_compute_matched.png, fig_ablation_errorbars.png - figures

## Documentation scorecard
- Score: 8/8