# Reflection and exit ticket

## Reflection confirmed by the student

> I used to think that very high accuracy was enough to demonstrate a good model; now I consider it necessary to check data separation, compare against simple models, and evaluate variation across runs.

The student explicitly confirmed this statement in Spanish on25 October 2026 and authorized its inclusion in English. The translation was prepared with AI assistance.

## Evidence from the five requested changes

The larger MLP reduced sample SD in this run from1.0147 to0.9193 percentage points; this is an observation, not a rule that larger networks are always more stable. Feature selection on all rows produced78%,90% and99% accuracy on pure noise as k increased; clean selection inside folds gave49%,45% and48%. Reducing the artificial patient fingerprint reduced the scan/patient gap from45.0 to7.5 points. Peeking50 times increased false alarms from18.6% to31.5% relative to10 checks. Increasing the group sample from20 to70 changed the p-value while the data-generating mean difference remained six points; the observed estimate also changed.

## One number from the field to question

Toapanta-Delgado et al.(2025), DOI10.37815/rte.v37nE1.1356, report RF R2=0.9538 for fragmentation prediction. This number deserves a validation question: does it describe an untouched, event-independent future test, or a more optimistic evaluation of compiled data? The inspected report does not establish prospective/grouped validation. This is a reason to request the exact split/tuning protocol, not evidence that the authors fabricated data or that leakage has been proved. It predicts an average-size/P50-related target, not the proposed mine's P80. A high R2 alone cannot demonstrate local transport savings.

## Application to the proposed project

Split by event/stope/time before learning transformations; keep related images together; record the baseline and metric before evaluating future events; freeze each prediction before observing its outcome; compare against simple and applicable empirical predictors. Report negative findings. The mine dataset and permissions remain future research conditions, distinct from the completed synthetic course exercise.

Paper-choice uniqueness remains unconfirmed: the student answered that they do not know classmates' selections. No claim of uniqueness has been made. The audit itself is complete as a documented assessment; failure to reproduce the paper's metrics is an audit finding, not a reason to manufacture a successful reproduction.
