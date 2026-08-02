# Applying SBNC Brand to One-Pagers (PDF)

Single-page PDFs — info sheets, program one-pagers, decision guides, peer-navigator overviews.

## Canonical layout

SBNC one-pagers (WBA Cohort Info Sheet, Peer Navigator One-Pager) all follow a near-identical structure. Replicate this:

```
┌─────────────────────────────────────────────────────────────┐
│ NAVY HEADER BAR                                              │
│ [SBNC mark]              [SECTION NAME big white Archivo]   │  ← 5px coral bottom border
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Section heading (Navy Poppins Bold)                         │
│  ── (short coral rule)                                       │
│                                                              │
│  Body paragraph in navy Poppins 11pt, 1.6 line-height.       │
│                                                              │
│  Section heading                                             │
│  ── (short coral rule)                                       │
│                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │  TECH       │  │  CAMPUS     │  │  DATA       │          │  ← Coral header bands
│  ├─────────────┤  ├─────────────┤  ├─────────────┤          │  ← Navy body boxes
│  │ • Navvy     │  │ • Cohorts   │  │ • Dashboard │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│                                                              │
│  ─────  TAGLINE BANNER (coral, white type)  ─────            │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│ NAVY FOOTER BAR                                              │
│ www.studentbasicneeds.com  [SBNC mark]  contact@sbnc.com    │  ← 5px coral top border
└─────────────────────────────────────────────────────────────┘
```

## Standard sections (for an info sheet)

1. **Header** — section name in white Archivo, with coral keyword swatch
2. **Mission** — single mission-line paragraph in navy Poppins ~12pt
3. **Three-pillar block** — Technology / Campus Engagement / Data Insights
4. **Key facts** — bulleted, ~5–7 items, navy with coral dots
5. **Partnership statement** — coral-bordered card with the "You bring / SBNC provides" framing
6. **Stat strip** — 2–3 supporting numbers in coral display type
7. **Tagline banner** — coral solid with white Archivo Black tagline
8. **Footer** — navy bar with the three-element pattern

## Page size and margins

- US Letter (8.5" × 11") portrait — the default for SBNC one-pagers
- Margins: ~0.4" (10mm) all sides — generous bleeds for the header/footer bars to run edge-to-edge
- Content column: full width minus content margins (~7.7")

## Production pipeline

**From a markdown source** (recommended for content-heavy info sheets):
1. Write the content as markdown
2. Convert to .docx with `scripts/build_sbnc_docx.js` (in `scripts/`)
3. Export to PDF from Word or via `soffice --convert-to pdf`

**From a designed layout** (recommended for visually rich one-pagers):
1. Design in Figma / Affinity Designer / Adobe Illustrator using the brand tokens
2. Export to PDF directly
3. Embed Poppins/Archivo Black fonts in the PDF so it renders consistently

**From HTML** (recommended for hybrid info-tools):
1. Build the page in HTML using `references/apply-to-html.md` patterns
2. Use the browser's "Print to PDF" or a headless Chrome / Puppeteer pipeline
3. Test the print stylesheet to ensure backgrounds print correctly

## Print considerations

- **Always embed fonts** in the final PDF. Without embedding, the recipient sees system fonts (which won't match the brand).
- **Test backgrounds print** — coral/navy headers and footers must render in print. In HTML, use `-webkit-print-color-adjust: exact` and `print-color-adjust: exact`.
- **Avoid hairline rules** that disappear at print resolution. Coral rules should be at least 1.5–2pt thick.
- **Verify color profile** — RGB for digital, CMYK for press. SBNC's coral may shift slightly when converted; commission a color-managed test print if it'll be press-printed.

## Examples from SBNC

Inspect these as references:
- WBA Cohort Info Sheet — strong example of pillar blocks + partnership framing
- Peer Navigator One Pager — strong example of stat strip + tagline banner placement
