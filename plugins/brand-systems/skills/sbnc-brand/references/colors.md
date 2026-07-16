# SBNC Color System

## Tokens

| Name | Hex | RGB | Notes |
|---|---|---|---|
| SBNC Navy | `#1E2658` | 30, 38, 88 | Primary brand color. Hero backgrounds, body text on white, footer bar |
| SBNC Coral | `#FF5A5F` | 255, 90, 95 | Primary accent. Logo, taglines, callouts, decorative dots, card borders |
| Coral Soft | `#FFE5E6` | 255, 229, 230 | Backgrounds for coral callouts and chip placeholders |
| Coral Dark | `#E84A4F` | 232, 74, 79 | Coral hover / pressed states |
| Navy Dark | `#161B42` | 22, 27, 66 | Coral-on-navy contrast cases |
| White | `#FFFFFF` | 255, 255, 255 | Text on navy, content page background |
| Soft Cream | `#F8F8F4` | 248, 248, 244 | Alternate content background, table row alternates, code blocks |
| Mid Gray | `#7A8093` | 122, 128, 147 | Source citations, captions, meta text |
| Line | `#E3E5EC` | 227, 229, 236 | Subtle borders and dividers |

## Rules

**Hero treatment** — white text on navy. Used for cover slides, title pages, hero stats, footer/header bars. Coral is reserved for accents within this treatment (decorative pyramid, tagline banner, one-word emphasis on stat callouts).

**Body treatment** — navy text on white. Used for content pages, body copy, paragraph text in documents. Coral is reserved for headings, callout labels, dots/dividers.

**Never put coral text on a white background at body size.** It loses legibility. Coral is fine at ≥18pt (headings, taglines, big stat words) and as a background color with white or navy text on top.

**One word per stat callout in coral.** When a big white-on-navy stat needs emphasis, color exactly one word coral — usually the operative word that names the problem or solution. Examples from SBNC materials:
- "59% of students have considered dropping out due to **financial strain**" (financial strain in coral)
- "Nearly half of college students experience **food insecurity**" (food insecurity in coral)
- "A student is 43% **less likely** to graduate if their basic needs are not met" (less likely in coral)

**Coral on navy is OK at display size** (the "1 in 3 students qualify for free food monthly" slide uses full-coral display type on navy). Test contrast at smaller sizes.

## Accessibility

| Pair | Contrast ratio | WCAG verdict |
|---|---|---|
| Navy on White | 12.97:1 | AAA for all sizes |
| White on Navy | 12.97:1 | AAA for all sizes |
| Coral on White | 3.42:1 | AA for large text (≥18pt or 14pt bold) only — not body |
| Coral on Navy | 3.79:1 | AA for large text only |
| Navy on Coral Soft | 11.86:1 | AAA for all sizes |
| Navy on Coral | 3.42:1 | AA for large text only |

For text smaller than 18pt, use Navy on White (preferred), White on Navy, or Navy on Coral Soft. Coral is for emphasis at display sizes.

## Mixing rules

- Combine **white + navy + one accent of coral** per layout. Don't mix in additional accent colors (greens, blues) — SBNC's brand is intentionally tight.
- Soft Cream is the only secondary background. Use it as an alternate row in tables, behind code blocks, or as a subtle section break — never as a third "accent."
- Mid Gray is for *citations and metadata only*, never for body text.

## CSS / web

```css
:root {
  --sbnc-navy: #1E2658;
  --sbnc-navy-dark: #161B42;
  --sbnc-coral: #FF5A5F;
  --sbnc-coral-soft: #FFE5E6;
  --sbnc-coral-dark: #E84A4F;
  --sbnc-cream: #F8F8F4;
  --sbnc-gray: #7A8093;
  --sbnc-line: #E3E5EC;
}
```

## docx-js

Pass hex values without the `#` prefix:

```js
const NAVY = '1E2658';
const CORAL = 'FF5A5F';
// etc.
new TextRun({ text: 'Heading', color: NAVY, bold: true });
new TableCell({ shading: { fill: NAVY, type: ShadingType.CLEAR }, ... });
```
