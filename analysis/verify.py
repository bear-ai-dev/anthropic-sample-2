#!/usr/bin/env python3
"""Verify Sample 2 scores, failure labels, and repaired-verifier evidence."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS = ["Fable 5.1", "GLM 5.3", "Grok 4.6", "Kimi K3", "GPT-5.6 Sol"]
EXPECTED = {"Fable 5.1": 31, "GLM 5.3": 23, "Grok 4.6": 19, "Kimi K3": 15, "GPT-5.6 Sol": 13}
REAL_SWE_TASKS = {
    "01-entitlement-overage-lines",
    "02-multi-region-sweep",
    "04-tax-jurisdiction",
    "06-api-token-metering",
    "07-api-keys-and-environments",
    "09-s3-datastore-measurement",
    "10-customer-identity-migration",
    "11-customer-billing-schedule-migration",
}


def read_json(path: Path):
    return json.loads(path.read_text())


def reward_at(path: Path) -> float:
    for name in ("reward.txt", "reward.json"):
        candidate = path / name
        if not candidate.exists():
            continue
        if name.endswith(".json"):
            doc = read_json(candidate)
            value = doc.get("reward", doc.get("score"))
        else:
            value = candidate.read_text().strip()
        return float(value)
    raise AssertionError(f"no reward artifact under {path.relative_to(ROOT)}")


trials = read_json(ROOT / "indexes/trials.json")
assert len(trials) == 400
assert len({r["task"] for r in trials}) == 10
assert set(r["model_label"] for r in trials) == set(MODELS)

cells = Counter((r["task"], r["model_label"]) for r in trials)
assert len(cells) == 50 and set(cells.values()) == {8}
assert len({(r['task'], r['model_label'], r['trial_number']) for r in trials}) == 400
assert Counter(r['admission'] for r in trials) == {'strict-valid': 398, 'scored-terminal-failure': 2}
for row in trials:
    trajectory = ROOT / row['trajectory']
    assert hashlib.sha256(trajectory.read_bytes()).hexdigest() == row['trajectory_sha256']
    assert read_json(trajectory).get('steps')
    verdict = read_json(ROOT / row['verification'] / 'canonical-verdict.json')
    assert verdict['reward'] == row['reward'] and verdict['passed'] == row['passed']
    assert verdict['admission'] == row['admission']
    if row['admission'] == 'scored-terminal-failure':
        assert row['model_label'] == 'GLM 5.3' and row['task'] == '04-tax-jurisdiction'
        assert row['trial_number'] in (5, 7) and row['reward'] == 0
        assert row['terminal_failure_reason'] == 'max_turns' and not row['canonical_valid']
totals = {m: sum(bool(r["passed"]) for r in trials if r["model_label"] == m) for m in MODELS}
assert totals == EXPECTED, totals
assert sum(totals.values()) == read_json(ROOT / "manifest.json")["passes"] == 101

with (ROOT / "analysis/failure-modes.csv").open(newline="") as handle:
    failures = list(csv.DictReader(handle))
assert len(failures) == 320
assert {r["task"] for r in failures} == REAL_SWE_TASKS
indexed = {(r["task"], r["model_label"], int(r["trial_number"])): r for r in trials}
for row in failures:
    key = (row["task"], row["model"], int(row["trial"]))
    source = indexed[key]
    assert float(row["reward"]) == float(source["reward"])
    assert (row["passed"] == "1") == bool(source["passed"])
    assert (ROOT / row["evidence"]).is_dir(), row["evidence"]
    if row["passed"] == "1":
        assert row["primary_label"] == "LEGITIMATE"
        assert not row["attribution"] and not row["mode"] and not row["mechanism"]
    else:
        assert row["primary_label"] != "LEGITIMATE"
        assert row["attribution"] in {"model", "spec", "harness"}
        assert row["mode"] and row["mechanism"]

repairs = read_json(ROOT / "analysis/verifier-repair-summary.json")["trials"]
assert len(repairs) == 12
assert sum(r["fixed_reward"] == 1 for r in repairs) == 7
assert sum(r["fixed_reward"] == 0 for r in repairs) == 5
for row in repairs:
    original = ROOT / row["original_evidence"]
    fixed = ROOT / row["fixed_evidence"]
    assert original.is_dir() and fixed.is_dir()
    assert reward_at(original) == float(row["original_reward"])
    assert reward_at(fixed) == float(row["fixed_reward"])
    key = (row["task"], row["model"], int(row["trial"]))
    assert float(indexed[key]["reward"]) == float(row["fixed_reward"])

manifest = read_json(ROOT / "manifest.json")
assert hashlib.sha256((ROOT / 'indexes/trials.json').read_bytes()).hexdigest() == manifest['index_sha256']
assert hashlib.sha256((ROOT / 'indexes/artifacts.json').read_bytes()).hexdigest() == manifest['artifact_index_sha256']
artifacts = read_json(ROOT / 'indexes/artifacts.json')
assert len(artifacts) == manifest['artifact_count']
for artifact in artifacts:
    path = ROOT / artifact['path']
    assert path.stat().st_size == artifact['bytes'], artifact['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == artifact['sha256'], artifact['path']
for task in manifest["tasks"]:
    repair = task.get("verifier_repair")
    if repair:
        assert (ROOT / repair["evidence"]).is_file()

print("PASS: 400 scored rows (398 strict-valid completions + 2 turn-limit failures); 10 x 5 x 8")
print(f"PASS: {len(artifacts)} artifact hashes and 400 trajectories verified")
for model in MODELS:
    print(f"  {model}: {totals[model]}/80 = {100 * totals[model] / 80:.1f}%")
print("PASS: 320 Real-SWE taxonomy rows; each failure has one cause and evidence")
print("PASS: 12 repaired rows = 7 flips to pass + 5 genuine model failures")
