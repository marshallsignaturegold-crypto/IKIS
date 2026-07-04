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

## 2. System Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    CONSUMPTION LAYER                         │
│  (AI agents, human reviewers, automation scripts, CI/CD)    │
├─────────────────────────────────────────────────────────────┤
│                    INTERFACE LAYER                           │
│  (README, AI_OPERATING_MANUAL, REPOSITORY_MAP, templates)   │
├─────────────────────────────────────────────────────────────┤
│                    KNOWLEDGE LAYER                           │
│  (sss-domain/, knowledge/, ontologies/)                     │
├─────────────────────────────────────────────────────────────┤
│                    GOVERNANCE LAYER                          │
│  (governance/, docs/06_governance_framework.md)             │
├─────────────────────────────────────────────────────────────┤
│                    SPECIFICATION LAYER                       │
│  (docs/, schemas/, templates/)                              │
├─────────────────────────────────────────────────────────────┤
│                    AUTOMATION LAYER                          │
│  (automation/, .github/workflows/)                          │
├─────────────────────────────────────────────────────────────┤
│                    FOUNDATION LAYER                          │
│  (Git, GitHub, JSON, YAML, Markdown, Turtle)                │
└─────────────────────────────────────────────────────────────┘
```

## 3. Knowledge Flow Architecture

```
Source Material → Capture → Curate → Validate → Store → Retrieve → Synthesize → Action
                    ↑         ↑         ↑         ↑         ↑           ↑
                 Template  Review   Schema   Metadata  Search   Intelligence
                 Driven    Gate     Valid.   Enrich.   Index    Brief
```

## 4. SSS Domain Representation

The SSS business domain is represented through a **multi-dimensional entity model**:

### 4.1 Entity Hierarchy

```
SSS Platform (Root)
├── Pillar A: SSS Firm
│   ├── Revenue Stream: Advisory
│   ├── Revenue Stream: Management Fees
│   └── Revenue Stream: Carried Interest
├── Pillar B: AIA Corridor
│   ├── Program: SSTP
│   ├── Corridor: AIA-SMCC
│   ├── Initiative: SovereignSomaliland PPP
│   │   └── Asset: SSTLC (Proposed)
│   └── Initiative: IndiSovereign PPP
│       └── Asset: BIBC (Proposed)
└── Pillar C: Corleone Holdings
    ├── Division: CPG (16-SKU Italian Heritage Line)
    ├── Division: Franchise (Don Vito's Pizza Oven)
    └── Division: Media & Licensing
```

## 5. Key Design Decisions

### Decision: Repository-as-Product

**Context**: Option to build a web application, API, or database-backed system.
**Decision**: The GitHub repository is the product.
**Rationale**:
- Git provides version history, branching, and collaboration natively
- Markdown + JSON is universally consumable by AI systems
- No deployment, hosting, or infrastructure dependencies
- Lower maintenance burden
- Future-compatible with APIs, databases, or applications

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
**Decision**: Legal gating rules are encoded in AI agent context and templates.
**Rationale**: Ensures all AI-generated SSS materials comply with legal constraints automatically.

## 6. Related Documentation

- [`AI_OPERATING_MANUAL.md`](./AI_OPERATING_MANUAL.md) — AI agent usage protocols
- [`REPOSITORY_MAP.md`](./REPOSITORY_MAP.md) — Complete directory guide
- [`docs/01_knowledge_model.md`](./docs/01_knowledge_model.md) — Knowledge classification

---

*Last updated: 2026-07-05*  
*Status: Validated*  
*Owner: marshallwmorrison*
