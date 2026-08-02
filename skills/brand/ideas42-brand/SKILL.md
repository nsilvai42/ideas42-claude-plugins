---
name: ideas42-brand
description: Apply ideas42 visual identity, writing style, terminology, logos, colors, patterns, and Figtree guidance to documents, decks, HTML, emails, and reports.
---

# ideas42 Brand & Style Guide Skill

Apply ideas42's visual identity and writing style consistently across all deliverables.

**Visual identity source:** ideas42 Brand Guidelines, Updated March 2026 (one-sheet PDF available at `assets/ideas42_Brand_Styleguide_OneSheet_FNL.pdf`)

**Writing style source:** ideas42 Style Guide, Updated December 5, 2023 (full guide at `references/writing-style-guide.md`)

## When to Use This Skill

Use whenever:
- Creating presentations, documents, reports, spreadsheets, or web content for ideas42
- Writing or editing any text that represents ideas42 (briefs, blog posts, emails, communications)
- Checking terminology, tone, or inclusive language for ideas42 content
- Formatting existing materials to match ideas42 brand
- User mentions ideas42 brand, colors, fonts, logo, patterns, style, or tone
- Designing email communications (focus-area headers are bundled)

---

## Part 1: Visual Brand Identity

### Color Palette

**Primary Colors** (main design elements):

| Color | HEX | RGB | CMYK | PMS |
|---|---|---|---|---|
| Green Apple | #7AC10A | 122, 193, 10 | 57, 0, 100, 0 | 2286 |
| Indigo | #004357 | 0, 66, 87 | 97, 66, 46, 34 | 302 |
| Spruce | #1C8A70 | 28, 138, 112 | 83, 24, 66, 7 | 7473 |
| Deep Sea | #087084 | 8, 112, 132 | 89, 44, 38, 10 | 2222 |
| Rich Black | #000000 | 0, 0, 0 | 60, 40, 40, 100 | Black 6 |

**Secondary Colors** (accents and supporting elements):

| Color | HEX | RGB | CMYK | PMS |
|---|---|---|---|---|
| Lichen | #D1E03B | 209, 224, 59 | 22, 0, 92, 0 | 102 |
| Cayenne | #EF6A00 | 239, 106, 0 | 2, 72, 100, 1 | 3564 |
| Citrus | #FCAB38 | 252, 171, 56 | 0, 38, 88, 0 | 1375 |
| Rain | #D9E1E2 | 221, 229, 237 | 14, 8, 6, 0 | 7541 |

### Typography

**Primary sans-serif: Figtree family** (displayed as "Fig Tree" in the brand guide, but the actual font family name is `Figtree` — one word — for CSS and font-picker purposes).

Font files are bundled in `assets/fonts/`:
- `Figtree-VariableFont_wght.ttf` — variable font covering all weights (100–900)
- `Figtree-Italic-VariableFont_wght.ttf` — italic variable
- Static weights: `Figtree-Light.ttf`, `Figtree-Regular.ttf`, `Figtree-SemiBold.ttf`, `Figtree-Bold.ttf`, `Figtree-Black.ttf`

**Usage guidance:**
- **Figtree Black** — large headlines, high-impact display text
- **Figtree SemiBold** — subheaders, emphasis
- **Figtree Light** — body copy, general text
- Use heavier weights for large headlines; light- and mid-weight for body copy

**Serif option: STIX TWO Text family** — use only where a serif font is specifically needed in body copy.
- STIX Two Text Bold — serif headers/emphasis
- STIX Two Text Regular — serif body copy

**CSS fallback stack** (when Figtree is not available):
```css
font-family: 'Figtree', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```
Serif alternative:
```css
font-family: 'STIX Two Text', Georgia, serif;
```

### CRITICAL: Loading Figtree in HTML, PDF, and Offline-Capable Deliverables

**Embed Figtree directly as base64 `@font-face` rules for any HTML that might be converted to PDF, rendered in a sandboxed browser, or viewed offline.** Do NOT make `fonts.googleapis.com` the primary loading path.

