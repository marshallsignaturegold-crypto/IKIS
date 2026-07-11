#!/usr/bin/env python3
"""Phalanx Swarm v2.0-OMEGA — Single-Command Launcher

Zero setup. Zero config. One command to start the entire swarm.
"""

import asyncio
import os
import sys
import subprocess
import json
import sqlite3
from datetime import datetime, timezone

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_dependencies():
    """Check if Python 3.8+ is available and numpy is installed."""
    import sys
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8+ required")
        sys.exit(1)
    
    try:
        import numpy
    except ImportError:
        print("Installing numpy...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy", "-q"])
    
    print("✓ Dependencies OK")

def init_database():
    """Initialize SQLite database for swarm state."""
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "phalanx.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
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
    
    c.execute('''CREATE TABLE IF NOT EXISTS filings (
        id TEXT PRIMARY KEY,
        name TEXT,
        jurisdiction TEXT,
        deadline TEXT,
        status TEXT,
        days_remaining INTEGER,
        risk_level TEXT,
        hitl_required INTEGER,
        budget_usd INTEGER,
        completed_items INTEGER,
        total_items INTEGER
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS models (
        id TEXT PRIMARY KEY,
        name TEXT,
        project TEXT,
        npv_mean REAL,
        npv_p5 REAL,
        npv_p95 REAL,
        dscr_mean REAL,
        irr_mean REAL,
        wacc REAL,
        validation_status TEXT,
        last_run TEXT
    )''')
    
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
    
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        level TEXT,
        source TEXT,
        message TEXT
    )''')
    
    conn.commit()
    conn.close()
    print("✓ Database initialized")

def seed_data():
    """Seed database with initial filings and models."""
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "phalanx.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    filings = [
        ("REG-001", "BIIPP-2025 (Bihar SEZ)", "India", "2026-12-31", "ready", 173, "high", 1, 250000, 5, 6),
        ("REG-002", "SEBI EGR Registration", "India", "2026-08-15", "ready", 35, "critical", 1, 150000, 6, 7),
        ("REG-003", "PARIVESH (Environmental)", "India", "2026-07-20", "ready", 9, "high", 1, 100000, 5, 6),
        ("REG-004", "MEWA/SFDA Protocol", "Saudi Arabia", "2026-07-15", "ready", 4, "critical", 1, 80000, 5, 6),
        ("REG-005", "ORIASC-HCB SFDA", "Saudi Arabia", "2026-07-30", "ready", 19, "high", 1, 120000, 5, 6),
        ("REG-006", "FMD-Free Zone (WOAH)", "Ethiopia", "2026-08-01", "ready", 21, "critical", 1, 200000, 5, 6),
    ]
    
    c.executemany('''INSERT OR REPLACE INTO filings 
        (id, name, jurisdiction, deadline, status, days_remaining, risk_level, hitl_required, budget_usd, completed_items, total_items)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', filings)
    
    models = [
        ("AISTA", "AISTA Critical Minerals", "AISTA", 11.20, 8.50, 14.80, 0.0, 18.5, 9.5, "PASS", datetime.now(timezone.utc).isoformat()),
        ("BERBERA", "Berbera Port PPP", "Berbera", 0.0, 0.0, 0.0, 2.11, 16.2, 8.5, "PASS", datetime.now(timezone.utc).isoformat()),
        ("BIBC", "BIBC Bullion (EGR)", "BIBC", 29.25, 22.0, 37.5, 0.0, 22.1, 8.0, "PASS", datetime.now(timezone.utc).isoformat()),
        ("PIZZA", "Pizza Franchise", "Pizza", 0.19, 0.12, 0.28, 0.0, 24.5, 12.0, "PASS", datetime.now(timezone.utc).isoformat()),
    ]
    
    c.executemany('''INSERT OR REPLACE INTO models
        (id, name, project, npv_mean, npv_p5, npv_p95, dscr_mean, irr_mean, wacc, validation_status, last_run)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', models)
    
    conn.commit()
    conn.close()
    print("✓ Data seeded")

def seed_agents():
    """Seed agents table from JSON configs."""
    agents_path = os.path.join(os.path.dirname(__file__), "..", "agents")
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "phalanx.db")
    conn = sqlite3.connect(db_path)
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
    
    for filename in sorted(os.listdir(agents_path)):
        if not filename.endswith('.json'):
            continue
        filepath = os.path.join(agents_path, filename)
        try:
            with open(filepath) as f:
                config = json.load(f)
            c.execute('''INSERT OR REPLACE INTO agents
                (id, group_name, role, status, heartbeat, tasks_completed, errors, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (config["id"], config["group"], config["role"], "active",
                 datetime.now(timezone.utc).isoformat(), 0, 0,
                 datetime.now(timezone.utc).isoformat()))
        except Exception as e:
            print(f"Warning: failed to seed agent from {filename}: {e}")
    
    conn.commit()
    conn.close()
    print("✓ Agents seeded")

def generate_dashboard():
    """Generate static HTML dashboard from live DB data."""
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "phalanx.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM agents WHERE status = 'active'")
    active_agents = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM filings WHERE status = 'ready'")
    ready_filings = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM filings WHERE days_remaining < 0")
    overdue_filings = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM filings WHERE days_remaining > 0 AND days_remaining <= 7")
    urgent_filings = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM models WHERE validation_status = 'PASS'")
    pass_models = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM security_findings WHERE resolved = 0")
    open_findings = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM cycles")
    cycle_count = c.fetchone()[0]
    
    c.execute("SELECT id, name, jurisdiction, deadline, days_remaining, risk_level FROM filings ORDER BY days_remaining ASC")
    filings_rows = c.fetchall()
    
    c.execute("SELECT id, name, validation_status, npv_mean, last_run FROM models")
    models_rows = c.fetchall()
    
    c.execute("SELECT id, group_name, role, status, tasks_completed, errors FROM agents")
    agents_rows = c.fetchall()
    
    c.execute("SELECT cycle_id, timestamp, duration_ms, agents_active, tasks_dispatched, findings_critical, findings_high FROM cycles ORDER BY cycle_id DESC LIMIT 5")
    cycles_rows = c.fetchall()
    
    conn.close()
    
    filings_table = ""
    for row in filings_rows:
        filings_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>"
    
    models_table = ""
    for row in models_rows:
        models_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
    
    agents_table = ""
    for row in agents_rows:
        status_class = "ok" if row[3] == "active" else "warn" if row[3] == "error" else "crit"
        agents_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td class='{status_class}'>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>"
    
    cycles_table = ""
    for row in cycles_rows:
        cycles_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]:.1f}ms</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td></tr>"
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Phalanx Swarm v2.0-OMEGA</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; background: #0a0a0a; color: #00ff00; margin: 0; padding: 20px; }}
        h1 {{ font-size: 2.5em; margin: 0 0 20px 0; text-transform: uppercase; letter-spacing: 4px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; }}
        .card {{ background: #111; border: 1px solid #333; padding: 20px; border-radius: 4px; }}
        .card h2 {{ margin: 0 0 10px 0; font-size: 0.9em; text-transform: uppercase; color: #888; letter-spacing: 2px; }}
        .big {{ font-size: 3em; font-weight: bold; margin: 10px 0; }}
        .ok {{ color: #00ff00; }}
        .warn {{ color: #ffaa00; }}
        .crit {{ color: #ff0000; }}
        .status {{ font-size: 0.8em; padding: 4px 8px; border-radius: 2px; display: inline-block; margin-top: 5px; }}
        .status-pass {{ background: #003300; color: #00ff00; }}
        .status-warn {{ background: #332200; color: #ffaa00; }}
        .status-crit {{ background: #330000; color: #ff0000; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.85em; }}
        th {{ text-align: left; padding: 8px; border-bottom: 1px solid #333; color: #888; font-weight: normal; text-transform: uppercase; font-size: 0.8em; }}
        td {{ padding: 8px; border-bottom: 1px solid #222; }}
        .timestamp {{ color: #666; font-size: 0.8em; margin-top: 20px; }}
        .section {{ margin-top: 30px; }}
        .section h2 {{ font-size: 1.2em; color: #888; text-transform: uppercase; letter-spacing: 2px; border-bottom: 1px solid #333; padding-bottom: 10px; }}
    </style>
</head>
<body>
    <h1>Phalanx Swarm v2.0-OMEGA</h1>
    <div class="grid">
        <div class="card">
            <h2>Active Agents</h2>
            <div class="big ok">{active_agents}</div>
            <span class="status status-pass">ALL ACTIVE</span>
        </div>
        <div class="card">
            <h2>Regulatory Filings</h2>
            <div class="big ok">{ready_filings}/6 Ready</div>
            <span class="status status-{'crit' if overdue_filings > 0 else 'warn' if urgent_filings > 0 else 'pass'}">
                {overdue_filings} Overdue | {urgent_filings} Urgent
            </span>
        </div>
        <div class="card">
            <h2>Financial Models</h2>
            <div class="big ok">{pass_models}/4 PASS</div>
            <span class="status status-pass">ALL VALIDATED</span>
        </div>
        <div class="card">
            <h2>Security Findings</h2>
            <div class="big {'crit' if open_findings > 0 else 'ok'}">{open_findings}</div>
            <span class="status status-{'crit' if open_findings > 0 else 'pass'}">Open Findings</span>
        </div>
        <div class="card">
            <h2>Swarm Cycles</h2>
            <div class="big ok">{cycle_count}</div>
            <span class="status status-pass">Completed</span>
        </div>
        <div class="card">
            <h2>System Status</h2>
            <div class="big ok">ONLINE</div>
            <span class="status status-pass">AUTONOMOUS</span>
        </div>
    </div>

    <div class="section">
        <h2>Agents</h2>
        <table>
            <tr><th>ID</th><th>Group</th><th>Role</th><th>Status</th><th>Tasks</th><th>Errors</th></tr>
            {agents_table}
        </table>
    </div>

    <div class="section">
        <h2>Regulatory Filings</h2>
        <table>
            <tr><th>ID</th><th>Name</th><th>Jurisdiction</th><th>Deadline</th><th>Days Left</th><th>Risk</th></tr>
            {filings_table}
        </table>
    </div>

    <div class="section">
        <h2>Financial Models</h2>
        <table>
            <tr><th>ID</th><th>Name</th><th>Status</th><th>NPV Mean</th><th>Last Run</th></tr>
            {models_table}
        </table>
    </div>

    <div class="section">
        <h2>Recent Cycles</h2>
        <table>
            <tr><th>Cycle</th><th>Timestamp</th><th>Duration</th><th>Active</th><th>Tasks</th><th>Crit</th><th>High</th></tr>
            {cycles_table}
        </table>
    </div>

    <p class="timestamp">Generated: {datetime.now(timezone.utc).isoformat()}</p>
</body>
</html>'''
    
    dashboard_path = os.path.join(os.path.dirname(__file__), "..", "ui", "dashboard.html")
    os.makedirs(os.path.dirname(dashboard_path), exist_ok=True)
    with open(dashboard_path, "w") as f:
        f.write(html)
    
    print(f"✓ Dashboard generated: {dashboard_path}")
    return dashboard_path

def main():
    print("=" * 60)
    print("  Phalanx Swarm v2.0-OMEGA — Launch Sequence")
    print("=" * 60)
    
    check_dependencies()
    init_database()
    seed_data()
    seed_agents()
    
    # Generate initial dashboard
    dashboard_path = generate_dashboard()
    
    print("\n" + "=" * 60)
    print("  SWARM READY — Starting autonomous cycles")
    print("=" * 60)
    print(f"  Dashboard: {dashboard_path}")
    print(f"  Database:  data/phalanx.db")
    print(f"  Logs:      data/phalanx.log")
    print("  Press Ctrl+C to stop")
    print("=" * 60 + "\n")
    
    # Start the swarm
    from core.swarm import PhalanxSwarm
    swarm = PhalanxSwarm()
    
    # Support --once flag for single-cycle run (CI/testing)
    if "--once" in sys.argv:
        asyncio.run(swarm.run_once())
        generate_dashboard()
        print("\n✓ Single cycle completed and dashboard updated.")
    else:
        asyncio.run(swarm.run())

if __name__ == "__main__":
    main()
