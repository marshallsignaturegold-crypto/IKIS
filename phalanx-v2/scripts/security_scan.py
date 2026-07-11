"""Phalanx Swarm v2.0-OMEGA — Security Scanner (Zero-External)

Pure Python file scanner. No Trivy, no Snyk, no API keys.
"""

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

class SecurityScanner:
    """7-layer security scanner using only Python stdlib."""
    
    SEVERITY_WEIGHTS = {"CRITICAL": 25, "HIGH": 10, "MEDIUM": 5, "LOW": 2, "INFO": 0}
    
    def __init__(self, target_path: str):
        self.target_path = Path(target_path)
        self.findings: List[Dict] = []
        self.layers_scanned: List[str] = []
    
    def _add_finding(self, severity: str, layer: str, rule: str, description: str, 
                     file_path: Optional[str] = None, line: Optional[int] = None,
                     remediation: Optional[str] = None):
        self.findings.append({
            "severity": severity,
            "layer": layer,
            "rule": rule,
            "description": description,
            "file": file_path,
            "line": line,
            "remediation": remediation,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })
    
    def scan_code(self):
        """Layer 1: Code integrity - scan for hardcoded secrets."""
        self.layers_scanned.append("code")
        
        patterns = [
            (r'password\s*[=:]\s*["\'][^"\']{3,}["\']', "Hardcoded password", "CRITICAL"),
            (r'api[_-]?key\s*[=:]\s*["\'][^"\']{10,}["\']', "Hardcoded API key", "CRITICAL"),
            (r'secret\s*[=:]\s*["\'][^"\']{10,}["\']', "Hardcoded secret", "CRITICAL"),
            (r'BEGIN\s+RSA\s+PRIVATE\s+KEY', "Embedded private key", "CRITICAL"),
            (r'BEGIN\s+OPENSSH\s+PRIVATE\s+KEY', "Embedded SSH key", "CRITICAL"),
            (r'BEGIN\s+CERTIFICATE', "Embedded certificate", "HIGH"),
        ]
        
        for root, _, files in os.walk(self.target_path):
            if any(skip in root for skip in ['.git', '__pycache__', '.archive', 'node_modules']):
                continue
            for file in files:
                if not file.endswith(('.py', '.js', '.ts', '.go', '.yaml', '.yml', '.json', '.tf', '.sh', '.md', '.txt')):
                    continue
                filepath = Path(root) / file
                try:
                    with open(filepath, 'r', errors='ignore') as f:
                        content = f.read()
                        for pattern, desc, sev in patterns:
                            for match in re.finditer(pattern, content, re.IGNORECASE):
                                line_num = content[:match.start()].count('\n') + 1
                                self._add_finding(sev, "code", "HARDCODED_SECRET", desc,
                                                str(filepath.relative_to(self.target_path)), line_num,
                                                "Use environment variables or secrets manager")
                except Exception:
                    pass
    
    def scan_configs(self):
        """Layer 2: Configuration security."""
        self.layers_scanned.append("config")
        
        config_patterns = [
            (r'allowPrivilegeEscalation:\s*true', "K8s privilege escalation enabled", "HIGH"),
            (r'runAsRoot:\s*true', "Container running as root", "HIGH"),
            (r'hostNetwork:\s*true', "Container using host network", "MEDIUM"),
            (r'hostPID:\s*true', "Container sharing host PID", "HIGH"),
            (r'0\.0\.0\.0/0', "Overly permissive CIDR", "MEDIUM"),
            (r'chmod\s+777', "Overly permissive file permissions", "MEDIUM"),
        ]
        
        for root, _, files in os.walk(self.target_path):
            if any(skip in root for skip in ['.git', '__pycache__']):
                continue
            for file in files:
                if not file.endswith(('.yaml', '.yml', '.tf', '.json', '.sh', '.py')):
                    continue
                filepath = Path(root) / file
                try:
                    with open(filepath, 'r', errors='ignore') as f:
                        content = f.read()
                        for pattern, desc, sev in config_patterns:
                            for match in re.finditer(pattern, content, re.IGNORECASE):
                                line_num = content[:match.start()].count('\n') + 1
                                self._add_finding(sev, "config", "INSECURE_CONFIGURATION", desc,
                                                str(filepath.relative_to(self.target_path)), line_num,
                                                "Apply principle of least privilege")
                except Exception:
                    pass
    
    def scan_secrets(self):
        """Layer 3: Secrets management."""
        self.layers_scanned.append("secrets")
        
        secret_files = ['.env', '.env.local', '.env.production', 'secrets.txt', 
                        'credentials.json', 'key.pem', 'id_rsa', 'token.txt']
        
        for secret_file in secret_files:
            filepath = self.target_path / secret_file
            if filepath.exists():
                self._add_finding("CRITICAL", "secrets", "UNENCRYPTED_SECRET_FILE",
                                  f"Unencrypted secrets file: {secret_file}",
                                  secret_file, None,
                                  "Remove from repo, add to .gitignore, use environment variables")
        
        # Check .gitignore exists and is comprehensive
        gitignore = self.target_path / ".gitignore"
        if not gitignore.exists():
            self._add_finding("MEDIUM", "secrets", "MISSING_GITIGNORE",
                              "No .gitignore file found",
                              None, None,
                              "Create .gitignore to prevent accidental secret commits")
    
    def scan_iam(self):
        """Layer 4: IAM and access control."""
        self.layers_scanned.append("iam")
        
        iam_patterns = [
            (r'"Action":\s*"\*"', "IAM wildcard action", "HIGH"),
            (r'"Resource":\s*"\*"', "IAM wildcard resource", "HIGH"),
            (r'Effect.*Allow.*\*.*\*', "Overly permissive IAM policy", "HIGH"),
        ]
        
        for root, _, files in os.walk(self.target_path):
            for file in files:
                if not file.endswith(('.json', '.yaml', '.yml')):
                    continue
                if 'iam' not in file.lower() and 'policy' not in file.lower():
                    continue
                filepath = Path(root) / file
                try:
                    with open(filepath, 'r', errors='ignore') as f:
                        content = f.read()
                        for pattern, desc, sev in iam_patterns:
                            if re.search(pattern, content, re.IGNORECASE):
                                self._add_finding(sev, "iam", "WILDCARD_PERMISSION", desc,
                                                str(filepath.relative_to(self.target_path)), None,
                                                "Scope to specific resources and actions")
                except Exception:
                    pass
    
    def scan_compliance(self):
        """Layer 5: Compliance documentation."""
        self.layers_scanned.append("compliance")
        
        required_docs = {
            'LICENSE': "License file",
            'SECURITY.md': "Security policy",
            'PRIVACY.md': "Privacy policy",
        }
        
        for doc, desc in required_docs.items():
            if not (self.target_path / doc).exists():
                self._add_finding("LOW", "compliance", "MISSING_DOCUMENTATION",
                                  f"Missing {desc}: {doc}",
                                  None, None,
                                  f"Add {doc} to repository")
    
    def calculate_score(self) -> float:
        """Calculate security score 0-100."""
        base = 100.0
        for finding in self.findings:
            base -= self.SEVERITY_WEIGHTS.get(finding["severity"], 0)
        return max(0.0, base)
    
    def run_quick_scan(self) -> Dict:
        """Run essential scans (code, secrets, configs)."""
        self.scan_code()
        self.scan_secrets()
        self.scan_configs()
        self.scan_iam()
        self.scan_compliance()
        
        score = self.calculate_score()
        passed = score >= 70 and not any(f["severity"] == "CRITICAL" for f in self.findings)
        
        return {
            "scan_id": hashlib.sha256(str(datetime.now(timezone.utc).timestamp()).encode()).hexdigest()[:16],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "target": str(self.target_path),
            "score": round(score, 1),
            "passed": passed,
            "layers_scanned": self.layers_scanned,
            "findings_count": len(self.findings),
            "findings": self.findings,
            "severity_counts": {
                "CRITICAL": sum(1 for f in self.findings if f["severity"] == "CRITICAL"),
                "HIGH": sum(1 for f in self.findings if f["severity"] == "HIGH"),
                "MEDIUM": sum(1 for f in self.findings if f["severity"] == "MEDIUM"),
                "LOW": sum(1 for f in self.findings if f["severity"] == "LOW"),
                "INFO": sum(1 for f in self.findings if f["severity"] == "INFO"),
            }
        }
