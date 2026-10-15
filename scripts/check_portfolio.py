#!/usr/bin/env python3
"""Check expected weekly pages and public evidence-manifest integrity."""

from __future__ import annotations

import csv
import re
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
WEEKS = [
    "week-01-aws-fundamentals",
    "week-02-ec2-web-server",
    "week-03-vpc-networking",
    "week-04-application-load-balancing",
    "week-05-high-availability",
    "week-06-serverless-architecture",
    "week-07-infrastructure-as-code",
    "week-08-monitoring-cdn-dns",
    "week-09-serverless-api",
    "week-10-governance-audit",
    "week-11-capstone-planning",
    "week-12-talentflow-ai",
]
CATEGORIES = {
    "Original internship artifact",
    "Sanitized evidence derivative",
    "Independent reconstruction",
    "Reproducible demonstration",
    "Independently validated",
    "Not established by retained evidence",
}
SKIP = {
    ".git",
    ".terraform",
    ".local-review",
    "recovery-audit",
    "weeks",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
}
ABSOLUTE_PATH = re.compile(r"(?i)(?:[a-z]:\\|\\\\[a-z0-9_.-]+\\)")
PLACEHOLDER = re.compile(r"(?i)\b(?:TODO|TBD|lorem ipsum|insert here|coming soon)\b")
REQUIRED_ARTIFACTS = (
    "scripts/aws_audit/audit.py",
    "scripts/aws_audit/cli.py",
    "scripts/aws_audit/README.md",
    "tests/test_aws_audit.py",
    "docs/EVIDENCE.md",
    "docs/SCOPE.md",
    "docs/SECURITY-NOTES.md",
    "samples/aws-audit-report.json",
    "samples/aws-audit-report.csv",
    "diagrams/aws-audit-workflow.mmd",
    "diagrams/repository-structure.mmd",
)
WEEK_PAGE_HEADINGS = (
    "Objective",
    "What I did or implemented",
    "Key concepts",
    "Evidence and links",
    "Limitations",
    "Next improvements",
)
INTERNAL_MARKER = re.compile(
    r"(?i)\bOWNER\s+TO\s+VERIFY\b"
    r"|\bas reported by the user\b"
    r"|\buser-reported\b"
    r"|\breported by (?:the )?user\b"
    r"|\b(?:the )?user supplied\b"
    r"|\bthis (?:review|task|update)\b"
    r"|\bTODO\b|\bTBD\b"
)


def internal_markers(text: str) -> list[str]:
    """Return internal-review phrases that must not appear in public prose."""
    return [match.group(0) for match in INTERNAL_MARKER.finditer(text)]


def missing_week_headings(content: str) -> list[str]:
    """Return required level-two headings absent from a weekly page."""
    headings = set(re.findall(r"(?m)^##\s+(.+?)\s*$", content))
    return [heading for heading in WEEK_PAGE_HEADINGS if heading not in headings]


