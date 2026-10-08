// Build narrative + executive brief .docx for a sample description.
//
// Inputs (read from config.json):
//   - input_dataset, output_dir, brand_path
//   - 05_Numeric-Profile.csv, 06_Categorical-Profile.csv, 07_Quality-Metrics.csv
//   - column_classification.json
//   - charts/*.png
//   - 04_Transformation-Ledger.csv (optional, may not exist on first run)
//
// Outputs (into output_dir):
//   - 01_Sample-Description_Narrative.docx
//   - 02_Sample-Description_Brief.docx
//   - 08_Methods-Boilerplate.docx  (if config.requested_outputs includes "methods")
//
// Usage:
//   node build_docs.js --config /abs/path/to/config.json

const fs   = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, AlignmentType, LevelFormat, HeadingLevel, BorderStyle,
  WidthType, ShadingType, PageBreak, Footer, PageNumber,
} = require("docx");

function parseArgs() {
  const args = process.argv.slice(2);
  const i = args.indexOf("--config");
  if (i < 0) { console.error("Missing --config"); process.exit(1); }
  return { configPath: args[i + 1] };
}

const { configPath } = parseArgs();
const cfg = JSON.parse(fs.readFileSync(configPath, "utf8"));
const brand = JSON.parse(fs.readFileSync(cfg.brand_path, "utf8"));
const OUT = cfg.output_dir;
const CHARTS = path.join(OUT, "charts");

// Brand color resolution
const color = (role) => {
  const key = brand.semantic[role] || role;
  return (brand.palette[key] || key).replace(/^#/, "");
};

// Image sizing: assume 6.5" content width (US Letter, 1" margins) → 624px @ 96 dpi
const CONTENT_PX = 620;

function imgPath(filename, widthPx = CONTENT_PX) {
  const fullPath = path.join(CHARTS, filename);
  if (!fs.existsSync(fullPath)) return null;
  const data = fs.readFileSync(fullPath);
  // Probe width/height via PNG header
  const w = data.readUInt32BE(16);
  const h = data.readUInt32BE(20);
  const ratio = h / w;
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 80 },
    children: [new ImageRun({
      type: "png",
      data,
      transformation: { width: widthPx, height: Math.round(widthPx * ratio) },
      altText: { title: filename, description: filename, name: filename },
    })],
  });
}

function caption(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 240 },
    children: [new TextRun({ text, italics: true, size: 18, color: color("footer_text") })],
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 180 },
    children: [new TextRun({ text, bold: true, color: color("title"), size: 32 })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 140 },
    children: [new TextRun({ text, bold: true, color: color("title"), size: 26 })],
  });
}
function p(textOrRuns) {
  const runs = (typeof textOrRuns === "string")
    ? [new TextRun({ text: textOrRuns, size: 22, color: color("body_text") })]
    : textOrRuns.map(r => new TextRun({ size: 22, color: color("body_text"), ...r }));
  return new Paragraph({ spacing: { after: 140, line: 300 }, children: runs });
}
function bullet(textOrRuns) {
  const runs = (typeof textOrRuns === "string")
    ? [new TextRun({ text: textOrRuns, size: 22, color: color("body_text") })]
    : textOrRuns.map(r => new TextRun({ size: 22, color: color("body_text"), ...r }));
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80, line: 280 },
    children: runs,
  });
}

function makeDoc(children) {
  return new Document({
    creator: brand.footer?.org_line_text || "describe-sample skill",
    title: `${cfg.study_name || "Study"} — Sample Description`,
    styles: {
      default: { document: { run: { font: brand.fonts.primary, size: 22 } } },
      paragraphStyles: [
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 32, bold: true, font: brand.fonts.primary, color: color("title") },
          paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 26, bold: true, font: brand.fonts.primary, color: color("title") },
          paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } },
      ],
    },
    numbering: {
      config: [{
        reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
      }],
    },
    sections: [{
      properties: {
        page: { size: { width: 12240, height: 15840 },
                margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 } },
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: `${brand.footer?.org_line_text || ""} · ${cfg.study_name || ""} · `,
                size: 16, color: color("footer_text") }),
              new TextRun({ children: [PageNumber.CURRENT], size: 16, color: color("footer_text") }),
              new TextRun({ text: " / ", size: 16, color: color("footer_text") }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: color("footer_text") }),
            ],
          })],
        }),
      },
      children,
    }],
  });
}

