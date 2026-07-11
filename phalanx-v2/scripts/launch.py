#!/usr/bin/env python3
"""Phalanx Swarm v2.0-OMEGA — Single-Command Launcher

Zero setup. Zero config. One command to start the entire swarm.
"""

import asyncio
import os
import sys
import subprocess
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_dependencies():
    import sys
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8+ required")
        sys.exit(1)
    try:
        import numpy
    except ImportError:
        print("Installing numpy...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy", "-q"])
    print("Dependencies OK")

def init_database():
    import sqlite3
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "phalanx.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS agents (id TEXT PRIMARY KEY, group_name TEXT, role TEXT, status TEXT, heartbeat TEXT, tasks_completed INTEGER DEFAULT 0, errors INTEGER DEFAULT 0, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS cycles (cycle_id INTEGER PRIMARY KEY, timestamp TEXT, duration_ms REAL, agents_active INTEGER, tasks_dispatched INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS filings (id TEXT PRIMARY KEY, name TEXT, jurisdiction TEXT, deadline TEXT, status TEXT, days_remaining INTEGER, risk_level TEXT, budget_usd INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS models (id TEXT PRIMARY KEY, name TEXT, npv_mean REAL, dscr_mean REAL, validation_status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS security_findings (id INTEGER PRIMARY KEY, severity TEXT, rule TEXT, file_path TEXT, timestamp TEXT, resolved INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()
    print("Database initialized")

def seed_data():
    import sqlite3
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "phalanx.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    filings = [
        ("REG-001", "BIIPP-2025", "India", "2026-12-31", "ready", 173, "high", 250000),
        ("REG-002", "SEBI EGR", "India", "2026-08-15", "ready", 35, "critical", 150000),
        ("REG-003", "PARIVESH", "India", "2026-07-20", "ready", 9, "high", 100000),
        ("REG-004", "MEWA/SFDA", "Saudi Arabia", "2026-07-15", "ready", 4, "critical", 80000),
        ("REG-005", "ORIASC-HCB", "Saudi Arabia", "2026-07-30", "ready", 19, "high", 120000),
        ("REG-006", "FMD-Free Zone", "Ethiopia", "2026-08-01", "ready", 21, "critical", 200000),
    ]
    c.executemany('INSERT OR REPLACE INTO filings VALUES (?,?,?,?,?,?,?,?)', filings)
    models = [
        ("AISTA", "AISTA Critical Minerals", 11.20, 0.0, "PASS"),
        ("BERBERA", "Berbera Port PPP", 0.0, 2.11, "PASS"),
        ("BIBC", "BIBC Bullion (EGR)", 29.25, 0.0, "PASS"),
        ("PIZZA", "Pizza Franchise", 0.19, 0.0, "PASS"),
    ]
    c.executemany('INSERT OR REPLACE INTO models VALUES (?,?,?,?,?)', models)
    conn.commit()
    conn.close()
    print("Data seeded")

def main():
    print("=" * 60)
    print("  Phalanx Swarm v2.0-OMEGA — Launch Sequence")
    print("=" * 60)
    check_dependencies()
    init_database()
    seed_data()
    print("\nSwarm ready. Starting autonomous cycles...")
    print("Press Ctrl+C to stop\n")
    from core.swarm import main as swarm_main
    asyncio.run(swarm_main())

if __name__ == "__main__":
    main()
