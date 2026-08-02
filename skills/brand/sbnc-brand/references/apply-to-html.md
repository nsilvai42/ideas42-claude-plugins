# Applying SBNC Brand to HTML / Interactive Tools

This guide covers single-file HTML artifacts, React/JSX components, dashboards, and any web-rendered deliverable.

## CSS tokens

Drop these into a `:root` block at the top of your stylesheet:

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

## Google Fonts

Drop these in the `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

And in your base CSS:

```css
html, body {
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--sbnc-navy);
  background: #fff;
  line-height: 1.55;
}
```

## Header pattern

A reusable header chrome for SBNC artifacts:

```html
<header class="sbnc-header">
  <div class="sbnc-header-row">
    <div class="sbnc-mark">
      <svg class="sbnc-pyramid" viewBox="0 0 100 100" aria-label="SBNC">
        <polygon points="50,18 78,40 22,40" fill="#FF5A5F"/>
        <polygon points="50,46 84,68 16,68" fill="#FF5A5F"/>
        <polygon points="50,74 90,96 10,96" fill="#FF5A5F"/>
      </svg>
      <div>
        <div class="sbnc-wordmark">SBNC</div>
        <div class="sbnc-subtitle">Student Basic Needs Coalition</div>
      </div>
    </div>
    <div class="sbnc-header-title">
      <h1>Document Title <span class="accent">Subtitle</span></h1>
      <p class="lead">One-line description of what this is.</p>
    </div>
  </div>
</header>
<div class="sbnc-tagline">Campus-owned. SBNC-supported. Student-driven.</div>
```

```css
.sbnc-header {
  background: var(--sbnc-navy);
  color: #fff;
  padding: 28px 36px 24px;
  border-bottom: 5px solid var(--sbnc-coral);
}
.sbnc-header-row {
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}
.sbnc-mark { display: flex; align-items: center; gap: 12px; }
.sbnc-pyramid { width: 42px; height: 42px; }
.sbnc-wordmark {
  font-family: 'Archivo Black', 'Poppins', sans-serif;
  font-size: 30px;
  color: var(--sbnc-coral);
  line-height: 1;
}
.sbnc-subtitle {
  font-size: 9.5px;
  color: var(--sbnc-coral);
  letter-spacing: 1px;
  margin-top: 3px;
  font-weight: 500;
  text-transform: uppercase;
}
.sbnc-header-title { flex: 1; min-width: 280px; }
.sbnc-header h1 {
  margin: 0;
  font-family: 'Archivo Black', 'Poppins', sans-serif;
  font-size: 26px;
  font-weight: 900;
  line-height: 1.15;
}
.sbnc-header h1 .accent { color: var(--sbnc-coral); }
.sbnc-header .lead {
  margin: 8px 0 0 0;
  font-size: 13px;
  color: rgba(255,255,255,0.78);
  max-width: 720px;
  line-height: 1.5;
}
.sbnc-tagline {
  background: var(--sbnc-coral);
  color: #fff;
  padding: 11px 36px;
  text-align: center;
  font-family: 'Archivo Black', 'Poppins', sans-serif;
  letter-spacing: 1.4px;
  font-size: 13px;
  text-transform: uppercase;
}
```

## Footer pattern

```html
<footer class="sbnc-footer">
  <a href="https://www.studentbasicneeds.com">www.studentbasicneeds.com</a>
  <div class="sbnc-footer-mark">
    <svg class="sbnc-pyramid" viewBox="0 0 100 100">
      <polygon points="50,18 78,40 22,40" fill="#FFFFFF"/>
      <polygon points="50,46 84,68 16,68" fill="#FFFFFF"/>
      <polygon points="50,74 90,96 10,96" fill="#FFFFFF"/>
    </svg>
    <div>
      <div class="sbnc-wordmark" style="color:#fff;">SBNC</div>
      <div class="sbnc-subtitle" style="color:rgba(255,255,255,0.7);">Student Basic Needs Coalition</div>
    </div>
  </div>
  <a href="mailto:contact@studentbasicneeds.com">contact@studentbasicneeds.com</a>
