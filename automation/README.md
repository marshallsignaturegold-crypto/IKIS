# automation/ — Automation Scripts

Scripts for repository validation, quality assurance, and maintenance.

## Scripts

| Script | Purpose | Run |
|--------|---------|-----|
| `health_check.py` | Comprehensive repository health check | Weekly / On demand |
| `schema_validator.py` | Validate artifacts against JSON schemas | CI / On demand |
| `metadata_verifier.py` | Verify metadata completeness | CI / On demand |
| `link_checker.py` | Verify internal link integrity | CI / On demand |
| `index_builder.py` | Build search index | Monthly / On demand |

## Installation

```bash
pip install -r automation/requirements.txt
```
