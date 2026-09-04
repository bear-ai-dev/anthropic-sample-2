The agent has access to the full source code for a private event-ticketing system and a local copy of the team's issue tracker. It must fix ticket scanning at a venue so one ticket cannot admit more people than it was bought for, even when staff scan it at several entrances at the same time. Repeating the same scan request must return the same answer, and the event organizer's dashboard must match the scan record.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 0 | 8 | 0.0% |
| GLM 5.3 | Claude Code | 2 | 8 | 25.0% |
| Grok 4.6 | Grok Build | 1 | 8 | 12.5% |
| Kimi K3 | Kimi Code | 0 | 8 | 0.0% |
| GPT-5.6 Sol | Codex CLI | 0 | 8 | 0.0% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 23m | 86,052.6 | 33.4 |
| GLM 5.3 | Claude Code | 48m | 172,487.5 | 209.0 |
| Grok 4.6 | Grok Build | 1h 19m | 260,828.6 | 90.2 |
| Kimi K3 | Kimi Code | 43m | 71,327.0 | 133.4 |
| GPT-5.6 Sol | Codex CLI | 16m | 37,301.0 | 73.4 |
