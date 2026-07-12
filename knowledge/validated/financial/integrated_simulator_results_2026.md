---
artifact_id: "IKIS-FIN-2026-002"
type: "financial_model"
title: "Integrated Portfolio Simulator Results — 5 Macro Scenarios (AISTA Orion, Berbera PPP, BIBC Bullion, Pizza Franchise, Ethiopia Halal)"
status: "validated"
confidence: "high"
pillar: "Portfolio"
portfolio_entity: "SSS Portfolio"
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
    - "IKIS-FIN-2026-001"
  validation_method: "expert_review"
  validated_by:
    - "marshallwmorrison"
  validated_date: "2026-07-11"
tags:
  - "portfolio"
  - "simulator"
  - "aista"
  - "berbera"
  - "bibc"
  - "pizza"
  - "ethiopia-halal"
  - "validated"
governance:
  classification: "financial"
  escalation_required: false
  legal_reviewed: false
---

# Integrated Portfolio Simulator Results — 5 Macro Scenarios

**Simulation Date:** 2026-07-11  
**Model Version:** v2.0 (AISTA terminology, P1-005/006 resolved)  
**Portfolio Weights:** AISTA 25%, Berbera 15%, BIBC 20%, Pizza 10%, Halal 15%, Cash 15%

---

## 1. Scenario Comparison Matrix

| Scenario | GDP Growth | Gold Chg | Pizza SSSG | Drought Prob | WACC Premium | Portfolio Return | Volatility | VaR 95% | Key Risk |
|----------|-----------|----------|------------|-------------|-------------|-----------------|------------|---------|----------|
| **Recession** | -2.0% | +15% | -5% | 35% | +2.0% | 50.0% | 29.3% | +1.9% | Gold volatility, drought |
| **Base** | +2.5% | +8% | +3% | 15% | 0.0% | 58.3% | 18.8% | +5.2% | Neutral |
| **Growth** | +4.5% | +12% | +6% | 5% | -1.0% | 66.7% | 15.4% | +9.2% | Optimal |
| **Inflation** | +1.0% | +25% | +1% | 20% | +1.5% | 62.5% | 24.2% | +6.7% | FX INR depreciation |
| **Stagflation** | -1.0% | +30% | -3% | 40% | +3.0% | 53.2% | 32.7% | **-2.1%** | Worst case (negative VaR) |

## 2. Individual Project Results by Scenario

### AISTA Orion

| Scenario | NPV ($B) | Prob Positive | WACC | Notes |
|----------|----------|--------------|------|-------|
| Recession | $9.83 | 94.5% | 12.8% | Political risk premium applies |
| Base | $12.15 | 97.2% | 10.8% | Optimal IRR |
| Growth | $14.67 | 98.8% | 9.8% | Best case |
| Inflation | $10.45 | 95.8% | 12.3% | Gold hedge helps |
| Stagflation | $7.21 | 88.3% | 14.8% | Political risk + FX stress |

### Berbera PPP

| Scenario | DSCR | IRR | Delay (mo) | Overrun | Covenant Status |
|----------|------|-----|------------|---------|-----------------|
| Recession | 2.06 | 22.3% | 6 | 2.5% | PASS |
| Base | 2.35 | 28.4% | 0 | 0.0% | PASS |
| Growth | 2.68 | 34.2% | 0 | 0.0% | PASS |
| Inflation | 2.18 | 25.1% | 3 | 1.5% | PASS |
| Stagflation | 1.78 | 18.5% | 9 | 4.5% | PASS (marginal) |

### BIBC Bullion

| Scenario | EBITDA ($B) | ROIC | Gold Spot | Notes |
|----------|------------|------|-----------|-------|
| Recession | $33.58 | 28,008% | $3,162 | Gold safe haven |
| Base | $35.02 | 29,169% | $2,970 | Optimal |
| Growth | $37.45 | 31,178% | $3,080 | Demand surge |
| Inflation | $40.12 | 33,400% | $3,438 | Gold hedge peak |
| Stagflation | $42.89 | 35,665% | $3,575 | Maximum gold price |

### Pizza Franchise

| Scenario | NPV ($M) | IRR | SSSG | Notes |
|----------|----------|-----|------|-------|
| Recession | $111.22 | 19.5% | -5% | Resilient (essential food) |
| Base | $127.55 | 22.1% | +3% | Optimal growth |
| Growth | $145.83 | 25.3% | +6% | Best case |
| Inflation | $118.34 | 20.5% | +1% | Margin pressure |
| Stagflation | $95.12 | 16.8% | -3% | Most vulnerable |

### Ethiopia Halal

| Scenario | Revenue ($M) | Margin | Drought Prob | Notes |
|----------|-------------|--------|-------------|-------|
| Recession | $107.49 | 48.2% | 35% | Drought risk elevated |
| Base | $118.67 | 52.1% | 15% | Optimal |
| Growth | $132.45 | 55.8% | 5% | Best case |
| Inflation | $112.15 | 50.3% | 20% | Input cost pressure |
| Stagflation | $98.34 | 45.5% | 40% | Worst case (drought + recession) |

## 3. Portfolio Risk Analysis

### Diversification Benefits
- **Gold correlation**: BIBC bullion provides inflation hedge (negative correlation with equity stress)
- **Geographic diversification**: Africa (Somaliland/Ethiopia), India (Bihar), Middle East (Berbera)
- **Sector diversification**: Mining/refining (BIBC), infrastructure (Berbera), food (Pizza, Halal), strategic minerals (AISTA)
- **Currency hedge**: INR depreciation partially offset by gold USD pricing

### Stress Test: Stagflation
- Only scenario with negative VaR 95% (-2.1%)
- BIBC bullion still delivers $42.9B EBITDA (gold price surge)
- Ethiopia Halal most vulnerable ($98M revenue, 45.5% margin)
- Berbera PPP DSCR drops to 1.78 (still above 1.5 covenant)
- **Portfolio survives** but with reduced margin of safety

## 4. P1 Gap Resolution Impact

| P1 Gap | Impact on Model | Resolution |
|--------|----------------|------------|
| P1-005 | BIBC token premium removed | EGR migration (+$21.5M EBITDA) |
| P1-006 | Pizza social media multiplier removed | 1.08x (peer-reviewed) |
| P1-007 | Portfolio overlap confirmed | 0.0% (structural independence) |

## 5. Key Recommendations

1. **Monitor stagflation signals**: Only scenario with negative VaR; consider increasing cash buffer to 20%
2. **Hedge INR exposure**: BIBC gold priced in USD but opex in INR; consider FX forwards
3. **Accelerate EGR migration**: SEBI registration critical path; delay risks $21.5M/year EBITDA
4. **Drought insurance for Ethiopia**: 40% drought probability in stagflation; parametric insurance recommended
5. **Berbera delay contingency**: 9-month delay in stagflation; pre-negotiate EPC contracts with liquidated damages

---

*Last updated: 2026-07-11*  
*Artifact ID: IKIS-FIN-2026-002*  
*Owner: marshallwmorrison*  
*Validation: Expert review, 2026-07-11*
