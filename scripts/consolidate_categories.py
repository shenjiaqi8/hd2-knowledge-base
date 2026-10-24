#!/usr/bin/env python3
"""Consolidate a per-entity HD2 Markdown knowledge base into one file per category.

Input: knowledge/generated/<category>/<entity-id>.md
Output: knowledge/generated/<category>.md

No third-party packages. Preserves every source page's text and per-item metadata.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

CATEGORY_NAMES = {
    'weapons': '武器', 'stratagems': '战略配备', 'armors': '护甲',
    'armor-sets': '护甲套装', 'boosters': '强化剂', 'passives': '护甲被动',
    'weapon-traits': '武器特性', 'warbonds': '战争债券',
    'helmets': '头盔', 'capes': '披风', 'player-cards': '玩家卡片',
    'emotes': '动作表情', 'patterns': '涂装', 'titles': '头衔',
}


def parse_page(path: Path):
    s = path.read_text(encoding='utf-8-sig')
    meta = {}
    if s.startswith('---\n'):
        end = s.find('\n---\n', 4)
        if end == -1:
            raise ValueError(f'Invalid YAML header: {path}')
        head, s = s[4:end], s[end + 5:]
        # Existing generator writes scalar fields as JSON-in-YAML.
        for line in head.splitlines():
            k, sep, v = line.partition(': ')
            if sep:
                try:
                    meta[k] = json.loads(v)
                except (ValueError, TypeError):
                    meta[k] = v
    m = re.search(r'^# (.+)$', s, re.M)
    name = str(meta.get('name') or (m.group(1) if m else path.stem))
    aliases = meta.get('aliases', [])
    if not isinstance(aliases, list):
        aliases = []
    return name, [str(a) for a in aliases if a], meta, s.strip()


def consolidate(knowledge: Path) -> dict[str, int]:
    root = knowledge / 'generated'
    folders = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith('.'))
    if not folders:
        # Already converted; stay idempotent.
        return {}
    output: dict[str, str] = {}
    counts = {}
    for folder in folders:
        pages = sorted(folder.glob('*.md'))
        if not pages:
            continue
        records = sorted((parse_page(p) for p in pages), key=lambda v: v[0].casefold())
        category = folder.name
        title = CATEGORY_NAMES.get(category, category)
        chunks = [
            f'# 绝地潜兵2 — {title}', '',
            f'> 本文件汇总 {len(records)} 条{title}资料；实体名称为二级标题，可直接按名称和别名检索。',
            '> 数据源为社区整理，数值可能随游戏版本变化。', '',
            '## 名称及别名索引', '',
        ]
        for name, aliases, meta, body in records:
            val = name.replace('\n', ' ').replace('|', '\\|')
            names = '、'.join(x.replace('|', '\\|') for x in aliases)
            id_part = f" · ID: `{meta['id']}`" if meta.get('id') else ''
            chunks.append(f'- **{val}**{id_part}' + (f' · 别名：{names}' if names else ''))
        chunks.extend(['', '---', '', '## 装备与条目详情', ''])
        for name, aliases, meta, body in records:
            # Original page: # Entity, ## details, ### attack mode.
            # Result: ## Entity, ### details, #### attack mode.
            lines = body.splitlines()
            normalized = []
            for line in lines:
                m = re.match(r'^(#{1,5}) (.*)', line)
                if m:
                    line = '#' * (len(m.group(1)) + 1) + ' ' + m.group(2)
                normalized.append(line)
            chunks += normalized + ['', '---', '']
        output[category + '.md'] = '\n'.join(chunks).rstrip() + '\n'
        counts[category] = len(records)

    # Write all complete pages before removing any original files.
    temp = knowledge / '.category-merge-temp'
    if temp.exists():
        shutil.rmtree(temp)
    temp.mkdir()
    try:
        for filename, content in output.items():
            (temp / filename).write_text(content, encoding='utf-8')
        # Move directory out of the way, then switch atomically to compact layout.
        backup = knowledge / '.generated-before-category-merge'
        if backup.exists():
            raise RuntimeError(f'Backup directory already exists: {backup}')
        root.rename(backup)
        try:
            temp.rename(root)
        except Exception:
            backup.rename(root)
            raise
        shutil.rmtree(backup)
    finally:
        if temp.exists():
            shutil.rmtree(temp)

    version = 'unknown'
    manifest_path = knowledge / 'manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        version = str(manifest.get('dataVersion') or 'unknown')
        manifest['fileCount'] = len(output)
        manifest['entityCount'] = sum(counts.values())
        manifest['layout'] = 'one-file-per-category'
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    idx = [
        '# 绝地潜兵2知识库目录', '',
        '> 每个游戏数据大类对应一份 Markdown 文件，详见分类文档中的名称及别名索引。',
        f'> 数据版本：`{version}`', '',
    ]
    for category, n in sorted(counts.items()):
        idx.append(f'- [{CATEGORY_NAMES.get(category, category)}（{n} 条）](generated/{category}.md)')
    idx.extend(['', '> 敌人数据（enemies）尚不在当前装备 JSON 数据源中，未虚构敌人词条。', ''])
    (knowledge / '_INDEX.md').write_text('\n'.join(idx), encoding='utf-8')
    return counts


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--knowledge', type=Path, default=Path('knowledge'))
    a = p.parse_args()
    stats = consolidate(a.knowledge.resolve())
    print('Merged categories:', stats if stats else 'already consolidated or no inputs')
