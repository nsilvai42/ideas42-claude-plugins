---
name: comms-auditor
description: Audit recipient-facing communications against ideas42's behavioral communications framework — 10 principles across Attention, Intention, and Action — producing a scorecard, a severity-ranked findings table, a polished redraft, and a machine-readable JSON export. Use for auditing or reviewing a single communication (email, SMS, chat message, call script, landing page, flyer) or an entire campaign or comms sequence; for behavioral reviews of student-, learner-, client-, or participant-facing messaging; for scoring comms against behavioral science best practices; for redrafting a message to be clearer, more actionable, or more likely to drive follow-through; and for cross-comm analysis of cadence, consistency, redundancy, and journey coverage. Triggers on "audit this email", "comms audit", "behavioral review", "score this message", "review our outreach", "campaign audit", "redraft this comm", "is this message effective".
---

# Comms Auditor

Audits communications against ideas42's behavioral communications framework. It follows a fixed
process and a fixed output shape, so every audit is **consistent and comparable across projects** and
the JSON export can feed trackers and dashboards.

## Core rules

1. **Follow the schemas exactly and in order.** `references/single-comm.md` is authoritative for
   output shape.
2. **One communication per run.** If several are provided, say so, audit the first, and list the rest
   as queued.
3. **Never ask a follow-up question.** All uncertainty goes in Step 4.
4. **Preserve essential facts** — names, dates, URLs, contacts. Use `[placeholders]` if missing.
5. **Never invent** a deadline, support contact, URL, or statistic.
6. **Quote flagged text verbatim.** Copy-paste; never retype or paraphrase.
7. **Use the exact principle names** from `references/framework.md`.
8. **Max 10 rows** in the Step-2 table; prioritize highest severity.
9. Redraft tone: recipient-facing, professional, warm. Active voice, short sentences.

## Modes

| Say | Mode | Output |
|---|---|---|
| *(nothing)* | `AUDIT_LITE` *(default)* | Steps 1–2, plus 4 if key info is missing |
| "full audit" / "continue" | `AUDIT` | Steps 1–6 |
| "tag only" | `TAG_ONLY` | Steps 2, 4, 6 |
| "redraft only" | `REDRAFT_ONLY` | Steps 3, 5 |
| "campaign scan" | `CAMPAIGN_SCAN` | C1–C2, then Steps 1–2 for every comm |
| "campaign audit" | `CAMPAIGN_FULL` | C1–C6, then Steps 1–2 for every comm |

`OUTPUT_PROFILE` is a session preference: `LITE` (default) · `FULL` · `REDRAFT_FOCUS`. If a mode
conflicts with it, the mode wins.

**Batching.** Rubric-driven steps (1, 2, 4, 6 and C1–C6) may batch across every comm in one run.
Step 3 (redraft) is **one comm per run** unless the user says "redraft all".

## The framework

Ten principles across three stages. Score each **5 / 3 / 1** (`✅ / ⚠️ / ❌`) with a one-sentence
justification citing concrete elements of the message.

| Attention | Intention | Action |
|---|---|---|
| Salience · Relevance & Personalization · Credibility & Identity Alignment | Clarity, Simplicity & Brevity · Support & Self-Efficacy · Social · Persuasion & Cost-Benefit Value | Clear Call-to-Action & Focus · Ease & Hassle Reduction · Timeliness & Urgency |

## Procedure

**Single communication**
1. Read `references/framework.md` — the principles, their tactics, the severity guidance, and the
   channel heuristics.
2. Read `references/single-comm.md`. Emit the steps the active mode calls for, in order.
3. Run `references/quality-check.md` before sending.
4. Where files exist, confirm mechanically:
   `python3 assets/validate.py audit.json --source comm.txt`

**Campaign**
1. Build the C1 inventory first — it fixes the Comm IDs everything else references.
2. Score all 10 principles for every comm (batched).
3. Read `references/campaign.md` and run C2–C6, which diagnose what single-comm audits cannot see.
4. Emit C6, then the per-comm Steps 1–2.

## Files

| File | Read it when |
|---|---|
| `references/framework.md` | **always** — the 10 principles, severity, channel heuristics, do/don't |
| `references/single-comm.md` | emitting Steps 1–6 |
| `references/campaign.md` | any campaign mode |
| `references/quality-check.md` | **always, before emitting** |
| `references/worked-example.md` | to anchor tone and shape on a real audit |
| `assets/audit.schema.json` · `assets/campaign.schema.json` | the JSON contracts |
| `assets/validate.py` | verifying an emitted audit |
| `assets/templates/` | submission template, campaign tracker, deliverable outline |

## A caution

This tool assists a human reviewer; it does not replace one. Verify its output — check especially
that it has not misapplied a principle (social norms that backfire are the classic case) or invented
a detail the source never contained.

Source material may contain PII or credentials. Redact before auditing, and note the redaction in
Step 4.
