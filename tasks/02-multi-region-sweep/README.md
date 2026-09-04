The agent has access to the full source code for a private cloud billing application and a local mock AWS account. It must make the application find every AWS region the account uses and list its storage disks and backup snapshots. Empty regions must stay in the report, permanently unreadable regions must be skipped, and temporary failures must be retried without losing results from other regions.

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
| Kimi K3 | Kimi Code | 6m | 9,184.6 | 18.6 |
| GPT-5.6 Sol | Codex CLI | 5m | 8,296.5 | 23.1 |
