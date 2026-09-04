The agent has access to a private NestJS and TypeScript billing backend. It must finish customer-based billing schedules, route billing jobs correctly, create invoices for the correct period, and report failures without partial records.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 3 | 8 | 37.5% |
| GLM 5.3 | Claude Code | 2 | 8 | 25.0% |
| Grok 4.6 | Grok Build | 0 | 8 | 0.0% |
| Kimi K3 | Kimi Code | 1 | 8 | 12.5% |
| GPT-5.6 Sol | Codex CLI | 0 | 8 | 0.0% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 11m | 26,216.4 | 20.0 |
| GLM 5.3 | Claude Code | 25m | 57,737.9 | 97.0 |
| Grok 4.6 | Grok Build | 9m | 6,050.0 | 16.9 |
| Kimi K3 | Kimi Code | 11m | Not recorded | 26.9 |
| GPT-5.6 Sol | Codex CLI | 18m | 12,946.1 | 28.1 |
