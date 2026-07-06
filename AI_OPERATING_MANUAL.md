# AI Operating Manual for IKIS

> **How AI agents should use the Institutional Knowledge & Intelligence System. Read this before any SSS-related task.**

---

## 1. Purpose of This Document

This manual is your instruction set for working with IKIS. Following these protocols ensures that your outputs are consistent with SSS standards, legally compliant, properly structured, and traceable.

**Read this entire document once.** Then use it as a reference for subsequent tasks.

## 2. Pre-Task Protocol

Before beginning any SSS-related task, perform these steps:

### 2.1 Load Domain Context

Always start by loading the SSS domain context:

1. Read [`sss-domain/00_sss_entity_index.md`](./sss-domain/00_sss_entity_index.md)
2. Read [`sss-domain/08_strategic_thesis.md`](./sss-domain/08_strategic_thesis.md)
3. Identify which pillar(s) and portfolio entities are relevant
4. Load relevant pillar-specific files from [`sss-domain/`](./sss-domain/)

### 2.2 Determine Artifact Type

Identify what type of artifact you are creating:

| Task Type | Use Template | Store In |
|-----------|-------------|----------|
| Knowledge capture | `templates/knowledge_capture_template.md` | `knowledge/validated/` |
| Decision record | `templates/decision_record_template.md` | `log/decisions/` |
| Intelligence brief | `templates/intelligence_brief_template.md` | `knowledge/derived/` |
| Gap report | `templates/gap_report_template.md` | `knowledge/derived/` |
| SSS Initiative | `templates/sss_initiative_template.md` | `sss-domain/initiatives/` |
| SSS Project | `templates/sss_project_template.md` | `sss-domain/projects/` |
| SSS Specification | `templates/sss_specification_template.md` | `sss-domain/specifications/` |

### 2.3 Apply Legal Gating

**CRITICAL**: For any SSS-facing document, apply the legal gating rules from [`ai-agents/context_injection/legal_gating_context.md`](./ai-agents/context_injection/legal_gating_context.md):

- All projects and structures remain "proposed" unless documented as approved
- Do NOT claim: concessions, government approvals, PPP awards, licenses, financing commitments, DFI/ECA support, banking authorization, securities offerings, or government endorsements
- Use hedged terms: "subject to review/approval/feasibility", "settlement-support", "treasury-support", "clearing-support", "trade-finance-support", "bank-ready transaction files"
- Heavily qualify or avoid: bank, clearinghouse, exchange, depository, token, stablecoin, security, "concession granted", "approved", "authorized", "licensed", "committed financing"
- Use "Government of Somaliland" (never "Somalian government")
- Use "Somaliland" (never "Somalia")
- All figures labeled "illustrative" unless explicitly sourced and validated

## 3. Content Production Protocols

### 3.1 Metadata Requirement

Every artifact you create MUST include the metadata block specified in [`docs/02_metadata_specification.md`](./docs/02_metadata_specification.md). Minimum required fields:

```yaml
---
artifact_id: "IKIS-[TYPE]-YYYY-[NNN]"
type: "[artifact_type]"
title: "[Descriptive Title]"
status: "draft"
pillar: "[A|B|C|multiple|none]"
confidence: "[high|medium|low|provisional]"
authors: ["ai-agent"]
owner: "marshallwmorrison"
created_date: "YYYY-MM-DD"
provenance:
  source_artifacts: []
governance:
  classification: "internal"
---
```

### 3.2 Program Hierarchy Discipline

Always use the full, exact program hierarchy for SSS materials:

```
Signature Sovereign Solutions, LLC
└── Sovereign SafeTrade Program (Sovereign SafeTrade Program (SSTP))
    └── Afro-Indian-American Strategic Minerals and Capital Corridor (AIA-SMCC)
        ├── SovereignSomaliland Public-Private Partnership Initiative
        │   └── proposed SovereignSomaliland SafeTrade and Logistics Complex (SSTLC)
        └── IndiSovereign Public-Private Partnership Initiative
            └── proposed IndiSovereign Bihar Integrated Bullion Complex (BIBC)
```

### 3.3 Cross-Reference Discipline

Always cross-reference related artifacts:

- Use artifact IDs when referencing other IKIS content
- Link to related files using relative Markdown links
- Tag related portfolio entities
- Document dependencies explicitly

### 3.4 Confidence Tagging

Tag all factual claims with confidence levels:

| Level | Meaning | Use When |
|-------|---------|----------|
| **High** | Verified against multiple authoritative sources | Multiple independent confirmations |
| **Medium** | Verified against at least one authoritative source | Single confirmation or strong inference |
| **Low** | Partially verified or inferred | Limited data, extrapolation |
| **Provisional** | Unverified, working assumption | Placeholder, needs validation |

### 3.5 Evidence Tiering

Classify sources using the evidence tier system:

| Tier | Source Type | Examples |
|------|-------------|----------|
| T1 | Government/Official | US Embassy, MEA India, SEC filings, DP World press releases |
| T2 | Academic/Research | IJSRM, RSIS International, peer-reviewed papers |
| T3 | Industry/Professional | Technavio, IMARC, Research and Markets, Davis Polk |
| T4 | Press/Media | BBC, FoodDive, Al Jazeera, Wardheernews |
| T5 | Social/Informal | Facebook, Instagram, unverified reports |

## 4. Post-Production Protocol

### 4.1 Validation Checklist

Before marking any artifact complete:

- [ ] Metadata block is complete and valid
- [ ] Schema validation passes (if applicable)
- [ ] All cross-references resolve correctly
- [ ] Legal gating rules applied (SSS materials)
- [ ] Confidence levels assigned to all factual claims
- [ ] Evidence tiers assigned to all sources
- [ ] Provenance documented (sources → artifact)
- [ ] Related artifacts tagged and linked

### 4.2 Commit Protocol

When committing artifacts:

1. Use conventional commit format: `type(scope): description`
2. Types: `knowledge`, `decision`, `spec`, `template`, `governance`, `automation`, `docs`
3. Scope: `sss-domain`, `pillar-a`, `pillar-b`, `pillar-c`, `automation`, `governance`, `ai-agents`

### 4.3 Handoff Notes

Always include handoff notes:

```markdown
## Handoff Notes

- **Status**: [Complete / In Progress / Blocked]
- **Next Steps**: [What should happen next]
- **Blockers**: [Any blockers or dependencies]
- **Assumptions Made**: [Explicit assumptions]
- **Gaps Identified**: [Known gaps]
- **Recommended Reviewer**: [Who should review]
```

## 5. Quick Reference Card

```
PRE-TASK:
  1. Load sss-domain/00_sss_entity_index.md
  2. Load relevant pillar files
  3. Identify artifact type → select template
  4. Load legal_gating_context.md (if SSS-facing)

DURING TASK:
  1. Follow template structure
  2. Include complete metadata block
  3. Apply legal gating rules
  4. Tag confidence and evidence tiers
  5. Cross-reference related artifacts

POST-TASK:
  1. Run validation checklist
  2. Include handoff notes
  3. Use conventional commit format
  4. Set status to "draft" for human review
```

---

*Last updated: 2026-07-05*  
*Status: Validated*  
*Owner: marshallwmorrison*
