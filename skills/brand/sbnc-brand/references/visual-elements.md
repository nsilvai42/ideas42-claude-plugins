# SBNC Visual Elements

This is the library of repeating UI / layout components that show up across SBNC materials. Use these patterns when assembling a new deliverable so the result feels native to the brand.

## Coral-bordered rounded card with floating dot

The signature card style. Used for grouping related content (per-touch message specs, role descriptions, decision boxes).

**Specs:**
- Border: 1.5px solid coral (`#FF5A5F`)
- Border-radius: 12px
- Padding: 24px × 28px
- Background: white
- Decorative element: a small filled coral circle, 14px diameter, sitting on the top center of the border (positioned with `top: -7px` so half is inside, half outside)

**CSS:**
```css
.sbnc-card {
  background: #fff;
  border: 1.5px solid var(--sbnc-coral);
  border-radius: 12px;
  padding: 24px 28px 22px;
  position: relative;
}
.sbnc-card::before {
  content: "";
  position: absolute;
  top: -7px;
  left: 50%;
  transform: translateX(-50%);
  width: 14px;
  height: 14px;
  background: var(--sbnc-coral);
  border-radius: 50%;
}
```

## Tagline banner

Used at the top of cover pages, info sheets, and as a section divider.

**Specs:**
- Background: coral (`#FF5A5F`)
- Padding: 10–12px vertical, full width
- Text: Archivo Black, UPPERCASE, white, +1.4px letter-spacing, 13px
- Content: "CAMPUS-OWNED.  SBNC-SUPPORTED.  STUDENT-DRIVEN." (double spaces between elements as a visual pause)

## Pillar block

Used to label the three SBNC pillars on intro slides. Stacked design: coral header label, navy body box.

**Layout:**
```
┌─────────────────────┐
│   TECHNOLOGY        │  ← coral solid bg, white Archivo Black UPPERCASE
├─────────────────────┤
│ • Navvy Deployment  │  ← navy solid bg, white Poppins body
│ • Peer Navigators   │
└─────────────────────┘
```

**Specs:**
- Header: coral bg, white text, Archivo Black 14–18px UPPERCASE, generous padding (10–14px vertical)
- Body: navy bg, white text, Poppins 14px, bullet markers in white or coral
- Width: full column width; usually displayed in a 3-up row

## Stat callout slide

Used to lead a story with a research statistic.

**Layout:**
- Navy full-page background
- Centered display headline, white, Archivo Black, 72–96px
- One operative word colored coral inline within the headline
- Source citation in lower-right corner: Poppins italic 14px, mid-gray (`#7A8093`)
- Small SBNC pyramid mark in lower-left (white or coral version)

**Example:**
> 59% of students have considered dropping out due to **financial strain**
>
> *Ellucian & EMI Research Solutions, 2024*

## Photo card with name plate

Used in team introductions, peer-navigator profiles, partner staff features.

**Layout:**
- Circular crop of headshot, 200–300px diameter
- Name plate below: stacked rectangles
  - Top: coral bg, white Archivo Black UPPERCASE name
  - Bottom: navy bg, white Poppins regular title
- Cards arranged in horizontal grid (2–4 across)

## Coral horizontal rule

Used under section headers to visually separate.

**Specs:**
- Color: coral
- Thickness: 2–3px
- Length: short — typically 60–80px (NOT full width)
- Margin: 8px above, 16px below the heading text

```css
.sbnc-section-rule {
  height: 3px;
  width: 60px;
  background: var(--sbnc-coral);
  margin: 8px 0 16px;
}
```

## Coral vertical left bar

Used on title pages and agenda slides as a decorative spine.

**Specs:**
- Coral solid bar, 24–32px wide
- Full slide height
- Positioned at the very left edge
- Content (title, agenda items) starts after a generous left margin

## Footer bar (navy)

Used at the bottom of every page in multi-page documents.

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ www.studentbasicneeds.com    [SBNC mark]    contact@sbnc.com   │  ← navy bg, coral border-top
└────────────────────────────────────────────────────────────────┘
```

**Specs:**
- Background: navy
- Padding: 22px vertical
- Top border: 5px solid coral
- Three-column flexbox (or table) layout
- Left: website URL, white opacity 0.85, Poppins 13px, hover → coral
- Center: SBNC pyramid (white version) + "SBNC" wordmark (white) + "Student Basic Needs Coalition" subtitle (white opacity 0.7)
- Right: contact email, same styling as left

**Plain-text fallback** (when a true bar isn't possible — e.g., docx footer area):

A single centered line in coral italic:
> www.studentbasicneeds.com  ·  **SBNC**  ·  contact@studentbasicneeds.com

## Header bar (navy, one-pagers)

Used at the top of single-page deliverables (info sheets, one-pagers).

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ [pyramid] SBNC                          WISCONSIN COHORT      │  ← navy bg, coral bottom border
│           Student Basic Needs Coalition  Information Session   │
└────────────────────────────────────────────────────────────────┘
```

**Specs:**
- Background: navy
- Bottom border: 5px solid coral
- Padding: 28px × 36px
- Left: SBNC mark (pyramid + wordmark + subtitle, all coral)
- Right: section headline in white Archivo Black, often with one keyword highlighted with a coral background swatch

## Subject-line / callout box

Used to highlight email subject options, important quotes, or coral-accent callouts inline.

**Specs:**
- Background: coral soft (`#FFE5E6`)
- Left border: 4px solid coral
- Padding: 12px × 16px
- Border-radius: 0 6px 6px 0 (rounded right, square left)
- Body text: navy

## Pyramid SVG

The three-stacked-chevron pyramid mark. Inline SVG for use in HTML headers, footers, and watermarks:

```html
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-label="SBNC">
  <polygon points="50,18 78,40 22,40" fill="#FF5A5F"/>
  <polygon points="50,46 84,68 16,68" fill="#FF5A5F"/>
  <polygon points="50,74 90,96 10,96" fill="#FF5A5F"/>
</svg>
```

For navy contexts, swap `fill="#FF5A5F"` to `fill="#FFFFFF"` for the white version.

See `assets/sbnc-pyramid.svg` for a standalone file.

## Decorative coral dot

Used as a small accent — on the top of cards, as a list marker, before section labels.

```css
.sbnc-dot {
  width: 8px;
  height: 8px;
  background: var(--sbnc-coral);
  border-radius: 50%;
  display: inline-block;
}
```

In bullet lists, replace the default disc with a small coral filled circle. In docx, use a `•` character colored coral.
