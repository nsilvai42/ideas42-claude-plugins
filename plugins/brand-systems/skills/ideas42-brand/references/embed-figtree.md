# Embedding Figtree in HTML and PDF Deliverables

Recipe for making Figtree render reliably in self-contained HTML and in HTML-to-PDF pipelines — independent of whether the rendering environment has access to `fonts.googleapis.com`.

## When to use this recipe

Use embedded base64 `@font-face` (the pattern below) for:
- HTML artifacts rendered in claude.ai or any sandboxed browser that may not reach external CDNs
- HTML files the user may open offline or share as a standalone asset
- Any HTML that will be converted to PDF via headless chromium, playwright, weasyprint, or similar
- Any situation where font fidelity matters and you cannot personally verify CDN reachability

Only skip embedding — and use `@import url('https://fonts.googleapis.com/...')` instead — when the HTML will be served from a live website with reliable external network access that you control.

## Why embedding is the default

When `fonts.googleapis.com` is unreachable (a common condition in sandboxed renderers), the Google Fonts request fails **silently**. The browser does not throw an error, does not log a warning, and does not flag the failure in any obvious way. It simply falls through to the next entry in your CSS fallback stack — typically DejaVu Sans, Liberation Sans, or Helvetica depending on the operating system. The resulting output looks superficially correct but is visibly off-brand on any careful review.

Base64-embedded fonts cannot fail this way. The font bytes travel with the HTML; if the HTML itself loads, the font loads.

## The recipe

### Step 1: Base64-encode the bundled variable font files

The two variable font files cover every weight (300–900) and italic variant.

```python
import base64, pathlib

FONT_DIR = "/mnt/skills/user/ideas42-brand/assets/fonts"

def b64(path):
    return base64.b64encode(pathlib.Path(path).read_bytes()).decode()

regular_b64 = b64(f"{FONT_DIR}/Figtree-VariableFont_wght.ttf")
italic_b64  = b64(f"{FONT_DIR}/Figtree-Italic-VariableFont_wght.ttf")
```

Approximate base64 sizes: ~82 KB regular + ~82 KB italic = ~165 KB of font data embedded in the final HTML. For a document-style deliverable, this is a fair trade for guaranteed fidelity.

If file size is a hard constraint and you know you'll only use a single weight (say, Regular for body and Black for headlines), use the static TTFs instead — `Figtree-Regular.ttf` and `Figtree-Black.ttf` are each ~40 KB raw (~54 KB base64) — and declare separate `@font-face` blocks per weight.

### Step 2: Inject `@font-face` rules at the top of your `<style>` block

```python
font_face_css = f"""
@font-face {{
  font-family: 'Figtree';
  font-style: normal;
  font-weight: 300 900;
  font-display: swap;
  src: url(data:font/ttf;base64,{regular_b64}) format('truetype-variations');
}}
@font-face {{
  font-family: 'Figtree';
  font-style: italic;
  font-weight: 300 900;
  font-display: swap;
  src: url(data:font/ttf;base64,{italic_b64}) format('truetype-variations');
}}
"""
```

Insert this as the very first content inside `<style>`. Then use `font-family: 'Figtree', ...` as normal throughout your CSS. The `font-weight: 300 900` range means a single `@font-face` entry supports every weight the variable font ships with — no need for one block per weight.

### Step 3: Verify the font actually loaded

**In playwright (before calling `page.pdf()`):**
```python
fonts_ok = page.evaluate("""async () => {
  await document.fonts.ready;
  return [
    document.fonts.check('300 14px Figtree'),
    document.fonts.check('400 16px Figtree'),
    document.fonts.check('700 18px Figtree'),
    document.fonts.check('900 44px Figtree'),
  ];
}""")
assert all(fonts_ok), f"Figtree did not load: {fonts_ok}"
```

**In a generated PDF:**
```bash
pdffonts output.pdf | grep -i figtree
```
If this returns no rows, Figtree did not embed. Check your `@font-face` syntax and the base64 data URIs.

**Visually:**
Figtree has a distinctive character set. If the output doesn't have these traits, the fallback font is in use:
- Lowercase `a`: double-story, rounded bowl (not the single-story `a` of Futura/Century Gothic)
- Lowercase `g`: double-story with a closed lower loop (not the single-story open-tail `g` of Helvetica/Arial)
- Numerals: geometric with rounded terminals; the `4` has an open counter
- Overall: warmer and more rounded than Helvetica, Arial, or the Liberation/DejaVu system substitutes

## Lighter alternative: Google Fonts import (use only when CDN is guaranteed)

For HTML served from a live website where you can verify `fonts.googleapis.com` is reachable from every expected viewer:

```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&display=swap');

body { font-family: 'Figtree', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
```

This is ~165 KB lighter but fails silently where the CDN is unreachable. **Never use this pattern if the output will be converted to PDF via headless chromium or rendered as a claude.ai artifact.** When in doubt, embed.
