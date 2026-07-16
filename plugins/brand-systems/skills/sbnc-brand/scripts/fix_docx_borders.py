#!/usr/bin/env python3
"""Post-process docx-js output: reorder paragraph border elements from
docx-js's incorrect (top, bottom, left, right) to OOXML's required
(top, left, bottom, right). Works in-place on the .docx zip."""

import re
import shutil
import sys
import zipfile
from pathlib import Path

# Matches the buggy 4-line block emitted by docx-js inside <w:pBdr>
# The pattern is intentionally permissive about attributes inside each element.
PBDR_PATTERN = re.compile(
    r'(<w:pBdr>\s*)'
    r'(<w:top [^/]*/>)\s*'
    r'(<w:bottom [^/]*/>)\s*'
    r'(<w:left [^/]*/>)\s*'
    r'(<w:right [^/]*/>)',
    re.DOTALL,
)

# Also handle the 3-element variants where top is missing
PBDR_NOTOP_PATTERN = re.compile(
    r'(<w:pBdr>\s*)'
    r'(<w:bottom [^/]*/>)\s*'
    r'(<w:left [^/]*/>)\s*'
    r'(<w:right [^/]*/>)',
    re.DOTALL,
)


def reorder_borders(xml_text):
    out = PBDR_PATTERN.sub(
        lambda m: f'{m.group(1)}{m.group(2)}\n          {m.group(4)}\n          {m.group(3)}\n          {m.group(5)}',
        xml_text,
    )
    out = PBDR_NOTOP_PATTERN.sub(
        lambda m: f'{m.group(1)}{m.group(3)}\n          {m.group(2)}\n          {m.group(4)}',
        out,
    )
    return out


def fix_docx(path: Path):
    tmp_path = path.with_suffix('.docx.tmp')
    with zipfile.ZipFile(path, 'r') as src, zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as dst:
        for item in src.namelist():
            data = src.read(item)
            if item.endswith('.xml'):
                text = data.decode('utf-8')
                text = reorder_borders(text)
                data = text.encode('utf-8')
            dst.writestr(item, data)
    shutil.move(str(tmp_path), str(path))


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    for p in paths:
        fix_docx(p)
        print(f'Fixed: {p}')


if __name__ == '__main__':
    main()
