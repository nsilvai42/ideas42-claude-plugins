# Quality Check Before Output

Run this before sending any audit. From `INSTRUCTIONS.pdf` §10, plus the two fidelity checks that
matter most in practice.

## Shape

- [ ] The six sections appear in order and are non-empty — unless the mode is `AUDIT_LITE`,
      `TAG_ONLY`, or `REDRAFT_ONLY`.
- [ ] Scorecard uses `✅ / ⚠️ / ❌` and `(Score: 5/3/1)` with one-sentence justifications; every stage
      carries a summary status.
- [ ] Table has ≤ 10 rows, `P1…Pn` sequential, with the exact columns and labels.
- [ ] Redraft block has a filename line; placeholders present where needed; tone fits.
- [ ] Validation checklist included, using `✅ + evidence` per applicable principle.
- [ ] Step 4 reflects the presence or absence of Key Information.
- [ ] Next Steps are either high-value items with their `ONLY_IF` triggers, or the explicit
      "No further strategic suggestions are needed."
- [ ] JSON Export is present and follows the schema.

## Fidelity — the two failures that damage trust

- [ ] **Every flagged quote appears verbatim in the source.** Copy-paste, don't retype. If the
      failure is an absence rather than defective text, say so in "Why It's a Problem" instead of
      inventing a quote.
- [ ] **No invented facts.** Every date, URL, contact, name, amount, and statistic in the redraft
      either appears in the source or is a bracketed `[Placeholder]`. Check each one individually.
      Never fabricate a social norm (principle 6) or a support contact (principle 10).

## Consistency

- [ ] Exact principle names used throughout, matching `framework.md`.
- [ ] JSON scores match the rendered scorecard.
- [ ] Every `P#` in Step 2 appears once in Step 3's "Summary of Key Changes".
- [ ] Essential facts from the source survive into the redraft.
- [ ] No follow-up question was asked.

## Mechanical confirmation

When a file is available:

```bash
python3 ~/.claude/skills/comms-auditor/assets/validate.py audit.json --source comm.txt
```

It checks the JSON shape, that scores are 5/3/1, that the table is within 10 rows and sequential,
that quotes are verbatim in the source, and that no unbracketed date, URL, phone number, or figure in
the redraft is absent from the source.

**What it cannot check:** whether a score is *right*. An audit that rates everything ✅ is well-formed
and wrong. That judgment stays with the reviewer.
