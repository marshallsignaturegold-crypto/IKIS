# 05 — Ontology Reference

> **Entity types, relationships, and controlled vocabulary for the SSS domain and IKIS system.**

---

## 1. Ontology Overview

IKIS uses formal ontologies to define:
- SSS business domain entities and their relationships
- Knowledge classification types
- AI agent interaction patterns

Ontologies are expressed in:
- **Turtle (.ttl)**: Human-readable, formal RDF
- **JSON-LD (.jsonld)**: Machine-readable, API-friendly

## 2. SSS Business Domain Entities

### Entity Types

| Entity Type | Description | Properties |
|-------------|-------------|------------|
| `Pillar` | Strategic business pillar | name, description, status, revenue_streams |
| `Program` | Top-level operational program | name, description, pillar, status |
| `Corridor` | Trade corridor | name, description, geography, status |
| `Initiative` | Country/regional initiative | name, description, corridor, status |
| `Asset` | Physical or financial asset | name, description, location, status |
| `SPV` | Special purpose vehicle | name, jurisdiction, status |
| `Division` | Operating division | name, description, parent_entity |
| `Project` | Defined project | name, description, initiative, status |
| `Specification` | Technical/business specification | name, description, type, version |
| `Decision` | Recorded decision | name, description, date, rationale |
| `Risk` | Identified risk | name, description, probability, impact |
| `Person` | Individual | name, role, entity |
| `Organization` | External organization | name, type, relationship |

### Relationship Types

| Relationship | Description |
|-------------|-------------|
| `hasChild` / `hasParent` | Hierarchical containment |
| `dependsOn` | Dependency relationship |
| `produces` | Output/production relationship |
| `risks` | Risk association |
| `validates` | Validation relationship |
| `supersedes` | Supersession |
| `derivesFrom` | Derivation |

## 3. Ontology Files

| File | Format |
|------|--------|
| `ontologies/sss_business_domain.ttl` | Turtle |
| `ontologies/sss_business_domain.jsonld` | JSON-LD |
| `ontologies/knowledge_ontology.ttl` | Turtle |
| `ontologies/ai_agent_ontology.ttl` | Turtle |

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-005*  
*Owner: marshallwmorrison*
