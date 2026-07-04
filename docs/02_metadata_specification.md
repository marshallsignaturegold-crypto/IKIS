# 02 — Metadata Specification

> **Required metadata for all artifacts in IKIS. Every artifact must include this metadata block.**

---

## 1. Metadata Block Format

All artifacts must include YAML frontmatter:

```yaml
---
artifact_id: "IKIS-[TYPE]-YYYY-[NNN]"
type: "[artifact_type]"
title: "[Descriptive Title]"
status: "[lifecycle_state]"
confidence: "[high|medium|low|provisional]"
pillar: "[A|B|C|multiple|none]"
portfolio_entity: "[entity_code|none]"
authors:
  - "[github_handle]"
owner: "[github_handle]"
created_date: "YYYY-MM-DD"
last_reviewed: "YYYY-MM-DD"
review_cycle_months: [3|6|12]
provenance:
  source_artifacts:
    - "[source_artifact_id]"
  validation_method: "[cross_reference|expert_review|automated|none]"
  validated_by:
    - "[github_handle]"
  validated_date: "YYYY-MM-DD"
tags:
  - "[tag]"
related_artifacts:
  - "[related_artifact_id]"
governance:
  classification: "[internal|confidential|public|restricted]"
  escalation_required: [true|false]
  legal_reviewed: [true|false]
---
```

## 2. Controlled Vocabularies

### Artifact Types
`knowledge_entry`, `source_note`, `intelligence_brief`, `decision_record`, `gap_report`, `assumption_record`, `sss_initiative`, `sss_project`, `sss_specification`, `sss_detail`, `portfolio_entity`, `ontology`, `template`, `schema`, `automation`, `governance`

### Lifecycle States
`draft`, `under_review`, `revision_requested`, `validated`, `deprecated`, `archived`

### Confidence Levels
`high`, `medium`, `low`, `provisional`

### Pillar Codes
`A` (SSS Firm), `B` (AIA Corridor), `C` (Corleone), `multiple`, `none`

### Portfolio Entity Codes
`SSTLC`, `BIBC`, `SSTP`, `AIA-SMCC`, `CORLEONE`, `DVPO`, `SSS`, `none`

### Classification Levels
`public`, `internal`, `confidential`, `restricted`

## 3. ID Format

```
IKIS-[TYPE]-YYYY-[NNN]
```

Type codes: `SSS`, `KNE`, `DCR`, `IBF`, `GPR`, `ASR`, `PFE`, `ONT`, `GOV`, `AUT`

## 4. Related Documentation

- `03_lifecycle_specification.md`
- `04_provenance_specification.md`

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-002*  
*Owner: marshallwmorrison*