**Why this matters:** Sandboxed rendering environments — including the headless chromium instance used for HTML-to-PDF conversion and claude.ai's artifact renderer — often cannot reach external CDNs. When the Google Fonts request fails, the browser silently falls back to a system sans-serif (typically DejaVu Sans, Liberation Sans, or Helvetica). The output looks "close enough" at first glance but is visibly off-brand in Figtree's distinctive rounded `a`, double-story `g`, and geometric numerals. **This failure mode is silent** — there is no error, no console warning, and it has caused real brand regressions.

**The fix:** Embed the bundled TTF files from `assets/fonts/` as base64 `@font-face` rules. See `references/embed-figtree.md` for a ready-to-paste recipe.

**Verification:** After generating HTML or PDF, confirm Figtree actually rendered. In a live browser or playwright, `document.fonts.check('400 16px Figtree')` must return `true`. In a generated PDF, `pdffonts output.pdf | grep -i figtree` must return matching entries. Visually, Figtree has a distinctive rounded lowercase `a` and double-story `g` — if the output looks like Helvetica or Arial, the font did not load.

Google Fonts (`@import url('https://fonts.googleapis.com/css2?family=Figtree:...')`) is acceptable only for HTML that will be served from a live website with reliable external network access. When in doubt, embed.

### Logo System

The 2026 brand package includes **seven logo variants**, each as both SVG (`assets/logos/svg/`) and PNG (`assets/logos/png/`):

| File | Appearance | Use On |
|---|---|---|
| `ideas42_Logo_PRIMARY` | Indigo "ideas" + Green Apple circle with white "42" | White/light backgrounds — **default choice** |
| `ideas42_Logo_WHITE_GREEN` | White "ideas" + Green Apple circle with white "42" | Dark/colored backgrounds — preserves brand green accent |
| `ideas42_Logo_WHITE` | All white (monochrome) | Dark backgrounds where single-color logo is required |
| `ideas42_Logo_BLACK` | All black (monochrome) | Single-color printing, faxes, low-color contexts |
| `ideas42_Logo_LT_GREY` | All light grey (monochrome) | Subtle/muted applications on white backgrounds |
| `ideas42_Logo_LT_GREY_GREEN` | Light grey "ideas" + Green Apple circle | Muted look that retains brand accent |
| `ideas42_Logo_LT_GREY_WHT` | Light grey "ideas" + white "42" circle | Specialized colored-background use |

**CRITICAL — Aspect ratio (to prevent distortion):**
- All 2026 logos ship at 806×356 px — aspect ratio is **2.264:1** (height = width ÷ 2.264).
- Common correct sizes: width 120 → height 53, width 150 → height 66, width 200 → height 88, width 300 → height 132.
- **NEVER set both width and height independently.** Always calculate one from the other using the 2.264:1 ratio. Prefer SVG when possible — it scales losslessly.

**Clear space:** Maintain clear space around the logo equal to the height of the "4" within the circular element of the logo. Do not crowd the logo with text or other graphic elements.

**Selection logic:**
1. Default to **PRIMARY** on white/light backgrounds.
2. On dark or colored backgrounds, use **WHITE_GREEN** to keep the brand green accent.
3. Use **BLACK** or **WHITE** monochromes only when color is unavailable or would clash.
4. Use **LT_GREY** variants for deliberately muted applications (e.g., footer marks, watermarks).

### Brand Patterns

The 2026 brand package includes decorative geometric patterns (PNG) as supporting graphic elements — useful for dividers, section breaks, background accents, slide decoration, or email graphics. Bundled in `assets/patterns/`:

