#!/usr/bin/env python3
"""
IKIS Contradiction Detection System
Cross-references knowledge base files to detect conflicting factual assertions.
Flags contradictions and routes them to the contradiction register.

Usage: python contradiction_detector.py [--knowledge-dir PATH] [--register PATH]
"""

import os
import re
import json
import yaml
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple, Optional
from datetime import datetime

# ── Configuration ──────────────────────────────────────────────────────────

CONTRADICTION_PATTERNS = [
    # Revenue / financial figures that differ across files
    (r'(?i)(?:revenue|corridor revenue)\s*(?:of|:)?\s*\$?([0-9.,]+)\s*[Mm]', 'revenue'),
    (r'(?i)(?:capital stack|total capital)\s*(?:of|:)?\s*\$?([0-9.,]+)\s*[MmB]', 'capital_stack'),
    (r'(?i)(?:irr|internal rate of return)\s*(?:of|:)?\s*([0-9.,]+)\s*%', 'irr'),
    (r'(?i)(?:moic|multiple)\s*(?:of|:)?\s*([0-9.,]+)\s*x', 'moic'),
    (r'(?i)(?:ebitda)\s*(?:of|:)?\s*\$?([0-9.,]+)\s*[Mm]', 'ebitda'),
    
    # Engagement status contradictions
    (r'(?i)(?:somaliland|bihar)\s*(?:status|engagement).{0,30}(active engagement|loi secured|approved|operational)', 'engagement_status'),
    (r'(?i)(?:corleone|don vito).{0,30}(proposed|active|incorporated|not incorporated)', 'corleone_status'),
    
    # Entity status contradictions
    (r'(?i)(?:sss, llc|signature sovereign).{0,30}(florida registered|delaware|active|proposed)', 'sss_registration'),
    (r'(?i)(?:aista|corridor).{0,30}(conceptual|active|proposed|approved)', 'aista_status'),
    
    # Personnel / role contradictions
    (r'(?i)(?:christopher konopka|marshall morrison).{0,30}(ceo|coo|co-founder|founder)', 'personnel_role'),
]

TOLERANCE_RANGES = {
    'revenue': 0.10,      # 10% variance allowed
    'capital_stack': 0.05, # 5% variance allowed
    'irr': 0.05,          # 5 percentage points
    'moic': 0.10,         # 10% variance
    'ebitda': 0.15,       # 15% variance
}

# ── Data Structures ────────────────────────────────────────────────────────

@dataclass
class FactAssertion:
    file: str
    line: int
    context: str
    fact_type: str
    value: str
    raw_match: str

@dataclass
class Contradiction:
    fact_type: str
    assertion_a: FactAssertion
    assertion_b: FactAssertion
    severity: str  # 'critical', 'warning', 'info'
    explanation: str
    detected_at: str


# ── Core Functions ─────────────────────────────────────────────────────────

def extract_facts(filepath: Path) -> List[FactAssertion]:
    """Extract all factual assertions from a knowledge base file."""
    facts = []
    try:
        content = filepath.read_text(encoding='utf-8')
    except (UnicodeDecodeError, IOError):
        return facts
    
    lines = content.split('\n')
    for line_num, line in enumerate(lines, start=1):
        for pattern, fact_type in CONTRADICTION_PATTERNS:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                facts.append(FactAssertion(
                    file=str(filepath),
                    line=line_num,
                    context=line.strip()[:200],
                    fact_type=fact_type,
                    value=match.group(1).replace(',', '').replace('.', '') if len(match.groups()) > 0 else match.group(0),
                    raw_match=match.group(0)
                ))
    return facts


def facts_conflict(a: FactAssertion, b: FactAssertion) -> Tuple[bool, str]:
    """Determine if two facts of the same type contradict each other."""
    if a.fact_type != b.fact_type:
        return False, ""
    
    # For numeric facts, check within tolerance
    if a.fact_type in TOLERANCE_RANGES:
        try:
            val_a = float(a.value)
            val_b = float(b.value)
            tolerance = TOLERANCE_RANGES[a.fact_type]
            
            # For percentages (IRR), absolute difference
            if a.fact_type == 'irr':
                diff = abs(val_a - val_b)
                if diff > tolerance:
                    return True, f"IRR values differ by {diff:.1f}% (tolerance: {tolerance*100:.0f}pp)"
                return False, ""
            
            # For other numeric, relative difference
            if val_a == 0 and val_b == 0:
                return False, ""
            avg = (abs(val_a) + abs(val_b)) / 2
            rel_diff = abs(val_a - val_b) / avg if avg > 0 else 0
            
            if rel_diff > tolerance:
                return True, f"Values differ by {rel_diff*100:.1f}% (tolerance: {tolerance*100:.0f}%)"
            return False, ""
        except ValueError:
            pass
    
    # For string-based facts, exact match required
    norm_a = re.sub(r'[^a-z0-9]', '', a.value.lower())
    norm_b = re.sub(r'[^a-z0-9]', '', b.value.lower())
    
    if norm_a != norm_b and len(norm_a) > 3 and len(norm_b) > 3:
        return True, f"Status assertions differ: '{a.value}' vs '{b.value}'"
    
    return False, ""


