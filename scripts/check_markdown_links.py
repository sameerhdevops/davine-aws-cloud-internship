#!/usr/bin/env python3
"""Check repository-local Markdown links and heading fragments."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".terraform", ".local-review", "node_modules", "recovery-audit", "weeks"}
FENCE_RE = re.compile(r"(?ms)^\s*(```+|~~~+).*?^\s*\1\s*$")
INLINE_RE = re.compile(r"(?<!!)\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
REFERENCE_RE = re.compile(r"(?m)^\s*\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))")
HEADING_RE = re.compile(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$")
HTML_ID_RE = re.compile(r"(?i)\bid\s*=\s*['\"]([^'\"]+)['\"]")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    )


def strip_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def heading_anchors(path: Path) -> set[str]:
    text = strip_code(path.read_text(encoding="utf-8"))
    anchors = set(HTML_ID_RE.findall(text))
    seen: dict[str, int] = {}
    for match in HEADING_RE.finditer(text):
        heading = re.sub(r"`([^`]*)`", r"\1", match.group(1))
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        base = heading.lower().strip()
        base = re.sub(r"[^\w\- ]", "", base)
        base = re.sub(r"\s+", "-", base)
        occurrence = seen.get(base, 0)
        seen[base] = occurrence + 1
        anchors.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return anchors


def targets(text: str) -> list[str]:
    text = strip_code(text)
    found: list[str] = []
    for regex in (INLINE_RE, IMAGE_RE, REFERENCE_RE):
        for match in regex.finditer(text):
            found.append(match.group(1) or match.group(2))
    return found


def check_target(source: Path, raw_target: str) -> str | None:
    parsed = urlsplit(raw_target)
    if parsed.scheme or parsed.netloc:
        return None

    relative_path = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    target = (source.parent / relative_path).resolve() if relative_path else source.resolve()

    try:
        target.relative_to(ROOT)
    except ValueError:
        return "target resolves outside the repository"

    if target.is_dir():
        target = next((target / name for name in ("README.md", "index.md") if (target / name).is_file()), target)
    if not target.exists():
        return "target does not exist"
    if fragment and target.suffix.lower() == ".md" and fragment not in heading_anchors(target):
        return f"heading fragment #{fragment} does not exist"
    return None


def main() -> int:
    files = markdown_files()
    failures: list[str] = []
    checked = 0
    for source in files:
        text = source.read_text(encoding="utf-8")
        for raw_target in targets(text):
            parsed = urlsplit(raw_target)
            if parsed.scheme or parsed.netloc:
                continue
            checked += 1
            error = check_target(source, raw_target)
            if error:
                failures.append(f"{source.relative_to(ROOT).as_posix()}: {raw_target} ({error})")

    if failures:
        print("Broken local Markdown links:")
        for failure in failures:
            print(f"- {failure}")
        print(f"Found {len(failures)} broken targets among {checked} local links in {len(files)} Markdown files.")
        return 1

    print(f"Checked {checked} local Markdown links in {len(files)} Markdown files; no broken targets found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
