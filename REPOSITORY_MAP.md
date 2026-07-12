# IKIS Repository Map

**Version:** 2.0 — Updated 2026-07-11  
**Status:** Reflects AISTA terminology remediation and new automation infrastructure

---

## Root Files

| File | Purpose | Status |
|------|---------|--------|
| `README.md` | Repository overview and quick-start | Current |
| `AI_OPERATING_MANUAL.md` | AI agent instructions and context injection protocols | Current |
| `ARCHITECTURE.md` | System architecture and design decisions | Current (AISTA-remediated) |
| `REPOSITORY_MAP.md` | This file — directory guide and navigation | Current |
| `high_intensity_vectors.json` | Q3 2026 research acceleration vectors | Current |
| `LICENSE` | Repository license | Current |
| `.gitignore` | Git ignore rules | Current |
| `.ikisrc` | IKIS configuration file | Current |

---

## Directory Structure

### `.github/` — GitHub Configuration

| File | Purpose |
|------|---------|
| `ISSUE_TEMPLATE/decision_record.yml` | Decision record issue template |

**Note:** GitHub Actions workflows (`terminology_check.yml`, `contradiction_scan.yml`, `knowledge_validation.yml`) must be added manually via GitHub UI due to API scope restrictions. See `.github/workflows/` setup instructions below.

---

### `ai-agents/` — AI Agent Infrastructure

| Directory | Purpose | Files |
|-----------|---------|-------|
| `context_injection/` | Domain context files loaded by AI agents | `legal_gating_context.md`, `sss_domain_context.md` (AISTA-remediated), `visual_system_context.md` |
| `prompt_library/` | Reusable prompt templates | `analysis_prompts.md`, `document_generation_prompts.md`, `research_prompts.md`, `validation_prompts.md` |
| `task_guides/` | Step-by-step guides for common tasks | `compliance_review_guide.md`, `investor_materials_guide.md`, `market_research_guide.md`, `submission_packet_guide.md` |

---

### `assets/` — Repository Assets

| File | Purpose |
|------|---------|
| `README.md` | Asset directory documentation |

---

### `automation/` — CI/CD and Validation Scripts

| Script | Purpose | Trigger | Status |
|--------|---------|---------|--------|
| `terminology_enforcer.py` | Scans all files for deprecated/prohibited terminology | Every PR/push | **NEW** |
| `contradiction_detector.py` | Cross-references KB for factual conflicts | Weekly + manual | **NEW** |
| `knowledge_confidence_scorer.py` | Scores KB entries on authority/depth/recency | Monthly | **NEW** |
| `health_check.py` | Repository health and integrity checks | Manual | Existing |
| `link_checker.py` | Validates internal cross-references | Manual | Existing |
| `metadata_verifier.py` | Validates YAML frontmatter compliance | Manual | Existing |
| `schema_validator.py` | Validates JSON schema conformance | Manual | Existing |
| `requirements.txt` | Python dependencies | — | Existing |

---

### `branding_assets/` — Visual Identity

| File | Purpose |
|------|---------|
| `bibc_hero.png` | BIBC visual asset |
| `brand_architecture.png` | Brand system diagram |
| `sss_architecture.png` | SSS platform architecture |
| `sstlc_hero.png` | SSTLC visual asset |
| `tmicesb_hero.png` | TMICESB visual asset |

---

### `data_governance/` — Knowledge Quality & Control

| File | Purpose | Population |
|------|---------|------------|
| `contradiction_register.md` | Tracks factual conflicts across KB | Auto (CI) |
| `refresh_queue.md` | Flags files needing review | Auto (CI) |
| `confidence_report.md` | Full KB confidence scoring | Auto (CI) |

---

### `docs/` — IKIS Documentation

| File | Purpose | Status |
|------|---------|--------|
| `01_knowledge_model.md` | Knowledge classification taxonomy | Current |
| `02_metadata_specification.md` | Frontmatter and metadata schema | Current |
| `03_lifecycle_specification.md` | Artifact lifecycle states | Current |
| `04_provenance_specification.md` | Source tracking and validation | Current |
| `05_ontology_reference.md` | Formal ontology definitions | Current |
| `06_governance_framework.md` | IKIS governance rules | Current |
| `07_contribution_guide.md` | How to add/modify artifacts | Current |
| `08_maintenance_guide.md` | Ongoing maintenance procedures | Current |
| `09_security_policy.md` | Data handling and access control | Current |
| `10_versioning_strategy.md` | Version numbering and releases | Current |
| `11_quality_standards.md` | Quality benchmarks and checks | Current |
| `12_ai_context_protocols.md` | AI-specific interaction rules | Current |
| `README.md` | Docs directory overview | Current |

---

### `governance/` — Project Governance

| File | Purpose |
|------|---------|
| `approval_workflow.md` | How decisions are approved |
| `conflict_resolution.md` | Dispute resolution process |
| `escalation_paths.md` | When and how to escalate |
| `lifecycle_states.md` | Artifact state definitions |
| `ownership_matrix.md` | Who owns what |
| `retention_policy.md` | Data retention rules |
| `review_cadence.md` | Review schedules |

---

### `knowledge/` — Knowledge Base

