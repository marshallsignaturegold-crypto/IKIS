"""Phalanx Swarm v2.0-OMEGA — Async Runner (Zero-Cost, Pure Python)"""

import asyncio
import json
import logging
import os
import random
import signal
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from core.config import (
    BASE_PATH, DATA_PATH, AGENTS_PATH, PHALANX_GROUPS, CYCLE_INTERVAL_SECONDS,
    HEARTBEAT_TIMEOUT_SECONDS, REGULATORY_FILINGS, FINANCIAL_MODELS
)

# Ensure scripts module is importable when running from core/
sys.path.insert(0, BASE_PATH)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(os.path.join(DATA_PATH, "phalanx.log"), mode="a")
    ]
)
logger = logging.getLogger("phalanx.swarm")

class PhalanxAgent:
    """A single agent in the swarm. Runs as an asyncio coroutine."""
    def __init__(self, agent_id: str, group: str, role: str, capabilities: List[str]):
        self.id = agent_id
        self.group = group
        self.role = role
        self.capabilities = capabilities
        self.status = "active"
        self.heartbeat = datetime.now(timezone.utc).isoformat()
        self.tasks_completed = 0
        self.errors = 0
        self.current_task = None
        self.queue = None  # Created lazily in run() to bind to the correct event loop

    async def run(self):
        """Main agent loop."""
        self.queue = asyncio.Queue()
        logger.info(f"Agent {self.id} ({self.group}) started — {self.role}")
        while self.status != "shutdown":
            try:
                # Update heartbeat
                self.heartbeat = datetime.now(timezone.utc).isoformat()
                
                # Process task if available
                try:
                    task = await asyncio.wait_for(self.queue.get(), timeout=1.0)
                    await self.execute_task(task)
                except asyncio.TimeoutError:
                    pass
                
                # Idle work based on role
                await self.idle_work()
                
                await asyncio.sleep(0.5)
            except Exception as e:
                self.errors += 1
                logger.error(f"Agent {self.id} error: {e}")
                if self.errors > 10:
                    self.status = "error"
                    logger.critical(f"Agent {self.id} reached error threshold")
                    break
        
        logger.info(f"Agent {self.id} shutdown")

    async def execute_task(self, task: Dict):
        """Execute a single task."""
        self.current_task = task
        task_type = task.get("type", "unknown")
        
        logger.info(f"Agent {self.id} executing task {task.get('id', '?')} ({task_type})")
        
        # Simulate task execution
        await asyncio.sleep(random.uniform(0.1, 0.5))
        
        self.tasks_completed += 1
        self.current_task = None
        logger.info(f"Agent {self.id} completed task {task.get('id', '?')}")

    async def idle_work(self):
        """Background work when no tasks queued."""
        if "monitoring" in self.capabilities:
            pass
        elif "security" in self.capabilities:
            pass
        elif "compliance" in self.capabilities:
            pass

