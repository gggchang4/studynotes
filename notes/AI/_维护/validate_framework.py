"""Validate the AI Obsidian framework without rewriting any topic notes."""
from __future__ import annotations

import argparse
import collections
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

AI = Path(__file__).resolve().parent.parent
VAULT = AI.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def norm(value: str) -> str:
    return re.sub(r"[\s*\x60|;；。，,：:（）()—–\-]", "", value).lower()


def prose(value: str) -> str:
    return re.sub(r"(?ms)^\x60\x60\x60[^\n]*\n.*?^\x60\x60\x60[^\n]*$", "", value)


def inside_ai(path: Path) -> bool:
    try:
        path.resolve().relative_to(AI)
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default=str(AI / "_维护" / "验证结果.json"))
    args = parser.parse_args()
    report_path = Path(args.report).resolve()
    if not inside_ai(report_path):
        parser.error("The report must stay inside AI/.")
    manifest = json.loads(read(AI / "_维护" / "框架清单.json"))
    sources = json.loads(read(AI / "_维护" / "来源清单.json"))
    topics = manifest["topics"]
    by_id = {t["id"]: t for t in topics}
    all_sources = sources["materials"] + sources["papers"]
    source_ids = {s["id"] for s in all_sources}
    errors: list[str] = []
    wiki_count = 0
    markdown_count = 0
    image_count = 0

    if len(by_id) != len(topics):
        errors.append("Duplicate topic IDs")
    if len(source_ids) != len(all_sources):
        errors.append("Duplicate source IDs")

    route_counts = collections.Counter(r for t in topics for r in t["rows"])
    expected_rows = {r["id"] for r in manifest["route_rows"]}
    if set(route_counts) != expected_rows:
        errors.append("Route coverage differs from manifest rows")
    for row_id, count in route_counts.items():
        if count != 1:
            errors.append(f"Route row {row_id} has {count} owners")

    for topic in topics:
        path = VAULT / topic["path"]
        if not path.is_file():
            errors.append(f"Missing topic: {topic['path']}")
            continue
        content = read(path)
        status_match = re.search(r"(?m)^status:\s*(\S+)", content)
        status = status_match.group(1) if status_match else ""
        if status not in {"framework", "draft", "reviewed"}:
            errors.append(f"Missing/unknown topic status: {topic['id']}")
        source_match = re.search(r"(?m)^sources:\s*(\[.*\])\s*$", content)
        try:
            note_sources = json.loads(source_match.group(1)) if source_match else []
        except (ValueError, AttributeError):
            note_sources = []
        if not note_sources:
            errors.append(f"No material references: {topic['id']}")
        for sid in note_sources:
            if sid not in source_ids:
                errors.append(f"Unknown source {sid}: {topic['id']}")
        if status == "framework":
            for row_id in topic["rows"]:
                row = next(r for r in manifest["route_rows"] if r["id"] == row_id)
                if norm(row["content"]) not in norm(content):
                    errors.append(f"Framework outline lost row {row_id}: {topic['id']}")
        for prerequisite in topic["pre"]:
            if prerequisite not in by_id:
                errors.append(f"Missing prerequisite {prerequisite}: {topic['id']}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(tid: str) -> None:
        if tid in visiting:
            errors.append(f"Prerequisite cycle at {tid}")
            return
        if tid in visited:
            return
        visiting.add(tid)
        for parent in by_id[tid]["pre"]:
            if parent in by_id:
                visit(parent)
        visiting.remove(tid)
        visited.add(tid)

    for tid in by_id:
        visit(tid)

    for path in sorted(AI.rglob("*.md")):
        markdown_count += 1
        content = read(path)
        if "\ufffd" in content:
            errors.append(f"Encoding replacement character: {path.relative_to(AI)}")
        text = prose(content)
        expected_columns = None
        for number, line in enumerate(text.splitlines(), 1):
            if line.startswith("|"):
                columns = len(re.split(r"(?<!\\)\|", line)[1:-1])
                if expected_columns is None:
                    expected_columns = columns
                elif columns != expected_columns:
                    errors.append(f"Table columns: {path.relative_to(AI)}:{number}")
            else:
                expected_columns = None

        for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
            wiki_count += 1
            target = match.group(1).replace("\\|", "|").split("|", 1)[0]
            name, _, anchor = target.partition("#")
            destination = (VAULT / name) if name else path
            if not destination.suffix:
                destination = Path(str(destination) + ".md")
            if not inside_ai(destination) or not destination.is_file():
                errors.append(f"Broken/out-of-scope wiki link: {path.relative_to(AI)} -> {target}")
                continue
            if anchor and destination.suffix == ".md":
                headings = {
                    re.sub(r"[*\x60]", "", value.strip())
                    for value in re.findall(r"(?m)^#{1,6}\s+(.+)$", read(destination))
                }
                if anchor not in headings:
                    errors.append(f"Broken heading: {path.relative_to(AI)} -> {target}")

        for match in re.finditer(r"(!?)\[[^\[\]]*\]\(([^)]+)\)", text):
            image, target = match.groups()
            target = target.strip().strip("<>")
            if target.startswith(("https://", "http://")):
                if image:
                    errors.append(f"Remote image was not localized: {path.relative_to(AI)}")
                continue
            if target.startswith("#"):
                continue
            destination = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            if not inside_ai(destination) or not destination.is_file():
                errors.append(f"Broken local link: {path.relative_to(AI)} -> {target}")
            elif image:
                image_count += 1
                if destination.suffix.lower() == ".svg":
                    try:
                        root = ET.parse(destination).getroot()
                        if root.tag != "{http://www.w3.org/2000/svg}svg":
                            errors.append(f"Invalid SVG root: {destination.name}")
                    except ET.ParseError as exc:
                        errors.append(f"Invalid SVG XML: {exc}")

    for source in all_sources:
        parsed = urlparse(source["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"Invalid source URL: {source['id']}")
        if not source.get("checked") or not source.get("verification"):
            errors.append(f"Missing source evidence scope: {source['id']}")

    previews = []
    for theme in ("light", "dark"):
        path = AI / "assets" / "figures" / f"ai-knowledge-map-{theme}.png"
        if not path.is_file():
            errors.append(f"Missing rendered preview: {theme}")
            continue
        header = path.read_bytes()[:24]
        if header[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"Invalid PNG preview: {theme}")
            continue
        width, height = struct.unpack(">II", header[16:24])
        previews.append({"background": theme, "width": width, "height": height})

    report = {
        "stage": "framework",
        "modules": len(manifest["modules"]),
        "topic_notes": len(topics),
        "markdown_files": markdown_count,
        "route_topics": len(expected_rows),
        "mapped_route_topics": len(route_counts),
        "prerequisite_edges": sum(len(t["pre"]) for t in topics),
        "wiki_links": wiki_count,
        "materials": len(sources["materials"]),
        "papers": len(sources["papers"]),
        "local_image_references": image_count,
        "rendered_previews": previews,
        "scope": [
            "Local Markdown links/headings, route coverage, framework outlines, source IDs and prerequisite DAG checked.",
            "External sources were checked through browsing; this script checks URL structure and recorded evidence scope, not live HTTP.",
            "SVG rendered with sharp 0.35.5 and visually inspected on light/dark backgrounds; Obsidian application theme switching not exercised.",
            "Detailed prose, code execution and paper-result reproduction are intentionally deferred."
        ],
        "errors": errors,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
