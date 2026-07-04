# 11 — Quality Standards

> **Quality standards and validation rules for all IKIS artifacts.**

---

## 1. Quality Dimensions

Every artifact is evaluated against these dimensions:

| Dimension | Weight | Measurement |
|-----------|--------|-------------|
| Accuracy | 25% | Cross-reference with sources |
| Completeness | 20% | Template compliance |
| Consistency | 20% | Ontology alignment |
| Traceability | 15% | Provenance chain |
| Clarity | 10% | Readability, structure |
| Actionability | 10% | Utility for decisions |

## 2. Quality Gates

### Automated Gates (CI/CD)

| Gate | Check | Threshold |
|------|-------|-----------|
| Schema compliance | Validate against JSON schema | 100% pass |
| Metadata completeness | All required fields present | 100% pass |
| Link integrity | All internal links resolve | 95% pass |
| Provenance chain | Source artifacts exist | 100% pass |

### Manual Gates (Review)

| Gate | Check | Reviewer |
|------|-------|----------|
| Content accuracy | Factual correctness | Domain expert |
| Legal gating | SSS legal compliance | Legal reviewer |
| Cross-references | Related artifacts accurate | Peer reviewer |

## 3. Quality Ratings

| Rating | Score | Action |
|--------|-------|--------|
| Excellent | 90-100% | Approve |
| Good | 70-89% | Approve with notes |
| Needs Work | 50-69% | Request revisions |
| Unacceptable | <50% | Reject |

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-011*  
*Owner: marshallwmorrison*
