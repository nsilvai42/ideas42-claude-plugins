// Build SBNC-branded Word docs from the toolkit markdowns.
// Run: node build_sbnc_docx.js
//
// Generates branded .docx for each of the three artifacts and writes them
// to the Benefits_SBNC/02_Working/ folder.

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, PageOrientation, LevelFormat,
  TabStopType, TabStopPosition, BorderStyle, WidthType, ShadingType,
  HeadingLevel, PageNumber,
} = require('docx');

// ===== SBNC brand tokens =====
const NAVY = '1E2658';
const CORAL = 'FF5A5F';
const CORAL_SOFT = 'FFE5E6';
const CREAM = 'F8F8F4';
const GRAY = '7A8093';
const LINE = 'E3E5EC';
const WHITE = 'FFFFFF';

const FONT_BODY = 'Calibri';
const FONT_DISPLAY = 'Calibri';
const FONT_MONO = 'Consolas';

// ===== Helpers =====

function border(color = LINE, size = 6) {
  return { style: BorderStyle.SINGLE, size, color };
}

function cellBorders(color = LINE) {
  const b = border(color);
  return { top: b, left: b, bottom: b, right: b };
}

// Strip common markdown character escapes that should render as literal.
function unescapeMarkdown(text) {
  return text.replace(/\\([\[\]\*_`{}<>#+\-.!|\\])/g, '$1');
}

// Parse inline markdown into TextRun children: **bold**, *italic*, `code`, {{chip}}
function parseInline(text) {
  const pattern = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\{\{[^}]+\}\})/g;
  const parts = text.split(pattern).filter(p => p && p.length > 0);
  return parts.map(p => {
    if (p.startsWith('**') && p.endsWith('**')) {
      return new TextRun({ text: unescapeMarkdown(p.slice(2, -2)), bold: true, color: NAVY, font: FONT_BODY });
    }
    if (p.startsWith('*') && p.endsWith('*') && p.length > 2) {
      return new TextRun({ text: unescapeMarkdown(p.slice(1, -1)), italics: true, color: NAVY, font: FONT_BODY });
    }
    if (p.startsWith('`') && p.endsWith('`')) {
      return new TextRun({ text: unescapeMarkdown(p.slice(1, -1)), font: FONT_MONO, color: NAVY, size: 20,
        shading: { fill: CREAM, type: ShadingType.CLEAR } });
    }
    if (p.startsWith('{{') && p.endsWith('}}')) {
      return new TextRun({ text: p, color: CORAL, bold: true, font: FONT_BODY,
        shading: { fill: CORAL_SOFT, type: ShadingType.CLEAR } });
    }
    return new TextRun({ text: unescapeMarkdown(p), color: NAVY, font: FONT_BODY });
  });
}

// Parse table row "| a | b | c |" into ["a","b","c"]
function parseTableRow(line) {
  return line.replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim());
}

function isTableSeparator(line) {
  return /^\s*\|?[\s:|-]+\|?\s*$/.test(line) && line.includes('-') && line.includes('|');
}

// ===== Markdown parser (focused on our toolkit's features) =====

function parseMD(md) {
  const lines = md.split('\n');
  const blocks = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }

    // Heading
    const h = line.match(/^(#{1,4})\s+(.+)$/);
    if (h) {
      blocks.push({ type: 'heading', level: h[1].length, text: h[2].trim() });
      i++; continue;
    }

    // Horizontal rule
    if (/^---+\s*$/.test(line)) {
      blocks.push({ type: 'hrule' });
      i++; continue;
    }

    // Table (line starts with | and next line is separator)
    if (line.trim().startsWith('|') && i + 1 < lines.length && isTableSeparator(lines[i + 1])) {
      const headerCells = parseTableRow(line);
      i += 2; // skip header + separator
      const rows = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        rows.push(parseTableRow(lines[i]));
        i++;
      }
      blocks.push({ type: 'table', header: headerCells, rows });
      continue;
    }

    // Fenced code block
    if (line.trim().startsWith('```')) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // skip closing fence
      blocks.push({ type: 'code', text: codeLines.join('\n') });
      continue;
    }

    // Blockquote
    if (line.startsWith('>')) {
      const blockLines = [];
      while (i < lines.length && lines[i].startsWith('>')) {
        blockLines.push(lines[i].replace(/^>\s?/, ''));
        i++;
      }
      blocks.push({ type: 'blockquote', text: blockLines.join(' ') });
      continue;
    }

    // List (bullet, numbered, or checkbox)
    if (/^\s*[-*+]\s+/.test(line) || /^\s*\d+\.\s+/.test(line)) {
      const items = [];
      while (i < lines.length && (/^\s*[-*+]\s+/.test(lines[i]) || /^\s*\d+\.\s+/.test(lines[i]))) {
        let text = lines[i].replace(/^\s*([-*+]|\d+\.)\s+/, '');
        const isOrdered = /^\s*\d+\.\s+/.test(lines[i]);
        let checkbox = null;
        const cbMatch = text.match(/^\[(x|X|\s)\]\s+(.*)$/);
        if (cbMatch) {
          checkbox = cbMatch[1].trim().toLowerCase() === 'x' ? 'checked' : 'unchecked';
          text = cbMatch[2];
        }
        items.push({ ordered: isOrdered, text, checkbox });
        i++;
        // Handle continuation lines (indented under a bullet)
        while (i < lines.length && /^\s{2,}\S/.test(lines[i]) && !/^\s*[-*+]\s+/.test(lines[i]) && !/^\s*\d+\.\s+/.test(lines[i])) {
          items[items.length - 1].text += ' ' + lines[i].trim();
          i++;
        }
      }
      blocks.push({ type: 'list', items });
      continue;
    }

    // Paragraph (collect contiguous lines)
    const paraLines = [line];
    i++;
    while (i < lines.length && lines[i].trim() &&
           !/^(#{1,4})\s+/.test(lines[i]) &&
           !/^---+\s*$/.test(lines[i]) &&
           !lines[i].trim().startsWith('|') &&
           !lines[i].trim().startsWith('```') &&
           !lines[i].startsWith('>') &&
           !/^\s*[-*+]\s+/.test(lines[i]) &&
           !/^\s*\d+\.\s+/.test(lines[i])) {
      paraLines.push(lines[i]);
      i++;
    }
    blocks.push({ type: 'paragraph', text: paraLines.join(' ') });
  }

  return blocks;
}

// ===== Block → docx-js builders =====

function buildHeading(level, text) {
  const styleMap = {
    1: { size: 36, color: NAVY, bold: true, before: 360, after: 120,
         underline: false, hasBottomBorder: true },
    2: { size: 28, color: NAVY, bold: true, before: 320, after: 100,
         hasBottomBorder: false },
    3: { size: 22, color: CORAL, bold: true, before: 240, after: 80 },
    4: { size: 18, color: NAVY, bold: true, before: 200, after: 60 },
  };
  const s = styleMap[level] || styleMap[4];
  const paraOpts = {
    spacing: { before: s.before, after: s.after, line: 280 },
    children: [new TextRun({ text, bold: s.bold, size: s.size, color: s.color, font: FONT_DISPLAY })],
  };
  if (s.hasBottomBorder) {
    paraOpts.border = { bottom: { color: CORAL, style: BorderStyle.SINGLE, size: 18, space: 4 } };
  }
  return new Paragraph(paraOpts);
}

function buildParagraph(text) {
  return new Paragraph({
    spacing: { before: 100, after: 100, line: 320 },
    children: parseInline(text),
  });
}

function buildHRule() {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    border: { bottom: { color: CORAL, style: BorderStyle.SINGLE, size: 12, space: 1 } },
    children: [],
  });
}