- **Arrows** (`assets/patterns/arrows/`) — arrow motif in 8 color variants: `CAYENNE`, `CITRUS`, `DEEP_SEA`, `GRN_APPLE`, `LICHEN`, `LT_GREY`, `SPRUCE`, `WHITE`
- **Dot gradients** (`assets/patterns/dots/`) — 2 variants: `dots_gradient_GREEN.png`, `dots_gradient_WHITE.png`
- **Geometric patterns** (`assets/patterns/geometric/`) — three distinct patterns in subfolders `1/`, `2/`, `3/`, each available in ~8 color variants (CAYENNE, CITRUS, DEEP_SEA, GRN_APPLE, LICHEN, RAIN, SPRUCE, WHITE — exact set varies slightly by pattern)

**Usage guidance:**
- Use patterns as accent elements, not as the primary content surface.
- Choose a pattern color that contrasts adequately with the background.
- Don't mix more than one pattern in a single layout.
- WHITE patterns are intended for dark/colored backgrounds; colored patterns for light backgrounds.

### Email Headers (Focus-Area Specific)

Pre-designed email header graphics for each ideas42 focus area, bundled in `assets/email-headers/`:

- `I42_EmailGraphics_2026_header_General.png` — generic / cross-focus use
- `I42_EmailGraphics_2026_header_CivilSociety.png` — Civil Society
- `I42_EmailGraphics_2026_header_Education.png` — Education
- `I42_EmailGraphics_2026_header_FinancialHealth.png` — Financial Health
- `I42_EmailGraphics_2026_header_GlobalDevelopment.png` — Global Development
- `I42_EmailGraphics_2026_header_Government.png` — Government
- `I42_EmailGraphics_2026_header_Health.png` — Health
- `I42_EmailGraphics_2026_header_S&J.png` — Safety & Justice

Use the header that matches the primary focus area of the communication. Default to `General` when the email spans multiple focus areas or is an organizational-level message.

---

## Part 2: Writing Style (Key Rules)

These are the most critical writing rules. For the complete detailed guide with all terms, examples, and further resources, load: `references/writing-style-guide.md`

### Terminology & Identity

- **Partners**: Organizations we work with (even if they also fund us)
- **Funders**: Pay for work on programs they don't themselves run
- **Clients/Users**: Individuals who use the programs we design (or use a more specific term like voters, business owners)
- **Team members**: People who work at ideas42. NEVER say: employees, workers, staff
- **U.S./Global**: NOT domestic/international (those terms center the U.S.)

### Key Term Preferences

- **behavioral science** (default term; use "behavioral economics" only when specifically appropriate)
- **behaviorally informed** (no hyphen)
- **behavioral barriers** (not bottlenecks)
- **criminal legal system** (not justice system)
- **data is** singular (not "data are")
- **insights** (not learnings)
- **nonprofit** (one word, no hyphen)
- **postsecondary** (one word)
- **well-being** (hyphenated)
- **U.S., U.K.** (with periods)
- **randomized controlled trials** (not "control trials")

### Inclusive Writing Principles

- **Self-determination**: Ask people how they want to be referred to. Take the lead from the people we work with.
- **Specificity**: Avoid sweeping terms. Be specific about who you're talking about.
- **Plain language**: Define behavioral science terms on first use. Avoid jargon.
- **Show agency**: Use active voice. Frame systems (not people) as responsible for poor outcomes.
- **Flexibility**: Language evolves. Respect for people we write about matters more than rigid consistency.

### Terms to Avoid

- **Capacity building** → use "professional development"
- **Empower** → only if actually giving people power; never disingenuously
- **Irrational/irrationality** → can be paternalistic; avoid
- **The poor / poor people** → use person-first language
- **Vulnerable** → be specific about conditions/risks instead
- **Welfare / food stamps** → use current program names (SNAP, TANF) unless providing historical context

### Spelling & Punctuation Essentials

