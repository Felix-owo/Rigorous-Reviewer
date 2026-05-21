from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "rigorous-reviewer" / "scripts" / "validate_review_report.py"
LINTER = ROOT / "rigorous-reviewer" / "scripts" / "lint_structured_review.py"
BENCHMARK = ROOT / "rigorous-reviewer" / "scripts" / "score_benchmark.py"


def run_script(script, *args):
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class ValidatorTests(unittest.TestCase):
    def test_valid_markdown_report_passes_strict(self):
        result = run_script(VALIDATOR, ROOT / "tests/fixtures/markdown/valid_review.md", "--strict")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_markdown_report_fails(self):
        result = run_script(VALIDATOR, ROOT / "tests/fixtures/markdown/invalid_missing_sections.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required section", result.stderr)

    def test_missing_evidence_ledger_fails(self):
        result = run_script(VALIDATOR, ROOT / "tests/fixtures/markdown/invalid_missing_evidence_ledger.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing Evidence Ledger table", result.stderr)

    def test_missing_decisive_readout_fails(self):
        result = run_script(VALIDATOR, ROOT / "tests/fixtures/markdown/invalid_missing_decisive_readout.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("decisive readout lacks", result.stderr)

    def test_accept_with_critical_fails_strict(self):
        result = run_script(VALIDATOR, ROOT / "tests/fixtures/markdown/invalid_accepts_critical_case.md", "--strict")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot recommend Accept", result.stderr)

    def test_valid_structured_review_passes(self):
        result = run_script(LINTER, ROOT / "tests/fixtures/json/valid_structured_review.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_structured_review_fails(self):
        result = run_script(LINTER, ROOT / "tests/fixtures/json/invalid_structured_review.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required field", result.stderr)

    def test_benchmark_definitions_are_valid(self):
        result = run_script(BENCHMARK, "--benchmark-root", ROOT / "benchmarks/v1.0")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
