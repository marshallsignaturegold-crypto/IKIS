#!/usr/bin/env python3
"""Metadata Verifier - Verify markdown files have complete metadata blocks."""
import re, sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent

def verify_file(filepath):
    path = Path(filepath)
    content = path.read_text()
    if not content.startswith("---"):
        print(f"FAIL: No metadata block in {path}")
        return False
    try:
        _, yaml_part, _ = content.split("---", 2)
        metadata = yaml.safe_load(yaml_part)
    except Exception as e:
        print(f"FAIL: Parse error in {path}: {e}")
        return False
    if not metadata:
        print(f"FAIL: Empty metadata in {path}")
        return False
    required = ["artifact_id", "type", "title", "status", "confidence", "authors", "owner", "created_date", "provenance", "governance"]
    valid = True
    for field in required:
        if field not in metadata:
            print(f"FAIL: Missing '{field}' in {path}")
            valid = False
    if "artifact_id" in metadata:
        if not re.match(r"^IKIS-[A-Z]{3}-\d{4}-\d{3}$", metadata["artifact_id"]):
            print(f"FAIL: Invalid artifact_id format in {path}")
            valid = False
    if valid:
        print(f"PASS: {path}")
    return valid

def main():
    if len(sys.argv) > 1:
        all_valid = True
        for fp in sys.argv[1:]:
            if not verify_file(fp):
                all_valid = False
        return 0 if all_valid else 1
    else:
        md_files = list(REPO_ROOT.rglob("*.md"))
        all_valid = True
        checked = 0
        for md_file in md_files:
            if md_file.name == "README.md":
                continue
            checked += 1
            if not verify_file(md_file):
                all_valid = False
        print(f"\nChecked {checked} files")
        return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())
