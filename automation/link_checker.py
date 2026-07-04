#!/usr/bin/env python3
"""Link Checker - Verify internal links in markdown files."""
import re, sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def check_file(filepath):
    path = Path(filepath)
    content = path.read_text()
    all_paths = {f.relative_to(REPO_ROOT).as_posix() for f in REPO_ROOT.rglob("*.md")}
    issues = []
    for match in LINK_PATTERN.finditer(content):
        text, target = match.groups()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_dir = path.relative_to(REPO_ROOT).parent
        target_path = (file_dir / target).resolve()
        try:
            target_rel = target_path.relative_to(REPO_ROOT.resolve()).as_posix()
            if target_rel not in all_paths:
                issues.append(target)
        except ValueError:
            issues.append(target)
    if issues:
        print(f"FAIL: {path}")
        for issue in issues:
            print(f"  Broken link: {issue}")
        return False
    else:
        print(f"PASS: {path}")
        return True

def main():
    if len(sys.argv) > 1:
        all_valid = True
        for fp in sys.argv[1:]:
            if not check_file(fp):
                all_valid = False
        return 0 if all_valid else 1
    else:
        for md_file in REPO_ROOT.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            check_file(md_file)
        return 0

if __name__ == "__main__":
    sys.exit(main())
