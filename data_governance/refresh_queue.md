# Refresh Queue

**0 knowledge base files need attention**

---

This queue is auto-populated by the `knowledge_confidence_scorer.py` script during monthly CI runs. Files are flagged for refresh when their confidence score falls below 0.35, or when they are stale (>1 year old), lack provenance metadata, or are not in a standard validation directory.

## Refresh Priority

| Priority | Condition | Action Required |
|----------|-----------|-----------------|
| **P0** | Score < 0.35 or missing frontmatter | Immediate review required |
| **P1** | Score 0.35–0.55 or stale 180–365 days | Schedule review within 30 days |
| **P2** | Score 0.55–0.75 or stale 90–180 days | Schedule review within 60 days |
| **P3** | Score > 0.75 and fresh < 90 days | No action required |

## Confidence Scoring Dimensions

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Source Authority | 35% | Primary source (1.0) → Secondary (0.6) → Inference (0.3) |
| Validation Depth | 40% | Live (1.0) → Institutional (0.8) → Final (0.7) → Frontier (0.4) |
| Recency | 25% | <30 days (1.0) → <90 days (0.8) → <180 days (0.6) → >1 year (0.2) |

---

*This file is auto-generated. Do not edit manually — changes will be overwritten on next CI run.*
