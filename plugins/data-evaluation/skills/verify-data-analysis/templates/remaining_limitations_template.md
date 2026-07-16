# Remaining Limitations Note Template

Documents what is *still* untested after the verification pass. Distinguishes verification limitations (things verification didn't catch) from study limitations (things the original study can't tell you).

## Sections

### Purpose

Two sentences: what this note covers, and what it doesn't.

### Limitations of the data itself

Original-study limitations that the verification pass does not change. Common buckets:

- Stated preference vs. behavioral. (Survey-based work.)
- Sampling: recruitment frame, screener-vs-self-report mismatch, demographic skew.
- Statistical power for subgroup cuts.
- Real-money / brand-specific effects not captured.
- Time-bounded fielding window.

### Limitations of the qualitative coding

What the open-text theme audit (if run) clears for precise reporting, and what stays directional. If no theme audit was run, this section says so explicitly and lists the affected claims.

### Limitations of the subgroup analyses

Small subgroups (n < ~30), exploratory cuts, power constraints on key contrasts.

### Limitations of the study design

Order effects, anchor effects, prompt phrasing, brand naming, etc.

### What was verified vs. what remains untested

A short table:

| Category | Verified | Untested |
|---|---|---|
| Fixed-choice descriptive stats | All H-stakes recomputed against clean.csv | — |
| Derived statistics (medians, intersections) | All H-stakes recomputed | — |
| Subgroup splits | Recomputed with corrected denominators | Small-n contrasts not powered |
| Multi-select / parsing | Re-parsed with corrected rules | — |
| Qualitative themes | Theme counts replicate from analysis.json | Theme validity (regex correctness) directional unless coding audit completed |
| Interpretive claims | Reviewed for overclaim | Real-world behavior unverified |
| Recommendations | Each recommendation traced to ≥1 supporting verified claim | Whether the recommendation will work in deployment |

### Recommended next steps

- One concrete next study / replication.
- One pre-publication ask (e.g., commission a coding audit if theme counts will be public).
- One generalization caveat (when other institutions could / couldn't reuse the findings).
