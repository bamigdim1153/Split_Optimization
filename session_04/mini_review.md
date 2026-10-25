# Mini review: fragmentation prediction and operational evaluation

Review question: which fragmentation outcomes and validation methods can inform a P80 predictor for one southern-Peruvian sublevel-stoping mine, and what evidence connects prediction to downstream costs?

## Search and selection

A bounded AI-assisted review was completed on 25 October 2026. Crossref supplied 50 exported records, Semantic Scholar's web interface supplied 10 broad-query records plus seven exact known-item matches, and the prior candidate list supplied nine records. The combined 76 records contained 15 DOI duplicates. Of 61 unique records, 41 were excluded by title/date, 20 reports were sought, seven were inaccessible and 13 full texts were assessed and included. Ten form the priority synthesis below; three provide supporting context. See screening_register.csv and search_log.md. No independent-study total or exhaustive coverage is claimed.

The primary API failed, but Semantic Scholar's UI worked. The post-hoc exact-title checks are disclosed; they cannot retrospectively turn the original candidate discovery into an unbiased database search. The first broad page is a small relevance-ranked sample. These limitations constrain novelty claims.

## Ten priority reports and critical appraisal

### C08 — Effect of the Inter-Ring Delay Time on Rock Fragmentation: Field Tests at the Underground Mine

