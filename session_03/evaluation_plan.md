# Evaluation plan

1. Freeze protocol and permissions before comparing models.
2. Audit event/stope/image IDs, dates, units, missingness, duplicates and cost linkage. The reported approximately 90% traceability is not a measured coverage result.
3. Predict before blasting; do not use observed P80, subsequent costs or realized tonnage as features if unavailable at prediction time.
4. Document Split Desktop sampling, scale, calibration, image count and measurement after transport. Origin identification does not eliminate measurement bias.
5. Separate development and test by time/groups; multiple images of one event are not independent events. State whether testing concerns new events in known stopes or unseen stopes.
6. Fit imputation, scaling and tuning only within training. Seed variation is not complete uncertainty or independent mine replication.
7. Predictive baselines: training mean, regularized regression and an empirical model if assumptions/inputs apply. AEGIS standard design is the operational comparator; do not call it a P80 predictor unless that module is verified.
8. Timestamp predictions before outcomes are known; evaluate first, update afterward under a new version.
9. Field changes require authorization, technical review and a comparison plan addressing geology, distance, fleet, shifts and availability. The synthetic demo cannot recommend operational charges or layouts.
10. Use compatible cost denominators and avoid double counting. Monthly explosives intensity = sum(kg)/sum(t); transport intensity = sum(USD)/sum(t×km). Do not average unweighted ratios or add USD/(t·km) directly to USD/t. Total compatible cost/t = sum(monetary costs)/sum(t). Compare budget and production within the same month.

No acceptable P80 threshold has yet been defined. Do not inherit the old surface-mining proposal's 18–20 cm target without evidence. Prospective economic effects and external generalization remain untested.
