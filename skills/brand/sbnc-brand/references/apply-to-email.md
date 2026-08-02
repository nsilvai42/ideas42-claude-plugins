# Applying SBNC Brand to Emails

## Two contexts, two treatments

**Partner-facing emails** (SBNC to campus staff, funders, board, internal team): apply full SBNC branding — navy header, coral tagline line in footer, individual SBNC sender identity, brand voice.

**Student-facing emails** (sent through a campus partner's channels to students): apply **no SBNC branding**. The trusted-messenger principle is that students should see their campus identity, not a third party. The campus's own brand carries the message. SBNC's role can be a one-line "Powered by SBNC" in the footer if appropriate — check first.

## Partner-facing HTML email

A reusable header chrome for HTML email (most email clients support inline CSS):

```html
<table width="100%" cellpadding="0" cellspacing="0" style="background:#1E2658;border-bottom:5px solid #FF5A5F;">
  <tr><td style="padding:24px 28px;color:#fff;font-family:'Poppins',Arial,sans-serif;">
    <span style="font-family:'Archivo Black',Arial Black,sans-serif;font-size:24px;color:#FF5A5F;letter-spacing:0.5px;">SBNC</span>
    <span style="font-size:11px;color:#FF5A5F;margin-left:10px;letter-spacing:1px;">STUDENT BASIC NEEDS COALITION</span>
  </td></tr>
</table>
```

Body in Poppins (or Arial fallback), 14px navy on white.

Footer:
```html
<table width="100%" cellpadding="0" cellspacing="0" style="background:#1E2658;border-top:5px solid #FF5A5F;">
  <tr><td align="center" style="padding:18px;color:#fff;font-family:'Poppins',Arial,sans-serif;font-size:12px;">
    <a href="https://www.studentbasicneeds.com" style="color:#FF5A5F;text-decoration:none;">www.studentbasicneeds.com</a>
    &nbsp;&middot;&nbsp; SBNC &nbsp;&middot;&nbsp;
    <a href="mailto:contact@studentbasicneeds.com" style="color:#FF5A5F;text-decoration:none;">contact@studentbasicneeds.com</a>
  </td></tr>
</table>
```

## Partner-facing plain-text email

For plain-text contexts (some campus systems strip HTML):

```
[Your name]
[Your title]
Student Basic Needs Coalition (SBNC)
www.studentbasicneeds.com  ·  contact@studentbasicneeds.com

Campus-owned. SBNC-supported. Student-driven.
```

The tagline appears below the signature as a quiet sign-off, not as a banner.

## Subject-line conventions

- **Direct, descriptive** — what the email is about, not clever marketing.
- **Cohort/program prefix** when relevant: `[Wisconsin Cohort]`, `[Navvy launch]`, `[Partner update]`
- **Avoid all-caps, multiple exclamation marks, "URGENT" framing** unless there's a real deadline.
- **Plain language** — no internal jargon (e.g., "WBA" only in established cohorts; spell it out for new partners).

Examples:
- ✅ "Next week's Wisconsin Cohort working session — agenda + pre-read"
- ✅ "Navvy launch update: schools onboarded as of June 1"
- ❌ "🚀 EXCITING UPDATE!!!"
- ❌ "Quick check-in"

## Email signature (individual SBNC staff)

```
[Name]
[Title]
Student Basic Needs Coalition (SBNC)
[email] | [phone, optional]
www.studentbasicneeds.com

Campus-owned. SBNC-supported. Student-driven.
```

For HTML email signatures, the SBNC pyramid SVG (`assets/sbnc-pyramid.svg`) can be inlined at 24px next to the wordmark. Most email clients render basic inline images well.

## Student-facing emails (when SBNC is supporting)

When sending through a campus partner's channels:

- **From:** the campus's named sender (e.g., "Maria Lopez (Basic Needs Center)" — never "SBNC" or "Navvy"
- **Body branding:** the campus's own brand identity, if any
- **SBNC mention:** in the footer only, and only with the campus's permission. Format: small italic line at the very bottom — *"Eligibility check powered by Navvy, in partnership with SBNC."*
- **Links:** point to the campus's Navvy URL, not a generic SBNC domain.

This is by design. From the Navvy outreach toolkit principles: students engage more when the message comes from a familiar campus office. SBNC's role is to make the campus's outreach effective, not to compete for student attention.

See the SBNC `Navvy Student Outreach Strategy Reference` (built as part of the toolkit) for the full trusted-messenger argument.