</footer>
```

```css
.sbnc-footer {
  background: var(--sbnc-navy);
  color: #fff;
  padding: 22px 36px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  border-top: 5px solid var(--sbnc-coral);
}
.sbnc-footer a {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-size: 13px;
}
.sbnc-footer a:hover { color: var(--sbnc-coral); }
.sbnc-footer-mark { display: flex; align-items: center; gap: 10px; }
.sbnc-footer-mark .sbnc-pyramid { width: 28px; height: 28px; }
```

## Card pattern (coral-bordered with floating dot)

```css
.sbnc-card {
  background: #fff;
  border: 1.5px solid var(--sbnc-coral);
  border-radius: 12px;
  padding: 24px 28px 22px;
  margin-bottom: 24px;
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
.sbnc-card h3 {
  font-family: 'Archivo Black', 'Poppins', sans-serif;
  font-size: 17px;
  margin: 0 0 6px 0;
  color: var(--sbnc-navy);
  letter-spacing: -0.2px;
}
.sbnc-card .meta {
  font-size: 12.5px;
  color: var(--sbnc-gray);
  margin-bottom: 16px;
  line-height: 1.45;
}
.sbnc-card .label {
  font-family: 'Archivo Black', 'Poppins', sans-serif;
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--sbnc-coral);
  margin: 16px 0 6px 0;
}
```

## Callout / banner patterns

```css
.sbnc-banner-info {
  padding: 14px 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  font-size: 13.5px;
  line-height: 1.5;
  background: rgba(30,38,88,0.05);
  border-left: 4px solid var(--sbnc-navy);
  color: var(--sbnc-navy);
}
.sbnc-banner-warning {
  padding: 14px 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  background: var(--sbnc-coral-soft);
  border-left: 4px solid var(--sbnc-coral);
  color: var(--sbnc-navy);
}
.sbnc-banner-warning strong {
  color: var(--sbnc-coral);
  font-weight: 700;
}
```

## Buttons

```css
.sbnc-btn {
  background: var(--sbnc-coral);
  color: #fff;
  border: none;
  padding: 8px 18px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  font-family: 'Poppins', sans-serif;
  letter-spacing: 0.3px;
  transition: background 0.15s;
}
.sbnc-btn:hover { background: var(--sbnc-coral-dark); }
.sbnc-btn:active { background: var(--sbnc-navy); }
```

## Forms (worksheet style)

```css
.sbnc-field { margin-bottom: 12px; }
.sbnc-field label {
  display: block;
  font-size: 12px;
  color: var(--sbnc-navy);
  margin-bottom: 4px;
  font-weight: 600;
}
.sbnc-field input,
.sbnc-field select,
.sbnc-field textarea {
  width: 100%;
  padding: 8px 10px;
  border: 1px solid var(--sbnc-line);
  border-radius: 6px;
  font-size: 13px;
  font-family: inherit;
  background: #fff;
  color: var(--sbnc-navy);
}
.sbnc-field input:focus,
.sbnc-field select:focus,
.sbnc-field textarea:focus {
  outline: none;
  border-color: var(--sbnc-coral);
  box-shadow: 0 0 0 3px rgba(255,90,95,0.18);
}
```

## Tabs

```css
.sbnc-tabs {
  display: flex;
  gap: 6px;
  border-bottom: 2px solid var(--sbnc-line);
  margin-bottom: 24px;
  flex-wrap: wrap;
}
.sbnc-tab {
  padding: 12px 18px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  color: var(--sbnc-gray);
  border-bottom: 3px solid transparent;
  margin-bottom: -2px;
  transition: color 0.15s;
}
.sbnc-tab:hover { color: var(--sbnc-coral); }
.sbnc-tab.active {
  color: var(--sbnc-navy);
  border-bottom-color: var(--sbnc-coral);
}
```

## Checklists

```css
.sbnc-check-item {
  display: flex;
  align-items: flex-start;
  padding: 7px 0;
  font-size: 14px;
  gap: 12px;
  border-bottom: 1px solid rgba(30,38,88,0.06);
}
.sbnc-check-item input[type="checkbox"] {
  margin-top: 3px;
  flex-shrink: 0;
  cursor: pointer;
  accent-color: var(--sbnc-coral);
  width: 16px;
  height: 16px;
}
.sbnc-check-item label {
  cursor: pointer;
  flex: 1;
  color: var(--sbnc-navy);
}
.sbnc-check-item.checked label {
  text-decoration: line-through;
  color: var(--sbnc-gray);
}
```

## Print styles

```css
@media print {
  .sbnc-tabs, .sbnc-btn { display: none; }
  .sbnc-card { break-inside: avoid; }
  .sbnc-header, .sbnc-tagline, .sbnc-footer {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
}
```

## Working example

A complete working example is the `04_Interactive_toolkit_branded.html` built for the Navvy outreach toolkit — single-file React with all SBNC patterns applied. Use it as a reference implementation.
