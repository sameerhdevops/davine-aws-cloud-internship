from __future__ import annotations

import copy
import csv
import tempfile
import unittest
from pathlib import Path
from scripts.check_markdown_links import check_target, targets
from scripts.check_portfolio import (
    ROOT,
    WEEK_PAGE_HEADINGS,
    WEEKS,
    check_public_markers,
    check_required_artifacts,
    check_week_pages,
    validate_manifest_rows,
)


class MarkdownLinkParsingTests(unittest.TestCase):
    def test_extracts_inline_image_and_reference_targets_but_skips_code(self) -> None:
        markdown = """\
[inline](docs/evidence-and-validation.md#classification-standard)
![image](evidence/manifest.csv)
[ref][policy]
[policy]: demos/week10_governance/policy_check.py
`[code](missing.md)` and ``![also code](missing.png)``
```md
[fenced](missing.md)
```
"""
        self.assertEqual(
            [
                "docs/evidence-and-validation.md#classification-standard",
                "evidence/manifest.csv",
                "demos/week10_governance/policy_check.py",
            ],
            targets(markdown),
        )

    def test_checks_url_encoded_paths_and_existing_heading_fragments(self) -> None:
        source = ROOT / "README.md"
        self.assertIsNone(check_target(source, "evidence/manifest%2Ecsv"))
        self.assertIsNone(
            check_target(source, "docs/evidence-and-validation.md#classification-standard")
        )
        self.assertIn("does not exist", check_target(source, "missing%2Etxt"))


class PortfolioManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (ROOT / "evidence/manifest.csv").open(encoding="utf-8-sig", newline="") as stream:
            cls.rows = list(csv.DictReader(stream))

    def assert_error(self, expected: str, errors: list[str]) -> None:
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_current_manifest_resolves_every_public_path(self) -> None:
        errors, public_count = validate_manifest_rows(copy.deepcopy(self.rows), ROOT)
        self.assertEqual([], errors)
        self.assertGreater(public_count, 0)

    def test_rejects_duplicate_ids_and_missing_public_descriptions(self) -> None:
        rows = copy.deepcopy(self.rows[:2])
        rows[1]["artifact_id"] = rows[0]["artifact_id"]
        rows[1]["limitations"] = ""
        errors, _ = validate_manifest_rows(rows, ROOT)
        self.assert_error("duplicate artifact_id", errors)
        self.assert_error("limitations is required", errors)

    def test_rejects_nonexistent_escaping_and_withheld_publication_paths(self) -> None:
        base = copy.deepcopy(self.rows[0])
        for publication_path, visibility, expected in (
            ("does/not/exist.png", "public", "does not resolve to a file"),
            ("../private.png", "public", "repository-relative"),
            ("evidence/manifest.csv", "withheld", "withheld artifact must not"),
        ):
            row = copy.deepcopy(base)
            row["publication_path"] = publication_path
            row["visibility"] = visibility
            with self.subTest(path=publication_path, visibility=visibility):
                errors, _ = validate_manifest_rows([row], ROOT)
                self.assert_error(expected, errors)

    def test_required_publication_artifacts_exist_and_missing_artifacts_are_reported(self) -> None:
        errors: list[str] = []
        check_required_artifacts(ROOT, errors)
        self.assertEqual([], errors)

        missing_errors: list[str] = []
        check_required_artifacts(ROOT / "missing-fixture", missing_errors)
        self.assertTrue(
            any("required portfolio artifact is missing" in error for error in missing_errors)
        )

    def test_every_week_page_has_the_standard_headings(self) -> None:
        errors: list[str] = []
        check_week_pages(errors)
        self.assertEqual([], [error for error in errors if "required heading" in error])

    def test_missing_week_heading_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            links = []
            for folder in WEEKS:
                page = root / "assignments" / folder / "README.md"
                page.parent.mkdir(parents=True, exist_ok=True)
                headings = list(WEEK_PAGE_HEADINGS)
                if folder == "week-04-application-load-balancing":
                    headings.remove("Key concepts")
                content = "\n".join(f"## {heading}" for heading in headings)
                if folder == "week-11-capstone-planning":
                    content += "\nnot a Week 11 task; not a Week 11 submission; planning context"
                page.write_text(content, encoding="utf-8")
                links.append(f"[page](assignments/{folder}/README.md)")
            (root / "README.md").write_text("\n".join(links), encoding="utf-8")

            errors: list[str] = []
            check_week_pages(errors, root)

        self.assertTrue(
            any(
                "weekly page is missing required heading '## Key concepts'" in error
                and "week-04-application-load-balancing" in error
                for error in errors
            ),
            errors,
        )

    def test_internal_review_markers_fail_in_markdown_and_manifest(self) -> None:
        marker_a = "TO" + "DO"
        marker_b = "T" + "BD"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "Status was as reported by the user; OWNER TO VERIFY", encoding="utf-8"
            )
            (root / "evidence").mkdir()
            (root / "evidence/manifest.csv").write_text(
                f"this task has {marker_a} and {marker_b} markers", encoding="utf-8"
            )
            errors: list[str] = []
            check_public_markers(root, errors)

        self.assertTrue(any("OWNER TO VERIFY" in error for error in errors), errors)
        self.assertTrue(any("as reported by the user" in error for error in errors), errors)
        self.assertTrue(any("this task" in error for error in errors), errors)
        self.assertTrue(any(marker_a in error for error in errors), errors)
        self.assertTrue(any(marker_b in error for error in errors), errors)

    def test_ordinary_user_experience_wording_is_not_an_internal_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "Queue work when the user experience allows it.", encoding="utf-8"
            )
            errors: list[str] = []
            check_public_markers(root, errors)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
