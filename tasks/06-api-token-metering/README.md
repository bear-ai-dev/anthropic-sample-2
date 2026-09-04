The agent has access to the full source code for a private usage and billing platform and a local database with example API traffic. It must turn each customer company's API request into billable usage, total those requests in six-hour periods, and bill the correct account exactly once. The same request may arrive more than once or arrive late, but it must never be charged twice or moved into the wrong billing period.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 1 | 8 | 12.5% |
| GLM 5.3 | Claude Code | 1 | 8 | 12.5% |
| Grok 4.6 | Grok Build | 0 | 8 | 0.0% |
| Kimi K3 | Kimi Code | 1 | 8 | 12.5% |
| GPT-5.6 Sol | Codex CLI | 0 | 8 | 0.0% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 30m | 95,330.1 | 27.4 |
| GLM 5.3 | Claude Code | 55m | 176,583.5 | 173.8 |
| Grok 4.6 | Grok Build | 20m | 15,178.4 | 27.1 |
| Kimi K3 | Kimi Code | 54m | 69,416.8 | 107.6 |
| GPT-5.6 Sol | Codex CLI | 18m | 30,694.9 | 45.0 |
