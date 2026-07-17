# End-of-process summary template

The final user-facing artifact is `00_SUMMARY.md`. It lives at the root of the dated output folder and is the first thing a user (or future analyst) reads to understand what the skill did.

## Required sections

### 1. Headline

A 2–3 sentence top-line summary of who's in the sample, with the n and key composition stats. Match the "one-line sample summary" pattern from the narrative.

### 2. What I did

Bullet list of every major decision the skill made with the user, in order:
- Scope (what was included / excluded)
- PII handling decision
- Source-priority choices (if applicable)
- Subjective transformations applied (link to ledger)
- Variable role overrides (if any)
- Adaptive choices triggered (small-n, large-n, longitudinal, etc.)

### 3. Files produced

Outline of every file in the output folder, grouped by category:

```
Narrative & briefs
- 01_Sample-Description_Narrative.docx  — full write-up with embedded charts
- 02_Sample-Description_Brief.docx       — 1–2 page exec summary

Data
- 03_Data-Dictionary.csv                 — column glossary
- 04_Transformation-Ledger.csv           — every subjective decision
- 05_Numeric-Profile.csv                 — full numeric stats
- 06_Categorical-Profile.csv             — frequency tables
- 07_Quality-Metrics.csv                 — retention + missingness + cell sizes

Charts (charts/)
- 01_Chart_Geography.png
- ... (one per variable family)

Optional outputs (if requested)
- 08_Methods-Boilerplate.docx
- 09_Sample-Description_Public.docx       — public-safe variant
- 10_Verification.md                      — spot-check results
```

### 4. What this skill did NOT do

Be explicit about what's out of scope, so users don't expect more than was delivered:
- Did not analyze response distributions
- Did not run inferential statistics
- Did not produce a final report (use the narrative as a starting point)
- Did not upload anything to the cloud (staged for manual drag-and-drop unless user authorized API upload)

### 5. Recommended next actions

- **Upload to project folder.** Recommend uploading the entire dated output folder to the project's shared Drive/Box/OneDrive location. Also recommend uploading the raw + intermediate + cleaned datasets so future analysts can reproduce.
- **Review the transformation ledger.** Even if every transformation was approved at the time, a fresh look before sharing is useful.
- **Read the limitations section** in the narrative — make sure the audience understands sample skews.
- **Consider follow-up workflows:** response-distribution analysis, segment crosstabs, regression modeling, etc. — point the user toward the right next skill if obvious.

### 6. Reproducibility info (small footer)

- Skill version
- Date the skill ran
- Input dataset path + file size + row count
- Output folder path
- (Optional) Random seed used for any sampling

## Tone and format

- Plain markdown, no inline images (this is a memo, not a deliverable)
- Sentences over bullets where it improves reading; bullets where it's a list
- Address the user in second person ("You asked for ...", "I recommend ...")
- No emojis unless the user's CLAUDE.md indicates they want them

## Example opener

```markdown
# Sample description — [Project Name] — [Date]

**Headline:** The cleaned analytic sample is 314 U.S. adults aged 25–65 (mean 39.6), 60% female, 72% white, with 17% Californian. 64% earn under $50K and 93% have at most some college — appropriate for the affordability research question.

## What I did

You asked me to describe the sample (demographics, quality, and behavioral traits) and produce a long-form .docx, executive brief, individual charts, CSV profile, and data dictionary using the ideas42 brand.

Key decisions, in order:
- Scope confirmed at: demographics + quality metrics + behavioral traits. Response distributions explicitly out of scope.
- 3 PII columns detected (IPAddress, LocationLatitude, LocationLongitude). You provided authorization to proceed; PII excluded from all outputs.
- 2 source-overlap pairs reconciled:
  - Income: Qualtrics primary (study-time, study-relevant categories)
  - Education: Qualtrics primary (Prolific reflects screening filter)
- 4 subjective transformations approved (see Transformation Ledger):
  - Employment "Other" write-ins → "Not in labor force" bucket (23 rows)
  - Age binned into 6 buckets (25–34, 35–44, 45–54, 55–64, 65+)
  - Ethnicity collapsed to White / Black / Mixed / Other / Asian / Prefer-not-to-say
  - State rolled up to 4-region Census classification
- Verification: 19 of 19 headline numbers reconcile with raw data ✓
```
