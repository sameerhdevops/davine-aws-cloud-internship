from __future__ import annotations

import copy
import csv
import unittest
from pathlib import Path

from scripts.check_markdown_links import check_target, targets
from scripts.check_portfolio import ROOT, validate_manifest_rows


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
        self.assertIsNone(check_target(source, "docs/evidence-and-validation.md#classification-standard"))
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


if __name__ == "__main__":
    unittest.main()
