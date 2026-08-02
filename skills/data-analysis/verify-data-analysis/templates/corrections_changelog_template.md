# Corrections Changelog Template

One entry per revised claim. The changelog is the cross-output index that proves every correction was applied consistently.

## Header

| Field | Example |
|---|---|
| Topic | Calbright Affordability Pilot |
| Verification date | 2026-05-19 |
| Verifier | Independent Claude pass against clean.csv + analysis.json |
| Outputs revised | Findings Report (Corrected).docx; Findings Dashboard (Corrected).html |
| Total claims verified | 126 (of 235 in master ledger; priority subset) |
| Replicated | 115 |
| Drift | 1 |
| Error | 5 |
| Method disagreement | 5 |
| Unable | 0 |
| Total revisions applied | 11 |

## Per-claim entry template

```
### CL-### — [status: Error / Drift / Method disagreement / Directional only]

Location: <section / chart / paragraph reference>

Issue:
<one paragraph describing the discrepancy, the original value, the verifier value, and why the original was wrong>

Fix applied:
<one paragraph describing what was changed in the output: new value, new wording, or new caveat>

Outputs changed:
<comma-separated list of file:section pairs, e.g., "Report §3.2; Dashboard RQ2 takeaway; Exec summary card 3; analysis.json phase2.confidence_factors">

Verifier note:
<verbatim from ledger row, optional>

Human reviewer note:
<verbatim from ledger row, optional>
```

## Verification-process notes (final section)

Always include short notes covering:

- Replicated rows: no edits required.
- Open-text / theme-coded rows: kept directional (or, if audited, the audit result).
- No new numerical claims introduced.
- Multi-select / parsing fixes documented in the Methods section.
- A short verification note added to the Methods section of the corrected outputs.

## Style

- One entry per claim, ordered by claim_id (or stakes-then-claim_id).
- Use the exact wording from `recommended_fix` (with any human edits) when describing the fix.
- Outputs-changed list must be exhaustive — if the corrected number appears in chart captions, exec summary cards, or appendix tables, those are listed too.
