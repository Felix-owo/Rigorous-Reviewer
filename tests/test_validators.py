import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "rigorous-reviewer" / "scripts" / "validate_review_report.py"
LINTER = ROOT / "rigorous-reviewer" / "scripts" / "lint_structured_review.py"
BENCHMARK = ROOT / "rigorous-reviewer" / "scripts" / "score_benchmark.py"


def run_script(script, *args):
    return subprocess.run(
        [sys.executable, "-S", str(script), *map(str, args)],
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

    def test_english_issue_labels_pass(self):
        report = """# Reviewer Report: Synthetic manuscript

## 1) Category Scores
- Top-Journal Novelty & Significance: 5/10 - Limited by causal evidence.

## 2) Pre-Review Contract Snapshot
- Contract status: locked.
- Central claim dependency: C1, the model makes a causal biological claim.
- Decisive evidence threshold: perturbation with rescue supports the mechanism.
- Failure condition: no perturbation or rescue keeps the mechanism claim at Major Revision.

## 3) Claim Maturity Gate
| Claim | Current maturity | Evidence basis | Blocking loophole | Upgrade readout | Required narrowing |
| --- | ---: | --- | --- | --- | --- |
| C1 | 2 | Association is present without perturbation or rescue. | Batch composition or stress response. | Perturbation with rescue supports the claim. | Narrow to association if causal evidence is absent. |

## 4) Field Evidence Map
- Central claim under review: The model makes a causal biological claim.

## 5) Calibration Against Gold / Near-Gold Papers
- Anchor set: Synthetic benchmark.

## 6) Reviewer Panel Synthesis
- EIC: Major Revision.

## 7) External Scientific Skills Used
- None.

## 8) Identified Issues
- [Major] Causal claim is under-supported
  Specific problem: The manuscript interprets association as mechanism without a perturbation or rescue test.
  Why serious: The conclusion depends on causal evidence rather than correlation.
  Evidence:
  - Manuscript-internal evidence: The provided results only show co-variation between marker and phenotype.
  - External evidence / standard: Synthetic benchmark standard, benchmark:rr.synthetic.standard.
  Impact: The central mechanism remains overclaimed and should be narrowed.
  Alternative explanation / loophole: Batch composition or stress response could produce the same association.
  Resolution: Add perturbation and rescue, or narrow the conclusion to association.
  Decisive readout: Perturbation with rescue would support the claim; failure to perturb or rescue would weaken the mechanism and force narrowing.

## 9) Literature / Source Search Hints
- Evidence gap / claim tested: causal mechanism.

## 10) Revision Suggested Actions
### Essential for supporting the main claim
- Target: central mechanism.

## 11) Evidence Ledger
| ID | Source | Type | Supports / challenges | Decision role | Identifier / link |
| --- | --- | --- | --- | --- | --- |
| S1 | Synthetic benchmark standard | benchmark | Major issue | decisive | benchmark:rr.synthetic.standard |

## 12) Red-Line Self-Audit
- Citation support: pass

## 13) Overall Recommendation
- Decision: Major Revision
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "english_review.md"
            path.write_text(report, encoding="utf-8")
            result = run_script(VALIDATOR, path)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_math_angle_brackets_do_not_trigger_placeholder_failure(self):
        base = (ROOT / "tests/fixtures/markdown/valid_review.md").read_text(encoding="utf-8")
        report = base.replace(
            "The central causal claim is not supported.",
            "The central causal claim is not supported; the proof sketch uses x < y and y > 0.",
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "math_review.md"
            path.write_text(report, encoding="utf-8")
            result = run_script(VALIDATOR, path, "--strict")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_valid_structured_review_passes(self):
        result = run_script(LINTER, ROOT / "tests/fixtures/json/valid_structured_review.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_valid_structured_review_passes_strict(self):
        result = run_script(LINTER, ROOT / "tests/fixtures/json/valid_structured_review.json", "--strict")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_structured_review_fails(self):
        result = run_script(LINTER, ROOT / "tests/fixtures/json/invalid_structured_review.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required field", result.stderr)

    def test_strict_structured_review_requires_source_ids(self):
        report = json.loads((ROOT / "tests/fixtures/json/valid_structured_review.json").read_text(encoding="utf-8"))
        report["issues"][0]["source_ids"] = []
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "missing_source_ids.json"
            path.write_text(json.dumps(report), encoding="utf-8")
            result = run_script(LINTER, path, "--strict")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("non-empty source_ids", result.stderr)


    def test_strict_structured_review_requires_linked_claim_ids(self):
        report = json.loads((ROOT / "tests/fixtures/json/valid_structured_review.json").read_text(encoding="utf-8"))
        report["issues"][0]["linked_claims"] = ["unmapped claim"]
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad_linked_claims.json"
            path.write_text(json.dumps(report), encoding="utf-8")
            result = run_script(LINTER, path, "--strict")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("linked_claims not present in claim_maturity_gate", result.stderr)

    def test_strict_structured_review_requires_artifact_traceability(self):
        report = json.loads((ROOT / "tests/fixtures/json/valid_structured_review.json").read_text(encoding="utf-8"))
        report["issues"][0].pop("manuscript_artifact_ids", None)
        report["issues"][0].pop("manuscript_location", None)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "missing_artifact_trace.json"
            path.write_text(json.dumps(report), encoding="utf-8")
            result = run_script(LINTER, path, "--strict")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("require a manuscript artifact trace", result.stderr)

    def test_strict_structured_review_rejects_vague_companion_identifier(self):
        report = json.loads((ROOT / "tests/fixtures/json/valid_structured_review.json").read_text(encoding="utf-8"))
        report["external_companion_evidence"][0]["returned_identifier"] = "unknown"
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "vague_companion_identifier.json"
            path.write_text(json.dumps(report), encoding="utf-8")
            result = run_script(LINTER, path, "--strict")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("returned_identifier must not be vague", result.stderr)

    def test_benchmark_definitions_are_valid(self):
        result = run_script(BENCHMARK, "--benchmark-root", ROOT / "benchmarks/v1.0")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
