#!/usr/bin/env python3
"""Build an HD2 Markdown knowledge base from a public, wiki-derived JSON catalog.

No third-party dependencies. Source: DionathaGoulart/Helldivers-api / The Helldivers Wiki.
Offline SQLite import supports the earlier HD2 Data Collector sample database.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import sqlite3
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from typing import Any

SRC_ROOTS = [
    ("api", "https://helldivers-api.dionatha.com.br/v1"),
    ("github", "https://raw.githubusercontent.com/DionathaGoulart/Helldivers-api/main/data/v1"),
]
REPO = "https://github.com/DionathaGoulart/Helldivers-api"
WIKI = "https://helldivers.wiki.gg/"
CORE = {"weapons", "stratagems", "armors", "armor-sets", "boosters", "passives", "weapon-traits", "warbonds"}
LABELS = {
    "weapons": "武器", "stratagems": "战略配备", "armors": "护甲", "armor-sets": "护甲套装",
    "boosters": "强化剂", "passives": "护甲被动", "weapon-traits": "装备特性", "warbonds": "战争债券",
    "helmets": "头盔", "capes": "披风", "player-cards": "玩家卡片", "emotes": "表情与动作",
    "patterns": "涂装", "titles": "头衔",
}
FIELD_LABELS = {
    "category": "类别", "subcategory": "子类别", "kind": "类型", "weight": "重量类型",
    "armorRating": "护甲值", "speed": "速度", "staminaRegen": "耐力恢复", "passiveId": "被动技能 ID",
    "effect": "效果", "cost": "消耗", "cooldownS": "冷却时间（秒）", "callInTimeS": "呼叫时间（秒）",
    "uses": "使用次数", "code": "输入指令", "traitIds": "特性 ID", "capacity": "容量",
    "spareMagazines": "备用弹匣", "fireRateRpm": "射速（RPM）", "recoil": "后坐力",
    "reloadTimeS": "装填时间（秒）", "startingMagazines": "初始弹匣", "standard": "常规伤害",
    "durable": "耐久伤害", "direct": "正面穿甲", "slightAngle": "小角度穿甲",
    "largeAngle": "大角度穿甲", "extremeAngle": "极大角度穿甲",
    "source": "获取来源", "warbondId": "战争债券 ID", "aliases": "其他名称",
}
HTTP_HEADERS = {"User-Agent": "HD2-Markdown-Collector/1.0 (personal noncommercial knowledge base)", "Accept": "application/json"}


def get_json(url: str, attempts: int = 3) -> Any:
    for i in range(attempts):
        try:
            with urlopen(Request(url, headers=HTTP_HEADERS), timeout=45) as res:
                size = res.headers.get("Content-Length")
                if size and int(size) > 30_000_000:
                    raise ValueError("Response too large")
                payload = res.read(30_000_001)
                if len(payload) > 30_000_000:
                    raise ValueError("Response too large")
                return json.loads(payload.decode("utf-8-sig"))
        except (OSError, HTTPError, URLError, ValueError, TimeoutError) as exc:
            if i == attempts - 1:
                raise RuntimeError(f"Failed {url}: {exc}") from exc
            time.sleep(i + 1)
    raise AssertionError("unreachable")


def validate(name: str, payload: Any, meta: dict) -> list[dict]:
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ValueError(f"{name}: expected {{meta, data: [...]}}")
    entries = payload["data"]
    version = meta.get("dataVersion")
    payload_version = payload.get("meta", {}).get("dataVersion")
    if version and payload_version and version != payload_version:
        raise ValueError(f"{name}: data version mismatch")
    expected = meta.get("collections", {}).get(name, {}).get("count")
    if expected is not None and len(entries) != expected:
        raise ValueError(f"{name}: manifest count {expected} != {len(entries)}")
    declared = payload.get("meta", {}).get("count")
    if declared is not None and len(entries) != declared:
        raise ValueError(f"{name}: response count {declared} != {len(entries)}")
    ids = []
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("id") or not entry.get("name"):
            raise ValueError(f"{name}: invalid entry id/name")
        ids.append(str(entry["id"]))
    if len(ids) != len(set(ids)):
        raise ValueError(f"{name}: duplicate ids")
    return entries


def sync_json(scope: str, chosen_source: str) -> tuple[dict, dict, dict]:
    errors = []
    for name, base in SRC_ROOTS:
        if chosen_source != "auto" and name != chosen_source:
            continue
        try:
            print(f"Connecting to {name}: {base}", flush=True)
            meta = get_json(base + "/meta.json")
            collections = meta.get("collections")
            if not isinstance(collections, dict) or not collections:
                raise ValueError("Invalid manifest")
            included = sorted(n for n in collections if (scope == "all" or n in CORE))
            data = {}
            for category in included:
                if not re.fullmatch("[a-z0-9-]+", category):
                    raise ValueError(f"Unsafe collection name: {category}")
                rows = validate(category, get_json(f"{base}/{category}.json"), meta)
                data[category] = rows
                print(f"  {category}: {len(rows)} records", flush=True)
                time.sleep(0.15)
            if not data:
                raise ValueError("No supported categories")
            info = {"inputMode": "sync", "sourceName": name, "sourceBase": base,
                    "generatedAt": meta.get("generatedAt"), "dataVersion": meta.get("dataVersion"),
                    "completeForScope": True}
            return data, info, meta
        except Exception as exc:
            errors.append(f"{name}: {exc}")
            print(f"{name} error: {exc}", file=sys.stderr, flush=True)
    raise RuntimeError("Could not download a consistent source set.\n" + "\n".join(errors))


def from_json_dir(directory: Path, scope: str):
    raw_dir = directory / "raw" if (directory / "raw" / "meta.json").exists() else directory
    meta = json.loads((raw_dir / "meta.json").read_text(encoding="utf-8"))
    collections = meta.get("collections", {})
    names = sorted(n for n in collections if scope == "all" or n in CORE)
    result = {}
    for name in names:
        obj = json.loads((raw_dir / f"{name}.json").read_text(encoding="utf-8"))
        result[name] = validate(name, obj, meta)
    info = {"inputMode": "local-json", "sourceName": "local JSON files", "dataVersion": meta.get("dataVersion"),
            "generatedAt": meta.get("generatedAt"), "completeForScope": True}
    return result, info, meta


def from_sqlite(file: Path, scope: str):
    con = sqlite3.connect(str(file))
    try:
        result = {}
        for category, raw in con.execute("SELECT collection, raw_json FROM entities ORDER BY collection, id"):
            if scope == "gameplay" and category not in CORE:
                continue
            row = json.loads(raw)
            if not isinstance(row, dict) or not row.get("name") or not row.get("id"):
                raise ValueError("Invalid row in SQLite")
            result.setdefault(category, []).append(row)
        metadata = {}
        try:
            for key, val in con.execute("SELECT key, value FROM metadata"):
                metadata[key] = json.loads(val)
        except sqlite3.OperationalError:
            pass
    finally:
        con.close()
    if not result:
        raise ValueError("SQLite contains no matching records")
    info = {"inputMode": "local-sqlite", "sourceName": "previous collector SQLite sample",
            "dataVersion": metadata.get("dataVersion", "unknown"),
            "generatedAt": metadata.get("dataGeneratedAt"), "completeForScope": False,
            "note": "SQLite import cannot certify that the catalog is complete"}
    return result, info, {}


def slug(value: Any) -> str:
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", str(value)).strip(".-")
    if not s or s in {".", ".."}:
        raise ValueError(f"Invalid entity id {value!r}")
    return s.lower()


def clean_text(s: Any) -> str:
    # Avoid treating incidental HTML in source fields as markup. Preserve literal values.
    text = html.unescape(str(s))
    text = re.sub(r"<[^>]*>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def md_escape(text: Any) -> str:
    return clean_text(text).replace("|", "\\|").replace("`", "\\`").replace("[", "\\[").replace("]", "\\]")


def plain(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "是" if value else "否"
    if isinstance(value, (str, int, float)):
        return md_escape(value)
    if isinstance(value, list):
        return ", ".join(plain(v) for v in value) if value else "—"
    if isinstance(value, dict):
        return "; ".join(f"{md_escape(k)}: {plain(v)}" for k, v in value.items()) if value else "—"
    return md_escape(value)


def field_name(key: str) -> str:
    return f"{FIELD_LABELS[key]} (`{key}`)" if key in FIELD_LABELS else f"`{key}`"


def rows_for_dict(data: dict, prefix: str = "", depth: int = 0) -> list[tuple[str, str]]:
    result = []
    for k, v in data.items():
        full = prefix + str(k)
        if isinstance(v, dict) and depth < 4:
            result += rows_for_dict(v, full + ".", depth + 1)
        elif isinstance(v, list) and v and any(isinstance(x, dict) for x in v):
            for n, child in enumerate(v, 1):
                if isinstance(child, dict):
                    result += rows_for_dict(child, full + f"[{n}].", depth + 1)
                else:
                    result.append((full + f"[{n}]", plain(child)))
        else:
            result.append((full, plain(v)))
    return result


def table(data: dict) -> str:
    entries = rows_for_dict(data)
    if not entries:
        return "_暂无可用属性。_\n"
    out = ["| 字段 | 数值 |", "|---|---|"]
    for path, value in entries:
        label = field_name(path) if "." not in path and "[" not in path else f"`{md_escape(path)}`"
        out.append(f"| {label} | {value} |")
    return "\n".join(out) + "\n"


def yaml_string(value: Any) -> str:
    # JSON-formatted strings/arrays are safe in YAML 1.2 frontmatter.
    return json.dumps(value, ensure_ascii=False)


def load_aliases(csv_path: Path | None) -> dict[tuple[str, str], list[str]]:
    if not csv_path:
        return {}
    if not csv_path.is_file():
        raise ValueError(f"Alias CSV missing: {csv_path}")
    out: dict[tuple[str, str], list[str]] = {}
    with csv_path.open(encoding="utf-8-sig", newline="") as fh:
        for item in csv.DictReader(fh):
            collection = (item.get("collection") or "").strip()
            id_ = (item.get("id") or "").strip()
            aliases = re.split(r"[,，;；]", item.get("aliases") or "")
            names = [v.strip() for v in aliases if v.strip()]
            if collection and id_ and names:
                out.setdefault((collection, id_), []).extend(names)
    return out


def render(entity: dict, collection: str, info: dict, alias_add: list[str], include_raw: bool) -> str:
    name = clean_text(entity["name"])
    wid = str(entity["id"])
    wiki = entity.get("wiki") if isinstance(entity.get("wiki"), dict) else {}
    wiki_url = str(wiki.get("url") or "")
    flags = wiki.get("flags") if isinstance(wiki.get("flags"), list) else []
    aliases = list(dict.fromkeys(x for x in (entity.get("aliases") or []) + alias_add if isinstance(x, str) and x.strip()))
    upcoming = entity.get("upcoming")
    status = "upcoming" if upcoming is True else "released" if upcoming is False else "unknown"
    source_url = f"https://helldivers-api.dionatha.com.br/v1/{collection}/{slug(wid)}.json"
    front = ["---", f"id: {yaml_string(wid)}", f"name: {yaml_string(name)}",
             f"collection: {yaml_string(collection)}", f"aliases: {yaml_string(aliases)}",
             f"status: {yaml_string(status)}", f"data_version: {yaml_string(info.get('dataVersion') or 'unknown')}",
             f"wiki_flags: {yaml_string(flags)}", f"wiki_url: {yaml_string(wiki_url)}",
             f"source_api_url: {yaml_string(source_url)}", "---", ""]
    body = [f"# {name}", "", f"**分类：** {LABELS.get(collection, collection)} (`{collection}`) · **ID：** `{wid}`"]
    if aliases:
        body.append(f"\n**别名：** {', '.join(md_escape(s) for s in aliases)}")
    if status == "upcoming":
        body.append("\n> ⚠️ 数据标记为尚未正式上线（upcoming）；具体参数可能变化。")
    if "potentially_outdated" in flags:
        body.append("\n> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。")
    if wiki_url:
        body += ["", f"**Wiki 原始词条：** {wiki_url}"]
    if entity.get("description"):
        body += ["", "## 简介", "", clean_text(entity["description"])]
    if entity.get("effect"):
        body += ["", "## 效果", "", clean_text(entity["effect"])]
    # Keep full entity context together. Distinguish actual firing modes and damage sources.
    ignore = {"id", "slug", "name", "aliases", "description", "effect", "upcoming", "wiki", "image", "source",
              "firearm", "attacks", "statsRaw"}
    base = {k: v for k, v in entity.items() if k not in ignore and v is not None}
    if base:
        body += ["", "## 主要属性", "", table(base)]
    if isinstance(entity.get("firearm"), dict):
        body += ["", "## 枪械属性", "", table(entity["firearm"])]
    if isinstance(entity.get("attacks"), list) and entity["attacks"]:
        body += ["", "## 攻击模式、伤害与穿甲"]
        for idx, attack in enumerate(entity["attacks"], 1):
            if not isinstance(attack, dict):
                continue
            title = clean_text(attack.get("name") or f"模式 {idx}")
            typ = clean_text(attack.get("kind") or "unknown")
            body += ["", f"### {idx}. {title}（{typ}）", "", table({k: v for k, v in attack.items() if k not in {"name", "kind"}})]
    if isinstance(entity.get("source"), dict):
        body += ["", "## 获取方式", "", table(entity["source"])]
    if include_raw and isinstance(entity.get("statsRaw"), dict):
        body += ["", "## Wiki 原始参数（可能存在冗余）", "", table(entity["statsRaw"])]
    body += ["", "## 数据来源与许可", "", f"- 来源数据：[{REPO}]({REPO})（基于 [The Helldivers Wiki]({WIKI})）",
             f"- API 记录：{source_url}"]
    if wiki_url:
        body.append(f"- Wiki 词条：{wiki_url}")
    body += [f"- 数据版本：`{info.get('dataVersion') or 'unknown'}`", "- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。", ""]
    return "\n".join(front + body) + "\n"


def build(out: Path, rows: dict, info: dict, meta: dict, aliases: dict, include_raw: bool, scope: str):
    out.mkdir(parents=True, exist_ok=True)
    stage = out / ".generated-stage"
    current = out / "generated"
    backup = out / ".generated-backup"
    if stage.exists():
        shutil.rmtree(stage)
    if backup.exists():
        raise RuntimeError(f"Backup directory exists; inspect and remove it before retrying: {backup}")
    stage.mkdir()
    index = ["# Helldivers 2 知识库目录", "", "> 原始数据经 Markdown 结构化转换；本目录文件为自动生成，手工补充内容请放在 `notes/`。", "",
             f"**数据版本：** `{info.get('dataVersion') or 'unknown'}`  ",
             f"**导入模式：** `{info.get('inputMode')}`  ",
             f"**采集范围：** `{scope}`", ""]
    counts = {}
    seen = set()
    try:
        for collection, items in sorted(rows.items()):
            counts[collection] = len(items)
            folder = stage / collection
            folder.mkdir(parents=True, exist_ok=True)
            category_links = []
            for entity in sorted(items, key=lambda x: str(x.get("name", "")).casefold()):
                id_ = str(entity["id"])
                key = (collection, id_)
                if key in seen:
                    raise ValueError(f"Duplicate entry {key}")
                seen.add(key)
                filename = slug(id_) + ".md"
                p = folder / filename
                if p.exists():
                    raise ValueError(f"Unsafe slug collision {p}")
                md = render(entity, collection, info, aliases.get(key, []), include_raw)
                p.write_text(md, encoding="utf-8")
                safe_name = clean_text(entity["name"]).replace("[", "\\[").replace("]", "\\]")
                category_links.append(f"- [{safe_name}](./generated/{collection}/{filename})")
            index += [f"## {LABELS.get(collection, collection)}（{collection}，{len(items)} 条）", "", *category_links, ""]
        if current.exists():
            current.rename(backup)
        try:
            stage.rename(current)
        except Exception:
            if backup.exists():
                backup.rename(current)
            raise
        if backup.exists():
            shutil.rmtree(backup)
        (out / "_INDEX.md").write_text("\n".join(index), encoding="utf-8")
        m = {**info,
             "scope": scope, "fileCount": sum(counts.values()), "collections": counts,
             "license": "CC BY-NC-SA 4.0; verify source page where applicable",
             "sourceRepository": REPO, "wiki": WIKI}
        (out / "manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        notes = out / "notes"
        notes.mkdir(exist_ok=True)
        if not (notes / "README.md").exists():
            (notes / "README.md").write_text("# 自定义笔记\n\n此目录不会被同步程序覆盖。可以在此添加中文别名、战术解释和版本核对笔记。\n", encoding="utf-8")
        print(f"Created {sum(counts.values())} Markdown pages in {current}")
        print(f"Index: {out / '_INDEX.md'}")
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def main():
    parser = argparse.ArgumentParser(description="Helldivers 2 JSON/SQLite -> Markdown knowledge base")
    inp = parser.add_mutually_exclusive_group()
    inp.add_argument("--json-dir", type=Path, help="Existing JSON directory (or parent folder with raw/meta.json)")
    inp.add_argument("--sqlite", type=Path, help="Previous hd2.sqlite file for offline conversion")
    parser.add_argument("--out", type=Path, default=Path("./HD2_Knowledge_Base"), help="Output knowledge base directory")
    parser.add_argument("--scope", choices=["gameplay", "all"], default="gameplay", help="Default: gameplay-relevant equipment only")
    parser.add_argument("--source", choices=["auto", "api", "github"], default="auto", help="Only for live sync")
    parser.add_argument("--aliases-csv", type=Path, help="Optional user-curated Chinese/English aliases CSV")
    parser.add_argument("--include-raw-stats", action="store_true", help="Also embed bulky statsRaw tables")
    args = parser.parse_args()
    try:
        if args.sqlite:
            rows, info, meta = from_sqlite(args.sqlite, args.scope)
        elif args.json_dir:
            rows, info, meta = from_json_dir(args.json_dir, args.scope)
        else:
            rows, info, meta = sync_json(args.scope, args.source)
        build(args.out.resolve(), rows, info, meta, load_aliases(args.aliases_csv), args.include_raw_stats, args.scope)
    except (RuntimeError, ValueError, OSError, KeyError, json.JSONDecodeError, sqlite3.Error) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
