# Elicitation templates

Canonical user-prompt patterns. **Default to the `visualize` MCP elicitation form** (`interactive elicitation tool`); fall back to `structured-question interface` if visualize is unavailable.

Always mark the best-practice default option with `(Recommended)` in the label text.

## interactive visualization capability usage

Before the first form, call:
```
tool schema reader({ modules: ["elicitation"], platform: "desktop" })
```
to load the form schema.

Form structure follows the locked elicitation shell: header (always `"[Subject] details"`), body with `.elicit-group` blocks, footer with Skip + Continue. Within each group, vary the visual format — pills, cards, preview tiles, range, date, file dropzone, textarea — based on what the question is asking. Don't render every question as plain pills.

## Form 1 — Scope check (run at Step 0, every time)

Header: "Sample description details"

Groups:
1. **What should this sample description cover?** (multi-select cards)
   - "Who the respondents are" (demographics) — (Recommended) — default on
   - "Sample quality metrics" (retention, attention, missingness) — (Recommended) — default on
   - "Behavioral / contextual traits" — default on
   - "Response distributions" — default off; warn this is out of scope for this skill

2. **Which demographics matter most for this study?** (multi-select pills, populated from detected columns)
   - All detected demographic columns listed
   - Mark "(important)" placeholder lets the user flag 1–3 as headline

3. **What deliverables do you want?** (multi-select cards)
   - Long-form narrative .docx — (Recommended)
   - Executive brief .docx — (Recommended)
   - Individual chart PNGs — (Recommended)
   - CSV profile tables — (Recommended)
   - Data dictionary CSV — (Recommended)
   - Methods boilerplate paragraph — default off
   - Public-safe variant (cell suppression + PII strip) — default off
   - Overview grid PNG — default off if n > 5000

4. **Is there benchmark or prior-wave data to compare against?** (single pill + optional file)
   - No, skip benchmarking — (Recommended) default
   - Yes — upload reference distribution
   - Yes — prior-wave data available in another folder (textarea for path)

5. **Are there any split-by columns I should adapt to?** (single pill + multi-select)
   - None — (Recommended) default
   - Treatment / arm column → name it
   - Site / cohort / wave column → name it
   - Specific demographic split → pick from list

6. **What's the study context?** (single pill, affects framing)
   - Behavioral research / survey — (Recommended)
   - Clinical / health
   - HR / employee
   - Marketing / consumer
   - Other (free text)

## Form 2 — Column role confirmation (Step 1, after profiling)

Header: "Column roles"

Show the auto-classified roles and ask the user to confirm/adjust:

- Pre-populated multi-select pills per role:
  - Demographic
  - Behavioral / contextual
  - Quality flag
  - Treatment / arm
  - Outcome (exclude from sample description)
  - Metadata
  - PII candidate (always show separately; default to "exclude until authorized")

User can drag columns between buckets in their head (since the form is single-render); for any column they want to re-classify, they pick it from the list and reassign.

## Form 3 — PII authorization (Step 1, if PII detected)

Header: "PII detected"

Layout: clear, short.

Group 1: list the PII-candidate columns with non-null counts.

Group 2: single-pill action:
- Drop the PII columns and proceed — (Recommended)
- Keep, but never display values in outputs
- I have authorization; proceed with full data
- Pause; I need to investigate

If user picks "I have authorization", check for an authorization code per their user preferences if applicable.

## Form 4 — Source priority (Step 2, only if multi-source overlap detected)

Header: "Source priorities"

For each detected overlap, one group:

> "I see `qualtrics_income` and `prolific_income` capture the same construct. Which should be the primary source?"

Pills:
- `qualtrics_income` (study-time, n non-null = X)
- `prolific_income` (signup-time, n non-null = Y)
- Average / reconcile across both — define rule
- Keep both, don't pick — show both in outputs

Optionally append: disagreement rate ("17% of rows disagree by > $20K") so the user can judge.

## Form 5 — Transformation approval (Step 3, every subjective transformation)

Header: "Transformation: [column]"

Group 1: the proposed rule, in plain language.

Group 2: 3 random examples (table or cards):
> `original_value` → `proposed_value`

Group 3: action pill, single select:
- Approve — (Recommended)
- Adjust (free text for the new rule)
- Skip this transformation

## Form 6 — Final upload prompt (Step 9, after summary)

Header: "Deliver to cloud folder"

Group 1: single pill action:
- Stage in local folder for manual drag-and-drop — (Recommended) — works for files of any size
- Try API upload via [detected connector]
- Skip cloud upload; keep local only

If user picks "API upload", warn that large binaries may fail and offer to fall back to drag.

## Fallback (structured-question interface)

If interactive visualization capability is unavailable, use structured-question interface with the same question hierarchy. Compress to ≤4 questions per call; pull "(Recommended)" labels through to the option text.

## Defaults if user skips

If the user clicks Skip on any form:
- Scope check → assume demographics + quality + behavioral; default deliverables; English; no benchmark; no split-by; behavioral-research context
- Role confirmation → use auto-classification as-is
- PII → drop PII columns (do not proceed with raw PII values without explicit auth)
- Source priority → ask once more; if skipped again, pick the study-time source for each overlap
- Transformation approval → DO NOT auto-apply subjective transformations; document them in the ledger as "skipped pending approval"
- Final upload → stage locally for manual drag-and-drop
