#!/usr/bin/env python3
"""
IKIS Terminology Enforcement Engine
Scans all markdown, YAML, and JSON files for deprecated labels and prohibited phrases.
Fails CI if violations found; suggests approved replacements via PR comments.

Usage: python terminology_enforcer.py [--fix] [--comment]
"""

import os
import re
import sys
import yaml
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Set

# ── Configuration ──────────────────────────────────────────────────────────

DEPRECATED_PATTERNS = {
    # Recursive corruption artifacts (must be caught first)
    r'Afro-Indian-American Strategic Minerals and Capital Corridor\s*\(Afro-Indian-American Strategic Trade Alliance\s*\(Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)\)\s*Corridor\)': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Trade Alliance\s*\(Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)\)\s*Corridor': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Minerals and Capital Corridor\s*\(Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)\s*Corridor\)': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)\s*Corridor\s*\(Afro-Indian-American Strategic': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Minerals and Capital Corridor\s*\(AIA-SMCC\)': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)\s*Corridor\s*\(Afro-Indian-American Strategic Minerals and Capital Corridor\)': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    
    # Standard deprecated patterns
    r'AIA-SMCC': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Minerals & Capital Corridor\s*\(AIA-SMCC\)': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Minerals & Capital Corridor': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)\s*Corridor': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    r'Afro-Indian-American Strategic Trade Alliance\s*\(AISTA\)': 'AISTA (African Infrastructure & SafeTrade Alliance / Corridor)',
    
    # Prohibited / high-risk phrases
    r'(?i)\bsovereign mandate\b': 'private-sector-led government interface',
    r'(?i)\btreaty-level platform\b': 'public-private partnership framework',
    r'(?i)\bofficial government-to-government channel\b': 'private-sector-led government interface',
    r'(?i)\blicensed settlement rail\b': 'settlement-support framework',
    r'(?i)\bbanking rail\b': 'treasury-administration framework',
    r'(?i)\bregulated settlement engine\b': 'settlement-support documentation system',
    r'(?i)\bsovereign guarantee\b': 'risk-mitigation structure (subject to approval)',
    r'(?i)\bDFI-backed\b': 'DFI-eligible (subject to approval)',
    r'(?i)\bfully insured\b': 'insurance review (subject to placement)',
    r'(?i)\bBasel III eligible\b': 'institutional standards-aligned (not certified)',
    r'(?i)\bfrictionless settlement\b': 'streamlined settlement-support workflow',
    r'(?i)\bstablecoin\b': 'digital asset support protocol (DASP) — not a token',
    r'(?i)\bsettlement coin\b': 'settlement-support record (not a payment instrument)',
    r'(?i)\btokenized security\b': 'digital evidence record (not a security)',
    
    # Common errors
    r'(?i)\bSomalian government\b': 'Government of Somaliland',
    r'(?i)\bSomalian\s+(?!Somaliland)': 'Somaliland',
}

APPROVED_SHORTFORMS = {
    'AISTA': 'African Infrastructure & SafeTrade Alliance / Corridor',
    'SSTP': 'Sovereign SafeTrade Program',
    'SSTLC': 'Somaliland SafeTrade & Logistics Center',
    'BIBC': 'Bihar Integrated Bullion Complex',
    'DASP': 'Digital Asset Support Protocol',
    'SSS': 'Signature Sovereign Solutions, LLC',
    'BIBC': 'Bihar Integrated Bullion Complex',
}

SCAN_EXTENSIONS = {'.md', '.yml', '.yaml', '.json', '.mdx', '.rst'}
SKIP_DIRS = {'.git', 'node_modules', '.github', '__pycache__', 'venv', '.env'}

# ── Core Functions ─────────────────────────────────────────────────────────

def find_files(root: Path) -> List[Path]:
    """Recursively find all scannable files under root."""
    files = []
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in SCAN_EXTENSIONS:
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            files.append(path)
    return files


