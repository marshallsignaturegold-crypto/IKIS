# 06 — Governance Framework

> **Ownership, review, approval, escalation, and lifecycle governance for IKIS.**

---

## 1. Governance Principles

IKIS governance is designed to be:
- **Lightweight enough** to support real use
- **Strong enough** to preserve trust and traceability
- **Transparent** — all decisions documented
- **Accountable** — every artifact has an owner

## 2. Ownership Model

Every artifact has a single owner responsible for lifecycle management, content accuracy, and responding to review comments.

## 3. Review Process

### Review Types

| Type | Description |
|------|-------------|
| Peer review | Review by another contributor |
| Expert review | Review by domain expert |
| Leadership review | Review by SSS leadership |
| Legal review | Review by legal counsel |
| Automated review | Automated validation |

### Review Workflow

```
Author submits → Reviewer assigned → Review conducted →
  ├─ Approve → Validated
  └─ Request changes → Author revises → Resubmit
```

## 4. Approval Levels

| Level | Authority | Applies To |
|-------|-----------|------------|
| L1 — Automated | CI/CD | All submissions |
| L2 — Peer | Any contributor | Knowledge entries |
| L3 — Expert | Domain expert | Specifications |
| L4 — Leadership | SSS leadership | Initiatives |
| L5 — Legal | Legal counsel | SSS-facing documents |

## 5. Related Documentation

- `governance/ownership_matrix.md`
- `governance/review_cadence.md`
- `governance/escalation_paths.md`

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-006*  
*Owner: marshallwmorrison*
