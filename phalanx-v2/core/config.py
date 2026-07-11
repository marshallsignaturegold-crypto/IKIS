"""Phalanx Swarm v2.0-OMEGA — Zero-Cost Configuration"""

import os
from dataclasses import dataclass, field
from typing import Dict, List

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, "data")
AGENTS_PATH = os.path.join(BASE_PATH, "agents")
REPORTS_PATH = os.path.join(BASE_PATH, "reports")

PHALANX_GROUPS = {
    "alpha": {"role": "Core Orchestration", "count": 4, "priority": 1},
    "beta": {"role": "Financial Modeling", "count": 4, "priority": 1},
    "gamma": {"role": "Compliance & Regulatory", "count": 4, "priority": 1},
    "delta": {"role": "Infrastructure & DevOps", "count": 4, "priority": 2},
    "epsilon": {"role": "Security & Monitoring", "count": 4, "priority": 2},
    "zeta": {"role": "ETL & Knowledge Graph", "count": 4, "priority": 2},
    "eta": {"role": "HITL Coordination", "count": 3, "priority": 3},
    "omega": {"role": "Disaster Recovery", "count": 3, "priority": 3},
}

CYCLE_INTERVAL_SECONDS = 300
HEARTBEAT_TIMEOUT_SECONDS = 60

REGULATORY_FILINGS = [
    {"id": "REG-001", "name": "BIIPP-2025 (Bihar SEZ)", "jurisdiction": "India", "deadline": "2026-12-31", "status": "ready", "budget_usd": 250000},
    {"id": "REG-002", "name": "SEBI EGR Registration", "jurisdiction": "India", "deadline": "2026-08-15", "status": "ready", "budget_usd": 150000},
    {"id": "REG-003", "name": "PARIVESH (Environmental)", "jurisdiction": "India", "deadline": "2026-07-20", "status": "ready", "budget_usd": 100000},
    {"id": "REG-004", "name": "MEWA/SFDA Protocol", "jurisdiction": "Saudi Arabia", "deadline": "2026-07-15", "status": "ready", "budget_usd": 80000},
    {"id": "REG-005", "name": "ORIASC-HCB SFDA", "jurisdiction": "Saudi Arabia", "deadline": "2026-07-30", "status": "ready", "budget_usd": 120000},
    {"id": "REG-006", "name": "FMD-Free Zone (WOAH)", "jurisdiction": "Ethiopia", "deadline": "2026-08-01", "status": "ready", "budget_usd": 200000},
]

FINANCIAL_MODELS = [
    {"id": "AISTA", "name": "AISTA Critical Minerals", "npv_billions": 11.20, "status": "pass"},
    {"id": "BERBERA", "name": "Berbera Port PPP", "dscr": 2.11, "status": "pass"},
    {"id": "BIBC", "name": "BIBC Bullion (EGR)", "npv_billions": 29.25, "status": "pass"},
    {"id": "PIZZA", "name": "Pizza Franchise", "npv_billions": 0.19, "status": "pass"},
]