// Parse inline markdown with extra overlay styles (applied per resulting TextRun)
function parseInlineWithOverlay(text, overlay) {
  const pattern = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\{\{[^}]+\}\})/g;
  const parts = text.split(pattern).filter(p => p && p.length > 0);
  return parts.map(p => {
    let opts = { text: unescapeMarkdown(p), color: NAVY, font: FONT_BODY };
    if (p.startsWith('**') && p.endsWith('**')) {
      opts = { ...opts, text: unescapeMarkdown(p.slice(2, -2)), bold: true };
    } else if (p.startsWith('*') && p.endsWith('*') && p.length > 2) {
      opts = { ...opts, text: unescapeMarkdown(p.slice(1, -1)), italics: true };
    } else if (p.startsWith('`') && p.endsWith('`')) {
      opts = { text: unescapeMarkdown(p.slice(1, -1)), font: FONT_MONO, color: NAVY, size: 20,
        shading: { fill: CREAM, type: ShadingType.CLEAR } };
    } else if (p.startsWith('{{') && p.endsWith('}}')) {
      opts = { text: p, color: CORAL, bold: true, font: FONT_BODY,
        shading: { fill: CORAL_SOFT, type: ShadingType.CLEAR } };
    }
    return new TextRun({ ...opts, ...overlay });
  });
}

