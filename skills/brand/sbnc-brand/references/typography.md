# SBNC Typography

## Type stack

| Use | Family | Weight | Letter-spacing | Case |
|---|---|---|---|---|
| Display / hero | **Archivo Black** | 900 | -0.3px | Often UPPERCASE for tagline; sentence case for titles |
| Section header | **Poppins** | 700 (Bold) | -0.2px | Sentence case |
| Subsection | **Poppins** | 600 (Semibold) | normal | Sentence case |
| Body | **Poppins** | 400–500 | normal | Sentence case |
| Caption / source | **Poppins** | 400 italic | normal | Italic |
| Tagline banner | **Archivo Black** | 900 | +1.4px | UPPERCASE |

Both fonts are on Google Fonts and free for commercial use.

## Google Fonts links

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

CSS:
```css
font-family: 'Poppins', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
/* For display heads: */
font-family: 'Archivo Black', 'Poppins', sans-serif;
```

## Sizing scale (web)

| Role | Size | Line-height |
|---|---|---|
| Hero (cover page H1) | 44–56px | 1.1 |
| Section H1 | 28–32px | 1.15 |
| Section H2 | 20–24px | 1.25 |
| Subsection H3 | 16–18px | 1.3 |
| Body | 14–15px | 1.55 |
| Small / caption | 12–13px | 1.45 |
| Footer line | 12px | 1.4 |
| Tagline banner | 13px (1.4px tracking, all caps) | 1.0 |

## Sizing scale (docx, half-point units)

In docx-js, font sizes are doubled (the "size" property is in half-points). For SBNC docs:

| Role | docx-js size | Visible pt |
|---|---|---|
| Cover title | 44 | 22pt |
| Heading 1 | 36 | 18pt |
| Heading 2 | 28 | 14pt |
| Heading 3 | 22 | 11pt |
| Body | 22 | 11pt |
| Caption / footer | 18 | 9pt |
| Monospace code / chip | 20 | 10pt |

## Rules

- **Display headlines are never all-lowercase.** Either sentence case (titles) or UPPERCASE (taglines, banner labels). Don't use Title Case.
- **Body is never all caps.** SBNC reserves caps for tagline and short labels.
- **Avoid serifs entirely.** The one slab-serif "1 in 3" stat slide is a deliberate display flourish, not part of the system. New materials should use Poppins/Archivo Black.
- **Italic is for citations only.** Use it for source attributions ("Trellis Financial Wellness Survey, 2023") and quotations — not for general emphasis.
- **For emphasis in body, use bold weight, not italic.** Pair with a coral accent if extra weight is needed at heading sizes.

## When Poppins/Archivo Black aren't available

For Word documents where the recipient might not have the fonts installed, fall back to a universally-available stack. The brand's color and weight conventions carry most of the identity even when the exact face is missing.

- Display: **Calibri Bold** at hero sizes (40pt+) reads "heavy display" close enough.
- Body: **Calibri** is a clean modern sans that pairs well.
- For PDFs (final deliverables), prefer to embed the Poppins/Archivo Black faces so the rendered output matches across platforms.

For internal Office work, declare the font as `"Poppins"` first in the docx font run — Word will fall back to its default if Poppins isn't installed, but users who have it (increasingly common) get the real face.

## SBNC-specific patterns

**Stat slides** — Display headline at 60–96px, white. One operative word colored coral. Citation in 12px italic mid-gray, lower-right.

**Section labels in coral solid blocks** (like "TECHNOLOGY", "CAMPUS ENGAGEMENT", "DATA INSIGHTS" on the "Who is SBNC?" slide) — Archivo Black, white text, +1px tracking, UPPERCASE, generous padding inside the coral block.

**Photo caption plates** — Stacked: name in Archivo Black UPPERCASE white-on-coral, title in Poppins regular white-on-navy below.

**Pillar headers** — Archivo Black UPPERCASE white, sitting on top of a navy info block. Used for the "TECHNOLOGY · CAMPUS ENGAGEMENT · DATA INSIGHTS" cards.
