# Anthropic Sample 2

Anthropic Sample 2 contains **576 strict-scored rollouts across 10 tasks**. Every row below is computed from [`indexes/trials.json`](indexes/trials.json), and each scored rollout resolves to a normalized trajectory and canonical verifier verdict.

## Table of contents

- [Pass rates](#pass-rates)
- [Efficiency](#efficiency)
- [Task distribution](#task-distribution)
- [Evidence and validity](#evidence-and-validity)
- [Repository layout](#repository-layout)

## Pass rates

| Model | Harness | Provider | Scope | Passes | Scored rollouts | Pass rate |
|---|---|---|---|---:|---:|---:|
| Opus 5 | Claude Code 2.1.250 | Bedrock | Real-SWE | 39 | 64 | 60.9% |
| Fable 5.1 | Claude Code 2.1.257 | Bedrock | Real-SWE | 31 | 64 | 48.4% |
| Grok 4.6 | mini-SWE-agent 2.4.5 | OpenRouter | company-simulation | 5 | 16 | 31.2% |
| GLM 5.3 | Claude Code 2.1.250 | OpenRouter | Real-SWE, company-simulation | 23 | 80 | 28.8% |
| Grok 4.6 | Grok Build 1.0.5 | Bedrock | Real-SWE | 18 | 64 | 28.1% |
| GPT-5.6 Sol | Codex CLI 0.151.0 | Bedrock | Real-SWE | 13 | 64 | 20.3% |
| Kimi K3 | Kimi Code 0.39.1 | OpenRouter | Real-SWE, company-simulation | 15 | 80 | 18.8% |
| Opus 5 | Claude Code 2.1.236 | Bedrock | company-simulation | 2 | 16 | 12.5% |
| Grok 4.6 | Grok Build ACP 1.0.18 | OpenRouter | company-simulation | 1 | 16 | 6.2% |
| Gemini 3.1 Pro | Antigravity 1.1.23 | OpenRouter | Real-SWE | 2 | 64 | 3.1% |
| Fable 5.1 | Claude Code 2.1.258 | Bedrock | company-simulation | 0 | 16 | 0.0% |
| GLM 5.3 | mini-SWE-agent 2.4.5 | OpenRouter | company-simulation | 0 | 16 | 0.0% |
| GPT-5.6 Sol | Codex CLI 0.151.0 | OpenRouter | company-simulation | 0 | 16 | 0.0% |

Rows are separated whenever provider, harness, or harness version differs. This prevents incompatible execution configurations from being presented as one unlabeled base-model score.

## Efficiency

| Model | Harness | Provider | Scope | Mean wall clock (s) | Mean output tokens | Mean steps | Coverage (wall/output/steps) |
|---|---|---|---|---:|---:|---:|---:|
| Opus 5 | Claude Code 2.1.250 | Bedrock | Real-SWE | 1,744.8 | 59,955.1 | 99.2 | 64/64, 64/64, 64/64 |
| Fable 5.1 | Claude Code 2.1.257 | Bedrock | Real-SWE | 1,274.6 | 57,957.4 | 25.9 | 64/64, 64/64, 64/64 |
| Grok 4.6 | mini-SWE-agent 2.4.5 | OpenRouter | company-simulation | 2,477.9 | 135,940.6 | 65.2 | 16/16, 16/16, 16/16 |
| GLM 5.3 | Claude Code 2.1.250 | OpenRouter | Real-SWE, company-simulation | 2,315.2 | 117,404.9 | 144.4 | 80/80, 80/80, 80/80 |
| Grok 4.6 | Grok Build 1.0.5 | Bedrock | Real-SWE | 958.0 | 11,364.6 | 26.1 | 64/64, 64/64, 64/64 |
| GPT-5.6 Sol | Codex CLI 0.151.0 | Bedrock | Real-SWE | 931.2 | 19,959.4 | 39.6 | 64/64, 64/64, 64/64 |
| Kimi K3 | Kimi Code 0.39.1 | OpenRouter | Real-SWE, company-simulation | 1,931.2 | Not recorded | 77.8 | 80/80, 0/80, 80/80 |
| Opus 5 | Claude Code 2.1.236 | Bedrock | company-simulation | 3,043.9 | 116,188.3 | 122.1 | 16/16, 16/16, 16/16 |
| Grok 4.6 | Grok Build ACP 1.0.18 | OpenRouter | company-simulation | 5,206.2 | 287,871.8 | 77.5 | 16/16, 16/16, 16/16 |
| Gemini 3.1 Pro | Antigravity 1.1.23 | OpenRouter | Real-SWE | 787.2 | Not recorded | 169.9 | 64/64, 0/64, 64/64 |
| Fable 5.1 | Claude Code 2.1.258 | Bedrock | company-simulation | 1,258.6 | 86,918.5 | 25.6 | 16/16, 16/16, 16/16 |
| GLM 5.3 | mini-SWE-agent 2.4.5 | OpenRouter | company-simulation | 2,189.2 | 118,574.2 | 176.6 | 16/16, 16/16, 16/16 |
| GPT-5.6 Sol | Codex CLI 0.151.0 | OpenRouter | company-simulation | 746.7 | 33,552.2 | 55.4 | 16/16, 16/16, 16/16 |

Wall clock is `finished_at - started_at` for a complete scored rollout. Output tokens are the total completion/output tokens recorded by the native harness. Steps are normalized trajectory events. Means use only recorded values, and the coverage column gives recorded counts in wall/output/steps order. Missing values are not treated as zero.

## Task distribution

The exact proposal distribution is eight Real-SWE tasks and two company-simulation tasks:

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

A rollout is scored only when it has no harness exception, a numeric verifier reward, a complete non-empty trajectory, verifier evidence, the frozen task identity, and the declared model route and harness. Infrastructure and provider failures are excluded from denominators.

- [`indexes/trials.json`](indexes/trials.json) is the canonical scored index.
- [`manifest.json`](manifest.json) records task identity, source commits, totals, and content hashes.
- [`trajectories/`](trajectories/) contains every normalized scored trajectory.
- [`verification/`](verification/) contains source verifier output and a canonical verdict for every scored trial.
- [`results/`](results/) preserves configuration-level cohort and redaction metadata.
- [`indexes/controls.json`](indexes/controls.json) records the frozen-task oracle/no-op evidence used for validity checks.

The licensed application workspace for the two company-simulation tasks is intentionally omitted. Their task contracts, verifiers, reference materials, frozen source hashes, trajectories, and verifier evidence are retained after credential and restricted-name redaction.

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
