# Session 6 reading notes

## Kapoor and Narayanan (2023)

The authors identify leakage across scientific applications and distinguish correctly rerunning code from correctly supporting a scientific claim. Their model-info-sheet approach makes data collection, splitting and transformations auditable. For this project, event/image lineage, pre-event feature availability and training-only transformations must be checked before interpreting accuracy. Reproducibility alone does not establish validity. [Published paper](https://doi.org/10.1016/j.patter.2023.100804), [open primary copy](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/).

## REFORMS

The authors' preprint presents32 questions in eight modules covering study goals, reproducibility, data quality/preprocessing, modeling, leakage, uncertainty and limitations. The checklist helps connect a scientific claim with a documented evaluation; it cannot replace sound design or independent verification. Applied here: state the synthetic scope, preserve hashes/code, disclose split/tuning choices, compare baselines, quantify variation and avoid mine-generalization claims. [Authors' preprint and checklist](https://arxiv.org/html/2308.07832v2); the course also cites the2024 Science Advances publication, DOI10.1126/sciadv.adk3452. These notes do not claim the student personally read sources in an unrecorded past session.
