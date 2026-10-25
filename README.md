# Split Optimization — Research Methods Portfolio

**Project:** A fragmentation-prediction prototype to support the economic assessment of blast-design decisions in sublevel stoping at one underground mine in southern Peru.

**Course:** Research Methods, Dr. Loveleen Gaur. All repository material is in English.

## Evidence boundaries

- The mining dataset is **SYNTHETIC**. No company records have been accessed or published.
- The student reports 120 historical blasts and expects about 30 new blasts/month for at least six months. These are reported/projected quantities, not an audited dataset or completed prospective study.
- Sessions 6 and 7 use the supplied course notebooks: public Wisconsin teaching data and synthetic statistical experiments. They are NOT mining results.
- Real-data publication and field trials remain subject to authorization. Acceptance of synthetic work for assessment is not assumed.

## Seven-session index

| Session | Main document | Evidence and status |
|---|---|---|
| 1 | [Paradigm justification](session_01/paradigm.md) | Draft for student review and defense |
| 2 | [Method-fit matrix](session_02/method_fit_matrix.md) | Proposed scores and weights; not empirical measurements |
| 3 | [Protocol v0.1](session_03/protocol.md) | Draft; permissions, dates and research budget pending |
| 4 | [Literature review](session_04/review_protocol.md) | Real candidate references; systematic screening/PRISMA still pending |
| 5 | [Reproducible synthetic pipeline](session_05/README.md) | Executed demonstration; seven seeds and paired ablations |
| 6 | [Reproducibility audit and labs](session_06/README.md) | Course checklist, real paper/code audit and Your turn exercises |
| 7 | [Benchmarking and documentation](session_07/README.md) | Course core exercises and own synthetic-project cards |

## Run

```bash
python -m venv .venv
# Activate the virtual environment using the command appropriate for your OS.
python -m pip install -r requirements-lock.txt
python src/generate_synthetic.py
python src/run_experiment.py
python src/build_project_cards.py
python src/execute_notebook.py notebooks/session_06_english.ipynb session_06/lab_results
python src/execute_notebook.py notebooks/session_07_english.ipynb session_07/course_demo
```

The standard-library notebook runner executes trusted local course adaptations without requiring Jupyter. Jupyter can also open the notebooks. Do not use the runner with unreviewed notebooks. Full Session 6 simulations can take several minutes.

Read [requirements and remaining work](control/requirements.md), [evaluation plan](session_03/evaluation_plan.md), and [provenance and AI assistance](control/provenance.md). No operational explosive-charge recommendations or proven cost savings are provided.

## One-page documents

- [Session 1 PDF](session_01/paradigm.pdf)
- [Session 2 PDF](session_02/method_fit_matrix.pdf)
- [Session 3 PDF](session_03/protocol.pdf)

Local verification: `python src/verify_portfolio.py`. The Session7 [own-project bundle](session_07/session7_deliverable.zip) contains the synthetic cards, code and portable result evidence.
