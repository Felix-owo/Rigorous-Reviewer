#!/usr/bin/env python3
"""Smoke-test bundled regression fixtures for package structure only."""
from __future__ import annotations
import json, sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
fixtures = list((root / "benchmarks" / "fixtures").glob("*.json"))
if not fixtures:
    print("No fixtures found", file=sys.stderr)
    raise SystemExit(1)
for f in fixtures:
    data = json.loads(f.read_text(encoding="utf-8"))
    for key in ["name", "task", "expected_gates"]:
        if key not in data:
            print(f"{f}: missing {key}", file=sys.stderr)
            raise SystemExit(1)
print(f"Regression fixture smoke test: PASS ({len(fixtures)} fixture(s))")
