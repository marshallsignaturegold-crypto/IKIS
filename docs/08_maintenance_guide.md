# 08 — Maintenance Guide

> **Operational maintenance procedures for IKIS maintainers.**

---

## 1. Routine Maintenance Tasks

### Weekly

| Task | Tool |
|------|------|
| Review open PRs | GitHub UI |
| Run health check | `automation/health_check.py` |

### Monthly

| Task | Tool |
|------|------|
| Build search index | `automation/index_builder.py` |
| Review stale artifacts | `automation/metadata_verifier.py` |

### Quarterly

| Task | Tool |
|------|------|
| Full validation | All automation scripts |
| Governance review | Manual |
| Archive outdated content | Manual |

## 2. Health Check Procedure

```bash
pip install -r automation/requirements.txt
python automation/health_check.py
```

Reports on: schema compliance, metadata completeness, link integrity, stale artifacts.

## 3. Handling Issues

### Schema Violations
1. Identify violating artifacts
2. Notify authors
3. Set deadline for correction

### Stale Artifacts
1. Identify overdue artifacts
2. Notify owners
3. Owner reviews and updates, deprecates, or archives

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-008*  
*Owner: marshallwmorrison*
