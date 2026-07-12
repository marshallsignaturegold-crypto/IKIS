# IKIS Architecture Overview

> **System architecture, design rationale, and structural decisions for the Institutional Knowledge & Intelligence System.**

---

## 1. Design Philosophy

IKIS is designed as a **GitHub-native AI Knowledge Operating System**. The repository itself is the product. Every structural decision prioritizes:

1. **AI Consumability** — Files should be parseable, cross-referenceable, and context-rich for AI agents
2. **Human Maintainability** — Clear organization, consistent naming, comprehensive documentation
3. **Traceability** — Every artifact has provenance, lifecycle state, and review history
4. **Extensibility** — New artifact types, domains, and automation can be added without destabilizing the core
5. **Governability** — Ownership, review, approval, and escalation are explicit, not implicit

---

## 2. System Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    CONSUMPTION LAYER                         │
│  (AI agents, human reviewers, automation scripts, CI/CD)    │
├─────────────────────────────────────────────────────────────┤
│                    INTERFACE LAYER                           │
│  (README, AI_OPERATING_MANUAL, REPOSITORY_MAP, templates)   │
├─────────────────────────────────────────────────────────────┤
│                    INTELLIGENCE LAYER                        │
│  (Knowledge base, ontologies, confidence scoring, live feeds)│
├─────────────────────────────────────────────────────────────┤
│                    GOVERNANCE LAYER                          │
│  (governance/, docs/06_governance_framework.md,              │
│   data_governance/contradiction_register.md,                 │
│   data_governance/refresh_queue.md)                         │
├─────────────────────────────────────────────────────────────┤
│                    SPECIFICATION LAYER                       │
│  (docs/, schemas/, templates/)                              │
├─────────────────────────────────────────────────────────────┤
│                    AUTOMATION LAYER                          │
│  (automation/, .github/workflows/)                          │
│  - Terminology Enforcement                                   │
│  - Contradiction Detection                                   │
│  - Knowledge Confidence Scoring                            │
│  - Health Checks & Link Validation                         │
├─────────────────────────────────────────────────────────────┤
│                    FOUNDATION LAYER                          │
│  (Git, GitHub, JSON, YAML, Markdown, Turtle)                │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Knowledge Flow Architecture

```
Source Material → Capture → Curate → Validate → Store → Score → Retrieve → Synthesize → Action
                    ↑         ↑         ↑         ↑        ↑         ↑           ↑
                 Template  Review   Schema   Confidence  Search   Intelligence
                 Driven    Gate     Valid.   Score     Index    Brief
```

---

## 4. SSS Domain Representation

The SSS business domain is represented through a **multi-dimensional entity model**:

### 4.1 Entity Hierarchy

```
SSS Platform (Root)
├── Pillar A: SSS Firm: SSS Firm
│   ├── Revenue Stream: Advisory
│   ├── Revenue Stream: Management Fees
│   └── Revenue Stream: Carried Interest
├── Pillar B: AISTA (African Infrastructure & SafeTrade Alliance / Corridor): AISTA (African Infrastructure & SafeTrade Alliance / Corridor)
│   ├── Program: Sovereign SafeTrade Program (SSTP)
│   ├── Corridor: AISTA (African Infrastructure & SafeTrade Alliance / Corridor)
│   ├── Initiative: SovereignSomaliland PPP
│   │   └── Asset: SSTLC (Proposed)
│   └── Initiative: IndiSovereign PPP
│       └── Asset: BIBC (Proposed)
└── Pillar C: Corleone Enterprise Holdings: Corleone Holdings
    ├── Division: CPG (16-SKU Italian Heritage Line)
    ├── Division: Franchise (Don Vito's Pizza Oven)
    └── Division: Media & Licensing
```

---

## 5. Automation Architecture (New)

### 5.1 Terminology Enforcement Pipeline

```
Push/PR → terminology_enforcer.py → Scan all .md/.yml/.json
    ↓
Violations? → PR comment with suggestions → FAIL CI → Block merge
No violations? → PASS CI → Allow merge
```

**Input:** `approved_terms.yml` (from linked governance repo)  
**Output:** CI pass/fail + PR comment with corrections

### 5.2 Contradiction Detection Pipeline

