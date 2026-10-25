# Session 7 — remaining Your turn modifications

Both explicit modifications from the supplied extension notebook are now executed. Results use public Wisconsin teaching data; they do not use company records.

## Exercise 7: untuned baseline C=0.001

Ten paired split seeds: GBM mean accuracy=0.968531; weak baseline=0.911189; mean paired gap=0.057343; naive paired p=9.00478e-07. A favorable comparison against a deliberately weak model does not establish superiority over a fairly tuned comparator. Overlapping resamples make this p-value illustrative rather than independent scientific replication.

## Exercise 9: thirty measured variables plus 5000 noise variables

Leaky feature selection accuracy=0.950831; clean pipeline accuracy=0.950831. Informative features can mask the leak. A small observed gap does not validate selection performed on all rows; transformations that learn from data must stay inside training folds.

## Scope of the mining prototype

The 120 mining records were generated mathematically for the reproducibility exercise. They are not measured or anonymized company observations. Actual code execution produces the reported demonstration metrics, but those metrics do not validate P80 prediction or cost savings at the mine. The supplied materials request the student's own model/data details; they do not explicitly authorize replacing the intended mine study with a simulation. Instructor acceptance of that substitution is not established. Company-data analysis remains subject to permission.

The study calendar and USD2,288 research budget are proposed planning assumptions, not approved company amounts or supplier quotations.
