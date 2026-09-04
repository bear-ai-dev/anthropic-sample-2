# Anthropic Sample 2 trace report

This report is computed from [`indexes/trials.json`](../indexes/trials.json). It covers 400 scored rollouts: ten tasks, five native model/harness configurations, and eight independent rollouts per task. The denominator includes 398 strict-valid completions and two GLM 5.3 turn-limit failures on Task 3, trials 05 and 07. Those two zeroes follow the source benchmark rule and are not strict-valid completions. Provider and infrastructure failures are excluded.

## Pass rates

| Model | Harness | Passes | Rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 31 | 80 | 38.8% |
| GLM 5.3 | Claude Code | 23 | 80 | 28.8% |
| Grok 4.6 | Grok Build / Grok Build ACP | 19 | 80 | 23.8% |
| Kimi K3 | Kimi Code | 15 | 80 | 18.8% |
| GPT-5.6 Sol | Codex CLI | 13 | 80 | 16.2% |

## Task-level resolution

Each cell is passes out of eight independent rollouts.

| Task | Fable 5.1 | GLM 5.3 | Grok 4.6 | Kimi K3 | GPT-5.6 Sol |
|---|---:|---:|---:|---:|---:|
| Task 5: `07-api-keys-and-environments` | 8/8 | 5/8 | 4/8 | 0/8 | 7/8 |
| Task 1: `01-entitlement-overage-lines` | 8/8 | 3/8 | 1/8 | 6/8 | 1/8 |
| Task 7: `10-customer-identity-migration` | 3/8 | 4/8 | 8/8 | 4/8 | 0/8 |
| Task 2: `02-multi-region-sweep` | 7/8 | 2/8 | 3/8 | 2/8 | 5/8 |
| Task 6: `09-s3-datastore-measurement` | 0/8 | 3/8 | 2/8 | 1/8 | 0/8 |
| Task 8: `11-customer-billing-schedule-migration` | 3/8 | 2/8 | 0/8 | 1/8 | 0/8 |
| Task 9: `01-linearizable-scan` | 0/8 | 2/8 | 1/8 | 0/8 | 0/8 |
| Task 4: `06-api-token-metering` | 1/8 | 1/8 | 0/8 | 1/8 | 0/8 |
| Task 3: `04-tax-jurisdiction` | 1/8 | 1/8 | 0/8 | 0/8 | 0/8 |
| Task 10: `03-analytics-stream-reducer` | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

## Verifier repair

The 2026-09-04 repair replayed the same saved submissions; it did not make new model calls. Within this proposal's eight repository-backed Real-SWE tasks, twelve affected rows were replayed: seven changed from 0 to 1 and five remained 0. The original and repaired verifier artifacts are both retained in `verification/` and indexed in [`verifier-repair-summary.json`](verifier-repair-summary.json).

The repaired task controls still satisfy the admission gate: oracle reward 1.0 and no-op reward 0.0.

## Failure modes

The taxonomy below covers the eight repository-backed Real-SWE tasks (64 rollouts per model). The two licensed company-workflow tasks remain in the pass-rate and task-resolution tables, but are excluded from this qualitative taxonomy so different task families are not silently pooled. Percentages use each model's failures in these eight tasks as the denominator and may differ by one point from 100% after rounding.

| Failure mode | Fable 5.1 | GLM 5.3 | Grok 4.6 | Kimi K3 | GPT-5.6 Sol |
|---|---:|---:|---:|---:|---:|
| Unverified assumption | 36% | 35% | 24% | 18% | 47% |
| Missed requirement | 6% | 19% | 65% | 41% | 20% |
| Integration error | 52% | 33% | 11% | 35% | 22% |
| Regression | 6% | — | — | — | 12% |
| Wrong file | — | 9% | — | 4% | — |
| Trial incomplete | — | 5% | — | 2% | — |

Every failing row has exactly one recorded primary label, attribution, mechanism, and evidence path in [`failure-modes.csv`](failure-modes.csv). These labels are provisional: nine API-token-metering entry-point labels require adjudication. The former Grok reward-only gap is closed: all 46 current Grok failures now link to original detailed consequences in [`grok-evidence-review.json`](grok-evidence-review.json). Recovery does not independently certify every causal label or replay the remaining S3 zeroes under a repaired grader. The absence of task-side labels in the current CSV does not prove the absence of grader defects. The two GLM turn-limit zeroes are labeled Trial incomplete under the termination rule. Failure taxonomy adapted from DeepSWE.

## Original evidence recovery

The September 4 recovery matched all 64 Grok repository-task traces to the original canonical audit using trajectory session IDs, step sequences, original hashes, result identities, and task checksums. It recovered 538 redacted files covering those trials and sixteen original controls. The controls retain eight oracle rewards of 1 and eight no-op rewards of 0. Source and released hashes are recorded in [`evidence-recovery.json`](evidence-recovery.json). These are historical results, not newly run controls. Scores, primary labels, cohort membership, and trajectory contents are unchanged.

The recovered reports record missing zero-price invoice lines, omitted snapshot regions, tax-contract mismatches, metering registration/account problems, ineffective key revocation, S3 configuration/DLQ failures, and billing-schedule routing failures. These are observed check outcomes; the retained mechanism labels are a separate inference. The API entry-point question still requires explicit fairness adjudication, and original S3 diagnostics must not be mistaken for a fresh repaired-grader replay.

## Recorded label distribution (provisional)

- Fable 5.1's largest bucket is integration error (52% of 33 failures).
- Grok 4.6's failures are concentrated in missed requirements (65% of 46 failures).
- GPT-5.6 Sol most often commits to an unverified assumption (47% of 51 failures).
- GLM 5.3 and Kimi K3 split more evenly between unverified assumptions, missed requirements, and integration errors.

These bullets describe the current label file, not independently confirmed causal percentages. In particular, do not infer a model integration failure solely because a grader selected an unreachable or unintended helper method. Resolving that issue requires controls and saved-submission replays; this follow-up does not change the Sample 2 grader or scores. Each score belongs to the model, harness, provider route, task set, and verifier version, not the base model alone.

## Reproduction

Run `python3 analysis/verify.py` from the repository root. It recomputes all pass tables from `indexes/trials.json`, checks the failure-label coverage against current rewards, and verifies that repaired evidence paths exist.