function buildBlockquote(text) {
  return new Paragraph({
    spacing: { before: 100, after: 100, line: 300 },
    border: {
      top: { color: CORAL_SOFT, style: BorderStyle.SINGLE, size: 4 },
      left: { color: CORAL, style: BorderStyle.SINGLE, size: 24, space: 12 },
      bottom: { color: CORAL_SOFT, style: BorderStyle.SINGLE, size: 4 },
      right: { color: CORAL_SOFT, style: BorderStyle.SINGLE, size: 4 },
    },
    indent: { left: 200 },
    shading: { fill: CREAM, type: ShadingType.CLEAR },
    children: parseInlineWithOverlay(text, { italics: true, color: NAVY }),
  });
}

function buildCodeBlock(text) {
  const lines = text.split('\n');
  const isFirst = (idx) => idx === 0;
  const isLast = (idx) => idx === lines.length - 1;
  return lines.map((line, idx) => new Paragraph({
    spacing: { before: isFirst(idx) ? 120 : 0, after: isLast(idx) ? 120 : 0, line: 280 },
    shading: { fill: CREAM, type: ShadingType.CLEAR },
    border: {
      top: isFirst(idx) ? border(LINE, 6) : { style: BorderStyle.NONE, size: 0, color: 'auto' },
      left: border(LINE, 6),
      bottom: isLast(idx) ? border(LINE, 6) : { style: BorderStyle.NONE, size: 0, color: 'auto' },
      right: border(LINE, 6),
    },
    children: [new TextRun({ text: line || ' ', font: FONT_MONO, size: 20, color: NAVY })],
  }));
}

function buildListItem(item, refKey) {
  const prefix = item.checkbox === 'unchecked' ? '☐  ' :
                 item.checkbox === 'checked'   ? '☑  ' : '';
  if (item.checkbox) {
    return new Paragraph({
      spacing: { before: 60, after: 60, line: 300 },
      indent: { left: 360, hanging: 240 },
      children: [
        new TextRun({ text: prefix, color: CORAL, font: FONT_BODY, size: 24 }),
        ...parseInline(item.text),
      ],
    });
  }
  return new Paragraph({
    numbering: { reference: refKey, level: 0 },
    spacing: { before: 60, after: 60, line: 300 },
    children: parseInline(item.text),
  });
}

function buildList(items, refKey) {
  return items.map(it => buildListItem(it, refKey));
}

