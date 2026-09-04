The agent has access to a private NestJS and TypeScript backend with local identity-provider and configuration-store emulators. It must build an environment-aware API key screen that lists, rotates, and retires only the current tenant's authorized credentials.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 8 | 8 | 100.0% |
| GLM 5.3 | Claude Code | 5 | 8 | 62.5% |
| Grok 4.6 | Grok Build | 4 | 8 | 50.0% |
| Kimi K3 | Kimi Code | 0 | 8 | 0.0% |
| GPT-5.6 Sol | Codex CLI | 7 | 8 | 87.5% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 29m | 71,285.1 | 31.8 |
| GLM 5.3 | Claude Code | 47m | 125,249.0 | 176.6 |
| Grok 4.6 | Grok Build | 26m | 15,721.6 | 37.0 |
| Kimi K3 | Kimi Code | 55m | Not recorded | 103.5 |
| GPT-5.6 Sol | Codex CLI | 15m | 25,003.6 | 51.0 |
