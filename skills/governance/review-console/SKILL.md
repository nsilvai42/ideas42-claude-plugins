---
name: review-console
description: Build a compact review console for comparing artifacts, decisions, skill candidates, drafts, evidence checks, or migration packages before acting.
---

# Review Console

Create a compact decision surface when the user needs to review multiple artifacts, candidates, claims, drafts, or migration choices without losing track of what still needs a human decision.

Use this skill when the user asks for a review console, decision console, review dashboard, comparison console, approval queue, artifact review surface, or a way to sort what to keep, revise, archive, approve, reject, or escalate.

## Core Behavior

1. **Start from the review object.** Identify what is being reviewed: skills, documents, claims, designs, data outputs, tasks, or migration artifacts.
2. **Separate facts from judgments.** Put objective details in one column and recommendation/rationale in another.
3. **Make the next action obvious.** Every row needs one recommended action: keep, revise, merge, archive, upload, provision, defer, or ask owner.
4. **Keep decisions reversible when possible.** Prefer archive/disable over delete unless the user explicitly asks for deletion.
5. **Flag missing source material.** If an expected item is not present, add it as a missing row instead of silently dropping it.

## Default Console Shape

Use a table unless an interactive artifact is explicitly useful.

```markdown
| Item | What it is | Status | Recommendation | Why | Owner / next action |
|---|---|---|---|---|---|
| [name] | [short description] | [ready / duplicate / missing / needs review] | [keep / revise / merge / archive / defer] | [reason] | [next step] |
```

## Review Modes

- **Migration review:** Compare old vs. new packages, show which item becomes canonical, and surface anything missing.
- **Skill review:** Evaluate trigger clarity, naming, redundancy, bundled resources, stale tool references, and upload readiness.
- **Evidence review:** List claims, verification status, source confidence, unresolved conflicts, and required human decisions.
- **Draft review:** Track sections, readiness, blocking questions, source gaps, and revision priority.
- **Design review:** Track screens/components, usability risks, accessibility issues, and acceptance checks.

## Output Rules

- Start with the console, not a long explanation.
- Include a short "missing or unresolved" section when anything expected is absent.
- End with one concrete next step for the user.
- Do not invent missing artifacts. If a named item cannot be found, say where you looked and mark it as missing.
