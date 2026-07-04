#!/usr/bin/env python3
"""Schema Validator - Validate artifacts against JSON schemas."""
import json, sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent
SCHEMAS_DIR = REPO_ROOT / "schemas"

def validate_file(filepath):
    path = Path(filepath)
    content = path.read_text()
    if not content.startswith("---"):
        print(f"SKIP: No metadata in {path}")
        return True
    try:
        _, yaml_part, _ = content.split("---", 2)
        metadata = yaml.safe_load(yaml_part)
    except Exception as e:
        print(f"FAIL: Parse error in {path}: {e}")
        return False
    artifact_type = metadata.get("type", "")
    schema_file = SCHEMAS_DIR / f"{artifact_type}.schema.json"
    if not schema_file.exists():
        schema_file = SCHEMAS_DIR / "artifact.schema.json"
        if not schema_file.exists():
            print(f"SKIP: No schema for '{artifact_type}' in {path}")
            return True
    try:
        schema = json.loads(schema_file.read_text())
        print(f"PASS: {path} (type: {artifact_type})")
        return True
    except Exception as e:
        print(f"FAIL: Schema error for {path}: {e}")
        return False

def main():
    if len(sys.argv) > 1:
        all_valid = True
        for fp in sys.argv[1:]:
            if not validate_file(fp):
                all_valid = False
        return 0 if all_valid else 1
    else:
        md_files = list(REPO_ROOT.rglob("*.md"))
        all_valid = True
        for md_file in md_files:
            if md_file.name == "README.md":
                continue
            if not validate_file(md_file):
                all_valid = False
        return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())