def find_contradictions(all_facts: List[FactAssertion]) -> List[Contradiction]:
    """Find all contradictions across a collection of fact assertions."""
    contradictions = []
    
    # Group by fact type
    by_type: Dict[str, List[FactAssertion]] = {}
    for fact in all_facts:
        by_type.setdefault(fact.fact_type, []).append(fact)
    
    for fact_type, facts in by_type.items():
        for i in range(len(facts)):
            for j in range(i + 1, len(facts)):
                a, b = facts[i], facts[j]
                
                # Skip if same file (internal contradictions are different)
                if a.file == b.file:
                    continue
                
                conflicts, explanation = facts_conflict(a, b)
                if conflicts:
                    severity = 'critical' if fact_type in ('revenue', 'capital_stack', 'irr') else 'warning'
                    contradictions.append(Contradiction(
                        fact_type=fact_type,
                        assertion_a=a,
                        assertion_b=b,
                        severity=severity,
                        explanation=explanation,
                        detected_at=datetime.utcnow().isoformat() + 'Z'
                    ))
    
    return contradictions


def generate_register(contradictions: List[Contradiction]) -> str:
    """Generate a markdown contradiction register."""
    lines = []
    lines.append("# Contradiction Register")
    lines.append(f"**Generated:** {datetime.utcnow().isoformat()}Z")
    lines.append(f"**Total contradictions detected:** {len(contradictions)}")
    lines.append("")
    
    if not contradictions:
        lines.append("✅ **No contradictions detected.** All knowledge base files are consistent.")
        return "\n".join(lines)
    
    # Group by severity
    by_severity: Dict[str, List[Contradiction]] = {}
    for c in contradictions:
        by_severity.setdefault(c.severity, []).append(c)
    
    for severity in ['critical', 'warning', 'info']:
        if severity not in by_severity:
            continue
        lines.append(f"## {severity.upper()} ({len(by_severity[severity])})")
        for i, c in enumerate(by_severity[severity], 1):
            lines.append(f"### {c.fact_type} — Contradiction #{i}")
            lines.append(f"- **Explanation:** {c.explanation}")
            lines.append(f"- **File A:** `{c.assertion_a.file}` (line {c.assertion_a.line})")
            lines.append(f"  - Context: `{c.assertion_a.context[:100]}`")
            lines.append(f"- **File B:** `{c.assertion_b.file}` (line {c.assertion_b.line})")
            lines.append(f"  - Context: `{c.assertion_b.context[:100]}`")
            lines.append(f"- **Detected:** {c.detected_at}")
            lines.append("")
    
    return "\n".join(lines)


def update_register_file(register_path: Path, contradictions: List[Contradiction]):
    """Write or update the contradiction register file."""
    content = generate_register(contradictions)
    register_path.write_text(content, encoding='utf-8')


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='IKIS Contradiction Detection System')
    parser.add_argument('--knowledge-dir', type=Path, default=Path('knowledge/validated'),
                        help='Directory containing knowledge base files')
    parser.add_argument('--register', type=Path, default=Path('data_governance/contradiction_register.md'),
                        help='Path to write contradiction register')
    parser.add_argument('--fail-on-critical', action='store_true',
                        help='Exit non-zero if critical contradictions found')
    args = parser.parse_args()
    
    if not args.knowledge_dir.exists():
        print(f"Knowledge directory not found: {args.knowledge_dir}")
        sys.exit(0)
    
    # Collect all facts
    all_facts: List[FactAssertion] = []
    files_scanned = 0
    
    for filepath in args.knowledge_dir.rglob('*'):
        if filepath.is_file() and filepath.suffix in {'.md', '.json', '.yml', '.yaml'}:
            facts = extract_facts(filepath)
            all_facts.extend(facts)
            files_scanned += 1
    
    print(f"Scanned {files_scanned} files, extracted {len(all_facts)} fact assertions")
    
    # Find contradictions
    contradictions = find_contradictions(all_facts)
    critical = sum(1 for c in contradictions if c.severity == 'critical')
    warning = sum(1 for c in contradictions if c.severity == 'warning')
    
    print(f"Contradictions: {critical} critical, {warning} warning, "
          f"{len(contradictions) - critical - warning} info")
    
    # Write register
    args.register.parent.mkdir(parents=True, exist_ok=True)
    update_register_file(args.register, contradictions)
    print(f"Register written to: {args.register}")
    
    if args.fail_on_critical and critical > 0:
        sys.exit(1)
    
    sys.exit(0)


if __name__ == '__main__':
    import sys
    main()
