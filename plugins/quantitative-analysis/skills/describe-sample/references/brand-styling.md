# Brand styling

The skill applies brand styling to charts and documents. Default brand is `ideas42`. To use another brand, supply a brand JSON.

## Brand config schema

A brand JSON lives in `assets/brand-defaults/<brand-name>.json` and follows this shape:

```json
{
  "name": "ideas42",
  "version": "2026.03",
  "fonts": {
    "primary": "Figtree",
    "fallback": ["-apple-system", "BlinkMacSystemFont", "Segoe UI", "Arial", "sans-serif"],
    "weights": {
      "regular": 400,
      "semibold": 600,
      "bold": 700
    },
    "font_file_dir": "assets/fonts"
  },
  "palette": {
    "primary":        "#004357",
    "primary_dark":   "#002633",
    "primary_light":  "#0a6680",
    "accent":         "#7AC10A",
    "accent_alt":     "#1C8A70",
    "warning":        "#EF6A00",
    "warning_light":  "#FCAB38",
    "neutral_text":   "#3A3A3A",
    "neutral_grid":   "#D9E1E2",
    "neutral_muted":  "#6B6B6B",
    "background":     "#FFFFFF"
  },
  "semantic": {
    "title":           "primary",
    "highlight":       "accent",
    "positive":        "accent",
    "negative":        "warning",
    "body_text":       "neutral_text",
    "grid_lines":      "neutral_grid",
    "footer_text":     "neutral_muted",
    "chart_bar_primary": "primary",
    "chart_bar_accent":  "accent",
    "treatment_arm_colors": ["primary", "accent", "warning_light", "accent_alt"]
  },
  "doc": {
    "heading_color":     "primary",
    "subheading_color":  "accent_alt",
    "body_font_size_pt": 11,
    "title_font_size_pt": 22,
    "h1_font_size_pt":   16,
    "h2_font_size_pt":   13,
    "page_size":         "us_letter",
    "margins_inches":    1.0
  },
  "footer": {
    "include_org_line":  true,
    "org_line_text":     "ideas42",
    "include_page_numbers": true
  }
}
```

## How a script consumes the brand

Python (charts):
```python
import json
with open("assets/brand-defaults/ideas42.json") as f:
    BRAND = json.load(f)

# Resolve a semantic role to a hex color
def color(role):
    palette_key = BRAND["semantic"].get(role, role)
    return BRAND["palette"].get(palette_key, palette_key)

title_color = color("title")        # → "#004357"
highlight = color("highlight")      # → "#7AC10A"
```

Node (docx):
```javascript
const brand = require("./brand.json");
const colorOf = (role) => {
  const key = brand.semantic[role] || role;
  return brand.palette[key] || key;
};
```

## Font loading

For Python / matplotlib:
- Use `matplotlib.font_manager.addfont()` on every `.ttf` in `brand.fonts.font_file_dir`
- Set `rcParams["font.family"] = brand.fonts.primary`
- If primary font not registered, fall back to first registered fallback

For docx-js:
- Set `default.document.run.font` to `brand.fonts.primary`
- Word will substitute if the user opens the doc without the font installed; the .docx still references it correctly

## Brand-override at runtime

If the user wants a different brand for a specific run, accept any of:
1. A path to a custom brand JSON
2. A brand name that matches a file in `assets/brand-defaults/`
3. Inline overrides via elicitation form (e.g., "change accent color to #FF6600")

Document the override in the end-of-process summary.

## Adding a new brand

To add a new brand:
1. Create `assets/brand-defaults/<brand-name>.json` matching the schema above
2. Drop any required `.ttf` files into `assets/fonts/`
3. The brand is now selectable by name

No code change required.

## What brand styling does NOT control

- Chart selection (controlled by `adaptive-charts.md`)
- Doc structure / sections (controlled by `SKILL.md` workflow)
- Statistical computations
- Variable role inference

Brand is purely visual.
