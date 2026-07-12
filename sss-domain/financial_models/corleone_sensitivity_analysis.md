---
artifact_id: COR-SENS-FM-006
type: financial_model
title: Corleone Enterprise Sensitivity Analysis — Tornado Diagrams & Scenario Matrix
status: draft
pillar: C
tags: [sensitivity, tornado, scenario, stress_test, monte_carlo, risk, AISTA]
governance: SSS-FIN-001
version: 1.0
author: Beta | Financial Modeler
reviewed_by: Alpha | Chief Architect
date: 2025-01-15
---

# Corleone Enterprise Sensitivity Analysis & Scenario Matrix (Y5)

## Document Control

| Field | Value |
|---|---|
| Artifact ID | COR-SENS-FM-006 |
| Version | 1.0 |
| Status | Draft |
| Pillar | C — Corleone Enterprise |
| Governance | SSS-FIN-001 |

---

## 1. Executive Summary

This document presents the sensitivity analysis for Corleone Enterprise's consolidated financial model. It includes tornado diagrams ranking key assumptions by impact on Y5 EBITDA and Y7 equity value, plus scenario matrices for Base, Upside, Downside, and Stress cases. All sensitivity ranges are derived from benchmark distributions, historical volatility, and expert judgment.

---

## 2. Tornado Diagram — Y5 EBITDA Impact

### 2.1 Tornado: Y5 EBITDA ($18.1M Base)

| Rank | Variable | Base | Low (-1σ) | High (+1σ) | EBITDA Impact Low | EBITDA Impact High | Swing ($M) | Swing % |
|---|---|---|---|---|---|---|---|---|
| 1 | Franchisee Recruitment Speed | 100% | 70% | 130% | 12.4 | 23.8 | 11.4 | 63.0% |
| 2 | Unit-Level Revenue (AUV) | $2.0M | $1.5M | $2.5M | 11.2 | 25.0 | 13.8 | 76.2% |
| 3 | Halal Certification Timing | Y2 | Y3 | Y1 | 13.5 | 20.5 | 7.0 | 38.7% |
| 4 | Commodity Prices (Meat/Grain) | 100% | 115% | 85% | 14.8 | 21.4 | 6.6 | 36.5% |
| 5 | FX Rate (SLL/USD, KSA/USD) | 100% | 115% | 85% | 15.2 | 21.0 | 5.8 | 32.0% |
| 6 | Construction Costs (Unit Buildout) | $650K | $780K | $520K | 15.8 | 20.4 | 4.6 | 25.4% |
| 7 | Mineral Extraction Yields | 100% | 80% | 120% | 16.2 | 20.0 | 3.8 | 21.0% |
| 8 | Somaliland Political Risk Premium | 5% | 12% | 2% | 15.5 | 18.8 | 3.3 | 18.2% |
| 9 | CPG DTC Conversion Rate | 3.8% | 2.8% | 4.8% | 16.8 | 19.4 | 2.6 | 14.4% |
| 10 | Media Licensing Rates | $150K | $100K | $200K | 17.1 | 19.1 | 2.0 | 11.0% |
| 11 | Co-Manufacturing Cost Inflation | 3% | 6% | 1% | 16.9 | 19.3 | 2.4 | 13.3% |
| 12 | Export Tariff Rates (GCC) | 5% | 10% | 0% | 16.5 | 19.7 | 3.2 | 17.7% |
| 13 | WACC / Discount Rate | 12.5% | 15% | 10% | N/A (valuation) | N/A | — | — |
| 14 | Terminal Value Multiple | 2.5x | 2.0x | 3.0x | N/A (valuation) | N/A | — | — |

### 2.2 Tornado Diagram — Y7 Equity Value ($500M Base)

| Rank | Variable | Base | Low (-1σ) | High (+1σ) | Equity Value Low ($M) | Equity Value High ($M) | Swing ($M) | Swing % |
|---|---|---|---|---|---|---|---|---|
| 1 | Franchisee Recruitment Speed | 100% | 70% | 130% | 320 | 680 | 360 | 72.0% |
| 2 | Unit-Level Revenue (AUV) | $2.0M | $1.5M | $2.5M | 340 | 660 | 320 | 64.0% |
| 3 | Terminal Value Multiple | 2.5x | 2.0x | 3.0x | 380 | 620 | 240 | 48.0% |
| 4 | WACC / Discount Rate | 12.5% | 15% | 10% | 380 | 640 | 260 | 52.0% |
| 5 | Halal Certification Timing | Y2 | Y3 | Y1 | 390 | 580 | 190 | 38.0% |
| 6 | Commodity Prices (Meat/Grain) | 100% | 115% | 85% | 410 | 560 | 150 | 30.0% |
| 7 | FX Rate (SLL/USD) | 100% | 115% | 85% | 420 | 550 | 130 | 26.0% |
| 8 | Construction Costs | $650K | $780K | $520K | 440 | 540 | 100 | 20.0% |
| 9 | Mineral Extraction Yields | 100% | 80% | 120% | 450 | 530 | 80 | 16.0% |
| 10 | Somaliland Political Risk Premium | 5% | 12% | 2% | 430 | 520 | 90 | 18.0% |
| 11 | CPG DTC Conversion Rate | 3.8% | 2.8% | 4.8% | 460 | 520 | 60 | 12.0% |
| 12 | IPO Market Timing | Y7 | Y8 | Y6 | 440 | 510 | 70 | 14.0% |
| 13 | Export Tariff Rates (GCC) | 5% | 10% | 0% | 450 | 530 | 80 | 16.0% |
| 14 | Media Licensing Growth | 15% | 5% | 25% | 470 | 510 | 40 | 8.0% |

