# 03 — Lifecycle Specification

> **Artifact lifecycle states, transition rules, and state-specific requirements.**

---

## 1. Lifecycle States

| State | Description | Terminal |
|-------|-----------|----------|
| **draft** | Initial creation, not yet reviewed | No |
| **under_review** | Under active review | No |
| **revision_requested** | Changes requested by reviewer | No |
| **validated** | Reviewed and approved | No |
| **deprecated** | Superseded by newer artifact | Yes |
| **archived** | Retained for historical reference | Yes |

## 2. Transition Rules

| From | To | Trigger |
|------|-----|---------|
| draft | under_review | Author submits for review |
| under_review | validated | Reviewer approves |
| under_review | revision_requested | Reviewer requests changes |
| revision_requested | under_review | Author resubmits |
| validated | deprecated | Newer artifact supersedes |
| validated | archived | Explicit archival decision |

## 3. State-Specific Requirements

### draft
- Metadata block complete
- Template structure followed
- Status: `draft`

### under_review
- All draft requirements met
- Reviewer assigned
- Status: `under_review`

### validated
- All reviewer comments addressed
- Schema validation passes
- Status: `validated`

### deprecated
- Newer artifact identified as replacement
- `superseded_by` field populated
- Status: `deprecated`

## 4. Review Cadence

| Artifact Type | Review Cycle |
|--------------|-------------|
| SSS initiatives | Quarterly |
| SSS projects | Monthly |
| SSS specifications | Quarterly |
| Decision records | Annually |
| Knowledge entries | Semi-annually |

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-003*  
*Owner: marshallwmorrison*
