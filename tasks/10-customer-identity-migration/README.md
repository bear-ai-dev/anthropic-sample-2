The agent has access to a private NestJS and TypeScript metering backend. It must move offering ownership and usage reads from legacy services to customers while preserving existing behavior and safely handling customers without offerings.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 3 | 8 | 37.5% |
| GLM 5.3 | Claude Code | 4 | 8 | 50.0% |
| Grok 4.6 | Grok Build | 8 | 8 | 100.0% |
| Kimi K3 | Kimi Code | 4 | 8 | 50.0% |
| GPT-5.6 Sol | Codex CLI | 0 | 8 | 0.0% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 19m | 67,102.0 | 27.6 |
| GLM 5.3 | Claude Code | 32m | 89,911.9 | 176.5 |
| Grok 4.6 | Grok Build | 18m | 19,616.1 | 39.6 |
| Kimi K3 | Kimi Code | 35m | Not recorded | 122.0 |
| GPT-5.6 Sol | Codex CLI | 22m | 23,782.4 | 45.5 |
