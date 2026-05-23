from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCORE_KEYWORD = ROOT / "rigorous-reviewer" / "scripts" / "score_benchmark.py"
SCORE_SEMANTIC = ROOT / "rigorous-reviewer" / "scripts" / "score_benchmark_semantic.py"
GOLDEN_INPUT = ROOT / "tests" / "golden" / "case_pseudoreplication_input.md"
GOLDEN_EXPECTED = ROOT / "tests" / "golden" / "case_pseudoreplication_expected.json"


def run_script(script, *args):
    return subprocess.run(
        [sys.executable, "-S", str(script), *map(str, args)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class BenchmarkScoringTests(unittest.TestCase):
    def test_golden_case_assets_are_present(self):
        self.assertIn("donor-level", GOLDEN_INPUT.read_text(encoding="utf-8"))
        self.assertIn("minimum_severity", GOLDEN_EXPECTED.read_text(encoding="utf-8"))

    def test_keyword_scorer_does_not_flag_negated_accept(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "cases").mkdir()
            (root / "outputs").mkdir()
            (root / "cases" / "case1.md").write_text("synthetic case", encoding="utf-8")
            (root / "expected_findings.json").write_text(
                '''{
  "case1": {
    "must_detect": ["pseudoreplication"],
    "minimum_severity": "Major",
    "forbidden_recommendations": ["Accept"]
  }
}
''',
                encoding="utf-8",
            )
            (root / "scoring_rubric.json").write_text('{"score_components": {"x": 1.0}}\n', encoding="utf-8")
            (root / "outputs" / "case1.md").write_text(
                "[Major] pseudoreplication is present. Do not Accept this manuscript.\n"
                "Decision: Major Revision\n",
                encoding="utf-8",
            )
            result = run_script(SCORE_KEYWORD, "--benchmark-root", root, "--outputs-dir", root / "outputs")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_semantic_scorer_does_not_flag_negated_accept(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "cases").mkdir()
            (root / "outputs").mkdir()
            (root / "cases" / "case1.md").write_text("synthetic case", encoding="utf-8")
            (root / "expected_findings.json").write_text(
                '''{
  "case1": {
    "must_detect": ["pseudoreplication"],
    "minimum_severity": "Major",
    "forbidden_recommendations": ["Accept"],
    "requires_decisive_readout": false,
    "pass_threshold": 0.8
  }
}
''',
                encoding="utf-8",
            )
            (root / "scoring_rubric.json").write_text(
                '{"score_components": {"concept_recall": 0.7, "severity_calibration": 0.2, "decisive_readout": 0.0, "recommendation_safety": 0.1}}\n',
                encoding="utf-8",
            )
            (root / "sources.json").write_text('{"case1": {"source": "synthetic"}}\n', encoding="utf-8")
            (root / "outputs" / "case1.md").write_text(
                "[Major] pseudoreplication is present. Do not Accept this manuscript.\n"
                "Decision: Major Revision\n",
                encoding="utf-8",
            )
            result = run_script(SCORE_SEMANTIC, "--benchmark-root", root, "--outputs-dir", root / "outputs")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
