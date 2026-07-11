"""Phalanx Swarm v2.0-OMEGA — Security Scanner (Zero-External)"""

import hashlib, json, os, re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

class SecurityScanner:
    SEVERITY_WEIGHTS = {"CRITICAL": 25, "HIGH": 10, "MEDIUM": 5, "LOW": 2, "INFO": 0}
    
    def __init__(self, target_path: str):
        self.target_path = Path(target_path)
        self.findings: List[Dict] = []
    
    def _add(self, sev, layer, rule, desc, file=None, line=None, rem=None):
        self.findings.append({"severity": sev, "layer": layer, "rule": rule, "description": desc, "file": file, "line": line, "remediation": rem, "timestamp": datetime.now(timezone.utc).isoformat()})
    
    def scan_code(self):
        patterns = [
            (r'password\s*[=:]\s*["\'][^"\']{3,}["\']', "Hardcoded password", "CRITICAL"),
            (r'api[_-]?key\s*[=:]\s*["\'][^"\']{10,}["\']', "Hardcoded API key", "CRITICAL"),
            (r'BEGIN\s+RSA\s+PRIVATE\s+KEY', "Embedded private key", "CRITICAL"),
        ]
        for root, _, files in os.walk(self.target_path):
            if any(s in root for s in ['.git', '__pycache__']): continue
            for f in files:
                if not f.endswith(('.py', '.js', '.yaml', '.json', '.tf', '.sh')): continue
                fp = Path(root) / f
                try:
                    with open(fp, 'r', errors='ignore') as fh:
                        content = fh.read()
                        for p, d, s in patterns:
                            for m in re.finditer(p, content, re.I):
                                self._add(s, "code", "HARDCODED_SECRET", d, str(fp.relative_to(self.target_path)), content[:m.start()].count('\n')+1, "Use env vars")
                except: pass
    
    def scan_configs(self):
        patterns = [
            (r'allowPrivilegeEscalation:\s*true', "K8s privilege escalation", "HIGH"),
            (r'runAsRoot:\s*true', "Container root", "HIGH"),
            (r'0\.0\.0\.0/0', "Overly permissive CIDR", "MEDIUM"),
        ]
        for root, _, files in os.walk(self.target_path):
            for f in files:
                if not f.endswith(('.yaml', '.tf', '.json')): continue
                fp = Path(root) / f
                try:
                    with open(fp, 'r', errors='ignore') as fh:
                        content = fh.read()
                        for p, d, s in patterns:
                            for m in re.finditer(p, content, re.I):
                                self._add(s, "config", "INSECURE", d, str(fp.relative_to(self.target_path)), content[:m.start()].count('\n')+1, "Least privilege")
                except: pass
    
    def scan_secrets(self):
        for sf in ['.env', 'secrets.txt', 'credentials.json', 'key.pem']:
            if (self.target_path / sf).exists():
                self._add("CRITICAL", "secrets", "UNENCRYPTED_FILE", f"Found: {sf}", sf, None, "Remove from repo")
    
    def calculate_score(self):
        base = 100.0
        for f in self.findings:
            base -= self.SEVERITY_WEIGHTS.get(f["severity"], 0)
        return max(0.0, base)
    
    def run_quick_scan(self):
        self.scan_code(); self.scan_secrets(); self.scan_configs()
        score = self.calculate_score()
        return {"scan_id": hashlib.sha256(str(datetime.now(timezone.utc).timestamp()).encode()).hexdigest()[:16], "timestamp": datetime.now(timezone.utc).isoformat(), "score": round(score, 1), "passed": score >= 70 and not any(f["severity"] == "CRITICAL" for f in self.findings), "findings": self.findings, "severity_counts": {s: sum(1 for f in self.findings if f["severity"] == s) for s in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]}}
