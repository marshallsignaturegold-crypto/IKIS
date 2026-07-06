# IKIS Repository Map

> **Complete directory-by-directory guide to navigating the Institutional Knowledge & Intelligence System.**

---

## Root Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Primary entry point, system overview, quick start | Everyone |
| `ARCHITECTURE.md` | System architecture, design rationale, key decisions | Technical stakeholders, AI agents |
| `AI_OPERATING_MANUAL.md` | How AI agents should use this repository | AI agents, developers |
| `REPOSITORY_MAP.md` | This file — navigation guide | Everyone |
| `LICENSE` | License terms | Legal, compliance |
| `.gitignore` | Git ignore rules | Contributors |
| `.ikisrc` | IKIS configuration file | Automation, CI/CD |

## `docs/` — Core Documentation

| # | Document | Purpose | Read When |
|---|----------|---------|-----------|
| 01 | `01_knowledge_model.md` | Knowledge classification, types, flow | Understanding knowledge architecture |
| 02 | `02_metadata_specification.md` | Required metadata for all artifacts | Creating or validating artifacts |
| 03 | `03_lifecycle_specification.md` | Lifecycle states and transitions | Understanding status fields |
| 04 | `04_provenance_specification.md` | Provenance and lineage tracking | Tracing information sources |
| 05 | `05_ontology_reference.md` | Entity types, relationships, vocabulary | Understanding domain model |
| 06 | `06_governance_framework.md` | Ownership, review, approval, escalation | Understanding governance |
| 07 | `07_contribution_guide.md` | How to contribute new knowledge | Contributing |
| 08 | `08_maintenance_guide.md` | Operational maintenance procedures | Maintaining IKIS |
| 09 | `09_security_policy.md` | Security and access policy | Security review |
| 10 | `10_versioning_strategy.md` | Versioning and release approach | Understanding versions |
| 11 | `11_quality_standards.md` | Quality standards and validation rules | Quality review |
| 12 | `12_ai_context_protocols.md` | AI agent consumption and production protocols | AI integration |

## `schemas/` — Validation Schemas

| Schema | Validates | File |
|--------|-----------|------|
| Base Artifact | Common artifact structure | `artifact.schema.json` |
| Metadata | Metadata block | `metadata.schema.json` |
| Knowledge Entry | Validated knowledge entries | `knowledge_entry.schema.json` |
| Decision Record | Decision records | `decision_record.schema.json` |
| Intelligence Brief | Intelligence briefs | `intelligence_brief.schema.json` |
| SSS Initiative | SSS initiatives | `sss_initiative.schema.json` |
| SSS Project | SSS projects | `sss_project.schema.json` |
| SSS Specification | SSS specifications | `sss_specification.schema.json` |
| Portfolio Entity | Portfolio entity profiles | `portfolio_entity.schema.json` |

## `templates/` — Reusable Templates

| Template | Use For | Output Location |
|----------|---------|----------------|
| `knowledge_capture_template.md` | New validated knowledge | `knowledge/validated/` |
| `decision_record_template.md` | Decision records | `log/decisions/` |
| `intelligence_brief_template.md` | Intelligence briefs | `knowledge/derived/` |
| `gap_report_template.md` | Gap reports | `knowledge/derived/` |
| `assumption_record_template.md` | Assumptions | `knowledge/validated/` |
| `sss_initiative_template.md` | SSS initiatives | `sss-domain/initiatives/` |
| `sss_project_template.md` | SSS projects | `sss-domain/projects/` |
| `sss_specification_template.md` | SSS specifications | `sss-domain/specifications/` |
| `portfolio_entity_template.md` | Portfolio entities | `sss-domain/` |
| `review_checklist_template.md` | Review checklists | `log/reviews/` |

## `ontologies/` — Domain Ontologies

| File | Format | Purpose |
|------|--------|---------|
| `sss_business_domain.ttl` | Turtle | SSS domain entities and relationships |
| `sss_business_domain.jsonld` | JSON-LD | Machine-readable SSS domain |
| `knowledge_ontology.ttl` | Turtle | Knowledge classification |
| `ai_agent_ontology.ttl` | Turtle | AI agent interactions |

## `sss-domain/` — SSS Business Domain

| File | Description |
|------|-------------|
| `00_sss_entity_index.md` | Master index of all SSS entities |
| `01_pillar_a_sss_firm.md` | Pillar A: SSS Firm: SSS Firm |
| `02_pillar_b_aia_corridor.md` | Pillar B: Afro-Indian-American Strategic Minerals and Capital Corridor (Afro-Indian-American Strategic Trade Alliance (Afro-Indian-American Strategic Trade Alliance (AISTA)) Corridor): Afro-Indian-American Strategic Minerals and Capital Corridor (Afro-Indian-American Strategic Trade Alliance (Afro-Indian-American Strategic Trade Alliance (AISTA)) Corridor) |
| `03_pillar_c_corleone.md` | Pillar C: Corleone Enterprise Holdings: Corleone Holdings |
| `04_sstlc_profile.md` | SSTLC profile |
| `05_bibc_profile.md` | BIBC profile |
| `06_franchise_portfolio.md` | Franchise portfolio |
| `07_personnel_directory.md` | Key personnel |
| `08_strategic_thesis.md` | Canonical strategic thesis |

## `ai-agents/` — AI Agent Assets

### `ai-agents/prompt_library/`

| File | Purpose |
|------|---------|
| `research_prompts.md` | Reusable prompts for research tasks |
| `analysis_prompts.md` | Reusable prompts for analysis tasks |
| `document_generation_prompts.md` | Reusable prompts for document production |
| `validation_prompts.md` | Reusable prompts for validation tasks |

### `ai-agents/task_guides/`

| File | Purpose |
|------|---------|
| `submission_packet_guide.md` | Guide for producing submission packets |
| `investor_materials_guide.md` | Guide for producing investor materials |
| `market_research_guide.md` | Guide for conducting market research |
| `compliance_review_guide.md` | Guide for compliance review |

### `ai-agents/context_injection/`

| File | Purpose | Load For |
|------|---------|----------|
| `sss_domain_context.md` | Full SSS domain context | Every SSS task |
| `legal_gating_context.md` | Legal constraints and hedging rules | SSS-facing documents |
| `visual_system_context.md` | Brand, visual, and formatting rules | Document production |

### `ai-agents/research_methodologies/`

| File | Purpose |
|------|---------|
| `market_validation_methodology.md` | Methodology for validating market claims |
| `competitor_analysis_methodology.md` | Methodology for competitive analysis |
| `regulatory_assessment_methodology.md` | Methodology for regulatory assessment |

## `automation/` — Automation Scripts

| File | Purpose | Run Frequency |
|------|---------|---------------|
| `health_check.py` | Comprehensive repository health check | Weekly / On demand |
| `schema_validator.py` | Validate artifacts against JSON schemas | On every PR |
| `metadata_verifier.py` | Verify metadata completeness | On every PR |
| `link_checker.py` | Verify internal link integrity | On every PR |
| `index_builder.py` | Build search index | Monthly / On demand |

## `governance/` — Governance Artifacts

| File | Purpose |
|------|---------|
| `ownership_matrix.md` | Artifact ownership by type |
| `review_cadence.md` | Review schedules and expectations |
| `approval_workflow.md` | Approval process definitions |
| `escalation_paths.md` | Escalation procedures |
| `lifecycle_states.md` | Lifecycle state definitions and transitions |
| `conflict_resolution.md` | Conflict resolution guidance |
| `retention_policy.md` | Retention and archival policy |

---

*This map is updated when the directory structure changes.*  
*Last updated: 2026-07-05*