function buildTable(header, rows, contentWidth = 9360) {
  const colCount = header.length;
  const colWidth = Math.floor(contentWidth / colCount);
  const columnWidths = Array(colCount).fill(colWidth);
  // Adjust last column to absorb rounding
  columnWidths[colCount - 1] = contentWidth - colWidth * (colCount - 1);

  const headerRow = new TableRow({
    tableHeader: true,
    children: header.map((cell, i) => new TableCell({
      width: { size: columnWidths[i], type: WidthType.DXA },
      shading: { fill: NAVY, type: ShadingType.CLEAR },
      borders: cellBorders(NAVY),
      margins: { top: 100, bottom: 100, left: 140, right: 140 },
      children: [new Paragraph({
        spacing: { before: 0, after: 0, line: 280 },
        children: parseInlineWithOverlay(cell, { color: WHITE, bold: true, font: FONT_DISPLAY, size: 20 }),
      })],
    })),
  });

  const bodyRows = rows.map((row, rowIdx) => new TableRow({
    children: row.map((cell, colIdx) => new TableCell({
      width: { size: columnWidths[colIdx], type: WidthType.DXA },
      shading: { fill: rowIdx % 2 === 0 ? WHITE : CREAM, type: ShadingType.CLEAR },
      borders: cellBorders(LINE),
      margins: { top: 100, bottom: 100, left: 140, right: 140 },
      children: [new Paragraph({
        spacing: { before: 0, after: 0, line: 280 },
        children: parseInline(cell),
      })],
    })),
  }));

  return new Table({
    width: { size: contentWidth, type: WidthType.DXA },
    columnWidths,
    rows: [headerRow, ...bodyRows],
  });
}

// Convert a block to one or more docx-js children
function blockToDocx(block, listRefCounter) {
  switch (block.type) {
    case 'heading':   return [buildHeading(block.level, block.text)];
    case 'paragraph': return [buildParagraph(block.text)];
    case 'hrule':     return [buildHRule()];
    case 'blockquote':return [buildBlockquote(block.text)];
    case 'code':      return buildCodeBlock(block.text);
    case 'list': {
      const refKey = `list_${listRefCounter.count++}`;
      // For unordered or ordered list (non-checkbox), declare a numbering ref
      // We'll register them all up front when building the doc
      return buildList(block.items, refKey);
    }
    case 'table':     return [buildTable(block.header, block.rows)];
    default:          return [];
  }
}

// ===== Document scaffolding (tagline + footer + title) =====

function buildTitleBlock(title, subtitle) {
  return [
    // Tagline banner
    new Paragraph({
      spacing: { before: 0, after: 0, line: 280 },
      shading: { fill: CORAL, type: ShadingType.CLEAR },
      alignment: AlignmentType.CENTER,
      border: {
        top: { color: CORAL, style: BorderStyle.SINGLE, size: 8 },
        left: { color: CORAL, style: BorderStyle.SINGLE, size: 8 },
        bottom: { color: CORAL, style: BorderStyle.SINGLE, size: 8 },
        right: { color: CORAL, style: BorderStyle.SINGLE, size: 8 },
      },
      children: [new TextRun({
        text: 'CAMPUS-OWNED.  SBNC-SUPPORTED.  STUDENT-DRIVEN.',
        color: WHITE, bold: true, size: 22, font: FONT_DISPLAY,
      })],
    }),
    // SBNC mark line
    new Paragraph({
      spacing: { before: 280, after: 120 },
      children: [
        new TextRun({ text: 'SBNC', color: CORAL, bold: true, size: 32, font: FONT_DISPLAY }),
        new TextRun({ text: '   ·   Student Basic Needs Coalition', color: CORAL, size: 18, font: FONT_BODY }),
      ],
    }),
    // Document title
    new Paragraph({
      spacing: { before: 200, after: 80, line: 300 },
      border: { bottom: { color: CORAL, style: BorderStyle.SINGLE, size: 18, space: 4 } },
      children: [new TextRun({ text: title, color: NAVY, bold: true, size: 44, font: FONT_DISPLAY })],
    }),
    new Paragraph({
      spacing: { before: 80, after: 240 },
      children: [new TextRun({ text: subtitle, color: GRAY, italics: true, size: 22, font: FONT_BODY })],
    }),
  ];
}

function buildFooter() {
  return new Footer({
    children: [new Paragraph({
      spacing: { before: 0, after: 0 },
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: 'www.studentbasicneeds.com  ·  ', color: CORAL, italics: true, size: 18, font: FONT_BODY }),
        new TextRun({ text: 'SBNC', color: CORAL, bold: true, size: 18, font: FONT_DISPLAY }),
        new TextRun({ text: '  ·  contact@studentbasicneeds.com', color: CORAL, italics: true, size: 18, font: FONT_BODY }),
      ],
    })],
  });
}

