from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "rigorous-reviewer" / "scripts" / "apply_trigger_keywords.py"
TRIGGER_JSON = ROOT / "rigorous-reviewer" / "templates" / "trigger_keywords.json"


def load_module():
    spec = importlib.util.spec_from_file_location("apply_trigger_keywords", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TriggerKeywordTests(unittest.TestCase):
    def test_trigger_registry_has_required_terms(self):
        data = json.loads(TRIGGER_JSON.read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "rigorous-reviewer")
        strong = " ".join(data["strong_trigger_keywords"]).lower()
        chinese = " ".join(data["chinese_trigger_keywords"])
        negative = " ".join(data["negative_routing_keywords"]).lower()
        for term in ["rigorous review", "manuscript review", "decisive evidence", "alternative explanation"]:
            self.assertIn(term, strong)
        for term in ["严格审稿", "顶刊审稿", "决定性证据", "替代解释"]:
            self.assertIn(term, chinese)
        for term in ["protocol", "sop", "figure styling", "database lookup only"]:
            self.assertIn(term, negative)

    def test_patch_standard_frontmatter(self):
        module = load_module()
        data = json.loads(TRIGGER_JSON.read_text(encoding="utf-8"))
        original = """---
name: rigorous-reviewer
description: Use when reviewing manuscripts, claims, evidence, novelty, reproducibility, and statistical validity for scientific peer review.
---

# Rigorous Reviewer

Core workflow.
"""
        patched = module.patch_skill_text(original, data)
        self.assertNotIn("\ntrigger_keywords:", patched)
        self.assertNotIn("\nnegative_trigger_keywords:", patched)
        self.assertIn("## Trigger Keywords and Routing", patched)
        self.assertIn("decisive evidence", patched)
        self.assertIn("替代解释", patched)
        self.assertIn("templates/trigger_keywords.json", patched)
        self.assertEqual(module.check_skill_text(patched), [])

    def test_patch_compact_frontmatter_adds_markdown_section(self):
        module = load_module()
        data = json.loads(TRIGGER_JSON.read_text(encoding="utf-8"))
        original = """--- name: rigorous-reviewer description: > Portable Agent Skill for elite scientific peer review of manuscripts, claims, evidence, novelty, reproducibility, and statistical validity. --- # Rigorous Reviewer
Core workflow.
"""
        patched = module.patch_skill_text(original, data)
        self.assertIn("## Trigger Keywords and Routing", patched)
        self.assertIn("rigorous scientific peer review", patched)
        self.assertIn("references/trigger_keywords.md", patched)
        self.assertEqual(module.check_skill_text(patched), [])


if __name__ == "__main__":
    unittest.main()
