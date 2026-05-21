from pathlib import Path
import importlib.util
import unittest


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("score_benchmark_semantic", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SemanticBenchmarkScoringTests(unittest.TestCase):
    def test_semantic_scoring_detects_aliases_and_severity(self):
        module = load_module(Path("rigorous-reviewer/scripts/score_benchmark_semantic.py"))
        spec = {
            "must_detect": [
                {"concept": "external validation", "aliases": ["independent validation cohort"]},
                {"concept": "calibration", "aliases": ["calibration plot"]},
            ],
            "minimum_severity": "Critical",
            "forbidden_recommendations": ["Accept"],
            "requires_decisive_readout": True,
            "pass_threshold": 0.8,
        }
        weights = {
            "concept_recall": 0.60,
            "severity_calibration": 0.20,
            "decisive_readout": 0.10,
            "recommendation_safety": 0.10,
        }
        text = """
        Critical issue: the manuscript lacks an independent validation cohort and does not show a calibration plot.
        A decisive experiment would be external validation with calibration and clinical utility assessment.
        Recommendation: Reject pending validation.
        """
        result = module.score_output(text, spec, weights)
        self.assertTrue(result["pass"])
        self.assertEqual(result["concept_recall"], 1.0)
        self.assertTrue(result["severity_ok"])
        self.assertTrue(result["decisive_readout_ok"])
        self.assertEqual(result["forbidden_recommendations_found"], [])

    def test_public_benchmark_definitions_are_valid(self):
        module = load_module(Path("rigorous-reviewer/scripts/score_benchmark_semantic.py"))
        errors = module.check_definitions(Path("benchmarks/v1.1-public"))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
