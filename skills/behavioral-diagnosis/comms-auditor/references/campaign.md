# Campaign Protocol — Steps C1–C6

A campaign audit is not a stack of single-comm audits. C2–C5 diagnose properties that only exist
*between* comms — and they are where **Credibility & Identity Alignment**'s "maintain consistency
across offices" finally becomes checkable.

| Mode | Output | C3–C6? |
|---|---|---|
| `CAMPAIGN_SCAN` | C1, C2, then Steps 1–2 for every comm | no |
| `CAMPAIGN_FULL` | C1–C6, then Steps 1–2 for every comm; redrafts on request | yes |

**Batching.** C1–C6 and Steps 1, 2, 4, 6 may batch across all comms in one run. Step 3 redrafts stay
one comm per run unless the user says "redraft all". After a batched scan, end with:
`Next: say "redraft <Comm ID>" for a rewrite, or "redraft all" to override one-at-a-time pacing.`

---

## C1 — Campaign Inventory & Tracker

`Comm ID | Label | Channel | Audience Segment | Trigger / Timing | Owner | Source | Status`

- `Comm ID` = `C01`, `C02`, … in journey order where known, else source order.
- Unknown fields get `[Unknown]` — never guessed.
- `Status` ∈ `scanned` · `audited` · `redrafted` · `queued`.
- The inventory fixes the ID space; every comm referenced in C2–C6 must appear here.

---

## C2 — Sequence & Cadence Map

A timeline of comms against the recipient journey, then flags. Name the comm IDs involved and the
threshold you used.

| Flag | Condition |
|---|---|
| `SILENT-GAP` | a long stretch with no contact immediately before a deadline or required action |
| `CLUSTER` | several messages to the same recipient within a day or two |
| `ORPHAN` | a comm assuming context no prior comm established |
| `NO-CONFIRM` | a completed action with no acknowledgement |
| `NO-RECOVERY` | a missable deadline or appointment with no follow-up for those who missed it |
| `IRREGULAR-CADENCE` | recurring comms of one type arriving on an unpredictable rhythm |
| `UNKNOWN-TIMING` | send timing unavailable — reduces confidence; never guess a schedule |

Where timing is missing, list it under `UNKNOWN-TIMING` rather than inferring a schedule.

---

## C3 — Cross-Comm Consistency Register

`Conflict ID | Type | Comm A (quote) | Comm B (quote) | Impact | Resolution`

- `Conflict ID` = `X1`, `X2`, … unique.
- `Type` ∈ `TERMINOLOGY` · `DATE` · `INSTRUCTION` · `SENDER` · `TONE` · `CALENDAR`
- **Both** quotes verbatim, each attributed to its Comm ID. A conflict with one quote is not a
  conflict — drop it. `Comm A` and `Comm B` must be different comms.
- `Resolution` names which version wins and why.

A terminology or date conflict is a **Credibility & Identity Alignment** failure in both comms named.
Re-score that principle for each and note in C6 whose Attention summary changed.

---

## C4 — Redundancy & Load

| Metric | Definition |
|---|---|
| Duplicate asks | the same action requested in ≥2 comms with no acknowledgement of the repeat |
| Repeated information | substantially identical content blocks across comms |
| Ask load | distinct actions requested per recipient per week |
| Channel load | comms per recipient per week, by channel |

Redundancy isn't automatically bad. Deliberate reinforcement of one high-stakes ask is
`REINFORCEMENT`, not `DUPLICATE` — classify each explicitly and say which it is.

---

## C5 — Journey Coverage Matrix

Journey stages as rows, comm IDs as columns, `●` where a comm serves that stage. Then:

- **Uncovered stages** — a journey stage with no comm.
- **Uncovered failure paths** — for each required action, is there a comm for the recipient who did
  *not* do it? Name every missing recovery path.
- **Over-served stages** — a stage crowded with comms while another has none.

If the journey isn't supplied, derive stages from the comms and label the matrix
`Derived journey — confirm with partner.`

---

## C6 — Campaign Scorecard & Roadmap

### Rolled-up scorecard

`Comm ID | Label | Attention | Intention | Action | Overall | Status`

Use the stage summary statuses from each comm's Step 1.

### Pattern rollup

`Pattern ID | Principle | Failing Comms | Frequency | Severity | Priority`

- `Frequency` = failing comms ÷ total comms in the inventory.
- Sort by severity, then frequency. A principle failing in most of the campaign is a systems problem,
  not a copy problem.
- `Failing Comms` must be corroborated by those comms' own Step-2 tables.

### Prioritized roadmap

- **Quick wins** — copy-level fixes, per comm, no process change needed.
- **Structural fixes** — anything needing a new sender, channel, segment, system, or schedule.
- **Template proposals** — for any principle failing across several comms, propose the reusable
  pattern. This is the `Meta-Level Suggestion` trigger from Step 5, at campaign scale.

### Campaign JSON

One fenced `json` block conforming to `assets/campaign.schema.json`: the campaign object plus the
full per-comm audit objects.

```bash
python3 ~/.claude/skills/comms-auditor/assets/validate.py campaign.json --campaign --source-dir <dir>
```
