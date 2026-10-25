# Protocol v0.2 — complete PPT structure, supplementary to the one-page oral version

The existing protocol.md/PDF preserves the oral instruction to defer the abstract and review. This supplementary version supplies all ten PPT headings without silently changing that earlier submission. Proposed study; no real-company results or approvals.

## 1. Title
A fragmentation-prediction prototype for economic assessment of blast-design decisions in sublevel stoping at one underground mine in southern Peru.

## 2. Abstract
This proposed study will develop and evaluate a decision-support prototype for production stopes using sublevel stoping. Reported problems include excessive explosive consumption, oversize and transport-budget deviations. After authorization, approximately 120 historical events will be audited and approximately 30 new events per month observed for at least six months. P80 measurement, event traceability and cost units will be standardized. Simple, empirical where applicable, and machine-learning predictors will use common group/time-aware evaluation. New-event predictions will be timestamped before observing outcomes. Economic assessment will distinguish predictive performance from the causal effect of operational changes; field trials require separate technical authorization. Expected outputs are an evaluated prototype, reproducible evidence and explicit limitations, including negative results.

## 3. Introduction/problem
The reported standard design uses AEGIS and technical calculations. High explosive use and oversize may contribute to downstream costs, but their magnitudes and causal relationships are unverified. Monthly tonnage targets, budget and compatible cost indicators will support diagnosis; no percentage saving is promised.

## 4. Literature review
The bounded Session 4 synthesis inspects thirteen full-text reports, with ten priority papers. Underground bench work (R01), caving measurements (R05/R06), tunnel comparisons (R10) and quarry/compiled-data prediction (R03/C14/R09/R11) inform different parts of the design. P50, mean size, oversize and P80 cannot be substituted. R12 includes percentile modeling but is caving-specific. The current evidence supports a scoped contextual/methodological question, not a global novelty claim. Search limitations and official-tool provenance are documented in session_04/search_log.md and prisma_status.md.

## 5. Questions, hypothesis and objectives
Primary predictive question: how accurately can P80 be predicted for future events at this operation relative to a training-mean baseline, regularized regression and an applicable empirical comparator? Proposed hypothesis: a model chosen using development data improves future-event MAE/RMSE under a common frozen protocol; no minimum effect is invented. Economic question: how do fragmentation and oversize relate to compatible total unit costs after accounting for geology, distance, fleet and availability? Objectives are to audit data, establish measurement validity, compare predictors, validate prospectively and evaluate authorized alternatives. A design change and its savings require a separately justified comparison, beyond prediction.

## 6. Methodology
Design science with quantitative evaluation in one mine. Reported 120 historical events and projected 180 future events are planning figures, not a sample-size justification. Define the event/ring/stope unit before analysis; repeated images/buckets are clustered. Audit traceability and missingness rather than treating the reported 90% as measured coverage. Record Split Desktop calibration and post-transport sampling. Features must be available before the prediction time. Hold out events by time/groups; select models and preprocess only inside development data. Freeze and timestamp predictions, evaluate before retraining, and retain version hashes. Report uncertainty and failure cases, not only the best seed. Use the separate evaluation_plan.md for cost denominators and confounding controls.

## 7. Ethics and permissions
General Management approval is pending. Request distinct permissions for academic analysis, anonymized publication and any field trial. Confirm university review requirements. Keep company data outside the public repository; obtain approval for each release. The current public pipeline uses only synthetic/public teaching data.

## 8. Expected outcomes/contribution
A validated measurement/data protocol, an evaluated prototype and reproducible comparative results. Negative results are acceptable. Potential contribution is a locally evaluated workflow connecting prediction with economic evidence; uniqueness and transferability are not established by this mini-review.

## 9. Proposed timeline and research budget

**Planning scenario, not an approved company budget or a vendor quotation.** Proposed calendar: November 2026-April 2027. Six complete observation months begin only after written academic-use authorization; a later approval shifts the schedule. Approximately30 future events/month and180 over six months are planning assumptions reported by the student, not completed observations or a power calculation.

| Month | Proposed activity and decision gate |
|---|---|
| November 2026 (M1) | Obtain permissions, define the event unit and measurement protocol, audit authorized historical data, freeze analysis plan; start observation only after approval |
| December 2026 (M2) | Establish simple/empirical baselines, training-only preprocessing and group/time-aware development |
| January 2027 (M3) | Select and freeze the prototype using development data; prepare timestamped future-event predictions |
| February 2027 (M4) | Prospective evaluation before updates; examine measurement and cost linkage |
| March 2027 (M5) | Continue observation and failure analysis; update only after scoring and versioning |
| April 2027 (M6) | Complete six authorized collection months where the start date permits; final comparative analysis and reporting afterward |

Current budget covers observation, data preparation and prototype evaluation. Operational design trials are a separately approved future stage, with their own technical review and budget; they are not silently costed as zero here.

| Category | Explicit illustrative estimation basis | Proposed USD |
|---|---|---:|
| Historical data audit |40hours x USD 10/hour |400 |
| Prospective image processing |180events x0.5hour x USD 10/hour |900 |
| Measurement quality checks |18events x0.5hour x USD 10/hour |90 |
| Model development and reporting |60hours x USD 10/hour |600 |
| Computing/storage allowance |6months x USD 15/month |90 |
| Incremental software licenses |USD 0 only in the scenario where existing licenses expressly permit the research use |0 |
| Subtotal |Sum of illustrative scenario costs |2080 |
| Contingency |10% of subtotal |208 |
| Total planning scenario |Includes imputed labor; funding and rates require validation |2288 |

USD 10/hour, task durations and the computing allowance are transparent planning assumptions introduced for this proposal, not observed payroll/vendor prices. Researcher time may be an in-kind contribution rather than a cash payment. If license rights, staffing, image workload or computing needs differ, revise the scenario before requesting funding. No payment or commitment has been made. The operational monthly explosives/transport budget is an outcome comparator, separate from this research budget.

## 10. Bibliography
Hevner et al. (2004), DOI 10.2307/25148625 (design science); Shields et al. (2025), DOI 10.1177/25726668241301880; Amoako et al. (2022), DOI 10.3390/mining2020013; Manzoor et al. (2023), DOI 10.1016/j.ijrmms.2023.105433. Full reviewed report metadata and links: ../session_04/extraction_and_appraisal.csv. Methodological reference and candidate background: ../session_04/references.md.
