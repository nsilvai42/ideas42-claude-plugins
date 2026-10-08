# Worked Example

A real onboarding email (PII redacted), scored against the ten principles. Read it to calibrate tone,
severity, and how much evidence a justification needs.

Fixtures: `Comms_Auditor/Verification/fixtures/` — `C01_welcome.txt` (source) and
`C01_welcome.audit.json` (the JSON export).

## The source (redacted)

> **Subject:** Congrats and next steps: Student Portal and Onboarding
> **From:** Calbright College <success@calbright.org> · Thu, Sep 21, 2023, 4:27 PM
>
> Dear [Student First Name], Congratulations on completing your Calbright College application! The
> next steps in order to begin your program are to access your Student Portal, log in to your
> Calbright College Student email account, and sign up for an Onboarding Session within the next
> week. It's easy, just follow these steps: **1.** Use the button below… **2.** Enter in your student
> email… **3.** Enter in your temporary password… **4.** Reset your password. **5.** Schedule your
> Onboarding Session using the link in your Student Portal.
> **[BUTTON] I'm Ready! Let's Get Started!**
> **Questions along the way?** …text us at (510) 330-1817, email success@calbright.org, or call our
> Success Team at (833) 956-0225. We're committed to your success! Your Calbright Success Team
> *(footer: social links, mission boilerplate, copyright, mailing address)*

Redaction removed a live student email address and a plaintext temporary password. When source
material carries credentials or PII, redact first and record it in Step 4.

## Scorecard

```
### Stage 1: Attention (Summary: ⚠️)
1. Salience: ⚠️ (Score: 3) — Channel and formatting are right, but the button sits below the whole
   five-step list and the subject line carries no urgency.
2. Relevance & Personalization: ✅ (Score: 5) — Opens with the recipient's name and congratulates the
   specific application they just completed.
3. Credibility & Identity Alignment: ⚠️ (Score: 3) — A credible unit is named, but no individual, and
   the marketing footer reads as a broadcast.

### Stage 2: Intention (Summary: ⚠️)
4. Clarity, Simplicity & Brevity: ⚠️ (Score: 3) — Steps are a numbered checklist, but the Onboarding
   Session is never explained and one sentence runs 35 words.
5. Support & Self-Efficacy: ⚠️ (Score: 3) — References prior success, but "It's easy" denies the
   challenge rather than validating it.
6. Social: — (n/a) — No local norm data exists in the source, and inventing a participation statistic
   is forbidden.
7. Persuasion & Cost-Benefit Value: ⚠️ (Score: 3) — "to begin your program" restates the action; no
   cost of delay is given.

### Stage 3: Action (Summary: ❌)
8. Clear Call-to-Action & Focus: ⚠️ (Score: 3) — One CTA, but the label names a feeling instead of a
   destination.
9. Ease & Hassle Reduction: ❌ (Score: 1) — The scheduling link is behind a navigate-and-find
   instruction, and credentials the email supplies must be retyped.
10. Timeliness & Urgency: ⚠️ (Score: 3) — A deadline exists but is relative, with no reason to act
    today.
```

## Why the calls landed where they did

**Ease & Hassle Reduction is the only 1, and it drives the stage to ❌.** Step 5 says *"Schedule your
Onboarding Session using the link in your Student Portal"* — the single most important action is
behind a navigate-and-find instruction. That is the severity guidance's "instructions
impossible/unavailable at time of ask", so it is High, and a core function of the Action stage fails.

**Salience is 3, not 1.** The CTA exists and is unambiguous; it is merely *buried* — which the
severity table lists as Medium. A missing or conflicting CTA would be High. Channel fit is correct and
the body is formatted.

**Social is n/a, not a failure.** No norm data exists anywhere in the source, and the framework
forbids inventing a statistic. Scoring a principle that could only be satisfied by fabrication is a
trap; say so in one clause and move on.

**Two findings quote the same button, under different principles.** *"I'm Ready! Let's Get Started!"*
appears at P4 (Salience — it sits too low) and P5 (Clear Call-to-Action & Focus — the label names an
emotion). Those are genuinely two defects in one string: placement and wording.

**Support & Self-Efficacy is 3 despite the congratulation.** It references prior success, which is the
principle's strongest tactic — but *"It's easy"* denies the challenge rather than validating it, which
is the opposite of "normalize challenge, not failure."

## What the comm gets right

Personalization is genuinely strong: the recipient's name, a specific completed step, and three real
support channels under a clear header. Relevance & Personalization earns a clean 5. An audit that
finds nothing good is not being rigorous — it is being lazy.

## Verify it

```bash
cd Comms_Auditor/Verification
./run-tests.sh
```

Or just this audit:

```bash
python3 ~/.claude/skills/comms-auditor/assets/validate.py \
    fixtures/C01_welcome.audit.json --source fixtures/C01_welcome.txt
```
