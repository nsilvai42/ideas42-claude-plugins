# Adaptive chart selection

The chart battery is not fixed — it adapts to what's in the dataset and what the user said matters in Step 0. This file describes the selection logic and the canonical chart templates.

## Selection logic

For each variable family the user confirmed is in scope, decide whether to render and which template to use.

### Variable families and default chart types

| Family | Trigger columns | Default chart |
|---|---|---|
| **Geography** | state, country, ZIP, region | Top-N bar; highlight user-flagged "key region" in brand accent color |
| **Age** | age (continuous) | Histogram + mean/median lines + bucket inset |
| **Sex / Gender** | sex, gender | Donut (3 categories or fewer) OR bar (4+ categories) |
| **Income** | income, household_income | Ordered horizontal bar (low → high); highlight "key threshold" segment (default sub-$50K) |
| **Education** | education, edu_level | Ordered horizontal bar; highlight modal buckets |
| **Employment** | employment, work_status | Horizontal bar; semantic color coding (working = brand-green, unemployed = brand-warning) |
| **Ethnicity / Race** | ethnicity, race | Bar with cautionary note if cells < 10 |
| **Origin / Nationality / Language** | nationality, country_of_origin, language | Composition bars (US/non-US, English/non-English) |
| **Behavioral / Contextual** | caregiver, prior_*, goals | 3-panel small-multiple if 3+ vars in family |

If a family has just one variable, render a single chart. If 2 closely related variables (e.g., age + sex), render a side-by-side panel. If 3+ closely related (e.g., behavioral cluster), render small multiples.

### Combinatorial rules

- Pair age + sex if both exist
- Pair income + education if both exist (socioeconomic panel)
- Group caregiver + prior_experience + goals into a "learner orientation" panel if all three exist; otherwise keep separate

### Cardinality-based template overrides

| Condition | Override |
|---|---|
| Variable has 2 categories | Donut OR a single horizontal bar (whichever the brand prefers) |
| 3–4 categories | Donut acceptable |
| 5–8 categories | Horizontal bar, ordered |
| 9+ categories | Top-N bar with "Other (N more)" aggregated row |
| Continuous | Histogram + mean/median (per `variable-types-and-stats.md`) |
| Continuous, n > 1000 | Add KDE overlay |

## Universal chart styling (any brand)

Every chart, regardless of brand, must include:

- **Descriptive title** — state the finding, not just the metric ("64% of sample earns under $50K" not "Income distribution")
- **n caption** — every chart shows the n it's based on, plus any filter applied
- **Source footer** — small italic line: "Source: [study name], [dates] · n = ___"
- **Value labels** — n and % next to each bar
- **Highlight color used meaningfully** — never decoratively; always to draw attention to the takeaway

## Brand-specific styling

Load the active brand JSON from `assets/brand-defaults/<brand>.json`. Apply:
- Font family (with fallback chain)
- Palette: primary, accent, neutral, warning
- Title color, body color, grid color
- Logo placement (if brand JSON specifies)

For ideas42 default:
- Font: Figtree (load from `assets/fonts/`)
- Title color: Indigo `#004357`
- Primary chart fill: Indigo `#004357`
- Accent / highlight: Green Apple `#7AC10A`
- Warning / negative: Cayenne `#EF6A00`
- Grid: Rain `#D9E1E2`
- Body text: dark grey `#3A3A3A`

## Adaptation triggers

These adapt the WHOLE chart battery, not just one chart.

### Small sample (n < 100)
- Every chart caption appends: "Small-sample caveat: estimates may be noisy."
- Skip charts where any category has n < 5

### Large sample (n > 5000)
- Skip the overview grid by default (it gets too dense)
- Collapse categorical charts to top-10 + Other
- Use sampling for histograms if n > 50,000

### Longitudinal data (wave/timepoint column present)
- Every demographic chart gets a small-multiple version split by wave
- Overall comparison: how did the sample composition shift across waves?

### Treatment arm detected
- Stratify each headline chart by arm
- Add an "Arm composition" chart showing arm sizes and demographic balance

### Multi-source data
- For variables that exist in both sources, render with the chosen "primary" source value; show the secondary as a faint overlay or note
- Document source choice in the chart caption ("Source: Qualtrics primary; Prolific shown for comparison")

## What to produce

For each chart:
1. A standalone PNG at 200 DPI in `charts/`
2. Width: 11–14 inches at 200 DPI (~2200–2800 px); panel charts can go wider
3. Filename: `NN_Chart_<Topic-Name>.png` — numeric prefix preserves intended display order

Always produce in addition:
- An overview grid PNG (2 columns × N rows) of all charts — unless n > 5000 or user opted out
- An individual SVG copy of each chart (optional — emit only if user requested vector outputs)

## Things NOT to do

- Pie charts (use donuts or bars)
- 3D effects of any kind
- Truncated y-axes on bar charts (zero baseline always)
- Encoding the same dimension twice (e.g., color + position for the same variable)
- Combining unrelated families into one chart for compactness
- Stacked bars for nominal categories that don't sum meaningfully

## Caption template

Every chart caption (placed below the chart, italics, neutral color):

> [Variable family name]. [Brief source note, e.g., "Qualtrics."] n = [N]. [Optional small-sample caveat or filter note.]

Example:
> Educational attainment (Qualtrics). n = 314. 1 "prefer-not-to-say" excluded.
