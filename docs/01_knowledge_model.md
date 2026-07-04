# 01 — Knowledge Model

> **Classification of knowledge types, their relationships, and their flow through IKIS.**

---

## 1. Knowledge Classification

IKIS distinguishes between seven primary knowledge types:

### 1.1 Knowledge Type Hierarchy

```
Knowledge (Root)
├── Source Material (Raw)
│   ├── Research Notes
│   ├── Meeting Notes
│   ├── External Documents
│   └── Agent Outputs
├── Curated Knowledge (Processed)
│   ├── Validated Knowledge Entries
│   └── Annotated Artifacts
├── Derived Intelligence (Synthesized)
│   ├── Intelligence Briefs
│   ├── Risk Assessments
│   ├── Gap Analysis Reports
│   └── Portfolio Summaries
├── Decision Records (Authoritative)
│   ├── Architecture Decisions
│   ├── Business Decisions
│   └── Policy Decisions
├── Operational Guidance (Actionable)
│   ├── Runbooks
│   ├── Templates
│   ├── Checklists
│   └── Workflows
├── Assumptions & Gaps (Provisional)
│   ├── Documented Assumptions
│   ├── Known Gaps
│   └── Open Questions
└── Historical Records (Temporal)
    ├── Change Logs
    ├── Review Logs
    └── Audit Trails
```

### 1.2 Knowledge Type Definitions

| Type | Definition | Confidence | Mutability |
|------|-----------|------------|------------|
| **Source Material** | Raw, unprocessed inputs | Unrated | Immutable |
| **Curated Knowledge** | Reviewed and annotated | Medium-High | Low |
| **Derived Intelligence** | Synthesized products | Medium | Medium |
| **Decision Records** | Authoritative decisions | High | Low |
| **Operational Guidance** | Actionable procedures | High | Medium |
| **Assumptions & Gaps** | Explicitly recorded uncertainties | Low | High |
| **Historical Records** | Temporal records | High | Immutable |

## 2. SSS-Specific Knowledge Types

| Type | Description | Example |
|------|-------------|---------|
| **SSS Initiative** | Strategic initiative | SovereignSomaliland PPP |
| **SSS Project** | Defined project | FDD Preparation |
| **SSS Specification** | Technical/business spec | DOP Ingredient Protocol |
| **SSS Detail Record** | Granular implementation detail | Unit Economics Model |
| **Portfolio Entity Record** | Named entity profile | SSTLC Profile |

## 3. Knowledge Flow

```
Source Material → Capture → Curate → Validate → Store → Retrieve → Synthesize → Action
```

## 4. Confidence and Authority

| Level | Definition | Authority for Decisions |
|-------|-----------|------------------------|
| **High** | Multiple authoritative sources | Yes — strategic decisions |
| **Medium** | At least one authoritative source | Yes — tactical decisions |
| **Low** | Partially verified or inferred | No — informational only |
| **Provisional** | Unverified assumption | No — explicitly provisional |

## 5. Related Documentation

- `02_metadata_specification.md` — Metadata requirements
- `03_lifecycle_specification.md` — Lifecycle states

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-001*  
*Owner: marshallwmorrison*