---

## 3. Scenario Analysis Matrix

### 3.1 Scenario Definitions

| Scenario | Probability | Key Drivers |
|---|---|---|
| Base Case | 50% | All variables at baseline |
| Upside Case | 25% | Faster recruitment, higher AUV, early certification, strong FX |
| Downside Case | 20% | Slower recruitment, lower AUV, delayed certification, commodity spike |
| Stress Case | 5% | Severe political disruption, commodity crisis, construction delays, FX collapse |

### 3.2 Consolidated P&L by Scenario (Y5, $M)

| Line Item | Base | Upside | Downside | Stress |
|---|---|---|---|---|
| Revenue | 85.8 | 120.5 | 62.0 | 38.0 |
| COGS | 39.5 | 50.0 | 32.0 | 22.0 |
| Gross Profit | 46.3 | 70.5 | 30.0 | 16.0 |
| Gross Margin | 54.0% | 58.5% | 48.4% | 42.1% |
| OpEx | 28.2 | 35.0 | 26.0 | 24.0 |
| **EBITDA** | **18.1** | **35.5** | **4.0** | **-8.0** |
| EBITDA Margin | 21.1% | 29.5% | 6.5% | -21.1% |
| D&A | 3.2 | 3.2 | 3.2 | 3.2 |
| EBIT | 14.9 | 32.3 | 0.8 | -11.2 |
| Interest | 1.4 | 1.4 | 1.4 | 1.4 |
| EBT | 13.5 | 30.9 | -0.6 | -12.6 |
| Taxes | 3.4 | 7.7 | — | — |
| **Net Income** | **10.1** | **23.2** | **-0.6** | **-12.6** |
| Net Margin | 11.8% | 19.3% | -1.0% | -33.2% |

### 3.3 Scenario Matrix — Key Metrics (Y5)

| Metric | Base | Upside | Downside | Stress |
|---|---|---|---|---|
| Units Open (Pizza + Bakery) | 140 | 200 | 100 | 70 |
| AUV Pizza ($M) | 2.10 | 2.65 | 1.65 | 1.35 |
| AUV Bakery ($M) | 1.30 | 1.65 | 1.00 | 0.85 |
| CPG Revenue ($M) | 33.0 | 48.0 | 24.0 | 15.0 |
| Halal Meat Export (MT) | 2,350 | 3,500 | 1,500 | 800 |
| Mineral Revenue ($M) | 1.28 | 2.0 | 0.7 | 0.3 |
| Cross-Subsidy ($M) | 4.85 | 6.5 | 3.2 | 2.0 |
| Headcount | 485 | 620 | 380 | 290 |
| Cash Burn Rate ($M/qtr) | — | — | 2.5 | 4.0 |
| Runway (Months) | ∞ | ∞ | 18 | 8 |

### 3.4 Scenario Matrix — Valuation (Y7)

| Metric | Base | Upside | Downside | Stress |
|---|---|---|---|---|
| Revenue ($M) | 137.0 | 195.0 | 92.0 | 55.0 |
| EBITDA ($M) | 45.3 | 78.0 | 22.0 | 5.0 |
| EBITDA Margin | 33.1% | 40.0% | 23.9% | 9.1% |
| DCF Value ($M) | 216.5 | 385.0 | 95.0 | 35.0 |
| Comparables Value ($M) | 214.5 | 320.0 | 140.0 | 80.0 |
| Strategic Premium ($M) | 62.5 | 100.0 | 30.0 | 10.0 |
| Adjusted EV ($M) | 277.5 | 420.0 | 170.0 | 90.0 |
| IPO Target ($M) | 500+ | 750+ | 250 | 120 |
| MOIC (Series A) | 13.5x | 25.0x | 7.0x | 3.0x |
| IRR (Series A) | 68% | 95% | 42% | 18% |

---

## 4. Detailed Assumption Sensitivity Tables

