# Session 6 — Experimental practice and reproducibility audit

The newly supplied original notebook and PPT were reviewed. The PPT audit checklist has nine Yes/Partial/No items; its closing instructions also request the labs and Your turn exercises.

## Executed English lab adaptation

[Executed notebook](../notebooks/session_06_english.ipynb) · [Measured results](lab_results/results.json) · [Peeking figure](lab_results/peeking_comparison.png).

The original computational settings are retained; bilingual commentary/plots are replaced by English summaries. All five requested modifications were executed:

| Modification | Measured result in this environment |
|---|---|
| MLP width 16 to 64, same 20 split/init seeds | Accuracy sample SD: 1.0147 to 0.9193 percentage points |
| Feature selection k=5/20/100 on pure noise | Leaky accuracy 78%/90%/99%; clean pipeline 49%/45%/48% |
| Patient fingerprint strength 3.0 to 0.5 | Scan/patient accuracy gap: 45.0 to 7.5 percentage points |
| Peeking 10 to 50 times, 2,000 simulations | False-positive percentage: 18.6% to 31.5% |
| Sample size 20 to 70 per group | p: 0.2016 to approximately 0.0000425; the generating effect stays six points but observed estimates differ |

These are public teaching/simulation results, not mining findings. They are environment-specific measurements, not guaranteed universal outcomes.

## Paper audit

[Audit report](audit_report.md) · [Course-aligned nine-item scorecard](audit_scorecard.csv). A real repository was inspected and an actual startup attempted. Metric reproduction remains incomplete because TensorFlow was absent in the audit environment; an unmatched image/mask was also found. Neither finding by itself proves the paper invalid.

## Reflection, exit ticket and capture

[Student-approved reflection and field-specific exit ticket](reflection_and_exit_ticket.md) · [Actual executed-output capture](evidence/executed_notebook_capture.png) · [Reading notes](reading_notes.md).

The reflection was confirmed by the student. The capture is an automated browser view of genuine saved notebook outputs, clearly labeled; no manual student execution is claimed. The paper/code audit is complete as an assessment with documented reproduction limitations. Its unsuccessful metric reproduction is a finding, not a manufactured success. The student's classmates' article choices are unknown, so the distinct-paper instruction remains a coordination check before submission.