- Use the **Oxford (serial) comma**
- **Avoid abbreviations** unless universally known (AIDS, NATO, NGO). Spell out on first use.
- **Headings**: Title Case (capitalize all words except articles and prepositions)
- **Do NOT capitalize** theory names (prospect theory), behavioral concepts (mental accounting), or generic roles
- **Months over seasons** (we're a global organization; seasons differ by hemisphere)
- **Em dashes**: Closed, no spaces — like this
- **Single space** after periods
- **Justify text** on external-facing documents
- **American English** unless partner/funder requires otherwise
- **Hyperlinks**: Link text should convey purpose. No "Click Here" or "Read More."

### Numbers

- Spell out one through nine; digits for 10+
- 100,000 (not 100k or 100 thousand)
- $10 million (not $10m)
- Use % (not "percent")
- Use numerals for decimals (4.25) even if under 10
- No superscripts except references (7th grade, not 7ᵗʰ)
- $0.10 (not 10¢)

### References & Footnotes

- Follow APSA citation guidelines
- Arabic numerals for footnotes (1, 2, 3) — not Roman or symbols
- Footnotes go outside punctuation at end of sentence
- Statistics: p values as footnotes in lay-audience materials, not inline
- Use "n =" only in graphs; describe sample sizes in text

### General Framing

- Define behavioral science principles upon first use
- Avoid myth-busting framing that repeats false messages
- Follow ideas42 style over partner/funder defaults unless explicitly asked to change
- Adhere to ideas42's DEI guidelines

---

## Part 3: Application Instructions

### For Presentations (PPTX)

1. Read the pptx skill for creation best practices
2. Apply color palette:
   - Title slides: Indigo (#004357) backgrounds with white text, optionally layer a pattern from `assets/patterns/` in WHITE or GRN_APPLE
   - Content slides: White backgrounds with Indigo headers
   - Accents: Green Apple (#7AC10A) for highlights and CTAs
   - Supporting accents: Spruce (#1C8A70) or Deep Sea (#087084)
   - Backgrounds/dividers: Rain (#D9E1E2)
3. Typography: Figtree family (embed TTFs from `assets/fonts/` if the tool supports it); fallback to system sans-serif
4. Logo: Use PRIMARY on light slides, WHITE_GREEN on dark/colored slides (from `assets/logos/`)
5. Follow all writing style rules for slide text

### For Documents (DOCX/PDF)

1. Read the docx skill for creation best practices
2. Headers: Figtree Black or SemiBold in Indigo (#004357)
3. Body: Figtree Light in Rich Black; or STIX Two Text Regular for serif
4. Accents: Green Apple (#7AC10A) for callouts and emphasis
5. Subtle backgrounds: Rain (#D9E1E2)
6. Logo: Include PRIMARY version in header or footer (from `assets/logos/png/ideas42_Logo_PRIMARY.png`)
7. Follow all writing style rules — terminology, inclusive language, punctuation

### For Spreadsheets (XLSX)

1. Read the xlsx skill for creation best practices
2. Header rows: Indigo (#004357) or Spruce (#1C8A70) background with white text
3. Body: Rich Black (#000000)
4. Highlighting: Green Apple (#7AC10A) or Lichen (#D1E03B)
5. Alternating rows: Rain (#D9E1E2)
6. Charts: Use primary color palette; clearly label axes and include titles

### For HTML Artifacts and Web Content

1. CSS variables:
```css
:root {
  --ideas42-green-apple: #7AC10A;
  --ideas42-indigo: #004357;
  --ideas42-spruce: #1C8A70;
  --ideas42-deep-sea: #087084;
  --ideas42-rich-black: #000000;
  --ideas42-lichen: #D1E03B;
  --ideas42-cayenne: #EF6A00;
  --ideas42-citrus: #FCAB38;
  --ideas42-rain: #D9E1E2;
}
```

2. **Typography — embed Figtree, don't @import it.** See `references/embed-figtree.md` for the full recipe. Skeleton:
```css
/* Paste at the TOP of your <style> block. Generate the base64 strings from
   assets/fonts/Figtree-VariableFont_wght.ttf and Figtree-Italic-VariableFont_wght.ttf
   using the Python snippet in references/embed-figtree.md */
@font-face {
  font-family: 'Figtree';
  font-style: normal;
  font-weight: 300 900;
  font-display: swap;
  src: url(data:font/ttf;base64,<BASE64_REGULAR>) format('truetype-variations');
}
@font-face {
  font-family: 'Figtree';
  font-style: italic;
  font-weight: 300 900;
  font-display: swap;
  src: url(data:font/ttf;base64,<BASE64_ITALIC>) format('truetype-variations');
}

body { font-family: 'Figtree', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
```
Serif alternative: `font-family: 'STIX Two Text', Georgia, serif;`

**Do NOT use `@import url('https://fonts.googleapis.com/...')` as the primary font source** — it fails silently in sandboxed browsers and HTML-to-PDF renderers. See the "CRITICAL: Loading Figtree" section in Part 1 for the full rationale.

**After rendering, verify the font loaded.** For HTML in a browser: `document.fonts.check('400 16px Figtree')` must return `true`. For a generated PDF: `pdffonts output.pdf` must list Figtree entries.

3. Headers: Indigo; Body: Rich Black; Buttons/CTAs: Green Apple; Subtle backgrounds: Rain

4. Logos in HTML: Prefer the SVG files from `assets/logos/svg/` (scale losslessly). When sizing with width alone, height will auto-adjust; when sizing both, use the 2.264:1 aspect ratio.

### For Email Communications

1. Select the matching focus-area email header from `assets/email-headers/` and place it at the top of the email.
2. Use `General` header if no specific focus area applies.
3. Apply all Part 2 writing style rules to the body copy.
4. Keep sign-off consistent with ideas42 identity language ("team members," not "staff").

### For Written Communications (Blog Posts, Briefs, Memos)

1. Apply all writing style rules from Part 2
2. For detailed term lists and edge cases, load `references/writing-style-guide.md`
3. Use ideas42 terminology over partner/funder defaults unless explicitly asked
4. Check inclusive writing principles for any content discussing people or communities

### For All Formats

**Do:**
- Use primary colors as the foundation; reserve Green Apple for strategic emphasis
- Maintain high contrast for readability
- Use consistent typography (Figtree family)
- Choose the logo variant that matches background color and desired emphasis
- Respect the 2.264:1 logo aspect ratio when sizing
- Use Oxford commas, American English, justified text for external docs
- Define jargon, use person-first language, be specific about populations

**Don't:**
- Overuse secondary accent colors
- Use accents as primary backgrounds for large areas
- Mix too many colors per layout (limit 3–4)
- Crowd the logo — always respect clear space (equal to the height of the "4")
- Distort the logo by setting width and height independently
- Use "employees" / "staff" / "domestic" / "international"
- Capitalize theory names or generic roles
- Use myth-busting framing or jargon without definition

---

## Bundled Resources

### `assets/`
- `ideas42_Brand_Styleguide_OneSheet_FNL.pdf` — official 2026 one-sheet (view if you need to show the user the canonical design)
- `logos/svg/` and `logos/png/` — all 7 logo variants in both formats
- `fonts/` — Figtree variable + key static weights (`Light`, `Regular`, `SemiBold`, `Bold`, `Black`) plus italic variable; `OFL.txt` is the license
- `patterns/arrows/` — 8 arrow-pattern color variants
- `patterns/dots/` — 2 dot-gradient variants
- `patterns/geometric/1/`, `2/`, `3/` — three geometric patterns, ~8 color variants each
- `email-headers/` — 8 focus-area email headers

### `references/`
- `writing-style-guide.md` — complete writing style guide: all terms, inclusive writing details, terms to avoid, punctuation rules, number formatting, citations, and further resource links. Load when you need full detail on writing style.
- `embed-figtree.md` — step-by-step recipe for embedding Figtree into HTML and PDF deliverables via base64 `@font-face`. **Load whenever building HTML that will be converted to PDF, rendered in a sandboxed browser, or viewed offline** — the Google Fonts path fails silently in those contexts.