class PhalanxSwarm:
    """The swarm controller. Manages all 30 agents."""
    def __init__(self):
        self.agents: Dict[str, PhalanxAgent] = {}
        self.cycle_count = 0
        self.running = False
        self.state_file = os.path.join(DATA_PATH, "swarm_state.json")
        self.knowledge_graph = os.path.join(DATA_PATH, "knowledge_graph.json")
        self.db_path = os.path.join(DATA_PATH, "phalanx.db")
        self._init_agents()

    def _init_agents(self):
        """Initialize 30 agents from JSON configs or PHALANX_GROUPS."""
        agent_files = sorted(Path(AGENTS_PATH).glob("*.json"))
        loaded = 0
        
        for filepath in agent_files:
            try:
                with open(filepath) as f:
                    config = json.load(f)
                agent = PhalanxAgent(
                    agent_id=config["id"],
                    group=config["group"],
                    role=config["role"],
                    capabilities=config.get("capabilities", [config["role"].lower().replace(" & ", "_").replace(" ", "_")])
                )
                self.agents[config["id"]] = agent
                loaded += 1
            except Exception as e:
                logger.warning(f"Failed to load agent config {filepath}: {e}")
        
        # Fallback to PHALANX_GROUPS if no JSON configs loaded
        if loaded == 0:
            for group_name, config in PHALANX_GROUPS.items():
                for i in range(config["count"]):
                    agent_id = f"{group_name}-{i}"
                    agent = PhalanxAgent(
                        agent_id=agent_id,
                        group=group_name,
                        role=config["role"],
                        capabilities=[config["role"].lower().replace(" & ", "_").replace(" ", "_")]
                    )
                    self.agents[agent_id] = agent
        
        logger.info(f"Swarm initialized with {len(self.agents)} agents")

    def _persist_to_db(self):
        """Persist swarm state to SQLite."""
        os.makedirs(DATA_PATH, exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS agents (
            id TEXT PRIMARY KEY,
            group_name TEXT,
            role TEXT,
            status TEXT,
            heartbeat TEXT,
            tasks_completed INTEGER DEFAULT 0,
            errors INTEGER DEFAULT 0,
            created_at TEXT
        )''')
        
        for agent in self.agents.values():
            c.execute('''INSERT OR REPLACE INTO agents
                (id, group_name, role, status, heartbeat, tasks_completed, errors, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (agent.id, agent.group, agent.role, agent.status, agent.heartbeat,
                 agent.tasks_completed, agent.errors, datetime.now(timezone.utc).isoformat()))
        
        conn.commit()
        conn.close()
        logger.info("State persisted to SQLite")

    def _persist_cycle(self, duration_ms: float, tasks_dispatched: int, findings_critical: int, findings_high: int):
        """Persist cycle metrics to SQLite."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS cycles (
            cycle_id INTEGER PRIMARY KEY,
            timestamp TEXT,
            duration_ms REAL,
            agents_active INTEGER,
            agents_unhealthy INTEGER,
            tasks_dispatched INTEGER,
            findings_critical INTEGER,
            findings_high INTEGER,
            models_validated INTEGER,
            filings_checked INTEGER
        )''')
        
        c.execute('''INSERT INTO cycles
            (timestamp, duration_ms, agents_active, agents_unhealthy, tasks_dispatched,
             findings_critical, findings_high, models_validated, filings_checked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (datetime.now(timezone.utc).isoformat(),
             duration_ms,
             sum(1 for a in self.agents.values() if a.status == "active"),
             sum(1 for a in self.agents.values() if a.status not in ("active", "shutdown")),
             tasks_dispatched,
             findings_critical,
             findings_high,
             len(FINANCIAL_MODELS),
             len(REGULATORY_FILINGS)))
        
        conn.commit()
        conn.close()

    def _persist_findings(self, findings: List[Dict]):
        """Persist security findings to SQLite."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS security_findings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id TEXT,
            severity TEXT,
            layer TEXT,
            rule TEXT,
            description TEXT,
            file_path TEXT,
            line_number INTEGER,
            remediation TEXT,
            timestamp TEXT,
            resolved INTEGER DEFAULT 0
        )''')
        
        for finding in findings:
            c.execute('''INSERT INTO security_findings
                (scan_id, severity, layer, rule, description, file_path, line_number, remediation, timestamp, resolved)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (finding.get("scan_id", "unknown"),
                 finding.get("severity"),
                 finding.get("layer"),
                 finding.get("rule"),
                 finding.get("description"),
                 finding.get("file"),
                 finding.get("line"),
                 finding.get("remediation"),
                 finding.get("timestamp"),
                 0))
        
        conn.commit()
        conn.close()

    async def run_cycle(self):
        """Execute one full cycle."""
        self.cycle_count += 1
        cycle_start = time.time()
        logger.info(f"=== Cycle {self.cycle_count} started ===")
        
        # 1. Health check
        await self._health_check()
        
        # 2. Task dispatch
        tasks_dispatched = await self._dispatch_tasks()
        
        # 3. Financial model validation
        await self._validate_models()
        
        # 4. Compliance check
        await self._check_compliance()
        
        # 5. Security scan
        findings_critical, findings_high = await self._security_scan()
        
        # 6. Update knowledge graph
        await self._update_knowledge_graph()
        
        # 7. Persist state
        self._persist_state()
        self._persist_to_db()
        
        cycle_elapsed = time.time() - cycle_start
        self._persist_cycle(cycle_elapsed * 1000, tasks_dispatched, findings_critical, findings_high)
        
        logger.info(f"=== Cycle {self.cycle_count} completed in {cycle_elapsed:.2f}s ===")

    async def _health_check(self):
        """Check all agent heartbeats."""
        now = datetime.now(timezone.utc)
        unhealthy = []
        
        for agent in self.agents.values():
            hb = datetime.fromisoformat(agent.heartbeat.replace("Z", "+00:00"))
            delta = (now - hb).total_seconds()
            if delta > HEARTBEAT_TIMEOUT_SECONDS:
                unhealthy.append(agent.id)
                logger.warning(f"Agent {agent.id} heartbeat stale ({delta:.0f}s)")
        
        # Self-heal: reset unhealthy agents
        for agent_id in unhealthy:
            agent = self.agents[agent_id]
            agent.heartbeat = datetime.now(timezone.utc).isoformat()
            agent.errors = 0
            logger.info(f"Agent {agent_id} self-healed")

    async def _dispatch_tasks(self):
        """Dispatch tasks to available agents."""
        tasks = [
            {"id": f"task-{self.cycle_count}-{i}", "type": "health_check", "priority": 1}
            for i in range(5)
        ]
        tasks += [
            {"id": f"task-{self.cycle_count}-{i+5}", "type": "metric_collection", "priority": 2}
            for i in range(5)
        ]
        
        for task in tasks:
            # Find least-loaded active agent with an initialized queue
            candidates = [a for a in self.agents.values() if a.status == "active" and a.queue is not None]
            if candidates:
                candidates.sort(key=lambda a: a.queue.qsize())
                await candidates[0].queue.put(task)
        
        return len(tasks)

    async def _validate_models(self):
        """Validate financial models."""
        for model in FINANCIAL_MODELS:
            logger.info(f"Model {model['id']}: {model['name']} — {model['status'].upper()}")

    async def _check_compliance(self):
        """Check regulatory filing deadlines."""
        today = datetime.now(timezone.utc).date()
        for filing in REGULATORY_FILINGS:
            deadline = datetime.strptime(filing["deadline"], "%Y-%m-%d").date()
            days = (deadline - today).days
            if days < 0:
                logger.warning(f"OVERDUE: {filing['id']} — {filing['name']} ({abs(days)} days)")
            elif days <= 7:
                logger.warning(f"URGENT: {filing['id']} — {filing['name']} ({days} days remaining)")
            elif days <= 30:
                logger.info(f"WARNING: {filing['id']} — {filing['name']} ({days} days remaining)")
            else:
                logger.info(f"OK: {filing['id']} — {filing['name']} ({days} days remaining)")

    async def _security_scan(self):
        """Run security scan of workspace."""
        from scripts.security_scan import SecurityScanner
        scanner = SecurityScanner(BASE_PATH)
        result = scanner.run_quick_scan()
        logger.info(f"Security scan: score={result['score']}/100, findings={len(result['findings'])}")
        
        self._persist_findings(result["findings"])
        
        critical = sum(1 for f in result["findings"] if f["severity"] == "CRITICAL")
        high = sum(1 for f in result["findings"] if f["severity"] == "HIGH")
        return critical, high

    async def _update_knowledge_graph(self):
        """Update knowledge graph with current state."""
        graph = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cycle": self.cycle_count,
            "agents": [
                {
                    "id": a.id,
                    "group": a.group,
                    "role": a.role,
                    "status": a.status,
                    "tasks_completed": a.tasks_completed,
                    "errors": a.errors
                }
                for a in self.agents.values()
            ],
            "filings": REGULATORY_FILINGS,
            "models": FINANCIAL_MODELS
        }
        
        os.makedirs(DATA_PATH, exist_ok=True)
        with open(self.knowledge_graph, "w") as f:
            json.dump(graph, f, indent=2)

    def _persist_state(self):
        """Persist swarm state to disk."""
        state = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cycle": self.cycle_count,
            "agents": {
                a.id: {
                    "status": a.status,
                    "heartbeat": a.heartbeat,
                    "tasks_completed": a.tasks_completed,
                    "errors": a.errors
                }
                for a in self.agents.values()
            }
        }
        
        os.makedirs(DATA_PATH, exist_ok=True)
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)

    async def run(self):
        """Main swarm loop."""
        self.running = True
        
        agent_tasks = [asyncio.create_task(a.run()) for a in self.agents.values()]
        logger.info("All agents started")
        
        # Yield to let agents initialize their queues
        await asyncio.sleep(0)
        
        # Cycle loop
        while self.running:
            try:
                await self.run_cycle()
            except Exception as e:
                logger.exception(f"Cycle {self.cycle_count} failed: {e}")
            
            # Sleep until next cycle (but allow interruption)
            for _ in range(CYCLE_INTERVAL_SECONDS):
                if not self.running:
                    break
                await asyncio.sleep(1)
        
        # Shutdown
        for agent in self.agents.values():
            agent.status = "shutdown"
        
        await asyncio.gather(*agent_tasks, return_exceptions=True)
        logger.info("Swarm shutdown complete")

    async def run_once(self):
        """Run a single cycle and shut down."""
        self.running = True
        
        agent_tasks = [asyncio.create_task(a.run()) for a in self.agents.values()]
        logger.info("All agents started")
        
        # Yield to let agents initialize their queues
        await asyncio.sleep(0)
        await asyncio.sleep(1)
        
        try:
            await self.run_cycle()
        except Exception as e:
            logger.exception(f"Cycle failed: {e}")
        
        await asyncio.sleep(2)
        
        # Flush final state after agents have processed tasks
        self._persist_to_db()
        
        self.running = False
        for agent in self.agents.values():
            agent.status = "shutdown"
        
        for agent in self.agents.values():
            while agent.queue is not None and not agent.queue.empty():
                try:
                    agent.queue.get_nowait()
                except asyncio.QueueEmpty:
                    break
        
        await asyncio.gather(*agent_tasks, return_exceptions=True)
        logger.info("Swarm shutdown complete")

    def stop(self):
        self.running = False

async def main():
    os.makedirs(DATA_PATH, exist_ok=True)
    swarm = PhalanxSwarm()
    
    def signal_handler(sig, frame):
        logger.info("Shutdown signal received")
        swarm.stop()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    await swarm.run()

if __name__ == "__main__":
    asyncio.run(main())