```
Weekly cron / manual trigger → contradiction_detector.py → Scan knowledge/validated/
    ↓
Critical contradictions? → GitHub Issue auto-created → FAIL CI
No critical contradictions? → Register updated → PASS CI
```

**Input:** All knowledge base files  
**Output:** `data_governance/contradiction_register.md` + GitHub Issue

### 5.3 Knowledge Confidence Scoring Pipeline

```
Monthly cron / manual trigger → knowledge_confidence_scorer.py → Score all KB entries
    ↓
Refresh queue items? → GitHub Issue created → Continue
No refresh queue? → Register updated → PASS CI
```

**Input:** Knowledge base files with YAML frontmatter  
**Output:** `data_governance/confidence_report.md` + `data_governance/refresh_queue.md`

---

## 6. Key Design Decisions

### Decision: Repository-as-Product

**Context**: Option to build a web application, API, or database-backed system.  
**Decision**: The GitHub repository is the product.  
**Rationale**: Git provides version history, branching, and collaboration natively. Markdown + JSON is universally consumable by AI systems. No deployment, hosting, or infrastructure dependencies.

### Decision: Schema-Governed but Flexible

**Context**: Need to enforce consistency without being overly rigid.  
**Decision**: JSON schemas define required structure; Markdown content allows flexibility.  
**Rationale**: Schemas ensure machine-parseable metadata and structure; Markdown allows rich human-readable content.

### Decision: Ontology-Backed Domain Model

**Context**: SSS domain has complex relationships between entities.  
**Decision**: Formal ontologies in Turtle and JSON-LD define the domain model.  
**Rationale**: Enables machine reasoning, cross-reference validation, and AI agent context understanding.

### Decision: Explicit Legal Gating

**Context**: SSS materials require careful legal hedging.  
**Decision**: Legal gating rules are encoded in AI agent context and enforced by CI.  
**Rationale**: Ensures all AI-generated SSS materials comply with legal constraints automatically.

### Decision: Automated Knowledge Validation

**Context**: 165+ knowledge files need ongoing quality control.  
**Decision**: Three-tier automation: terminology enforcement, contradiction detection, confidence scoring.  
**Rationale**: Manual review at scale is infeasible. Automation catches drift before it propagates.

---

## 7. Data Governance Integration

### 7.1 Contradiction Register

| Field | Description |
|-------|-------------|
| `fact_type` | Category of contradicting assertion (revenue, IRR, status, etc.) |
| `assertion_a` | File A: line, context, value |
| `assertion_b` | File B: line, context, value |
| `severity` | critical / warning / info |
| `explanation` | Human-readable description of conflict |
| `detected_at` | ISO timestamp |

### 7.2 Confidence Score Dimensions

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Source Authority | 35% | Primary (1.0) → Secondary (0.6) → Inference (0.3) |
| Validation Depth | 40% | Live (1.0) → Institutional (0.8) → Final (0.7) → Frontier (0.4) |
| Recency | 25% | <30 days (1.0) → <90 days (0.8) → <180 days (0.6) → >1 year (0.2) |

### 7.3 Refresh Queue Priority

| Priority | Condition | SLA |
|----------|-----------|-----|
| P0 | Score < 0.35 | Immediate |
| P1 | Score 0.35–0.55 | 30 days |
| P2 | Score 0.55–0.75 | 60 days |
| P3 | Score > 0.75 | No action |

---

## 8. Related Documentation

- [`AI_OPERATING_MANUAL.md`](./AI_OPERATING_MANUAL.md) — AI agent usage protocols
- [`REPOSITORY_MAP.md`](./REPOSITORY_MAP.md) — Complete directory guide
- [`docs/01_knowledge_model.md`](./docs/01_knowledge_model.md) — Knowledge classification
- [`docs/02_metadata_specification.md`](./docs/02_metadata_specification.md) — Frontmatter schema
- [`automation/terminology_enforcer.py`](./automation/terminology_enforcer.py) — Terminology enforcement script
- [`automation/contradiction_detector.py`](./automation/contradiction_detector.py) — Contradiction detection script
- [`automation/knowledge_confidence_scorer.py`](./automation/knowledge_confidence_scorer.py) — Confidence scoring script

---

*Last updated: 2026-07-11*  
*Status: Validated, AISTA-remediated, automation-enhanced*  
*Owner: marshallwmorrison*
