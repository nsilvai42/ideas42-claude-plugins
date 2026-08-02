# Applying SBNC Brand to Slide Decks (.pptx)

This guide applies the brand to PowerPoint / Keynote / Google Slides decks.

## Slide-deck conventions

SBNC decks lean on a few recurring slide patterns. Use these as templates.

### Title slide

- Full-bleed navy background
- Coral vertical left bar (~30px wide, full slide height)
- SBNC pyramid + wordmark + subtitle, top-left (white or coral)
- Document title centered or left-aligned, white Archivo Black, 44–56pt
- Coral subtitle line below, sentence case, 20–24pt

Example: "Wisconsin Benefits Access Cohort: 26/27 Information Session"

### Agenda slide

- Navy background
- Coral vertical left bar
- "Today's Agenda" / "Agenda" headline top-left, white Archivo Black
- Stacked list of agenda items, each separated by a short coral horizontal rule
- Items in Poppins regular white, sentence case

### "Who is SBNC?" / about slide

- Navy background
- Centered mission-line paragraph in white Poppins, ~20pt
- Three pillar blocks below (Technology / Campus Engagement / Data Insights)
- Each pillar block: coral solid header (Archivo Black UPPERCASE white) + navy body box with bullet items

### Stat callout slide

- Navy background
- Centered display headline, white Archivo Black, 60–96pt
- One operative word in coral
- Small italic mid-gray source citation in lower-right (Poppins 14pt italic)
- Small SBNC pyramid (white or coral) in lower-left

### Photo / team slide

- Navy background
- Headshot grid (typically 3 across) with circular crops
- Each headshot has a stacked name plate:
  - Top: coral solid bg, white Archivo Black UPPERCASE name
  - Bottom: navy solid bg, white Poppins regular title

### Content slide (text-heavy)

- Cream or white background
- Navy section heading top-left, Poppins Bold 28–32pt
- Short coral horizontal rule (60–80px) under the heading
- Body text Poppins regular 14–18pt navy
- Use coral-bordered cards for grouped content

### Section divider slide

- Coral solid background
- White Archivo Black UPPERCASE section name, centered, 48pt
- Optional small SBNC pyramid in lower-right (white)

### Closing / contact slide

- Navy background
- Coral tagline banner across the middle
- "Get in touch" or similar headline
- Contact info: name, role, email — Poppins regular white
- SBNC mark + website in footer area

## Slide master setup

When setting up a custom slide master in PowerPoint / Keynote / Google Slides:

**Master colors** (define as theme colors):
- Color 1 (Background dark): `#1E2658` Navy
- Color 2 (Accent 1): `#FF5A5F` Coral
- Color 3 (Background light): `#F8F8F4` Cream
- Color 4 (Text light): `#FFFFFF` White
- Color 5 (Text dark): `#1E2658` Navy

**Master fonts**:
- Headings: Archivo Black (fall back to Calibri Bold, Arial Black)
- Body: Poppins (fall back to Calibri)

**Master placeholders**:
- Slide number bottom-right in Poppins italic, 10pt, white/coral depending on slide bg
- Optional small SBNC pyramid in lower-left (5–10mm)

## Spacing scale (16:9 deck at 1920×1080)

| Element | Size |
|---|---|
| Cover title | 88–112px (≈44–56pt) |
| Section title | 56–72px (≈28–36pt) |
| Subhead | 40–48px (≈20–24pt) |
| Body | 28–32px (≈14–16pt) |
| Caption / source | 22px (≈11pt) |
| Slide margins (left/right) | 96px (~50px on 4:3) |
| Slide margins (top/bottom) | 64px |

## Voice on slides

- One thought per slide. SBNC decks are visually heavy and verbally sparse.
- Stat slides: one statistic, one citation. Don't overload.
- Use the three-part parallel structure when listing — even if it means trimming.
- Use coral for the "load-bearing" word in any stat or quote.
- Source citations always cited (in italic gray, lower-right).

## Working from the `pptx` skill

When generating slides programmatically with the docx skill's `pptx` sibling:

1. Set theme colors in the master to the SBNC palette.
2. Set heading/body fonts to Archivo Black / Poppins.
3. Build slides using the patterns above.
4. Set the cover slide to use the navy + coral-bar layout.
5. Add an SBNC mark to the master so it appears on every slide.

Refer to the `pptx` skill's documentation for the actual API calls — this skill provides the brand vocabulary, not the slide-construction mechanics.
