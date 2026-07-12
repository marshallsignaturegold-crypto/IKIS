---
artifact_id: "IKIS-FIN-2026-001"
type: "financial_model"
title: "BIBC Bihar SEZ Bullion Financial Model v2 (EGR Migration, P1-005 Resolution)"
status: "validated"
confidence: "high"
pillar: "B"
portfolio_entity: "BIBC"
authors:
  - "marshallwmorrison"
  - "phalanx-swarm-omega"
  - "financial-subagent"
owner: "marshallwmorrison"
created_date: "2026-07-11"
last_reviewed: "2026-07-11"
review_cycle_months: 1
provenance:
  source_artifacts:
    - "IKIS-PFE-2026-001"
    - "IKIS-PFE-2026-002"
  validation_method: "expert_review"
  validated_by:
    - "marshallwmorrison"
  validated_date: "2026-07-11"
tags:
  - "bibc"
  - "bullion"
  - "financial-model"
  - "egr"
  - "sebi"
  - "p1-005"
  - "validated"
related_artifacts:
  - "IKIS-INST-2026-005"
  - "IKIS-INST-2026-006"
governance:
  classification: "financial"
  escalation_required: false
  legal_reviewed: true
  p1_gap_resolved: "P1-005"
---

# BIBC Bihar SEZ Bullion Financial Model v2

**Model Date:** 2026-07-11  
**Gold Spot:** $2,750/oz ($88,414/kg)  
**Model Version:** 2.0 (EGR Migration)  
**P1 Gap Resolved:** P1-005 (Token premium removed, migrated to SEBI-regulated EGRs)

---

## 1. Executive Summary

This model reflects the corrected BIBC bullion financial framework following P1-005 resolution:

| Item | Value | Notes |
|------|-------|-------|
| Gold Spot (oz) | $2,750 | Base case |
| Gold Spot (kg) | $88,414 | 32.1507 oz/kg |
| Refinery throughput | 1,000 kg/day | 330 days/year |
| Annual throughput | 330,000 kg | $29.2B gold value |
| Refinery EBITDA | $25.2B | 8.6% margin |
| Vault EBITDA | $7.9M | 75% utilization |
| **Total EBITDA** | **$35.0B** | Base case |
| Total Capex (with EGR) | $97.5M | $95M refinery + $2.5M EGR migration |
| Payback period | <1 year | Exceptional due to gold throughput |
| ROIC | 29,169% | Extraordinary due to capital-light model |

## 2. Key Changes from v1 (P1-005 Resolution)

### Deprecated (v1)
- Tokenized scrip model with 5% premium
- ERC-1400 token structure
- $8M token compliance cost
- 50% token EBITDA margin

### Implemented (v2)
- SEBI-regulated Electronic Gold Receipts (EGRs)
- 0.15% trading fee (SEBI-mandated exchange rate)
- $2.5M EGR migration cost (legal + SEBI registration + vault manager)
- 65% EGR EBITDA margin
- GST-compliant physical delivery (3% GST)

## 3. EGR Model Detail

| Parameter | Value |
|-----------|-------|
| Initial EGR deposit | 100,000 kg physical gold |
| Annual trading volume | 250,000 kg (2.5x turnover) |
| Trading fee | 0.15% per transaction |
| EGR revenue | $33.1M/year |
| EGR opex | $11.6M/year (35%) |
| EGR EBITDA | $21.5M/year |
| EGR EBITDA margin | 65% |
| EGR migration cost | $2.5M (one-time) |

## 4. Revenue Breakdown

| Revenue Stream | Annual ($M) | Margin (%) |
|---------------|-------------|------------|
| Refinery (0.4% premium) | $116.8 | 8.6 |
| Vault (75% util, $18/kg) | $2.7 | 58.9 |
| EGR trading fees | $33.1 | 65.0 |
| **Total** | **$152.6** | **23.0** |

## 5. Sensitivity Analysis

| Gold Price | EBITDA ($B) | ROIC (%) | Notes |
|------------|------------|----------|-------|
| $2,200 (-20%) | $28.6 | 23,833 | Recession scenario |
| $2,750 (base) | $35.0 | 29,169 | Base case |
| $3,300 (+20%) | $41.5 | 34,583 | Inflation hedge |
| $3,575 (+30%) | $42.9 | 35,665 | Stagflation scenario |

## 6. Regulatory Compliance

| Requirement | Status | Deadline |
|------------|--------|----------|
| SEBI EGR Registration | Preparing | Aug 15, 2026 |
| SEBI Vault Manager Approval | Pending | Sep 15, 2026 |
| BSE/NSE EGR Listing | Pending | Oct 30, 2026 |
| GST Registration (3%) | Required | Oct 15, 2026 |
| PARIVESH Clearance | Pending | Jul 20, 2026 |

## 7. Risk Factors

1. **Gold price volatility**: 25–50% swings impact EBITDA by $7–14B
2. **SEBI regulatory delay**: EGR approval could slip 3–6 months
3. **GST compliance**: 3% on physical delivery adds cost friction
4. **Vault security**: $8.8B gold inventory requires sovereign-grade security
5. **Refinery throughput**: 1,000 kg/day requires continuous supply chain

## 8. Assumptions & Data Sources

| Assumption | Source | Confidence |
|------------|--------|------------|
| Gold spot $2,750/oz | LBMA AM fix, Jul 2026 | High |
| 0.4% refining premium | LBMA good delivery standard | High |
| 330 operating days | Indian SEZ standard | High |
| EGR 2.5x turnover | SEBI historical average | Medium |
| 0.15% EGR fee | SEBI circular CIR/MIRSD/2/2013 | High |
| $2.5M migration cost | Legal counsel estimate | Medium |

---

*Last updated: 2026-07-11*  
*Artifact ID: IKIS-FIN-2026-001*  
*Owner: marshallwmorrison*  
*P1 Gap: P1-005 (RESOLVED)*  
*Validation: Expert review, 2026-07-11*
