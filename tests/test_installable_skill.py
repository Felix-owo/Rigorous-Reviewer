from pathlib import Path
import importlib.util
import unittest


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("check_installable_skill", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class InstallableSkillTests(unittest.TestCase):
    def test_frontmatter_parser_accepts_standard_skill_md(self):
        module = load_module(Path("rigorous-reviewer/scripts/check_installable_skill.py"))
        text = """---\nname: rigorous-reviewer\ndescription: Use this skill to review manuscript claim evidence novelty and reproducibility.\n---\n# Body\n"""
        metadata = module.parse_frontmatter(text)
        self.assertEqual(metadata["name"], "rigorous-reviewer")
        self.assertIn("manuscript", metadata["description"])


if __name__ == "__main__":
    unittest.main()
