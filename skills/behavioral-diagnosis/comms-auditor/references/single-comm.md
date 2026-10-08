# Single-Comm Protocol — Steps 1–6

Emit only the steps the active mode calls for, always in numeric order, using these exact headings.

| Mode | Steps |
|---|---|
| `AUDIT_LITE` *(default)* | 1, 2, plus 4 only if key info is missing |
| `AUDIT` | 1, 2, 3, 4, 5, 6 |
| `TAG_ONLY` | 2, 4, 6 |
| `REDRAFT_ONLY` | 3, 5 |

`AUDIT_LITE` ends with exactly:
`Next: say "continue" for Steps 3–6, or "redraft" for Step 3 only.`

---

## 1. Executive Summary & Behavioral Scorecard

One paragraph (2–4 sentences) on overall effectiveness: what works, what doesn't, and the single
biggest lever.

Then the scorecard — three stage blocks, each with a stage summary status, then its principles:

```
### Stage 1: Attention (Summary: ⚠️)
1. Salience: ❌ (Score: 1) — Subject line is the program name only, and the button sits below a
   five-step list.
2. Relevance & Personalization: ✅ (Score: 5) — Opens with the recipient's name and the application
   they just completed.
3. Credibility & Identity Alignment: ❌ (Score: 1) — Signed by a team, not a person; no name anywhere.
```

Repeat for **Stage 2: Intention** (principles 4–7) and **Stage 3: Action** (principles 8–10).

Justifications are one sentence and must reference concrete elements of the message — never restate
the principle name.

---

## 2. Behavioral Analysis Table

Columns, in this exact order:

`Problem ID | Principle/Deficit | Severity (High/Medium/Low) | Flagged Quote | Why It's a Problem | Recommended Revision`

- `Problem ID` = `P1`, `P2`, `P3`, … sequential.
- `Principle/Deficit` uses the exact principle name, numbered: `8. Clear Call-to-Action & Focus`.
- Quote the exact text that triggers the issue, verbatim.
- `Why It's a Problem` names the behavioral mechanism, not just the rule.
- `Recommended Revision` is behaviorally specific and paste-ready.
- **Max 10 rows**, prioritizing higher severity. If you dropped any, add one line below the table:
  `N additional lower-severity findings omitted (max 10).`

### Mini example

> **Problem ID:** P1
> **Principle/Deficit:** 8. Clear Call-to-Action & Focus
> **Severity:** High
> **Flagged Quote:** "…register, meet your advisor, and check aid…"
> **Why It's a Problem:** Multiple CTAs create choice overload and reduce follow-through.
> **Recommended Revision:** Focus on a single CTA — "Register for Fall 2025 Classes" with a
> [Register Now] link at top.

---

## 3. Revised Communication & Final Validation

### 3A — Rewrite

A fenced Markdown block (or a Canvas document where the environment supports one — preferred, for
easier review and editing). The first line inside the block, or the Canvas title, is a filename in
square brackets. Include the subject line if it's an email.

````
```
[DRAFT_EMAIL_Register_By_Deadline.md]
Subject: Action Needed: Register for Fall 2025 by [Deadline]

Dear [First Name],

You're almost ready to start classes. Please register for your Fall 2025 classes by [Deadline].
It takes ~10 minutes.

👉 Register now: [URL]

If you already chose classes, you can finish faster by confirming your picks on the next screen.

Need help? Reply to this email or call [Support Number] during [Hours].

— [Advisor Name], [Office/Program]
```
````

Rules:
- Keep every essential fact: names, dates, URLs, contacts, amounts.
- Use `[Deadline]`, `[URL]`, `[Program Name]`, `[Support Contact]` for anything missing.
  **Never invent one.**
- Recipient-facing, professional, warm. Active voice, short sentences.
- The rewrite should resolve every High-severity finding. If one can't be fixed in copy alone (wrong
  channel, wrong sender), say so and route it to Step 5.

After the block: **Summary of Key Changes** — a list mapping each `Problem ID` to what changed.

```
- P1 → Single, top-placed CTA with direct link and deadline.
- P2 → Removed competing CTAs; simplified copy; added support info.
```

### 3B — Final Validation Checklist

Heading: `Final Validation Checklist`. For each **applicable** principle, one line prefixed `✅` with
a short evidence clause:

```
- ✅ Salience: CTA appears in first paragraph and includes [URL].
```

---

## 4. Assumptions & Missing Information

- No Key Information supplied → list the assumptions made and the gaps.
- Key Information supplied → list only the remaining questions.
- Nothing missing → `No assumptions needed.`
- List every placeholder used in Step 3 and the fact that would fill it.

**Never request a follow-up.** All clarifications appear here.

---

## 5. Suggested Next Steps

High-value items only; otherwise state exactly:
`No further strategic suggestions are needed.`

Conditional offers, with their triggers and canonical text:

| Trigger | Say |
|---|---|
| Original was designed HTML | *"This email could be enhanced with visual design. If you'd like an HTML mockup, provide brand HEX colors and logo."* |
| Content–channel mismatch | *"This message is better suited for SMS. Would you like an SMS draft?"* |
| Sender credibility is weak | *"This message may be more effective from a named sender. Should I adjust the tone to reflect that?"* |
| A recurring pattern suggests a template or design system | *"Repeated issues suggest a reusable template. Want me to propose one?"* |

---

## 6. JSON Export

A single fenced `json` block at the very end, conforming to `assets/audit.schema.json`. Ten principle
scores, grouped by stage, each `5`, `3`, `1`, or `null` where a principle does not apply.

`processing_timestamp` is `null` on emit — the validator stamps it.

Validate with:

```bash
python3 ~/.claude/skills/comms-auditor/assets/validate.py audit.json --source comm.txt
```

---

## Conflict resolution

If these schemas and the framework file disagree on **formatting**, follow the schemas here. For
**rationale and tactics**, `framework.md` governs.
