# Final Verification Memo Template

One-page summary for stakeholders. Lives at the top of the verification bundle.

## Header

```
Topic:       <project name>
Date:        <verification completion date>
Verifier:    <who / what — must specify that this is independent of the original analysis model>
Outputs:     <list of revised outputs, with "(Corrected)" suffix>
```

## TL;DR (3–5 bullets)

- How many claims were checked.
- How many replicated; how many required revision.
- The strongest finding from the original analysis that holds up.
- The one finding that was substantively revised (if any).
- The biggest remaining limitation.

## Scope

| Audit type | Run? | Coverage |
|---|---|---|
| Numerical verification | Yes / No | High-stakes only / all priority claims |
| Data-prep audit | Yes / No | Which fields |
| Analytical completeness audit | Yes / No | Which research questions |
| Interpretive overclaim audit | Yes / No | Exec summary, key takeaways, recommendations |
| Correction QA | Yes / No | All revised claims |

## Verification statistics

| Status | Count | % of priority claims |
|---|---|---|
| Replicated | | |
| Drift | | |
| Error | | |
| Unable | | |
| Method disagreement | | |
| Directional only | | |

## Key revisions

A short bulleted list — 5–10 max — of the revisions most likely to change a downstream decision.

## Findings that hold

A short bulleted list of the original headline findings that survived verification unchanged.

## Gates check

- [ ] No H-stakes Error / Unable rows are open.
- [ ] No unreviewed Method-disagreement rows on recommendation-driving claims.
- [ ] No cross-output inconsistencies on H-stakes claims.
- [ ] Data-prep audit passed for fields used in H-stakes claims.
- [ ] Every executive-summary interpretive claim traces to a verified numerical claim in the body.
- [ ] Corrections changelog matches the ledger.

## Sign-off

| Role | Name | Date |
|---|---|---|
| Verifier | | |
| Analyst (original) | | |
| Reviewer (human) | | |
| Publishing approver | | |
