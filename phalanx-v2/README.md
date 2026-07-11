# Phalanx Swarm v2.0-OMEGA — Zero-Cost Autonomous Stack

**Built entirely from free, publicly accessible tools. Zero human config required.**

## Architecture

```
phalanx-swarm-v2/
├── agents/          — 30 agent configs (Python, JSON, no K8s)
├── core/            — Async runner, scheduler, message bus
├── data/            — SQLite + JSON (no Neo4j/Redis/Kafka)
├── scripts/         — Deploy, test, run everything
├── ui/              — Static HTML dashboard (single file, no server)
├── reports/         — Auto-generated markdown dashboards
└── README.md        — This file
```

## How to Run (Single Command)

```bash
cd /agent/workspace/phalanx-swarm-v2
python3 scripts/launch.py
```

That's it. No AWS. No Terraform. No Docker. No credentials. No human config.

## What It Does

1. **Spawns 30 logical agents** in async Python coroutines (not containers)
2. **Runs 5-minute cycles** — health checks, task dispatch, self-healing
3. **Tracks everything** in SQLite (`data/phalanx.db`) and JSON (`data/knowledge_graph.json`)
4. **Models finances** with Monte Carlo (numpy, no external APIs)
5. **Checks compliance** against 6 regulatory deadlines
6. **Scans security** of all files in this workspace
7. **Generates a dashboard** as a single HTML file you can open in any browser
8. **Commits to GitHub** via existing integration (no extra auth)

## Data Storage (All Free, Local)

| Layer | Technology | Cost |
|-------|-----------|------|
| State | SQLite3 | $0 |
| Cache | Python `dict` + JSON | $0 |
| Messaging | `asyncio.Queue` | $0 |
| Knowledge Graph | JSON file | $0 |
| Logs | Rotating text files | $0 |
| Dashboard | Static HTML | $0 |

## Cost

**$0.00** — Uses only your existing sandbox, free Python libraries, and already-connected integrations.
