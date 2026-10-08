# Phase 5 — Final report template

Use this exact structure. Cap each item at ~3 sentences. Every item carries a vote label: **(Unanimous)**, **(Majority)**, **(Mixed Opinions — owner call)**; rejected recommendations don't appear outside Verification notes. Items name file:line / selector / page references inline.

```markdown
# Review Council — {artifact name}
_{date} · Artifact: {scope one-liner} · Reviewed in source {and rendered at {URL/viewer}, or
"source only — rendered output not inspected"} · Three reviewers (Visual/Structural,
UX/Behavioral, Content/IA), verification pass, vote-labeled synthesis._

**Project checks:** {results of the repo's own QA scripts, or "none available"}
**Focus question answered:** {1–3 sentences directly answering the owner's focus question}

## 1. Launch-Critical Changes (before {milestone})
{Numbered. Visible breakage, placeholder content, dead CTAs, state bugs, trust damage —
per the scoped severity bar. Each: what/where (file:line), why, fix, vote label.}

## 2. High-Value Improvements
{Numbered. Strongly recommended, not gating. Same per-item format.}

## 3. Nice-to-Have Improvements
{Bulleted, one line each. Can wait an iteration.}

## 4. Cross-Section Consistency Fixes
{Table: # | Element | State in section A | State in section B | Canonical / fix.
This is where the declared canonical reference does its work — every row has a direction.}

## 5. Top 10 Recommended Edits (Impact ÷ Effort, highest first)
{Ranked list referencing the section numbers above. One line each: edit + why it ranks here.
List owner-decision (Mixed) items separately at the bottom, unranked.}

## 6. Verification notes
{Two short lists: ✅ Confirmed — claims checked and held (with how they were checked).
❌ Rejected — reviewer claims that failed verification, with the evidence. Showing
rejections is what makes the rest of the report trustworthy.}
```

## Delivery checklist

1. Save the report into the project's audit-doc location (e.g., `01_Context/` in six-folder projects) as `review-council-{artifact-slug}-{YYYY-MM-DD}.md`.
2. Present the file to the user.
3. If the project keeps a status/tasks doc, add one line pointing at the report.
4. Offer to apply the trivial fixes (≤~5-line diffs) as a batch on the project's working branch — with approval, never unprompted. Respect the project's branch workflow (never commit to a protected branch).
5. Chat summary: headlines only — the launch-critical count and themes, the focus-question answer, and the offer. The user can read the report for the rest.
```
