# Reproducibility Audit Report

## Paper metadata
Jin et al. (2023), Study on segmentation of blasting fragment images from open-pit mine based on U-CARFnet. PLoS ONE 18(9):e0291115. https://doi.org/10.1371/journal.pone.0291115. The author-linked repository is https://github.com/U-CARFnet-Y/code1; inspected commit: `791d0760be35c88d7923c351af608396e0fb1b72`.

This is surface-mine image segmentation, not pre-blast P80 prediction in stoping; it is a related measurement/reproducibility case. The student must confirm exclusive paper selection within the class.

## Experimental setup and evidence
The publication describes TensorFlow 2.4, computer/GPU configuration and an 80/20 training/test division, with unlabeled images described as validation data (section 5.1). The clone contains 30 training images, 29 masks and five test images. `9.png` lacks a same-named training mask. No exact train/test image duplicates were found by SHA-256; that does not rule out transformed or event-related overlap. No requirements lock, HDF5 weights, LICENSE file or seed-setting occurrence was found in the inspected scripts/copy.

## Leakage check and statistical rigor
The paper describes augmentation. The available inventory does not establish independence of source images/events across partitions. This is unresolved risk, not demonstrated leakage. No complete multi-seed evaluation, paired statistical comparison, effect-size confidence interval or external-site validation was reproduced in this audit. A single reported accuracy is not copied as a new result.

## Actual execution attempt
The unchanged `U_CARFnet_train.py` startup returned exit code 1 with `ModuleNotFoundError: No module named 'tensorflow'` under Python3.12.14. README specifies tensorflow-gpu2.4.0, which was not installed in this audit environment. See evidence/startup.txt and inventory hashes. This environment-specific failure does not show that the historical environment cannot run the code. The missing-mask failure was not dynamically reached.

## Overall score and judgment
The nine course items are in audit_scorecard.csv. An explicit analyst convention assigns Yes=1, Partial=0.5 and No=0, yielding **2.5/9** for the inspected reproducibility documentation/evidence. This mapping is not a course grading rubric and is not a scientific-validity score. No means sufficient supporting evidence was not established within inspected materials; it does not prove the authors never performed the procedure.

**Judgment:** partial reproducibility support; reported metrics NOT reproduced.

## Three prioritized fixes
1. Provide a complete compatible environment, commands and version/hardware/runtime record; rerun in that environment.
2. Resolve the missing mask and dataset coverage, document original-image/event lineage and split before augmentation, and clarify reuse permissions.
3. Publish repeated-seed results, tuning separation and appropriate paired uncertainty/statistical reporting, plus an independently justified external test where feasible.

The repository datasheet states publication-use restrictions; no third-party images or source code are redistributed here. Raw company data are unrelated and were not accessed.
