The agent has access to the full source code for a private usage and billing platform and a local mock AWS account. It must let customers send usage records through Amazon S3 file storage, create secure access for each customer, and pass valid records into billing. Invalid records must be copied with error details into a separate failure folder so they can be reviewed later.

| Model | Harness | Passes | Scored rollouts | Pass rate |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 0 | 8 | 0.0% |
| GLM 5.3 | Claude Code | 3 | 8 | 37.5% |
| Grok 4.6 | Grok Build | 2 | 8 | 25.0% |
| Kimi K3 | Kimi Code | 1 | 8 | 12.5% |
| GPT-5.6 Sol | Codex CLI | 0 | 8 | 0.0% |

| Model | Harness | Mean wall clock | Mean output tokens | Mean steps |
|---|---|---:|---:|---:|
| Fable 5.1 | Claude Code | 23m | 61,918.9 | 29.9 |
| GLM 5.3 | Claude Code | 37m | 120,877.6 | 142.5 |
| Grok 4.6 | Grok Build | 12m | 12,509.8 | 22.6 |
| Kimi K3 | Kimi Code | 20m | 32,143.8 | 45.1 |
| GPT-5.6 Sol | Codex CLI | 24m | 24,790.8 | 48.6 |
