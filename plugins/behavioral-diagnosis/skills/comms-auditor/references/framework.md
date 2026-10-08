# Framework — 10 Behavioral Principles (AIA)

Source of truth: *Behavioral Communications Audit — Machine Reference* (`INSTRUCTIONS.pdf` v1.1),
grounded in ideas42's *Checklist for Effective Student Communications* and *Behavioral Guidelines for
Effective Communication*.

Use these **exact principle names** in the scorecard and in the Step-2 table. The keyword list at the
bottom is the canonical spelling for tagging.

---

## ATTENTION

### 1. Salience
**GOAL:** Key info stands out immediately; scanning-friendly.
**TACTICS:**
- Clear subject lines; CTA near the top.
- Headers, bullets, bolding, spacing; avoid clutter.
- Channel fit: email for multi-step processes; SMS for quick nudges.
- For short reminders: rely on brevity + placement rather than heavy formatting.

**WHY:** People scan; an immediate "what/why" reduces misses.

### 2. Relevance & Personalization
**GOAL:** Feels for-me; references current status and actions.
**TACTICS:**
- Acknowledge progress; make the next step explicit.
- Avoid self-sorting ("If you already did X…"). Segment instead.

**WHY:** Tailored relevance increases engagement; self-sorting creates friction.

### 3. Credibility & Identity Alignment
**GOAL:** Trustworthy sender; tone matches sender identity.
**TACTICS:**
- Specific person or credible unit named.
- Peer = informal support; department head = professional authority.
- Maintain consistency across offices.

**WHY:** Trust reduces skepticism and improves compliance.

---

## INTENTION

### 4. Clarity, Simplicity & Brevity
**GOAL:** Plain language; active voice; short sentences; minimal extraneous info.
**TACTICS:**
- Break complex steps into checklists.
- If multiple options: highlight a smart default.

**WHY:** Cognitive load creates drop-off; clarity sustains intention.

### 5. Support & Self-Efficacy
**GOAL:** Normalize challenge (not failure); build capability and confidence.
**TACTICS:**
- Validate ("Life gets busy."); avoid normalizing failure ("Most people forget").
- Reference prior success: "You already completed X — nice work."

**WHY:** Confidence drives follow-through; reassurance reduces avoidance.

### 6. Social
**GOAL:** Use positive, identity-relevant norms.
**TACTICS:**
- Cite timely, truthful positive behaviors.
- Never imply negative behaviors are common.
- Align the reference group with recipient identity.

**WHY:** Norms motivate when credible and identity-aligned.

### 7. Persuasion & Cost-Benefit Value
**GOAL:** Show the value of acting and the cost of inaction, tied to the recipient's goals.
**TACTICS:**
- Benefits: save money, reduce stress, graduate sooner.
- Costs: lost aid, closed classes, delays.

**WHY:** Perceived value shapes intention.

---

## ACTION

### 8. Clear Call-to-Action & Focus
**GOAL:** One clear CTA; group and prioritize if multiple steps are unavoidable.
**TACTICS:**
- Put the CTA high; embed direct links at point-of-action.
- Use descriptive buttons and links ("Submit FAFSA").

**WHY:** Competing CTAs cause choice overload.

### 9. Ease & Hassle Reduction
**GOAL:** Remove friction; make action effortless.
**TACTICS:**
- Direct links; minimize logins; mobile-friendly.
- In SMS: short, tappable links. In email: fewer clicks.
- Remove unnecessary steps.

**WHY:** Small hassles drive disproportionate drop-off.

### 10. Timeliness & Urgency
**GOAL:** Ask when action is possible; use deadlines to anchor action.
**TACTICS:**
- Provide real deadlines; avoid obviously false ones.
- For early awareness: focus on "do now", or on plan-when-to-do (implementation intention).
- Include support info only if provided; never invent it.

**WHY:** Specific timing counters procrastination.

---

## Severity guidance

| Severity | Examples |
|---|---|
| **High** ❌ | Missing or unclear CTA; conflicting CTAs. No deadline where timing is critical. Instructions impossible or unavailable at the time of the ask. |
| **Medium** ⚠️ | Jargon; long, complex sentences; CTA buried. Generic tone where personalization data exists. |
| **Low** ⚠️/✅ | Minor formatting polish; redundant phrasing; non-blocking style issues. |

Score each principle **5 / 3 / 1** with the matching status: `5 = ✅`, `3 = ⚠️`, `1 = ❌`. Give a
one-sentence justification referencing concrete elements of the message.

**Stage summary:** after rating every principle in a stage, give the stage a single status — `❌` if a
core function of that stage fails, `⚠️` if the stage works but with friction, `✅` if it is sound.

Score only **applicable** principles. If a principle genuinely cannot apply to the artifact (no
options exist, so no smart default is possible; no norm data exists, and inventing a statistic is
forbidden), say so in one clause rather than manufacturing a failure.

---

## Channel heuristics

- **SMS** — short reminders; single action; immediate timing; link included.
- **Email** — multi-step processes; documents; multiple but grouped actions.
- **Landing page** — long instructions; email and SMS should deep-link to it.

**Rule:** if the action requires multi-screen instructions, email + landing page beats SMS.

---

## Do and don't

**Do**
- Place the CTA early; include a reason to act now plus a deadline.
- Use descriptive links and buttons; embed links at the point of action.
- Segment audiences; reference prior progress; keep sentences short.

**Don't**
- Don't use self-sorting "if/then" trees in a single message.
- Don't imply negative behaviors are common.
- Don't invent support contacts or deadlines.

---

## Principle keywords (canonical spelling for tagging)

"Salience" · "Relevance & Personalization" · "Credibility & Identity Alignment" ·
"Clarity, Simplicity & Brevity" · "Support & Self-Efficacy" · "Social" ·
"Persuasion & Cost-Benefit Value" · "Clear Call-to-Action & Focus" ·
"Ease & Hassle Reduction" · "Timeliness & Urgency"

JSON keys, in the same order: `salience`, `relevance_personalization`,
`credibility_identity_alignment`, `clarity_simplicity_brevity`, `support_self_efficacy`, `social`,
`persuasion_cost_benefit_value`, `clear_cta_focus`, `ease_hassle_reduction`, `timeliness_urgency`.
