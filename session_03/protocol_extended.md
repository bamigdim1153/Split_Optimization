# Protocol v0.2 — complete PPT structure, supplementary to the one-page oral version

The existing protocol.md/PDF preserves the oral instruction to defer the abstract and review. This supplementary version supplies all ten PPT headings without silently changing that earlier submission. Proposed study; no real-company results or approvals.

## 1. Title
A fragmentation-prediction prototype for economic assessment of blast-design decisions in sublevel stoping at one underground mine in southern Peru.

## 2. Abstract
This proposed study will develop and evaluate a decision-support prototype for production stopes using sublevel stoping. Reported problems include excessive explosive consumption, oversize and transport-budget deviations. After authorization, approximately 120 historical events will be audited and approximately 30 new events per month observed for at least six months. P80 measurement, event traceability and cost units will be standardized. Simple, empirical where applicable, and machine-learning predictors will use common group/time-aware evaluation. New-event predictions will be timestamped before observing outcomes. Economic assessment will distinguish predictive performance from the causal effect of operational changes; field trials require separate technical authorization. Expected outputs are an evaluated prototype, reproducible evidence and explicit limitations, including negative results.

## 3. Introduction/problem
The reported standard design uses AEGIS and technical calculations. High explosive use and oversize may contribute to downstream costs, but their magnitudes and causal relationships are unverified. Monthly tonnage targets, budget and compatible cost indicators will support diagnosis; no percentage saving is promised.

## 4. Literature review
The bounded Session4 synthesis inspects twelve full-text reports, with ten priority papers. Underground bench work (R01), caving measurements (R05/R06), tunnel comparisons (R10) and quarry/compiled-data prediction (R03/C14/R09/R11) inform different parts of the design. P50, mean size, oversize and P80 cannot be substituted. R12 includes percentile modeling but is caving-specific. The current evidence supports a scoped contextual/methodological question, not a global novelty claim. Search-source and official-tool deviations are documented in session_04/search_log.md and prisma_status.md.

## 5. Questions, hypothesis and objectives
Primary predictive question: how accurately can P80 be predicted for future events at this operation relative to a training-mean baseline, regularized regression and an applicable empirical comparator? Proposed hypothesis: a model chosen using development data improves future-event MAE/RMSE under a common frozen protocol; no minimum effect is invented. Economic question: how do fragmentation and oversize relate to compatible total unit costs after accounting for geology, distance, fleet and availability? Objectives are to audit data, establish measurement validity, compare predictors, validate prospectively and evaluate authorized alternatives. A design change and its savings require a separately justified comparison, beyond prediction.

## 6. Methodology
Design science with quantitative evaluation in one mine. Reported 120 historical events and projected 180 future events are planning figures, not a sample-size justification. Define the event/ring/stope unit before analysis; repeated images/buckets are clustered. Audit traceability and missingness rather than treating the reported 90% as measured coverage. Record Split Desktop calibration and post-transport sampling. Features must be available before the prediction time. Hold out events by time/groups; select models and preprocess only inside development data. Freeze and timestamp predictions, evaluate before retraining, and retain version hashes. Report uncertainty and failure cases, not only the best seed. Use the separate evaluation_plan.md for cost denominators and confounding controls.

## 7. Ethics and permissions
General Management approval is pending. Request distinct permissions for academic analysis, anonymized publication and any field trial. Confirm university review requirements. Keep company data outside the public repository; obtain approval for each release. The current public pipeline uses only synthetic/public teaching data.

## 8. Expected outcomes/contribution
A validated measurement/data protocol, an evaluated prototype and reproducible comparative results. Negative results are acceptable. Potential contribution is a locally evaluated workflow connecting prediction with economic evidence; uniqueness and transferability are not established by this mini-review.

## 9. Timeline and research budget
Relative schedule after approval: M1 audit and protocol freeze; M1-M6 collect prospective observations; M2-M3 development on authorized historical data; M4-M6 continue frozen prospective evaluation and separately approved trials if feasible; final analysis after collection. Calendar start/end depend on approval and must not be invented.

| Research cost category | Estimation basis | Current amount/status |
|---|---|---|
| Data extraction and audit | Staff hours x approved hourly cost | Not quoted |
| Fragmentation measurement/QA | Images or events x labor/time; calibration resources | Not quoted |
| Software | Incremental AEGIS/Split Desktop/research licenses, if required | Existing access reported; incremental cost unconfirmed |
| Computing/storage | Required resources x approved rate | Not quoted |
| Field coordination/trials | Incremental approved monitoring and trial costs | Requires separate approval |
| Academic reporting | Printing/publication or institutional charges actually required | Not quoted |

Research budget = sum of approved incremental category costs, avoiding double counting existing resources. Monthly operational explosives/transport budgets are evaluation references, not this research budget. Amounts and funding source require actual quotations/authorization; zero is not assumed.

## 10. Bibliography
Hevner et al. (2004), DOI 10.2307/25148625 (design science); Shields et al. (2025), DOI 10.1177/25726668241301880; Amoako et al. (2022), DOI 10.3390/mining2020013; Manzoor et al. (2023), DOI 10.1016/j.ijrmms.2023.105433. Full reviewed report metadata and links: ../session_04/extraction_and_appraisal.csv. Methodological reference and candidate background: ../session_04/references.md.