// ---------------------------------------------------------------------------
// Build narrative
// ---------------------------------------------------------------------------
function buildNarrative() {
  const study = cfg.study_name || "Sample";
  const n = cfg.n_total || "?";
  const children = [];

  // Title block
  children.push(new Paragraph({
    spacing: { after: 80 },
    children: [new TextRun({ text: study, bold: true, size: 24, color: color("highlight") })],
  }));
  children.push(new Paragraph({
    spacing: { after: 80 },
    children: [new TextRun({ text: "Sample Description", bold: true, size: 44, color: color("title") })],
  }));
  children.push(new Paragraph({
    spacing: { after: 320 },
    children: [new TextRun({
      text: `Who responded — characteristics of the ${n} participants`,
      italics: true, size: 22, color: color("footer_text"),
    })],
  }));

  children.push(new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: color("highlight"), space: 6 } },
    spacing: { after: 240 },
  }));

  // Headline placeholder — SKILL.md fills in
  children.push(h1("1. Headline summary"));
  children.push(p(cfg.headline_summary
    || "[Placeholder — SKILL.md should populate this with a 2–3 sentence top-line characterization of the sample.]"));

  // One section per chart family
  children.push(h1("2. Sample composition"));
  const chartFiles = fs.existsSync(CHARTS)
    ? fs.readdirSync(CHARTS).filter(f => f.endsWith(".png") && !f.startsWith("00_")).sort()
    : [];
  for (const f of chartFiles) {
    const family = f.replace(/^\d+_Chart_/, "").replace(/_.*\.png$/, "").replace(/-/g, " ");
    children.push(h2(family));
    const im = imgPath(f);
    if (im) {
      children.push(im);
      children.push(caption(`${family}. n = ${n}.`));
    }
  }

  // Limitations
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(h1("3. Limitations"));
  const limits = cfg.limitations || [
    "Sample composition is described as-is; representativeness vs. target population is not assessed unless benchmarking was requested.",
    "Small categorical cells (n < 10) are flagged but not suppressed in this internal-use document.",
    "Demographic disagreements between data sources (where applicable) are surfaced but not adjudicated.",
  ];
  for (const l of limits) children.push(bullet(l));

  // One-line summary
  children.push(h1("4. One-line sample summary"));
  children.push(new Paragraph({
    border: { left: { style: BorderStyle.SINGLE, size: 24, color: color("highlight"), space: 12 } },
    indent: { left: 360 },
    spacing: { before: 120, after: 240, line: 320 },
    children: [new TextRun({
      text: cfg.one_line_summary || "[SKILL.md should fill in a one-line summary here.]",
      italics: true, size: 22, color: color("body_text"),
    })],
  }));

  return makeDoc(children);
}

// ---------------------------------------------------------------------------
// Build executive brief
// ---------------------------------------------------------------------------
function buildBrief() {
  const study = cfg.study_name || "Sample";
  const n = cfg.n_total || "?";
  const children = [];

  children.push(new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: study, bold: true, size: 20, color: color("highlight") })],
  }));
  children.push(new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: "Sample at a Glance — Executive Brief",
      bold: true, size: 36, color: color("title") })],
  }));
  children.push(new Paragraph({
    spacing: { after: 240 },
    children: [new TextRun({
      text: `n = ${n}  ·  ${cfg.recruitment_summary || "see narrative for details"}`,
      italics: true, size: 18, color: color("footer_text"),
    })],
  }));

  children.push(new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: color("highlight"), space: 4 } },
    spacing: { after: 200 },
  }));

  children.push(new Paragraph({
    spacing: { before: 120, after: 100 },
    children: [new TextRun({ text: "Key takeaways", bold: true, size: 24, color: color("title") })],
  }));
  const takeaways = cfg.takeaways || [
    "[Placeholder — SKILL.md should populate 4–7 bullet takeaways here.]",
  ];
  for (const t of takeaways) bullet([{ text: t }]);
  for (const t of takeaways) children.push(bullet([{ text: t }]));

  // Overview chart if present
  const overview = imgPath("00_Chart_Overview-Grid.png", 600);
  if (overview) {
    children.push(overview);
    children.push(caption(`All sample-description charts at a glance. n = ${n}.`));
  }

  children.push(new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: color("highlight"), space: 4 } },
    spacing: { before: 80, after: 160 },
  }));

  children.push(new Paragraph({
    spacing: { before: 120, after: 100 },
    children: [new TextRun({ text: "Bottom line", bold: true, size: 24, color: color("title") })],
  }));
  children.push(new Paragraph({
    border: { left: { style: BorderStyle.SINGLE, size: 24, color: color("highlight"), space: 12 } },
    indent: { left: 360 },
    spacing: { before: 80, after: 200, line: 320 },
    children: [new TextRun({
      text: cfg.one_line_summary || "[Bottom line — populated by SKILL.md.]",
      italics: true, size: 22, color: color("body_text"),
    })],
  }));

  children.push(p([
    { text: "See ", italics: true, size: 18, color: color("footer_text") },
    { text: "01_Sample-Description_Narrative.docx", italics: true, size: 18, color: color("chart_bar_accent") },
    { text: " for the full write-up, individual chart files, and Limitations section.",
      italics: true, size: 18, color: color("footer_text") },
  ]));

  return makeDoc(children);
}

// ---------------------------------------------------------------------------
async function main() {
  const narrative = buildNarrative();
  fs.writeFileSync(
    path.join(OUT, "01_Sample-Description_Narrative.docx"),
    await Packer.toBuffer(narrative)
  );
  console.log("Wrote: 01_Sample-Description_Narrative.docx");

  const brief = buildBrief();
  fs.writeFileSync(
    path.join(OUT, "02_Sample-Description_Brief.docx"),
    await Packer.toBuffer(brief)
  );
  console.log("Wrote: 02_Sample-Description_Brief.docx");
}

main().catch(e => { console.error(e); process.exit(1); });