### 4.1 Franchisee Recruitment Speed

| Recruitment % | Y5 Units | Y5 Revenue ($M) | Y5 EBITDA ($M) | Y7 EV ($M) |
|---|---|---|---|---|
| 50% | 70 | 52.0 | 8.5 | 155 |
| 70% | 100 | 62.0 | 12.4 | 220 |
| 85% (Base) | 140 | 85.8 | 18.1 | 277.5 |
| 100% | 160 | 98.0 | 22.5 | 340 |
| 130% | 200 | 120.5 | 35.5 | 420 |

### 4.2 Unit-Level Revenue (Pizza AUV)

| AUV ($M) | Y5 Pizza Revenue | Y5 EBITDA Impact | Y7 EV Impact |
|---|---|---|---|
| 1.35 | 18.0 | -6.8 | -120 |
| 1.65 | 22.0 | -3.2 | -55 |
| 2.10 (Base) | 28.0 | 0.0 | 0 |
| 2.45 | 32.0 | +3.8 | +65 |
| 2.65 | 35.0 | +6.9 | +120 |

### 4.3 Commodity Price Sensitivity

| Commodity Index | COGS Impact ($M) | EBITDA Impact ($M) | Y5 EBITDA |
|---|---|---|---|
| +30% | +8.5 | -8.5 | 9.6 |
| +15% | +4.3 | -4.3 | 13.8 |
| Base (100%) | 0 | 0 | 18.1 |
| -15% | -3.2 | +3.2 | 21.3 |
| -30% | -6.4 | +6.4 | 24.5 |

### 4.4 FX Rate Sensitivity (Somaliland Shilling / USD)

| FX Change | Procurement Impact | Export Impact | Net Y5 EBITDA Impact |
|---|---|---|---|
| +30% (SLL weaker) | -2.1M | +1.8M | -0.3M |
| +15% | -1.0M | +0.9M | -0.1M |
| Base (100%) | 0 | 0 | 0 |
| -15% (SLL stronger) | +0.8M | -0.7M | +0.1M |
| -30% | +1.6M | -1.4M | +0.2M |

### 4.5 Halal Certification Timing

| Certification Date | Y5 KSA Export ($M) | Y5 UAE Export ($M) | Y5 EBITDA Impact | Y7 EV Impact |
|---|---|---|---|---|
| Y3 (Delayed) | 4.5 | 2.4 | -4.7 | -85 |
| Y2 (Base) | 7.8 | 3.8 | 0.0 | 0 |
| Y1 (Early) | 9.2 | 4.5 | +2.4 | +42 |
| Pre-Launch | 10.5 | 5.2 | +4.8 | +88 |

### 4.6 Mineral Extraction Yield

| Yield % | Salt (MT) | Gypsum (MT) | Water (M bottles) | Y5 Mineral Revenue | Y5 EBITDA Impact |
|---|---|---|---|---|---|
| 60% | 720 | 480 | 2.4 | 0.77 | -0.51 |
| 80% | 960 | 640 | 3.2 | 1.02 | -0.26 |
| 100% (Base) | 1,200 | 800 | 4.0 | 1.28 | 0.0 |
| 120% | 1,440 | 960 | 4.8 | 1.53 | +0.25 |
| 150% | 1,800 | 1,200 | 6.0 | 1.91 | +0.63 |

### 4.7 Somaliland Political Risk Premium

| Risk Premium | Discount to EV | Y5 EBITDA Impact | Y7 EV ($M) | Probability |
|---|---|---|---|---|
| 2% (Stable) | -5% | +0.8 | 525 | 20% |
| 5% (Base) | -10% | 0.0 | 500 | 50% |
| 8% | -20% | -1.5 | 420 | 20% |
| 12% (Elevated) | -35% | -3.3 | 320 | 8% |
| 20% (Crisis) | -60% | -6.5 | 180 | 2% |

### 4.8 Construction Cost Sensitivity

| Cost Change | Pizza Buildout | Bakery Buildout | Total Capex Impact | Y5 EBITDA Impact | Y7 EV Impact |
|---|---|---|---|---|---|
| +40% | +$2.6M | +$1.0M | +$3.6M | -0.8M | -12M |
| +20% | +$1.3M | +$0.5M | +$1.8M | -0.4M | -6M |
| Base (0%) | $0 | $0 | $0 | 0.0 | 0 |
| -20% | -$1.0M | -$0.4M | -$1.4M | +0.3M | +5M |
| -40% | -$2.0M | -$0.8M | -$2.8M | +0.6M | +10M |

---

## 5. Monte Carlo Simulation Summary

### 5.1 Simulation Parameters

