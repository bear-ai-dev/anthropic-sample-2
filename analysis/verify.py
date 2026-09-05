#!/usr/bin/env python3
"""Verify Sample 2 scores, failure labels, and repaired-verifier evidence."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from evidence_checks import failure_checks


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
for folder in ('results', 'verification', 'trajectories', 'controls', 'analysis', 'indexes', 'docs', 'tasks'):
    for path in (ROOT/folder).rglob('*'):
        if path.is_dir():
            assert not re.search(r'bedrock|open.?router', path.name, re.I), path
assert len(trials) == 400
trajectory_labels = {Path(r['trajectory']).parent.name for r in trials}
assert {p.name for p in (ROOT/'results').iterdir() if p.is_dir()} == trajectory_labels
for label in trajectory_labels:
    model_rows = read_json(ROOT/'results'/label/'index.json')
    expected_rows = [r for r in trials if Path(r['trajectory']).parent.name == label]
    key = lambda r: (r['task'], r['trial_number'])
    assert len(model_rows) == 80 and sorted(model_rows, key=key) == sorted(expected_rows, key=key)
    cohort = read_json(ROOT/'results'/label/'cohort.json')
    assert cohort['scored_trials'] == 80 and cohort['passes'] == sum(r['passed'] for r in model_rows)
    if 'cohorts' in cohort:
        assert sum(c['scored_trials'] for c in cohort['cohorts']) == 80
        assert {c['arm'] for c in cohort['cohorts']} == {r['arm'] for r in model_rows}
assert len({r["task"] for r in trials}) == 10
assert set(r["model_label"] for r in trials) == set(MODELS)

cells = Counter((r["task"], r["model_label"]) for r in trials)
assert len(cells) == 50 and set(cells.values()) == {8}
assert len({(r['task'], r['model_label'], r['trial_number']) for r in trials}) == 400
assert Counter(r['admission'] for r in trials) == {'strict-valid': 398, 'scored-terminal-failure': 2}
for row in trials:
    trajectory = ROOT / row['trajectory']
    assert Path(row['verification']).parts[2] == trajectory.parent.name
    assert 'bedrock' not in trajectory.parent.name and 'openrouter' not in trajectory.parent.name
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
assert sum(totals.values()) == read_json(ROOT / "indexes/manifest.json")["passes"] == 101

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

manifest = read_json(ROOT / "indexes/manifest.json")
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

recovery = read_json(ROOT / 'analysis/evidence-recovery.json')
review = read_json(ROOT / 'analysis/grok-evidence-review.json')['trials']
assert len(recovery['trials']) == len(review) == 64
assert len(recovery['controls']) == 16
assert Counter((r['agent'], r['reward']) for r in recovery['controls']) == {('oracle', 1.0): 8, ('nop', 0.0): 8}
for record in recovery['trials'] + recovery['controls']:
    for artifact in record['files']:
        assert hashlib.sha256((ROOT / artifact['path']).read_bytes()).hexdigest() == artifact['sha256']
        assert len(artifact['source_sha256']) == 64
    result_path = next(f['path'] for f in record['files'] if f['path'].endswith('/result-summary.json'))
    result = read_json(ROOT / result_path)
    assert result['exception_info'] is None and result['finished_at']
    assert result['verifier_result']['rewards']['reward'] == record.get('original_reward', record.get('reward'))
for record in review:
    trial = indexed[(record['task'], 'Grok 4.6', record['trial'])]
    assert record['effective_reward'] == trial['reward']
    assert record['trajectory'] == trial['trajectory']
    checks, source = failure_checks(ROOT / record['original_verifier'], trial['reward'])
    assert checks == record['recorded_failing_checks'] and source == record['checks_source']
    assert trial['passed'] or checks
assert sum(r['effective_reward'] == 0 for r in review) == 46

print("PASS: 400 scored rows (398 strict-valid completions + 2 turn-limit failures); 10 x 5 x 8")
print(f"PASS: {len(artifacts)} artifact hashes and 400 trajectories verified")
for model in MODELS:
    print(f"  {model}: {totals[model]}/80 = {100 * totals[model] / 80:.1f}%")
print("PASS: 320 Real-SWE taxonomy rows; each failure has one recorded label and evidence reference")
print("PASS: 12 recorded repairs = 7 flips to pass + 5 retained zeroes")
print("PASS: 64 exact Grok original evidence bundles, 46 detailed failure records, 16 original controls")
print("LIMIT: recovered evidence is not a fresh replay or causal sign-off; entry-point fairness remains open. See docs/HANDOFF.md")
