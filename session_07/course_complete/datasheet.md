# Datasheet — Wisconsin Breast Cancer (educational use)

## Motivation
- **Purpose:** Originally created to study automated diagnosis of breast masses from FNA imaging features.
- **Created by / funded by:** Originating clinical researchers (UCI ML Repository). Funding: UNKNOWN — to investigate.

## Composition
- **What instances represent:** 569 fine-needle-aspirate samples, each with 30 computed cell-nucleus features.
- **Labels:** Binary: malignant / benign.
- **Sample vs population:** A sample; NOT all possible patients. No demographic attributes recorded.
- **Missing data:** None reported in features; demographics entirely absent.

## Collection process
- **How collected:** Image analysis of digitized FNA slides; features computed automatically.
- **Timeframe:** Historical (1990s). Distribution may not reflect current populations.
- **Consent / ethics:** UNKNOWN — to investigate (predates modern consent documentation norms).

## Preprocessing / cleaning / labeling
- **Steps:** Features pre-computed; we additionally apply StandardScaler at train time (fit on train split only).
- **Raw data available:** Raw images NOT included — only derived features.

## Uses
- **Appropriate uses:** Methods teaching, benchmarking documentation practice.
- **Should NOT be used for:** Real clinical decisions or as evidence about any present-day population.

## Distribution
- **How distributed:** Public via UCI ML Repository / scikit-learn.
- **License / restrictions:** UNKNOWN — to investigate.

## Maintenance
- **Maintainer:** No active maintainer; static historical dataset.
- **Update plan:** None expected.