[Chen, Hui; Liu, Chengyu; Feng, Yin; Yin, Haojie (2024); DOI 10.3390/app14146372](https://doi.org/10.3390/app14146372). Underground field comparison. Field tests at Beizhan iron mine. Target: Fragmentation distribution and economic indicators. Compares an existing design with alternatives; image-based outcomes. Appraisal: Useful underground field evidence; site-specific comparison does not establish a transport-cost effect at the proposed mine. Full-text locator: Methods and field-test/results sections.

### C14 — Performance evaluation of rock fragmentation prediction based on RF‐BOA, AdaBoost‐BOA, GBoost‐BOA, and ERT‐BOA hybrid models

[Zhao, Junjie; Li, Diyuan; Zhou, Jian; Armaghani, Danial J.; Zhou, Aohui (2024); DOI 10.1002/dug2.12089](https://doi.org/10.1002/dug2.12089). Compiled blasting data; not local stoping. 102 observations; seven inputs. Target: X50 as defined by the authors. RF/AdaBoost/GBoost/ERT with Bayesian optimization; RMSE, MAE and R2. Appraisal: Target is not P80; optimizer and small-data split need independent grouped/prospective validation. Full-text locator: Data and methods; model evaluation.

### C27 — Percentile Fragment Size Predictions for Blasted Rock and the Fragmentation–Energy Fan

[Ouchterlony, Finn; Sanchidrián, José A.; Moser, Peter (2016); DOI 10.1007/s00603-016-1094-x](https://doi.org/10.1007/s00603-016-1094-x). Laboratory/field fragmentation methodology. Historical experimental datasets. Target: Percentile fragment-size predictions. Fragmentation-energy fan framework across percentiles. Appraisal: Supports specifying the percentile explicitly; not a learned model validated in this mine. Full-text locator: Percentile framework and validation examples.

### R01 — Underground bench blast fragmentation: Comparison of a multivariate regression model to established predictive models

[Shields, L.; Calnan, J.; Silva, J.; Agioutantis, Z. (2025); DOI 10.1177/25726668241301880](https://journals.sagepub.com/doi/10.1177/25726668241301880). Underground bench blasting. 38 tabulated tests; confidential site. Target: Fragment-size distributions. Multivariate regression versus modified Kuz-Ram and KCO; random validation subset; error metrics. Appraisal: NDA restricts provenance; random validation at one context is not prospective sublevel-stoping evidence. Full-text locator: Methodology/Table 1 and model comparison.

### R03 — Rock Fragmentation Prediction Using an Artificial Neural Network and Support Vector Regression Hybrid Approach

[Amoako, R.; Jha, A.; Zhong, S. (2022); DOI 10.3390/mining2020013](https://doi.org/10.3390/mining2020013). Compiled multi-mine surface blast data. 102 blasts; 90 training and 12 testing. Target: Mean fragment size. ANN and SVR; five-fold model selection; scaling. Appraisal: Test selection matches Kuznetsov predictions to actual size, so the holdout is not a neutral sample; not P80. Full-text locator: Sections 4.1 and 4.2.

### R05 — Modelling the relationship between oversize fragments and nature of rock mass for a sublevel caving operation

[Manzoor, S.; Gustafson, A.; Schunnesson, H. (2023); DOI 10.1016/j.ijrmms.2023.105433](https://ltu.diva-portal.org/smash/record.jsf?pid=diva2%3A1751901). Malmberget sublevel caving. Eight rings; drilling and bucket observations. Target: Oversize proportion. Multiple linear regression and partial least squares; reported R2 0.78 and 0.73. Appraisal: Many drilling/bucket rows are clustered; caving differs from stoping and measurement coverage matters. Full-text locator: Field data, analysis and conclusions.

### R06 — Rock fragmentation measurements in sublevel caving: field tests at LKAB’s Malmberget mine

[Manzoor, S.; Gustafson, A.; Schunnesson, H.; Tariq, M.; Wettainen, T. (2022); DOI 10.36487/ACG_repo/2205_26](https://papers.acg.uwa.edu.au/p/2205_26_Manzoor/). Malmberget sublevel caving. 7258 assessed buckets from over 15000 videos. Target: QRS size classes and X50-related measurement. Field image/video measurement protocol. Appraisal: Buckets are not independent blasts; no P80 prediction or direct savings test; possible dataset overlap with R05. Full-text locator: Field-test and measurement sections.

### R11 — Prediction of Rock Fragmentation by Blasting Using Symbolic Regression and Explainable Artificial Intelligence

[Ozyurt, M. C. (2026); DOI 10.3390/app16157673](https://www.mdpi.com/2076-3417/16/15/7673). Quarries. 221 subsets; 63 blasts; 16 quarries. Target: P50. Symbolic regression and explainability; Blast_ID split: 50 train/13 test blasts; grouped internal validation. Appraisal: Good example of event grouping; quarry data and P50 do not establish transport savings or transfer to underground stoping. Full-text locator: Sections 3.1-3.3.

### R12 — Impact of blast design parameters on rock fragmentation in sub-level caving: A multivariate regression approach

[Khodayari, A.; Xu, C.; Dare-Bryan, P.; Dowd, P.; Lapcevic, V.; Metcalfe, A. (2026); DOI 10.1016/j.jrmge.2025.07.038](https://digital.library.adelaide.edu.au/items/692d5d1e-454b-433a-9294-bab89826634a). Ernest Henry sublevel caving. Field reference data and 34 modeled scenarios. Target: P20, P50 and P80. Multivariate regression with numerical fragmentation modeling. Appraisal: Relevant percentile coverage; simulated scenarios are not 34 independent field trials; caving differs from stoping. Full-text locator: Methodology, modeling and regression results.

### S09 — Preliminary Blast Fragmentation Modeling in an Underground Aggregate Operation

[Shields, L.; Calnan, J.; Silva, J.; Maldonado, E.; Agioutantis, Z. (2024); DOI 10.56952/ARMA-2024-0053](https://doi.org/10.56952/ARMA-2024-0053). Underground aggregate modeling; compiled-data development. Multivariate analysis using data assembled from five literature sources. Target: 20%, 50% and 80% passing sizes. Multivariate regression; initial fitted relationships; external prediction/validation proposed as future work. Appraisal: Relevant percentile targets, but fitted significance is not prospective predictive accuracy; source-data overlap with related Shields reports must be checked. Full-text locator: ARMA 2024 paper 0053, methods and conclusions, six pages.

## Interpretation and proposed research response

Prediction, measurement validity and economic benefit need separate evidence. The proposed study will specify P80 and its measurement stage, preserve event/image/stope lineage, use time/group-aware validation and compare against simple and applicable empirical baselines. P50, mean size, oversize and P80 are different targets. Caving, underground benches, tunnelling and quarries supply methodological context; none automatically validates transfer to this mine. A prediction model alone cannot establish cost savings caused by a design change.

The supporting reports R09, R10 and C29 remain in the extraction table. R09 and R10 were not found by the exact-title Semantic Scholar checks; they are retained from the documented other-method search, not falsely described as indexed matches. The ten priority reports have actual Semantic Scholar links in semantic_scholar_searches.json.

R05/R06 share the Malmberget setting; S09 and related Shields reports may reuse earlier data; R03/C14/R09 use compiled datasets with potential overlap. Reports are not independent experiments. No pooled sample size, effect estimate or ranking of cross-study error metrics is justified. Access restrictions, single assisted screening, short result export and targeted confirmation can miss contradictory evidence. The four candidate gaps are scoped to this inspected set.