| Directory | Purpose | Validation Level | File Count |
|-----------|---------|-----------------|------------|
| `validated/live/` | Real-time intelligence feeds | Live (1.0) | ~18 |
| `validated/institutional/` | DFI-grade validated findings | Institutional (0.8) | ~4 |
| `validated/final/` | Final peer-reviewed outputs | Final (0.7) | ~10 |
| `validated/frontier/` | Emerging/risk-tolerant research | Frontier (0.4) | ~5 |
| `validated/granular/` | Deep-dive technical specs | Granular (0.6) | ~18 |
| `validated/ultra_deep/` | Exhaustive analytical depth | Ultra Deep (0.5) | ~60 |
| `validated/recursive/` | Self-referential synthesis cycles | Recursive (0.6) | ~2 |
| `validated/research_results_*` | Categorized research outputs | Research Results (0.6) | ~18 |
| `validated/v25/` | Version 25 research artifacts | V25 (0.5) | ~24 |
| `derived/` | Synthesized reports and extractions | Derived (0.5) | ~6 |
| `README.md` | Knowledge base directory guide | — | — |

**Total Knowledge Files:** ~165+

---

### `log/` — Audit Trail

| Directory | Purpose |
|-----------|---------|
| `reviews/` | Detailed audit reports for each research category |

---

### `ontologies/` — Formal Domain Models

| File | Format | Purpose |
|------|--------|---------|
| `ai_agent_ontology.ttl` | Turtle | AI agent capability and role definitions |
| `knowledge_ontology.ttl` | Turtle | Knowledge classification and relationships |
| `sss_business_domain.jsonld` | JSON-LD | SSS business entity model |
| `sss_business_domain.ttl` | Turtle | SSS business entity model (Turtle) |

---

### `output/` — Generated Reports

| File | Purpose | Generation |
|------|---------|------------|
| `SSS_Master_Program_Report_FINAL.pdf` | Comprehensive program report | Manual |
| `sss_master_program_full_content.md` | Markdown version of master report | Manual |

---

### `schemas/` — JSON Schemas

| Schema | Validates |
|--------|-----------|
| `artifact.schema.json` | General artifact metadata |
| `decision_record.schema.json` | Decision records |
| `intelligence_brief.schema.json` | Intelligence briefs |
| `knowledge_entry.schema.json` | Knowledge base entries |
| `metadata.schema.json` | Frontmatter metadata |
| `portfolio_entity.schema.json` | Portfolio entities |
| `sss_initiative.schema.json` | SSS initiatives |
| `sss_project.schema.json` | SSS projects |
| `sss_specification.schema.json` | Technical specifications |

---

### `sss-domain/` — SSS Business Domain

| File | Purpose | Status |
|------|---------|--------|
| `00_sss_entity_index.md` | Master entity index (canonical) | **AISTA-remediated** |
| `01_pillar_a_sss_firm.md` | Pillar A: SSS Firm details | Current |
| `02_pillar_b_aista_corridor.md` | Pillar B: AISTA corridor details | **NEW — replaces corrupted 02_pillar_b_aia_corridor.md** |
| `03_pillar_c_corleone.md` | Pillar C: Corleone Holdings | Current |
| `04_sstlc_profile.md` | SSTLC profile | Current |
| `05_bibc_profile.md` | BIBC profile | Current |
| `06_franchise_portfolio.md` | Franchise portfolio | Current |
| `07_personnel_directory.md` | Personnel directory | Current |
| `08_strategic_thesis.md` | Strategic thesis | Current |
| `README.md` | SSS domain overview | Current |
| `repositories/` | Repository summaries | Current |

---

### `templates/` — Document Templates

| Template | Purpose |
|----------|---------|
| `assumption_record_template.md` | Record assumptions |
| `decision_record_template.md` | Record decisions |
| `gap_report_template.md` | Document gaps |
| `intelligence_brief_template.md` | Intelligence briefs |
| `knowledge_capture_template.md` | Capture knowledge |
| `portfolio_entity_template.md` | Portfolio entities |
| `review_checklist_template.md` | Review checklists |
| `sss_initiative_template.md` | SSS initiatives |
| `sss_project_template.md` | SSS projects |
| `sss_specification_template.md` | Specifications |

---

## GitHub Actions Setup (Manual)

Due to API scope restrictions, the following workflows must be created manually via GitHub UI:

1. Navigate to **Actions → New workflow**
2. Create `.github/workflows/terminology_check.yml` — paste content from `automation/terminology_enforcer.py` docstring
3. Create `.github/workflows/contradiction_scan.yml` — paste content from `automation/contradiction_detector.py` docstring
4. Create `.github/workflows/knowledge_validation.yml` — paste content from `automation/knowledge_confidence_scorer.py` docstring

Alternatively, clone the repo locally, create the files, and push.

---

## Quick Navigation

- **AI Context:** `ai-agents/context_injection/`
- **Knowledge Base:** `knowledge/validated/`
- **Automation:** `automation/`
- **SSS Domain:** `sss-domain/`
- **Governance:** `governance/`
- **Ontologies:** `ontologies/`
- **Schemas:** `schemas/`
- **Templates:** `templates/`
- **Data Governance:** `data_governance/`

---

*Last updated: 2026-07-11*  
*Version: 2.0*  
*Status: AISTA-remediated, automation-enhanced*
