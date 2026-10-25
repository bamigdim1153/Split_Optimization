# Mini review: fragmentation prediction and operational evaluation

**Completed bounded review, with source/tool deviations.** Read search_log.md before interpreting this review. Twelve full-text reports were included; ten are selected for the priority synthesis, with two supplementary methodological/field reports. This is not a claim of twelve independent studies or comprehensive coverage. Import review_library.ris into Zotero/Mendeley; the import itself has not been performed in the student's account.

## Question and synthesis

Which fragmentation outcomes and validation methods can inform a P80 predictor for one southern-Peruvian sublevel-stoping mine, and what evidence connects prediction to downstream costs?

Prediction methods exist; novelty cannot be claimed from merely applying an ANN or random forest. The ten priority reports below span regression, machine learning, field measurement and operational comparison. Their targets and contexts differ. Numerical scores cannot be pooled across target definitions, units, partitions or mines. No meta-analysis is justified by this small heterogeneous set.

### C08 — Effect of the Inter-Ring Delay Time on Rock Fragmentation: Field Tests at the Underground Mine

[2024; DOI 10.3390/app14146372](https://doi.org/10.3390/app14146372). Underground field comparison. Field tests at Beizhan iron mine. Target: Fragmentation distribution and economic indicators. Compares an existing design with alternatives; image-based outcomes. Appraisal: Useful underground field evidence; site-specific comparison does not establish a transport-cost effect at the proposed mine. Full-text locator: Methods and field-test/results sections.

### C14 — Performance evaluation of rock fragmentation prediction based on RF‐BOA, AdaBoost‐BOA, GBoost‐BOA, and ERT‐BOA hybrid models

[2024; DOI 10.1002/dug2.12089](https://doi.org/10.1002/dug2.12089). Compiled blasting data; not local stoping. 102 observations; seven inputs. Target: X50 as defined by the authors. RF/AdaBoost/GBoost/ERT with Bayesian optimization; RMSE, MAE and R2. Appraisal: Target is not P80; optimizer and small-data split need independent grouped/prospective validation. Full-text locator: Data and methods; model evaluation.

### R01 — Underground bench blast fragmentation: Comparison of a multivariate regression model to established predictive models

[2025; DOI 10.1177/25726668241301880](https://journals.sagepub.com/doi/10.1177/25726668241301880). Underground bench blasting. 38 tabulated tests; confidential site. Target: Fragment-size distributions. Multivariate regression versus modified Kuz-Ram and KCO; random validation subset; error metrics. Appraisal: NDA restricts provenance; random validation at one context is not prospective sublevel-stoping evidence. Full-text locator: Methodology/Table 1 and model comparison.

### R03 — Rock Fragmentation Prediction Using an Artificial Neural Network and Support Vector Regression Hybrid Approach

[2022; DOI 10.3390/mining2020013](https://doi.org/10.3390/mining2020013). Compiled multi-mine surface blast data. 102 blasts; 90 training and 12 testing. Target: Mean fragment size. ANN and SVR; five-fold model selection; scaling. Appraisal: Test selection matches Kuznetsov predictions to actual size, so the holdout is not a neutral sample; not P80. Full-text locator: Sections 4.1 and 4.2.

### R05 — Modelling the relationship between oversize fragments and nature of rock mass for a sublevel caving operation

[2023; DOI 10.1016/j.ijrmms.2023.105433](https://ltu.diva-portal.org/smash/record.jsf?pid=diva2%3A1751901). Malmberget sublevel caving. Eight rings; drilling and bucket observations. Target: Oversize proportion. Multiple linear regression and partial least squares; reported R2 0.78 and 0.73. Appraisal: Many drilling/bucket rows are clustered; caving differs from stoping and measurement coverage matters. Full-text locator: Field data, analysis and conclusions.

### R06 — Rock fragmentation measurements in sublevel caving: field tests at LKAB’s Malmberget mine

[2022; DOI 10.36487/ACG_repo/2205_26](https://papers.acg.uwa.edu.au/p/2205_26_Manzoor/). Malmberget sublevel caving. 7258 assessed buckets from over 15000 videos. Target: QRS size classes and X50-related measurement. Field image/video measurement protocol. Appraisal: Buckets are not independent blasts; no P80 prediction or direct savings test; possible dataset overlap with R05. Full-text locator: Field-test and measurement sections.

### R09 — Rock Fragmentation by Blasting in Open-Pit Mining: an AI Predictive Model

[2025; DOI 10.37815/rte.v37nE1.1356](https://rte.espol.edu.ec/index.php/tecnologica/en/article/view/1356). Compiled open-pit data. 97 internationally sourced records. Target: Average size; P50 notation in figures. RF/SVR/KRR versus Kuz-Ram; reports RF R2 0.9538. Appraisal: Reporting does not establish prospective/grouped holdout validation; cannot equate average/P50 with P80; compiled-data overlap needs checking. Full-text locator: Methodology and results, pp. 40-49.

### R10 — Comparative Analysis of Fragmentation Models for Underground Blasting

[2021; DOI 10.5937/podrad2139029F](https://ume.rgf.bg.ac.rs/index.php/ume/article/view/164). Kittila underground tunnelling. Case-study size-distribution comparison. Target: Fragmentation curves. Kuz-Ram and Swebrec curves compared with measured fragmentation. Appraisal: Tunnelling differs from production stoping; fitting curves is not prospective ML generalization. Full-text locator: Case study and comparison sections.

### R11 — Prediction of Rock Fragmentation by Blasting Using Symbolic Regression and Explainable Artificial Intelligence

[2026; DOI 10.3390/app16157673](https://www.mdpi.com/2076-3417/16/15/7673). Quarries. 221 subsets; 63 blasts; 16 quarries. Target: P50. Symbolic regression and explainability; Blast_ID split: 50 train/13 test blasts; grouped internal validation. Appraisal: Good example of event grouping; quarry data and P50 do not establish transport savings or transfer to underground stoping. Full-text locator: Sections 3.1-3.3.

### R12 — Impact of blast design parameters on rock fragmentation in sub-level caving: A multivariate regression approach

[2026; DOI 10.1016/j.jrmge.2025.07.038](https://digital.library.adelaide.edu.au/items/692d5d1e-454b-433a-9294-bab89826634a). Ernest Henry sublevel caving. Field reference data and 34 modeled scenarios. Target: P20, P50 and P80. Multivariate regression with numerical fragmentation modeling. Appraisal: Relevant percentile coverage; simulated scenarios are not 34 independent field trials; caving differs from stoping. Full-text locator: Methodology, modeling and regression results.

## Cross-report interpretation

Predictive accuracy, measurement validity and economic benefit require separate evidence. The project must define a P80 measurement protocol, connect each transported image sample to its source event, and distinguish original fragmentation from handling-induced changes. Oversize and secondary-breaking records complement P80; they are not interchangeable targets. Use event/time grouping and evaluate new events before updating the model. A prediction model alone does not identify the causal effect of changing a design on costs.

Two supporting reports are included in extraction_and_appraisal.csv: C27 addresses percentile prediction, and C29 supplies additional open-pit field context. They are retained transparently rather than silently discarded to force a count of ten.

## Dependence and limitations

R05 and R06 concern Malmberget and may overlap in underlying observations; they are complementary reports, not independent replication. R03/C14/R09 draw on compiled fragmentation datasets; overlap must be checked against source identifiers before any quantitative aggregation. The exact number of independent studies is unresolved. No pooled sample count or evidence strength based on twelve independent datasets is claimed.

The bounded one-source fallback, prior-candidate selection, seven inaccessible full texts and single assisted reviewer can miss contradictory evidence. The candidate gaps in candidate_gaps.md apply only to this inspected set. Broaden the database search before claiming doctoral novelty.
