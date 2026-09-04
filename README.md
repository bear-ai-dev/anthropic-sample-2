# Anthropic Sample 2

Anthropic Sample 2 is a Real SWE benchmark sample of engineering tasks on private, real world company codebases. It contains **400 strict-scored rollouts across 10 tasks**. Every row below is computed from [`indexes/trials.json`](indexes/trials.json), and each scored rollout resolves to a normalized trajectory and verifier verdict.

## Table of contents

- [Pass rates](#pass-rates)
- [Efficiency](#efficiency)
- [Task distribution](#task-distribution)
- [Evidence and validity](#evidence-and-validity)
- [Repository layout](#repository-layout)

## Pass rates

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 31 | 80 | 38.8% |
| GLM 5.3 | Claude Code | 23 | 80 | 28.8% |
| Grok 4.6 | Grok Build | 19 | 80 | 23.8% |
| Kimi K3 | Kimi Code | 15 | 80 | 18.8% |
| GPT-5.6 Sol | Codex CLI | 13 | 80 | 16.2% |

All pass rates aggregate the complete Real SWE benchmark by model and listed harness family. The Grok Build row combines 64 Grok Build rollouts and 16 Grok Build ACP rollouts.

## Efficiency

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 21m | 63,749.6 | 25.8 |
| GLM 5.3 | Claude Code | 39m | 117,404.9 | 144.4 |
| Grok 4.6 | Grok Build | 30m | 66,666.1 | 36.4 |
| Kimi K3 | Kimi Code | 32m | Not recorded | 77.8 |
| GPT-5.6 Sol | Codex CLI | 15m | 22,678.0 | 42.8 |

Wall clock is `finished_at - started_at` for a complete scored rollout and is rounded to the nearest minute. Output tokens are the total completion/output tokens recorded by the native harness. Steps are normalized trajectory events. Means use only recorded values, and missing values are not treated as zero.

## Task distribution

The benchmark contains ten Real SWE tasks:

- [`01-entitlement-overage-lines`](tasks/01-entitlement-overage-lines/instruction.md)
- [`02-multi-region-sweep`](tasks/02-multi-region-sweep/instruction.md)
- [`04-tax-jurisdiction`](tasks/04-tax-jurisdiction/instruction.md)
- [`06-api-token-metering`](tasks/06-api-token-metering/instruction.md)
- [`07-api-keys-and-environments`](tasks/07-api-keys-and-environments/instruction.md)
- [`09-s3-datastore-measurement`](tasks/09-s3-datastore-measurement/instruction.md)
- [`10-customer-identity-migration`](tasks/10-customer-identity-migration/instruction.md)
- [`11-customer-billing-schedule-migration`](tasks/11-customer-billing-schedule-migration/instruction.md)
- [`01-linearizable-scan`](tasks/01-linearizable-scan/instruction.md)
- [`03-analytics-stream-reducer`](tasks/03-analytics-stream-reducer/instruction.md)

## Evidence and validity

A rollout is scored only when it has no harness exception, a numeric verifier reward, a complete non-empty trajectory, verifier evidence, the task identity, and the declared model route and harness. Infrastructure and provider failures are excluded from denominators.

- [`indexes/trials.json`](indexes/trials.json) is the scored index.
- [`manifest.json`](manifest.json) records task identity, source commits, totals, and content hashes.
- [`trajectories/`](trajectories/) contains every normalized scored trajectory.
- [`verification/`](verification/) contains source verifier output and a verifier verdict for every scored trial.
- [`results/`](results/) preserves configuration-level cohort and redaction metadata.
- [`indexes/controls.json`](indexes/controls.json) records the task oracle/no-op evidence used for validity checks.

The licensed application workspaces for two Real SWE tasks are intentionally omitted. Their task contracts, verifiers, reference materials, source hashes, trajectories, and verifier evidence are retained after credential and restricted-name redaction.

Private chain-of-thought fields and encrypted provider reasoning blobs are intentionally blanked in every trajectory. Observable assistant messages, tool activity, final answers, metrics, and verifier evidence are retained.

## Repository layout

```text
tasks/<task>/
results/<model-harness-provider>/
trajectories/<task>/<model-harness-provider>/trajectory-trial-<01-08>.json
verification/<task>/<model-harness-provider>/trial-<01-08>/
indexes/trials.json
indexes/artifacts.json
indexes/controls.json
manifest.json
```