def scan_file(filepath: Path) -> List[Tuple[int, str, str, str]]:
    """
    Scan a single file for deprecated patterns.
    Returns list of (line_number, line_content, matched_pattern, replacement).
    """
    violations = []
    try:
        content = filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return violations
    
    lines = content.split('\n')
    for line_num, line in enumerate(lines, start=1):
        for pattern, replacement in DEPRECATED_PATTERNS.items():
            if re.search(pattern, line, re.IGNORECASE):
                violations.append((line_num, line.strip(), pattern, replacement))
    return violations


def generate_report(violations_by_file: Dict[Path, List[Tuple]]) -> str:
    """Generate a human-readable violation report."""
    if not violations_by_file:
        return "✅ No terminology violations found. All files use approved language."
    
    lines = []
    lines.append("# Terminology Enforcement Report")
    lines.append(f"**Total violations:** {sum(len(v) for v in violations_by_file.values())}")
    lines.append(f"**Files affected:** {len(violations_by_file)}")
    lines.append("")
    
    for filepath, violations in sorted(violations_by_file.items()):
        lines.append(f"## {filepath}")
        for line_num, line_content, pattern, replacement in violations:
            lines.append(f"- **Line {line_num}:** `{line_content[:80]}`")
            lines.append(f"  - Match: `{pattern[:60]}`")
            lines.append(f"  - Suggest: *{replacement}*")
            lines.append("")
    
    return "\n".join(lines)


def fix_file(filepath: Path, violations: List[Tuple]) -> int:
    """Apply auto-fixes to a file. Returns count of replacements made."""
    content = filepath.read_text(encoding='utf-8')
    count = 0
    for _, _, pattern, replacement in violations:
        new_content, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if n > 0:
            content = new_content
            count += n
    if count > 0:
        filepath.write_text(content, encoding='utf-8')
    return count


def generate_pr_comment(violations_by_file: Dict[Path, List[Tuple]]) -> str:
    """Generate a GitHub PR comment with violation summary."""
    lines = ["## 🚨 Terminology Enforcement Results", ""]
    
    total = sum(len(v) for v in violations_by_file.values())
    if total == 0:
        lines.append("✅ **All terminology checks passed.** No deprecated or prohibited language found.")
        return "\n".join(lines)
    
    lines.append(f"**{total} violation(s)** found across {len(violations_by_file)} file(s).")
    lines.append("")
    lines.append("Please review and update the following:")
    lines.append("")
    
    for filepath, violations in sorted(violations_by_file.items())[:10]:
        lines.append(f"### `{filepath}` ({len(violations)} issue(s))")
        for line_num, line_content, pattern, replacement in violations[:3]:
            lines.append(f"- Line {line_num}: Replace with *{replacement}*")
        if len(violations) > 3:
            lines.append(f"- ... and {len(violations) - 3} more")
        lines.append("")
    
    if len(violations_by_file) > 10:
        lines.append(f"*... and {len(violations_by_file) - 10} more files*")
    
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='IKIS Terminology Enforcement Engine')
    parser.add_argument('--root', default='.', help='Root directory to scan')
    parser.add_argument('--fix', action='store_true', help='Auto-fix violations in place')
    parser.add_argument('--comment', action='store_true', help='Output PR comment format')
    parser.add_argument('--output', type=Path, help='Write report to file')
    parser.add_argument('--fail-on-violation', action='store_true', help='Exit non-zero if violations found')
    args = parser.parse_args()
    
    root = Path(args.root).resolve()
    files = find_files(root)
    
    violations_by_file: Dict[Path, List[Tuple]] = {}
    total_fixes = 0
    
    for filepath in files:
        violations = scan_file(filepath)
        if violations:
            relative = filepath.relative_to(root)
            violations_by_file[relative] = violations
            if args.fix:
                fixes = fix_file(filepath, violations)
                total_fixes += fixes
                print(f"  Fixed {fixes} violation(s) in {relative}")
    
    report = generate_report(violations_by_file)
    
    if args.comment:
        print(generate_pr_comment(violations_by_file))
    else:
        print(report)
    
    if args.output:
        args.output.write_text(report, encoding='utf-8')
        print(f"\nReport written to: {args.output}")
    
    if args.fix and total_fixes > 0:
        print(f"\n🔧 Total auto-fixes applied: {total_fixes}")
    
    if args.fail_on_violation and violations_by_file:
        sys.exit(1)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
