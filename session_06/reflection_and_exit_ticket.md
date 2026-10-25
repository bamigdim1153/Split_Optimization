# Session 6 — Reflection and exit ticket

## Reflection

> I used to think that very high accuracy was enough to demonstrate a good model;
> now I think it is necessary to check how the data are split, compare against
> simple models, and look at the variation across runs.

## What the five "Your turn" changes showed me

| Change | Result in my run |
|---|---|
| MLP hidden layer 16 → 64 | Standard deviation across seeds went from 1.01 to 0.92 percentage points |
| Feature selection on pure noise, k = 5 / 20 / 100 | With leakage: 78% / 90% / 99% accuracy. Clean pipeline: 49% / 45% / 48% |
| Patient fingerprint 3.0 → 0.5 | Gap between scan split and patient split went from 45.0 to 7.5 points |
| Peeking 10 → 50 times | False positives went from 18.6% to 31.5% |
| Group size 20 → 70 | p-value went from 0.20 to about 0.00004; the true effect stayed at 6 points |

The one that surprised me most was feature selection: with leakage, a model reached
99% accuracy on pure noise. The larger network was a bit more stable in this run,
but I would not generalize that from one experiment.

## One number from my field that I would question

Toapanta-Delgado et al. (2025), DOI 10.37815/rte.v37nE1.1356, report R² = 0.9538 for
fragmentation prediction with random forest. Before trusting this number I would ask:
was it tested on new, independent blasts, or on a random split of compiled data? The
paper does not make this clear. Also, it predicts an average size (P50-type), not P80,
and a high R² alone does not show transport-cost savings.

## What I will apply in my project

- Split the data by blast, stope or time **before** any scaling or feature selection.
- Keep images from the same blast together, on the same side of the split.
- Fix the baseline and the metric before evaluating on new blasts.
- Record each prediction before observing the real result.
- Always compare against simple models, and report negative results too.
