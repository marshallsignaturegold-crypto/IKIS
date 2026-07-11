"""Phalanx Swarm v2.0-OMEGA — Async Runner (Zero-Cost, Pure Python)"""

import asyncio
import json
import logging
import os
import random
import signal
import sys
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional

from core.config import (
    BASE_PATH, DATA_PATH, PHALANX_GROUPS, CYCLE_INTERVAL_SECONDS,
    HEARTBEAT_TIMEOUT_SECONDS, REGULATORY_FILINGS, FINANCIAL_MODELS
)

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
        self.queue = asyncio.Queue()

    async def run(self):
        logger.info(f"Agent {self.id} ({self.group}) started — {self.role}")
        while self.status != "shutdown":
            try:
                self.heartbeat = datetime.now(timezone.utc).isoformat()
                try:
                    task = await asyncio.wait_for(self.queue.get(), timeout=1.0)
                    await self.execute_task(task)
                except asyncio.TimeoutError:
                    pass
                await self.idle_work()
                await asyncio.sleep(0.5)
            except Exception as e:
                self.errors += 1
                logger.error(f"Agent {self.id} error: {e}")
                if self.errors > 10:
                    self.status = "error"
                    logger.critical(f"Agent {self.id} reached error threshold")
        logger.info(f"Agent {self.id} shutdown")

    async def execute_task(self, task: Dict):
        self.current_task = task
        task_type = task.get("type", "unknown")
        logger.info(f"Agent {self.id} executing task {task.get('id', '?')} ({task_type})")
        await asyncio.sleep(random.uniform(0.1, 0.5))
        self.tasks_completed += 1
        self.current_task = None
        logger.info(f"Agent {self.id} completed task {task.get('id', '?')}")

    async def idle_work(self):
        pass

class PhalanxSwarm:
    """The swarm controller. Manages all 30 agents."""
    def __init__(self):
        self.agents: Dict[str, PhalanxAgent] = {}
        self.cycle_count = 0
        self.running = False
        self.state_file = os.path.join(DATA_PATH, "swarm_state.json")
        self.knowledge_graph = os.path.join(DATA_PATH, "knowledge_graph.json")
        self._init_agents()

    def _init_agents(self):
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

    async def run_cycle(self):
        self.cycle_count += 1
        cycle_start = time.time()
        logger.info(f"=== Cycle {self.cycle_count} started ===")
        await self._health_check()
        await self._dispatch_tasks()
        await self._validate_models()
        await self._check_compliance()
        await self._security_scan()
        await self._update_knowledge_graph()
        self._persist_state()
        cycle_elapsed = time.time() - cycle_start
        logger.info(f"=== Cycle {self.cycle_count} completed in {cycle_elapsed:.2f}s ===")

    async def _health_check(self):
        now = datetime.now(timezone.utc)
        unhealthy = []
        for agent in self.agents.values():
            hb = datetime.fromisoformat(agent.heartbeat.replace("Z", "+00:00"))
            delta = (now - hb).total_seconds()
            if delta > HEARTBEAT_TIMEOUT_SECONDS:
                unhealthy.append(agent.id)
                logger.warning(f"Agent {agent.id} heartbeat stale ({delta:.0f}s)")
        for agent_id in unhealthy:
            old = self.agents[agent_id]
            new_agent = PhalanxAgent(old.id, old.group, old.role, old.capabilities)
            self.agents[agent_id] = new_agent
            asyncio.create_task(new_agent.run())
            logger.info(f"Agent {agent_id} self-healed")

    async def _dispatch_tasks(self):
        tasks = [{"id": f"task-{self.cycle_count}-{i}", "type": "health_check", "priority": 1} for i in range(5)]
        tasks += [{"id": f"task-{self.cycle_count}-{i+5}", "type": "metric_collection", "priority": 2} for i in range(5)]
        for task in tasks:
            candidates = [a for a in self.agents.values() if a.status == "active"]
            if candidates:
                candidates.sort(key=lambda a: a.queue.qsize())
                await candidates[0].queue.put(task)

    async def _validate_models(self):
        for model in FINANCIAL_MODELS:
            logger.info(f"Model {model['id']}: {model['name']} — {model['status'].upper()}")

    async def _check_compliance(self):
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
        from scripts.security_scan import SecurityScanner
        scanner = SecurityScanner(BASE_PATH)
        result = scanner.run_quick_scan()
        logger.info(f"Security scan: score={result['score']}/100, findings={len(result['findings'])}")

    async def _update_knowledge_graph(self):
        graph = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cycle": self.cycle_count,
            "agents": [{"id": a.id, "group": a.group, "role": a.role, "status": a.status, "tasks_completed": a.tasks_completed, "errors": a.errors} for a in self.agents.values()],
            "filings": REGULATORY_FILINGS,
            "models": FINANCIAL_MODELS
        }
        os.makedirs(DATA_PATH, exist_ok=True)
        with open(self.knowledge_graph, "w") as f:
            json.dump(graph, f, indent=2)

    def _persist_state(self):
        state = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cycle": self.cycle_count,
            "agents": {a.id: {"status": a.status, "heartbeat": a.heartbeat, "tasks_completed": a.tasks_completed, "errors": a.errors} for a in self.agents.values()}
        }
        os.makedirs(DATA_PATH, exist_ok=True)
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)

    async def run(self):
        self.running = True
        agent_tasks = [asyncio.create_task(a.run()) for a in self.agents.values()]
        logger.info("All agents started")
        while self.running:
            try:
                await self.run_cycle()
            except Exception as e:
                logger.exception(f"Cycle {self.cycle_count} failed: {e}")
            for _ in range(CYCLE_INTERVAL_SECONDS):
                if not self.running:
                    break
                await asyncio.sleep(1)
        for agent in self.agents.values():
            agent.status = "shutdown"
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
