The agent has access to a private NestJS billing backend with local tax-authority and ledger emulators. It must restore tax calculation, exemptions, VAT details, and settled-invoice reporting.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 1 | 8 | 12.5% |
| GLM 5.3 | Claude Code | 1 | 8 | 12.5% |
| Grok 4.6 | Grok Build | 0 | 8 | 0.0% |
| Kimi K3 | Kimi Code | 0 | 8 | 0.0% |
| GPT-5.6 Sol | Codex CLI | 0 | 8 | 0.0% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 23m | 77,579.4 | 30.5 |
| GLM 5.3 | Claude Code | 47m | 140,669.8 | 201.8 |
| Grok 4.6 | Grok Build | 19m | 11,602.2 | 31.6 |
| Kimi K3 | Kimi Code | 33m | Not recorded | 77.8 |
| GPT-5.6 Sol | Codex CLI | 15m | 22,271.9 | 45.4 |