def check_required_artifacts(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_ARTIFACTS:
        if not (root / relative).is_file():
            errors.append(f"required portfolio artifact is missing: {relative}")
    readme = root / "README.md"
    if not readme.is_file():
        return
    content = readme.read_text(encoding="utf-8")
    for link in (
        "scripts/aws_audit/README.md",
        "docs/EVIDENCE.md",
        "docs/SCOPE.md",
        "docs/SECURITY-NOTES.md",
        "evidence/README.md",
    ):
        if f"]({link})" not in content:
            errors.append(f"root README must link to {link}")


def check_week_pages(errors: list[str], root: Path = ROOT) -> None:
    root_readme_path = root / "README.md"
    root_readme = root_readme_path.read_text(encoding="utf-8") if root_readme_path.is_file() else ""
    for folder in WEEKS:
        path = root / "assignments" / folder / "README.md"
        if not path.is_file():
            errors.append(f"missing weekly page: assignments/{folder}/README.md")
            continue
        content = path.read_text(encoding="utf-8")
        if not re.search(
            rf"\]\(assignments/{re.escape(folder)}/README\.md(?:#[^)]*)?\)", root_readme
        ):
            errors.append(f"root README does not link weekly page: assignments/{folder}/README.md")
        for heading in missing_week_headings(content):
            errors.append(
                f"weekly page is missing required heading '## {heading}': assignments/{folder}/README.md"
            )
    if len(WEEKS) != 12:
        errors.append("internal quality check does not list exactly 12 weeks")
    completion_statement = "All 12 weeks and the assigned weekly work are complete."
    if completion_statement not in root_readme:
        errors.append("root README must clearly state that all 12 weeks and assigned work are complete")

    week12_row = re.search(
        r"(?m)^\|\s*12\s*\|\s*TalentFlow AI capstone\s*\|\s*Completed\s*\|",
        root_readme,
    )
    if not week12_row:
        errors.append("root README must mark Week 12 as Completed")

    week11 = root / "assignments/week-11-capstone-planning/README.md"
    if week11.is_file():
        content = week11.read_text(encoding="utf-8")
        for phrase in ("planning context",):
            if phrase not in content:
                errors.append(f"Week 11 page must explicitly contain: {phrase}")


REQUIRED_MANIFEST_COLUMNS = {
    "artifact_id",
    "week",
    "type",
    "provenance",
    "evidence_category",
    "visibility",
    "publication_path",
    "date_status",
    "supported_claim",
    "limitations",
    "sanitization_or_withheld_reason",
}
REQUIRED_MANIFEST_VALUES = REQUIRED_MANIFEST_COLUMNS - {"publication_path"}


def validate_manifest_rows(rows: list[dict[str, str]], root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    seen: set[str] = set()
    public_count = 0
    for line, row in enumerate(rows, start=2):
        for field in REQUIRED_MANIFEST_VALUES:
            if not (row.get(field) or "").strip():
                errors.append(f"manifest line {line}: {field} is required")

        artifact_id = (row.get("artifact_id") or "").strip()
        if not artifact_id or artifact_id in seen:
            errors.append(f"manifest line {line}: blank or duplicate artifact_id")
        seen.add(artifact_id)
        if (row.get("evidence_category") or "").strip() not in CATEGORIES:
            errors.append(f"manifest line {line}: unrecognized evidence_category")

        visibility = (row.get("visibility") or "").strip().lower()
        publication_path = (row.get("publication_path") or "").strip()
        if visibility == "public":
            public_count += 1
            if not publication_path:
                errors.append(f"manifest line {line}: public artifact has no publication_path")
                continue
            relative = PurePosixPath(publication_path)
            if relative.is_absolute() or ".." in relative.parts or "\\" in publication_path:
                errors.append(
                    f"manifest line {line}: publication_path must be repository-relative with forward slashes"
                )
                continue
            target = (root / Path(*relative.parts)).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append(f"manifest line {line}: publication_path escapes the repository")
                continue
            if not target.is_file():
                errors.append(
                    f"manifest line {line}: publication_path does not resolve to a file: {publication_path}"
                )
        elif visibility == "withheld":
            if publication_path:
                errors.append(
                    f"manifest line {line}: withheld artifact must not have a publication_path"
                )
        else:
            errors.append(f"manifest line {line}: visibility must be public or withheld")
    if not rows:
        errors.append("evidence manifest contains no records")
    return errors, public_count


def check_manifest(errors: list[str]) -> int:
    path = ROOT / "evidence/manifest.csv"
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            missing = REQUIRED_MANIFEST_COLUMNS - set(reader.fieldnames or [])
            if missing:
                errors.append(f"manifest missing columns: {', '.join(sorted(missing))}")
                return 0
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        errors.append(f"could not read evidence manifest: {exc}")
        return 0

    row_errors, public_count = validate_manifest_rows(rows, ROOT)
    errors.extend(row_errors)
    return public_count


def check_public_text(errors: list[str]) -> tuple[int, int]:
    checked = 0
    placeholders = 0
    extensions = {".md", ".csv", ".py", ".json", ".tf", ".mmd", ".yml", ".yaml", ".toml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue  # This checker contains its own path and placeholder detection patterns.
        relative = path.relative_to(ROOT)
        if any(part in SKIP for part in relative.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"public text file is not UTF-8: {relative.as_posix()}")
            continue
        checked += 1
        if ABSOLUTE_PATH.search(text):
            errors.append(f"possible absolute machine path in public text: {relative.as_posix()}")
        if PLACEHOLDER.search(text):
            placeholders += 1
            errors.append(f"placeholder text found in public text: {relative.as_posix()}")
        if path.suffix.lower() == ".md" and re.search(r"(?m)^#{1,6}\s*$", text):
            errors.append(f"empty Markdown heading found: {relative.as_posix()}")
    return checked, placeholders


def check_public_markers(root: Path, errors: list[str]) -> None:
    """Reject internal-review language in public Markdown and the evidence CSV."""
    paths = list(root.rglob("*.md"))
    manifest = root / "evidence/manifest.csv"
    if manifest.is_file():
        paths.append(manifest)
    for path in paths:
        relative = path.relative_to(root)
        if any(part in SKIP for part in relative.parts):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"public marker file is not UTF-8: {relative.as_posix()}")
            continue
        for marker in internal_markers(content):
            errors.append(
                f"internal-review marker '{marker}' in public text: {relative.as_posix()}"
            )


def main() -> int:
    errors: list[str] = []
    check_required_artifacts(ROOT, errors)
    check_week_pages(errors)
    public_count = check_manifest(errors)
    check_public_markers(ROOT, errors)
    checked_text, _ = check_public_text(errors)

    if errors:
        print("Portfolio quality check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"Portfolio quality check passed: {len(WEEKS)} weekly pages, {public_count} public manifest paths, and {checked_text} public text files checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
