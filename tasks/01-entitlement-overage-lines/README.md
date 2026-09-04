The agent has access to a private NestJS and TypeScript billing backend with a local AWS-compatible emulator. It must restore allowance and overage billing so invoices show the correct usage lines and quantities.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 8 | 8 | 100.0% |
| GLM 5.3 | Claude Code | 3 | 8 | 37.5% |
| Grok 4.6 | Grok Build | 1 | 8 | 12.5% |
| Kimi K3 | Kimi Code | 6 | 8 | 75.0% |
| GPT-5.6 Sol | Codex CLI | 1 | 8 | 12.5% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 18m | 34,069.4 | 21.0 |
| GLM 5.3 | Claude Code | 39m | 68,281.0 | 124.4 |
| Grok 4.6 | Grok Build | 14m | 7,437.2 | 22.9 |
| Kimi K3 | Kimi Code | 37m | Not recorded | 69.1 |
| GPT-5.6 Sol | Codex CLI | 7m | 11,889.1 | 30.4 |
