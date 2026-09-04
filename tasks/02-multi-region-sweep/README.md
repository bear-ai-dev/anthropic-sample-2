The agent has access to a private NestJS and TypeScript backend with a local AWS-compatible emulator. It must discover enabled regions and make storage inventory sweeps handle empty, blocked, and temporarily rate-limited regions correctly.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 7 | 8 | 87.5% |
| GLM 5.3 | Claude Code | 2 | 8 | 25.0% |
| Grok 4.6 | Grok Build | 3 | 8 | 37.5% |
| Kimi K3 | Kimi Code | 2 | 8 | 25.0% |
| GPT-5.6 Sol | Codex CLI | 5 | 8 | 62.5% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 18m | 30,157.9 | 19.0 |
| GLM 5.3 | Claude Code | 17m | 53,076.9 | 66.2 |
| Grok 4.6 | Grok Build | 10m | 2,801.6 | 11.4 |
| Kimi K3 | Kimi Code | 6m | Not recorded | 18.6 |
| GPT-5.6 Sol | Codex CLI | 5m | 8,296.5 | 23.1 |
