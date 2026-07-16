# Applying SBNC Brand to Word Documents

This guide is for generating branded `.docx` files. The skill ships with a working Node.js generator (`scripts/build_sbnc_docx.js`) that converts SBNC toolkit markdowns into branded Word documents. Use it as a starting point.

## Prerequisites

```bash
# Install docx-js once
npm install docx
# (or globally: npm install -g docx)

# Python 3 with zipfile (standard library) for the post-process step
```

## Quick start

For a single doc that follows the standard SBNC pattern (cover with tagline banner, navy footer, navy/coral heading hierarchy):

1. Copy `scripts/build_sbnc_docx.js` to your working directory.
2. Update the `WORKING` path and the input/output file paths in the `main` block.
3. Run: `node build_sbnc_docx.js`.
4. Run the border fix: `python scripts/fix_docx_borders.py output.docx`.
5. Validate (optional): use the office validate script.

## The two scripts

**`scripts/build_sbnc_docx.js`** — Reads a markdown file, parses it into structured blocks (headings, paragraphs, tables, lists, blockquotes, code blocks, horizontal rules), and emits a branded `.docx`. Inline parsing handles `**bold**`, `*italic*`, `` `code` ``, and `{{Chip Name}}` placeholders. Chip placeholders render with a soft-coral background so they're impossible to miss during customization.

**`scripts/fix_docx_borders.py`** — Post-processes the generated docx to fix an OOXML schema validation issue in docx-js v9.x. The library emits paragraph borders in `top, bottom, left, right` order; OOXML schema requires `top, left, bottom, right`. The script unzips the docx, regex-replaces the border element order in `document.xml`, and re-zips. The output renders identically in Word/LibreOffice but passes strict validation.

## Style mapping

The generator applies these mappings automatically:

| Markdown | docx treatment |
|---|---|
| `# H1` | Archivo-Black-style heading, navy, 18pt, with coral bottom border (3pt) |
| `## H2` | Navy heading, 14pt bold, no underline |
| `### H3` | Coral heading, 11pt bold |
| Body paragraph | Poppins/Calibri, navy, 11pt, 1.6 line-height |
| `**bold**` | Bold weight, navy |
| `*italic*` | Italic, navy |
| `` `code` `` | Consolas, 10pt, navy, cream background |
| `{{Chip Name}}` | Coral, bold, soft-coral background — visible like a Smart Chip |
| `> blockquote` | Cream bg, coral left border (thick), italic text, navy |
| Table | Navy header row with white bold text; body rows alternating white / soft cream |
| `- bullet` | Coral `•` marker, 0.5" indent |
| `1. numbered` | (Currently rendered as bullets; extend if needed) |
| `- [ ] checkbox` | Coral `☐` glyph + body text |
| `---` horizontal rule | 3pt coral line, generous vertical spacing |
| Cover preamble | Tagline banner (coral bg, white Archivo Black) → SBNC wordmark → title with coral underline |
| Footer | Centered coral italic line: `www.studentbasicneeds.com · SBNC · contact@studentbasicneeds.com` |

## Customizing per-document

Open `scripts/build_sbnc_docx.js` and edit the `main` block at the bottom. Each `buildDoc()` call takes:

- `title` — the H1 that appears below the tagline banner (e.g., "Navvy Student Outreach")
- `subtitle` — the italic line below the title (e.g., "Strategy Reference · Read once before you customize anything.")
- `mdPath` — input markdown file
- `outPath` — output .docx file

To adjust colors or fonts (e.g., when SBNC publishes a brand refresh):
- Color constants are at the top of the file (`NAVY`, `CORAL`, etc.)
- Font constants are also at the top (`FONT_BODY`, `FONT_DISPLAY`, `FONT_MONO`)
- Heading sizes are in the `buildHeading()` function's `styleMap`

## Font fallback

The generator declares `Calibri` as the body font because Poppins isn't universally installed on Windows machines. If your audience has Poppins installed (e.g., internal SBNC team), change `FONT_BODY` and `FONT_DISPLAY` to `'Poppins'` at the top of the script. Calibri renders the brand acceptably — the color and weight conventions carry most of the identity even when the exact face is missing.

For final-form deliverables, export to PDF using `soffice` or Word — that bakes the Poppins font into the file and ensures cross-platform fidelity.

## Validation

After generating, you can validate against OOXML schema:

```bash
python scripts/office/validate.py output.docx
```

If you skipped the `fix_docx_borders.py` step, you'll see warnings about `<w:left>` element ordering inside `<w:pBdr>`. Run the fix script to clear these. The output is valid in both cases (Word and LibreOffice are forgiving), but strict validation requires the fix.

## What to NOT use this for

- **Editing existing Word docs.** This generator builds from markdown source. To edit an existing docx, use pandoc with a reference document, or unpack/edit XML/repack per the `docx` skill's instructions.
- **Highly custom layouts** with text boxes, image overlays, or complex page elements. docx-js handles flow content well; if you need pixel-precise placement, build the layout in Word/Pages first and use this only for color/font theming via reference templates.
- **Student-facing materials** sent through campus channels. Don't brand those as SBNC — see SKILL.md "Light-touch vs. full-treatment" section.

## Iterating on the brand

When SBNC publishes a refreshed brand:

1. Update the token constants at the top of `build_sbnc_docx.js`
2. Update the matching tokens in `references/colors.md` and `references/typography.md`
3. Re-run the generator on existing markdowns to refresh deliverables
4. (Optional) Update the SBNC pyramid SVG in `assets/sbnc-pyramid.svg`

The brand reference docs (`colors.md`, `typography.md`, `voice.md`, `visual-elements.md`) are the source of truth — the script's constants are a working copy. Keep them in sync.
