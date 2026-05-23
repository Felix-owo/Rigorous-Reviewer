from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK_CONTRACT = ROOT / "rigorous-reviewer" / "scripts" / "check_review_contract.py"
VALID_CONTRACT = ROOT / "rigorous-reviewer" / "examples" / "regression_fixtures" / "contract_valid_claim_dependency.json"


def run_script(script, *args):
    return subprocess.run(
        [sys.executable, "-S", str(script), *map(str, args)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class ReviewContractTests(unittest.TestCase):
    def test_valid_contract_fixture_passes(self):
        result = run_script(CHECK_CONTRACT, VALID_CONTRACT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_partial_contract_requires_missing_material(self):
        text = VALID_CONTRACT.read_text(encoding="utf-8")
        text = text.replace('"contract_status": "locked"', '"contract_status": "partial_material_contract"')
        text = text.replace('"missing_decisive_material": []', '"missing_decisive_material": []')
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "partial_contract.json"
            path.write_text(text, encoding="utf-8")
            result = run_script(CHECK_CONTRACT, path)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("partial_material_contract requires missing_decisive_material", result.stderr)


if __name__ == "__main__":
    unittest.main()