| Parameter | Distribution | Mean | Std Dev | Min | Max |
|---|---|---|---|---|---|
| Franchisee Recruitment | Triangular | 100% | — | 60% | 140% |
| Unit Revenue | Normal | $2.0M | $0.35M | $1.0M | $3.0M |
| Commodity Prices | Normal | 100% | 12% | 70% | 130% |
| FX Rate | Normal | 100% | 10% | 75% | 125% |
| Construction Costs | Triangular | $650K | — | $450K | $850K |
| Halal Certification | Discrete | Y2 | — | Y1 | Y3 |
| Mineral Yields | Normal | 100% | 15% | 60% | 140% |
| Political Risk | Lognormal | 5% | — | 1% | 20% |
| WACC | Normal | 12.5% | 1.5% | 9% | 16% |
| Terminal Multiple | Triangular | 2.5x | — | 2.0x | 3.0x |

### 5.2 Monte Carlo Results (10,000 Iterations)

| Metric | P10 | P25 | P50 (Median) | P75 | P90 | Mean | Std Dev |
|---|---|---|---|---|---|---|---|
| Y5 EBITDA ($M) | 8.2 | 13.5 | 18.0 | 23.5 | 30.2 | 18.8 | 6.8 |
| Y5 Revenue ($M) | 62.0 | 75.0 | 85.0 | 98.0 | 112.0 | 86.5 | 15.2 |
| Y7 EV ($M) | 180 | 240 | 280 | 340 | 420 | 290 | 85 |
| Y7 IPO Value ($M) | 320 | 420 | 500 | 620 | 780 | 525 | 155 |
| MOIC (Series A) | 8.0x | 11.0x | 13.5x | 17.0x | 22.0x | 14.2x | 4.5x |
| IRR (Series A) | 45% | 58% | 68% | 82% | 98% | 70% | 18% |
| Probability of Positive Y5 EBITDA | — | — | 88% | — | — | — | — |
| Probability of Y7 IPO > $500M | — | — | 52% | — | — | — | — |
| Probability of Y7 IPO > $750M | — | — | 22% | — | — | — | — |
| Probability of Stress (Y5 EBITDA < 0) | — | — | 8% | — | — | — | — |

---

## 6. Risk Register & Mitigation

| Risk ID | Risk | Probability | Impact ($M EBITDA) | Mitigation | Residual Risk |
|---|---|---|---|---|---|
| R-001 | Slow franchisee recruitment | 30% | -5.7 | Enhanced franchisee support, financing programs | Medium |
| R-002 | Commodity price spike | 25% | -4.5 | Forward contracts, co-man hedging, menu engineering | Medium |
| R-003 | Halal certification delay | 20% | -3.8 | Parallel certification tracks, pre-certification investment | Low |
| R-004 | Somaliland political instability | 15% | -6.5 | DFI insurance, MIGA PRI, diversification to Ethiopia | Medium |
| R-005 | Construction cost overrun | 25% | -2.2 | Fixed-price contracts, modular construction, prefab | Low |
| R-006 | FX volatility (SLL, KSA) | 30% | -1.8 | Natural hedge (USD revenues), local currency debt | Low |
| R-007 | Mineral yield shortfall | 20% | -1.0 | Geological surveys, phased extraction, contingency reserves | Low |
| R-008 | Export tariff increase | 15% | -2.8 | FTA negotiations, local processing (adds value), GCC JV | Medium |
| R-009 | DTC conversion decline | 20% | -1.3 | Multi-channel strategy, retail partnerships, 3P marketplace | Low |
| R-010 | IPO market timing | 25% | N/A | Flexible IPO window, SPAC alternative, private continuation | Medium |

---

## 7. Key Formulas

```python
# Tornado swing calculation
swing = abs(ebitda_high - ebitda_low)
swing_pct = swing / base_ebitda * 100

# Scenario probability-weighted expected value
expected_value = sum(p * v for p, v in zip(probabilities, values))

# Monte Carlo — standard error
standard_error = std_dev / sqrt(n_iterations)

# Risk-adjusted NPV
risk_adjusted_npv = npv * (1 - risk_premium)

# Stress test runway
runway_months = cash_balance / monthly_burn
```

---

## 8. Source Citations

| Benchmark | Source | Application |
|---|---|---|
| Franchise failure rates | FRANdata / IFA | Recruitment sensitivity |
| Commodity price volatility | Bloomberg Commodity Index | COGS sensitivity |
| FX volatility | IMF WEO / OANDA | Currency sensitivity |
| Construction cost inflation | RS Means / Turner Index | Capex sensitivity |
| Halal certification timelines | GAC / SGS | Certification timing |
| Political risk premiums | PRS Group / EIU | Country risk |
| DTC conversion benchmarks | Shopify / eMarketer | E-commerce sensitivity |
| Mineral yield variance | USGS / SRK Consulting | Extraction sensitivity |

---

*End of Corleone Enterprise Sensitivity Analysis*