// ===== Build a single document =====

async function buildDoc(title, subtitle, mdPath, outPath) {
  const md = fs.readFileSync(mdPath, 'utf8');

  // Strip the first H1 from the markdown if it matches the title
  // (so we don't duplicate it after the cover block)
  const lines = md.split('\n');
  let mdBody = md;
  if (lines[0] && lines[0].startsWith('# ')) {
    // remove first heading and any blank lines that follow
    let cut = 1;
    while (cut < lines.length && !lines[cut].trim()) cut++;
    mdBody = lines.slice(cut).join('\n');
  }

  // Some artifacts have a "For:" / "What this is:" / "Companion docs:" block at the top.
  // Leave it in; it'll render as paragraphs.

  const blocks = parseMD(mdBody);
  const listRefCounter = { count: 0 };

  // Pre-scan blocks to count lists; we need numbering configs for each list with a unique ref
  const listRefs = [];
  for (const b of blocks) {
    if (b.type === 'list') {
      // We'll generate a unique ref per list later when building
      listRefs.push(null); // placeholder
    }
  }

  // Build content
  const cover = buildTitleBlock(title, subtitle);
  const content = [];
  for (const b of blocks) {
    const items = blockToDocx(b, listRefCounter);
    for (const it of items) content.push(it);
  }

  // Numbering config: bullets + numbers; we'll keep them shared (continuing) per type
  // To keep lists separate, declare per-ref. Build configs:
  const numberingConfigs = [];
  for (let i = 0; i < listRefCounter.count; i++) {
    numberingConfigs.push({
      reference: `list_${i}`,
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
        style: {
          paragraph: { indent: { left: 720, hanging: 360 } },
          run: { color: CORAL, font: FONT_DISPLAY, bold: true },
        },
      }],
    });
  }
  // also add a generic ordered fallback (not used because we treat ordered lists as bullets for simplicity)

  const doc = new Document({
    creator: 'SBNC',
    title,
    description: subtitle,
    styles: {
      default: { document: { run: { font: FONT_BODY, size: 22, color: NAVY } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 36, bold: true, font: FONT_DISPLAY, color: NAVY },
          paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 28, bold: true, font: FONT_DISPLAY, color: NAVY },
          paragraph: { spacing: { before: 320, after: 100 }, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 22, bold: true, font: FONT_DISPLAY, color: CORAL },
          paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 2 } },
      ],
    },
    numbering: { config: numberingConfigs.length ? numberingConfigs : [{
      reference: 'unused',
      levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
    }] },
    sections: [{
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }, // 0.75"
        },
      },
      footers: { default: buildFooter() },
      children: [...cover, ...content],
    }],
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(outPath, buffer);
  console.log(`Wrote ${outPath} (${buffer.length} bytes)`);
}

// ===== Main =====

const WORKING = '/sessions/relaxed-hopeful-cray/mnt/Benefits_SBNC/02_Working';

(async () => {
  await buildDoc(
    'Navvy Student Outreach',
    'Strategy Reference  ·  Read once before you customize anything.',
    path.join(WORKING, '01_Strategy_reference.md'),
    path.join(WORKING, '01_Strategy_reference.docx'),
  );
  await buildDoc(
    'Navvy Student Outreach',
    'Editable Templates  ·  The customizable templates. Fill the worksheet, then send.',
    path.join(WORKING, '02_Editable_templates.md'),
    path.join(WORKING, '02_Editable_templates.docx'),
  );
  await buildDoc(
    'Navvy Student Outreach',
    'Pre-Send Checklist  ·  Use before every send.',
    path.join(WORKING, '03_Pre_send_checklist.md'),
    path.join(WORKING, '03_Pre_send_checklist.docx'),
  );
  console.log('All three docs generated.');
})().catch(err => { console.error(err); process.exit(1); });
