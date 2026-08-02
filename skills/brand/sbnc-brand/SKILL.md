---
name: sbnc-brand
description: Apply Student Basic Needs Coalition (SBNC) brand guidelines — visual identity, messaging, and tone — to any deliverable. Covers the full color palette (Navy #1E2658, Coral #FF5A5F), typography (Archivo Black for display, Poppins for body), the SBNC pyramid logo and wordmark, the "Campus-owned. SBNC-supported. Student-driven." tagline, voice and language patterns, and layout conventions for slides, one-pagers, reports, and digital materials. Use when creating or formatting any content for SBNC, the Student Basic Needs Coalition, Navvy (their benefits-access platform), or partner-school toolkits — including presentations, Word documents, spreadsheets, HTML artifacts, emails, social posts, newsletters, signage, or any professional deliverable. Also use when the user mentions SBNC brand, style, colors, fonts, logo, tagline, or partner-facing toolkit materials, even if they just say "make it on-brand" in an SBNC or Navvy context.
---

# SBNC Brand Skill

Apply the Student Basic Needs Coalition visual identity and voice to any deliverable. The brand system was extracted from the WBA (Wisconsin Benefits Access) Cohort info sheet, slide deck, the Peer Navigator one-pager, the Campus Basic Needs Survey, and the studentbasicneeds.com / navvyai.com sites — verified across multiple SBNC materials.

## When to use this skill

Apply SBNC branding when the deliverable is:

- A partner-facing document (toolkit, info sheet, one-pager, decision guide, FAQ)
- A campus partner email, newsletter, or social post about an SBNC program
- A presentation deck (info sessions, all-hands, fundraiser, board update)
- An internal report or memo
- A Navvy outreach asset (email templates, short-channel assets, signage)
- An HTML artifact, dashboard, or interactive tool
- Anything where SBNC is the publisher, even if Navvy or a campus partner is the topic

Use the lighter touch (color palette + tagline + footer line) when SBNC is co-publishing with a campus partner — let the campus brand carry primary visual identity.

## Core brand at a glance

**Tagline (always available, often used as a banner):**
> Campus-owned. SBNC-supported. Student-driven.

**Mission line:**
> SBNC ensures students are identified, enrolled, and supported in public benefits and basic needs resources so financial insecurity does not prevent college completion.

**Three pillars (used in introductory materials):**
Technology · Campus Engagement · Data Insights

**Partnership framing (used with campus partners):**
> You bring context and relationships. SBNC provides tech, training, support, and data.

## Primary palette

| Role | Hex | Used for |
|---|---|---|
| **SBNC Navy** | `#1E2658` | Hero backgrounds, body text on white, footer bar, headings |
| **SBNC Coral** | `#FF5A5F` | Accents — tagline banner, callout words, card borders, dot accents, the logo |
| White | `#FFFFFF` | Text on navy backgrounds, content-page background |
| Soft cream | `#F8F8F4` | Optional content-page background, table-row alternates |
| Mid gray | `#7A8093` | Source citations, captions, meta text |

**Quick rules:**
- White text on navy is the hero treatment; navy on white is the body treatment.
- Reserve coral for ≥18pt text — it loses legibility at body size.
- In stat callouts, put one word in coral as the emphasis (e.g., "due to **financial strain**").

See `references/colors.md` for full color guidance, accessibility notes, and tinting rules.

## Typography

| Use | Family | Weight | Fallback |
|---|---|---|---|
| Display / hero headlines | **Archivo Black** | 900 | Impact, Arial Black, Calibri Bold |
| Section headers | **Poppins** | 700 | Calibri Bold |
| Body | **Poppins** | 400–500 | Calibri Regular |
| Captions / sources | **Poppins Italic** | 400 italic | Calibri Italic |

Both fonts are free on Google Fonts. See `references/typography.md` for sizing scale, line-height rules, and how to handle docs where the partner can't install custom fonts.

## Logo

The SBNC mark has three parts:

1. **Pyramid** — three stacked coral chevrons (see `assets/sbnc-pyramid.svg`).
2. **Wordmark** — "SBNC" in heavy display sans, coral, where the `I` ends in an upward arrow tip.
3. **Subtitle** — "Student Basic Needs Coalition" in smaller coral below the wordmark.

When using inline (no logo file available), substitute the wordmark with bold coral "**SBNC**" text plus the pyramid SVG.

**Navvy lockup** (SBNC's benefits-screening platform): the word **"NAVVY"** in white inside a **coral rounded-square badge**, set on a **near-black** bar (`~#0B0E23`) — the app/header treatment; supporting line "Connecting students to benefits." This is distinct from the SBNC pyramid. Use the Navvy lockup when Navvy is the sender or surface (the app, the screener, post-account emails); use the SBNC pyramid + wordmark when SBNC is the sender (pre-account emails, partner materials). Canonical link: **navvyai.com** (screener embed: `eligibility.navvyai.com`).

## Tagline, voice, language

Read `references/voice.md` for:
- The full set of approved taglines and slogans
- Three-part parallel-structure patterns SBNC favors
- Do/don't language list
- Tone when writing to students vs. partners vs. funders
- Mission-line variants by audience

## Applying to specific formats

This skill ships with scripts and step-by-step guides for the formats SBNC ships most often:

| Format | Where to look |
|---|---|
| Word documents (.docx) | `references/apply-to-docx.md` + `scripts/build_sbnc_docx.js` + `scripts/fix_docx_borders.py` |
| HTML / interactive tools | `references/apply-to-html.md` (CSS tokens + chrome patterns ready to paste) |
| Slide decks (.pptx) | `references/apply-to-pptx.md` |
| One-pagers (PDF) | `references/apply-to-onepager.md` |
| Emails (HTML or plain) | `references/apply-to-email.md` |
| Notion pages (SBNC teamspace) | See **Applying to Notion** below — orange-bg section headers, toggles for detail, branded covers |

For docx generation specifically, the bundled `build_sbnc_docx.js` is a working Node.js generator that converts SBNC toolkit markdowns to branded `.docx` files using docx-js. It handles SBNC color theming, Smart-Chip-style `{{placeholder}}` rendering, branded tables with navy headers, and the navy footer pattern. Pair with `fix_docx_borders.py` to clear an OOXML schema warning from docx-js v9.x (a paragraph-border element-order bug).

## Applying to Notion (SBNC teamspace)

Observed across SBNC's live Notion teamspace (Resource Hub, Campus Programs, Five Minute Impact toolkit — 2026-06). Notion's block-color presets are limited, so SBNC uses a consistent set of *native* Notion conventions rather than recreating the full print palette:

- **Section headers (H1) use Notion's orange-background block color** (`{color="orange_bg"}`) — the Notion analog of the navy header bar. Examples in the wild: "Quick Toolkits," "Benefits 101," "NAVVY Screener Implementation Guide." Reserve orange-bg for top-level section banners. **This is a Notion-only convention** — the print / web / email brand palette stays navy + coral; do not introduce orange into those.
- **Heading hierarchy:** orange-bg H1 section banner → H2 program/topic ("SNAP," "Medicaid," "Using NAVVY") → H3 sub-topics. Keep pages scannable.
- **Toggles for detail / optional content** (`{toggle="true"}`): state-specific info (e.g. Wisconsin, New Mexico), per-office breakdowns, long eligibility detail. Default to collapsed so the page stays light.
- **Branded Notion cover images:** pages carry SBNC/Navvy cover graphics (the `Notion_Covers` / `Resource_Hub_Notion` series) as the page cover; section graphics (Navvy posters, QR codes, tearaways) embed inline, usually in **two-column layouts** (graphic on one side, short description on the other). Reuse the real cover/asset files from the teamspace rather than recreating them.
- **Callouts** for orientation ("What students see at the end," privacy/data notes); **quote blocks** for ready-to-paste language (syllabus statements, email outreach copy).
- **Coral + navy** for inline emphasis and icons; the "one word in coral" emphasis pattern still applies.
- **Links:** canonical product link is **navvyai.com**; support is `help@studentbasicneeds.com`.

Logos in Notion: **Navvy** = the coral "NAVVY" wordmark badge on near-black (the app lockup); **SBNC** = the coral pyramid + wordmark. Match the sender to the surface (SBNC pre-account, Navvy post-account).

## Visual element library

SBNC materials lean on a small consistent set of components:

- **Coral-outlined rounded rectangle cards** with a small filled coral circle floating at the top center
- **Coral horizontal rule** under section headers (short, accent-width)
- **Pillar block** — coral solid header + navy solid body, stacked
- **Stat slide** — navy background, huge white display headline, one word in coral, small italic gray source attribution lower-right
- **Coral vertical left bar** on title and agenda slides (~30px wide, full height)
- **Photo cards** — circular crops on navy background, with coral name plates below
- **Navy footer bar** with `www.studentbasicneeds.com · SBNC mark · contact@studentbasicneeds.com`
- **Navy header bar** with SBNC mark on left + section name on right (one word optionally highlighted in coral)

Detailed examples and dimensions: `references/visual-elements.md`.

## Header / footer conventions

**Footer (every page of multi-page docs):**
A navy bar across the bottom with three elements separated by `·`:

- Left: `www.studentbasicneeds.com`
- Center: SBNC mark (pyramid + wordmark)
- Right: `contact@studentbasicneeds.com`

Fallback for plain-text contexts: a single line in coral italic with the three items separated by `·`.

**Header (one-pagers and slide cover):**
A navy bar across the top, split visually:

- Left half: SBNC pyramid + wordmark + "Student Basic Needs Coalition" subtitle
- Right half: large white display headline naming the section (e.g., `WISCONSIN COHORT`, `PEER NAVIGATOR PROGRAM`) — often with a coral background swatch behind one keyword

## Light-touch vs. full-treatment

When deciding how heavily to brand:

- **Full treatment** — SBNC-published deliverable (internal report, partner toolkit, info session): apply tagline banner, footer pattern, full color/typography, visual element library.
- **Light touch** — co-published with campus partner, or a working internal document: color palette + tagline at the bottom + SBNC contact line. Let other branding lead.
- **Minimal** — student-facing emails or SMS sent through a campus partner's channels: NO SBNC branding on the message itself (per the trusted-messenger principle — students should see their campus, not a third party). SBNC's role can be acknowledged in a small "Powered by" footer if appropriate, but check first.

## Decision quick-reference

| Question | Answer |
|---|---|
| Need a tagline? | Use "Campus-owned. SBNC-supported. Student-driven." in coral uppercase. |
| Need an SBNC color? | Coral `#FF5A5F` for accents, Navy `#1E2658` for everything else. |
| Need a font? | Archivo Black (display) and Poppins (body). Calibri / Arial Black as fallback. |
| Building a docx? | Use `scripts/build_sbnc_docx.js` + `scripts/fix_docx_borders.py`. |
| Building HTML? | Pull tokens from `references/apply-to-html.md`. |
| Putting one word in coral for emphasis? | Yes — it's an SBNC signature, especially on stat callouts. |
| Three roles named in a row? | Yes — three-part parallel structure is an SBNC voice pattern. |
| Sending a student-facing message? | Don't brand it SBNC — let the campus carry it. |
