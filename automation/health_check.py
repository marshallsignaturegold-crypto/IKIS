#!/usr/bin/env python3
"""IKIS Repository Health Check"""
import re, os, sys
from datetime import datetime, timedelta
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent

def check_metadata_completeness():
    issues = []
    for md_file in REPO_ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        content = md_file.read_text()
        if not content.startswith("---"):
            issues.append(f"Missing metadata: {md_file.relative_to(REPO_ROOT)}")
            continue
        try:
            _, yaml_part, _ = content.split("---", 2)
            metadata = yaml.safe_load(yaml_part)
            for field in ["artifact_id", "type", "title", "status", "confidence", "authors", "owner", "created_date", "provenance", "governance"]:
                if field not in metadata:
                    issues.append(f"Missing '{field}' in {md_file.relative_to(REPO_ROOT)}")
        except Exception as e:
            issues.append(f"Parse error: {md_file.relative_to(REPO_ROOT)}: {e}")
    return issues

def check_link_integrity():
    issues = []
    md_files = list(REPO_ROOT.rglob("*.md"))
    all_paths = {f.relative_to(REPO_ROOT).as_posix() for f in md_files}
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for md_file in md_files:
        content = md_file.read_text()
        for match in link_pattern.finditer(content):
            text, target = match.groups()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_dir = md_file.relative_to(REPO_ROOT).parent
            target_path = (file_dir / target).resolve()
            try:
                target_rel = target_path.relative_to(REPO_ROOT.resolve()).as_posix()
                if target_rel not in all_paths:
                    issues.append(f"Broken link: {md_file.relative_to(REPO_ROOT)} -> {target}")
            except ValueError:
                issues.append(f"Broken link: {md_file.relative_to(REPO_ROOT)} -> {target}")
    return issues

def check_stale_artifacts():
    issues = []
    now = datetime.now()
    for md_file in REPO_ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        content = md_file.read_text()
        if not content.startswith("---"):
            continue
        try:
            _, yaml_part, _ = content.split("---", 2)
            metadata = yaml.safe_load(yaml_part)
            if not metadata or "last_reviewed" not in metadata or not metadata["last_reviewed"]:
                continue
            review_cycle = metadata.get("review_cycle_months", 6)
            review_date = datetime.strptime(metadata["last_reviewed"], "%Y-%m-%d")
            due_date = review_date + timedelta(days=30 * review_cycle)
            if now > due_date:
                days_overdue = (now - due_date).days
                issues.append(f"Stale ({days_overdue}d overdue): {md_file.relative_to(REPO_ROOT)}")
        except Exception:
            continue
    return issues

def main():
    print("=" * 60)
    print("IKIS Repository Health Check")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)
    metadata_issues = check_metadata_completeness()
    print(f"\n[1/3] Metadata issues: {len(metadata_issues)}")
    for issue in metadata_issues[:10]:
        print(f"  - {issue}")
    link_issues = check_link_integrity()
    print(f"\n[2/3] Link issues: {len(link_issues)}")
    for issue in link_issues[:10]:
        print(f"  - {issue}")
    stale_issues = check_stale_artifacts()
    print(f"\n[3/3] Stale artifacts: {len(stale_issues)}")
    for issue in stale_issues[:10]:
        print(f"  - {issue}")
    total = len(metadata_issues) + len(link_issues) + len(stale_issues)
    print(f"\nTOTAL: {total} issues")
    return 0 if total == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
