from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK_FIXTURE = ROOT / "rigorous-reviewer" / "scripts" / "check_claim_strength_fixture.py"
VALID_FIXTURE = ROOT / "benchmarks" / "fixtures" / "claim_strength_fixture.json"


def run_script(script, *args):
    return subprocess.run(
        [sys.executable, "-S", str(script), *map(str, args)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class ClaimStrengthFixtureTests(unittest.TestCase):
    def test_claim_strength_fixture_passes(self):
        result = run_script(CHECK_FIXTURE, VALID_FIXTURE)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_claim_strength_fixture_rejects_fake_doi(self):
        fixture = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        fixture["available_evidence"][1]["identifier"] = "DOI:10.0000/rr.synthetic.fake"
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "claim_strength_fixture.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            result = run_script(CHECK_FIXTURE, path)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("fake DOI", result.stderr)


if __name__ == "__main__":
    unittest.main()
