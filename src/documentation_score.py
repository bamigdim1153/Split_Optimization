# Adapted from the supplied Session 7 course notebook, Exercise 6.
# Completeness check only; not a validation, grading or conformity certificate.
def score_documentation(model_card, datasheet):
    checks = []

    def add(label, passed, why=''):
        checks.append((label, bool(passed), why))

    def flatten(card):
        parts = []
        for fields in card.values():
            for k, v in fields.items():
                parts.append(str(k).lower())
                parts.append(str(v).lower())
        return ' '.join(parts)
    flat_mc = flatten(model_card)
    flat_ds = flatten(datasheet)
    add('Model Card has all 9 sections', len(model_card) == 9)
    add('Datasheet has all 7 sections', len(datasheet) == 7)
    add('Intended MISUSE / out-of-scope stated', 'not for' in flat_mc or 'out-of-scope' in flat_mc or 'should not' in flat_mc)
    add('Performance reported with variation (± / std / seeds)', '±' in flat_mc or 'std' in flat_mc or 'seed' in flat_mc)
    add('Metrics disaggregated (per-class / per-group)', 'per-class' in flat_mc or 'per class' in flat_mc or 'disaggreg' in flat_mc)
    add("Dataset 'should NOT be used for' stated", 'should not be used' in flat_ds or 'not for' in flat_ds)
    add('Collection process described', len(datasheet['Collection process']) > 0 and 'how collected' in ' '.join(datasheet['Collection process'].keys()).lower())
    add("Gaps flagged honestly ('unknown')", 'unknown' in flat_mc or 'unknown' in flat_ds, "Flagging what you don't know beats a confident blank.")
    passed = sum((1 for _, p, _ in checks if p))
    tick, cross = ('✓', '✗')
    print('DOCUMENTATION SCORECARD')
    print('=' * 52)
    for label, p, why in checks:
        mark = tick if p else cross
        print('[' + mark + '] ' + label)
        if why and (not p):
            print('      hint: ' + why)
    print('=' * 52)
    pct = 100 * passed / len(checks)
    print(f'Score: {passed}/{len(checks)}  ({pct:.0f}%)')
    if pct == 100:
        print('Submission-ready. A stranger could understand and re-run this.')
    elif pct >= 75:
        print('Close — fix the unchecked items before Wednesday.')
    else:
        print('Keep going: the unchecked items are where reviewers (and regulators) look first.')
    return (passed, len(checks))
