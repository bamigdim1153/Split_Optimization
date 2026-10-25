# Split Optimization
Humberto Sánchez 

PhD in Deep Tech, UNMSM

Research Methods portfolio · Dr. Loveleen Gaur · Sessions 1–7

The proposed research concerns fragmentation prediction and economic assessment in sublevel stoping at one underground mine in southern Peru. The implemented course prototype uses **synthetic data**; public Wisconsin data are used only in the supplied teaching exercises. No company records or field results are published.

## Deliverables by session

| Session | Deliverable |
|---|---|
|1| [Paradigm justification](session_01/paradigm.md) |
|2| [Method-fit matrix](session_02/method_fit_matrix.md) |
|3| [Complete research protocol](session_03/protocol_extended.md) |
|4| [Mini-review](session_04/mini_review.md), [PRISMA](session_04/prisma_status.md), [gap table](session_04/candidate_gaps.md), [reference library](session_04/review_library.ris) |
|5| [Reproducible experiments and verification](session_05/README.md) |
|6| [Audit and labs](session_06/README.md), [reflection/exit ticket](session_06/reflection_and_exit_ticket.md) |
|7| [Model Card, Datasheet and complete practice](session_07/README.md) |

## Run the synthetic project

```bash
python -m venv .venv
# Activate the environment for your operating system.
python -m pip install -r requirements-lock.txt
python src/generate_synthetic.py
python src/run_experiment.py
python src/build_project_cards.py

```

The generator creates 120 fictional events. Evaluation uses a 90/30 disjoint-group holdout, training-only tuning, seven seeds, simple baselines and paired ablations. Ridge has lower holdout error than random forest in this demonstration; model complexity is not treated as evidence of superiority.

## Retrieve versioned teaching data

```bash
python -m pip install -r requirements-dvc.txt
python -m dvc pull
```

DVC restores `data/versioned/blasts_SYNTHETIC.csv` from the public read-only teaching cache. SHA256: `7ebd3c2edcefc67024d9ab4ca9f09332615573930c6e93e3c70043f43dc97332`. The pipeline uses the identical tracked copy in `data/synthetic/`. [Fresh public clone/pull evidence](session_05/dvc_results/public_stranger_test.json) and [successful container execution](control/container_ci_evidence.json) are included.

## Execute course notebooks

```bash
python src/execute_notebook.py notebooks/session_06_english.ipynb session_06/lab_results
python src/execute_notebook.py notebooks/session_07_complete_english.ipynb session_07/course_complete
```

Runs the notebooks without opening Jupyter. Earlier NB1/NB3/NB4 evidence is indexed in Session 5. Statistical examples describe teaching data and overlapping resamples, not mine effects.

[Provenance and assistance](control/provenance.md) 

Company data are not included; the mining prototype uses synthetic data until General Management approves academic use. AI assistance is declared in provenance. 

Additional Exercise 7/9 Your turn modifications are executed in [the addendum](session_07/your_turn_addendum/README.md).
