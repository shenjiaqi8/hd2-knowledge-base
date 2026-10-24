#!/usr/bin/env python3
"""One-time patch installer for shenjiaqi8/hd2-knowledge-base.
Run from repository root after copying patch files to scripts/.
"""
from pathlib import Path

root = Path(__file__).resolve().parent
source = root / 'scripts' / 'hd2_to_markdown.py'
plugin = root / 'scripts' / 'consolidate_categories.py'
assert plugin.is_file(), 'Missing scripts/consolidate_categories.py'
assert source.is_file(), 'Missing scripts/hd2_to_markdown.py'
s = source.read_text(encoding='utf-8')
marker = '\ndef main():'
if 'from consolidate_categories import consolidate' in s:
    print('Patch already installed; no changes needed.')
else:
    old = '\ndef build(out: Path, rows: dict, info: dict, meta: dict, aliases: dict, include_raw: bool, scope: str):'
    assert old in s, 'Unexpected collector version. No file changed.'
    assert marker in s, 'Cannot find main() in collector. No file changed.'
    s = s.replace(old, old.replace('def build(', 'def _build_individual('), 1)
    wrapper = '''\ndef build(out: Path, rows: dict, info: dict, meta: dict, aliases: dict, include_raw: bool, scope: str):
    # Generate faithful item pages using the original converter, then combine
    # every category into one Markdown. The final repository contains only
    # generated/<category>.md, never hundreds of tiny pages.
    from consolidate_categories import consolidate
    _build_individual(out, rows, info, meta, aliases, include_raw, scope)
    stats = consolidate(out)
    print(f"Consolidated into {len(stats)} Markdown category files.")

'''
    s = s.replace(marker, wrapper + marker, 1)
    source.write_text(s, encoding='utf-8')
    print('Patched scripts/hd2_to_markdown.py')

# Convert already-generated files without re-fetching data.
from scripts.consolidate_categories import consolidate
stats = consolidate(root / 'knowledge')
print('Existing knowledge files:', stats or 'already consolidated')
print('Next: git add -A; git commit -m "Group HD2 data by category"; git push')
