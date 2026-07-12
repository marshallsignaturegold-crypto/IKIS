---
artifact_id: COR-FUND-FM-008
type: financial_model
title: CEI Fund Architecture — ETN, Growth, Income, Emerging Markets
status: draft
pillar: C
tags: [fund_architecture, etn, growth_fund, income_fund, emerging_markets, aum, fee_structure, AISTA]
governance: SSS-FIN-001
version: 1.0
author: Beta | Financial Modeler
reviewed_by: Alpha | Chief Architect
date: 2025-01-15
---

# CEI Fund Architecture Model — AISTA Sovereign Wealth Products (Y1–Y10)

## Document Control

| Field | Value |
|---|---|
| Artifact ID | COR-FUND-FM-008 |
| Version | 1.0 |
| Status | Draft |
| Pillar | C — Corleone Enterprise |
| Governance | SSS-FIN-001 |

---

## 1. Executive Summary

The CEI (Corleone Enterprise Index) Fund Architecture is the capital-raising and asset-management pillar of the AISTA ecosystem. It comprises four vehicles: (1) the CEI Index (ETN) providing liquid exposure to the CE operating performance; (2) the CEI Growth Fund (open-end, $75M target) investing in CE equity and expansion; (3) the CEI Income Fund (closed-end REIT, $50M target) monetizing corridor real estate and infrastructure; and (4) the CEI Emerging Markets Fund (PE-style, $25M target) capturing frontier-market opportunities along the AISTA Corridor. This model details mechanics, tracking, AUM projections, fee structures, redemption terms, investor targeting, and marketing strategy.

---

## 2. CEI Index (ETN) — Exchange-Traded Note

### 2.1 ETN Mechanics

| Parameter | Specification |
|---|---|
| Issuer | Corleone Enterprise SPV (Cayman) |
| Underlying | Custom CEI Index |
| Index Composition | 40% Revenue-Weighted (Pizza, Bakery, Products, Media, Halal) + 30% Asset-Weighted (PP&E, IP, Concessions) + 20% EBITDA-Weighted + 10% Mineral Reserve-Weighted |
| Issuance Currency | USD |
| Maturity | 10 years (callable Y5) |
| Coupon | 3.5% p.a. (accrued, paid at maturity or call) |
| Tracking Error Target | < 50 bps p.a. |
| Listing Venue | OTC (Y1–Y3), Luxembourg Stock Exchange (Y4+) |
| ISIN Prefix | XS |
| CUSIP | 21085P |

### 2.2 Index Calculation Formula

```
CEI Index_t = CEI_{t-1} * (1 + r_t)

where r_t = (w_rev * Revenue_Growth_t) + (w_asset * Asset_Growth_t) + (w_ebitda * EBITDA_Growth_t) + (w_mineral * Mineral_Reserve_Growth_t)

w_rev = 0.40, w_asset = 0.30, w_ebitda = 0.20, w_mineral = 0.10

Revenue_Growth_t = (Rev_t - Rev_{t-1}) / Rev_{t-1}
Asset_Growth_t = (Assets_t - Assets_{t-1}) / Assets_{t-1}
EBITDA_Growth_t = (EBITDA_t - EBITDA_{t-1}) / EBITDA_{t-1}  [if EBITDA_{t-1} > 0, else 0]
Mineral_Reserve_Growth_t = (Proven_Reserves_t - Proven_Reserves_{t-1}) / Proven_Reserves_{t-1}
```

### 2.3 Index Historical & Projected Values

| Year | Revenue ($M) | Assets ($M) | EBITDA ($M) | Mineral Reserves (MT) | Index Level | Index Return | Cumulative Return |
|---|---|---|---|---|---|---|---|
| Y0 | — | 4.0 | -0.7 | 0 | 100.00 | — | — |
| Y1 | 5.7 | 15.2 | -2.2 | 0 | 95.50 | -4.50% | -4.50% |
| Y2 | 19.1 | 15.1 | -1.3 | 0 | 101.20 | +6.02% | +1.20% |
| Y3 | 37.9 | 39.5 | 4.9 | 1,200 | 118.40 | +17.00% | +18.40% |
| Y4 | 60.2 | 53.0 | 10.6 | 2,800 | 138.50 | +16.98% | +38.50% |
| Y5 | 85.8 | 85.1 | 18.1 | 5,200 | 165.00 | +19.13% | +65.00% |
| Y6 | 111.0 | 110.2 | 34.0 | 8,000 | 198.00 | +20.00% | +98.00% |
| Y7 | 137.0 | 161.3 | 45.3 | 12,000 | 235.00 | +18.69% | +135.00% |
| Y8 | 163.0 | 197.4 | 56.6 | 16,000 | 272.00 | +15.74% | +172.00% |
| Y9 | 189.0 | 243.5 | 67.9 | 20,000 | 308.00 | +13.24% | +208.00% |
| Y10 | 215.0 | 299.6 | 79.2 | 24,000 | 342.00 | +11.04% | +242.00% |

### 2.4 ETN Issuance & AUM ($M)

| Year | Units Issued (M) | Avg Price | Gross Issuance | Redemptions | Net AUM | Coupon Accrued | Total Liability |
|---|---|---|---|---|---|---|---|
| Y1 | 2.0 | $95.50 | $191.0 | — | $191.0 | $6.7 | $197.7 |
| Y2 | 1.5 | $101.20 | $151.8 | — | $342.8 | $12.0 | $354.8 |
| Y3 | 2.5 | $118.40 | $296.0 | — | $638.8 | $22.4 | $661.2 |
| Y4 | 3.0 | $138.50 | $415.5 | — | $1,054.3 | $36.9 | $1,091.2 |
| Y5 | 4.0 | $165.00 | $660.0 | $50.0 | $1,664.3 | $58.3 | $1,722.6 |
| Y6 | 3.0 | $198.00 | $594.0 | $100.0 | $2,158.3 | $75.5 | $2,233.8 |
| Y7 | 2.0 | $235.00 | $470.0 | $200.0 | $2,428.3 | $85.0 | $2,513.3 |
| Y8 | 1.5 | $272.00 | $408.0 | $150.0 | $2,686.3 | $94.0 | $2,780.3 |
| Y9 | 1.0 | $308.00 | $308.0 | $100.0 | $2,894.3 | $101.3 | $2,995.6 |
| Y10 | 0.5 | $342.00 | $171.0 | $100.0 | $2,965.3 | $103.8 | $3,069.1 |

### 2.5 ETN Risk & Hedging

| Risk Factor | Exposure | Hedge Instrument | Cost (% of AUM) |
|---|---|---|---|
| CE Revenue Volatility | Direct | Internal rebalancing (subsidiary swaps) | 0.10% |
| FX (SLL, KSA, AED) | Indirect | Forward contracts, NDFs | 0.15% |
| Commodity (meat, grain) | Indirect | Futures, options collars | 0.12% |
| Credit (CE SPV) | Issuer risk | CDS (if available), collateral posting | 0.08% |
| Interest Rate | Coupon / discounting | IRS, floating-rate reset | 0.05% |
| **Total Hedging Cost** | — | — | **0.50%** |

---

## 3. CEI Growth Fund (Open-End, $75M Target)

### 3.1 Fund Parameters

| Parameter | Specification |
|---|---|
| Structure | Open-End Investment Company (OEIC) — Luxembourg SICAV |
| Target AUM | $75.0M |
| Base Currency | USD |
| Investment Focus | Corleone Enterprise equity (primary + secondary), expansion capex, technology platform |
| Domicile | Luxembourg |
| Administrator | Apex Group |
| Custodian | BNY Mellon |
| Auditor | PwC Luxembourg |
| Regulatory | CSSF (Lux), SEC 3(c)(1) (US) |
| Fund Manager | AISTA Capital Management (Pillar B) |
| Initial Closing | Y3 Q2 |
| Final Closing | Y4 Q4 |

### 3.2 Investment Strategy & Allocation

| Asset Class | Target % | Min | Max | Y5 AUM ($M) | Y10 AUM ($M) |
|---|---|---|---|---|---|
| CE Common Equity | 40% | 30% | 50% | 30.0 | 120.0 |
| CE Preferred Equity (Series B/C) | 25% | 20% | 35% | 18.8 | 75.0 |
| Expansion Capex (Convertible) | 15% | 10% | 20% | 11.3 | 45.0 |
| Technology Platform (IP / SaaS) | 10% | 5% | 15% | 7.5 | 30.0 |
| Cash / Equivalents | 10% | 5% | 20% | 7.5 | 30.0 |
| **Total** | **100%** | — | — | **75.0** | **300.0** |

### 3.3 Fee Structure

| Fee Type | Rate | Base | Annual Amount (Y5, $M) | Annual Amount (Y10, $M) |
|---|---|---|---|---|
| Management Fee | 2.0% p.a. | NAV | $1.50 | $6.00 |
| Performance Fee | 20% | Hurdle 8% | $0.00 (below hurdle) | $4.80 |
| Hurdle Rate | 8.0% p.a. | Preferred return | — | — |
| High Water Mark | Yes | Reset annually | — | — |
| Clawback | 3-year | Look-back | — | — |
| Subscription Fee | 0% | — | — | — |
| Redemption Fee | 1% | < 2 years | — | — |
| **Total Fee Burden (Y5)** | — | — | **$1.50M** | **$10.80M** |
| **Total Fee Burden (% AUM)** | — | — | **2.00%** | **3.60%** |

### 3.4 Redemption Terms

| Term | Specification |
|---|---|
| Redemption Frequency | Quarterly (Q1, Q3) with 45-day notice |
| Gate Provision | 10% of NAV per quarter if requests exceed 15% |
| Lock-Up | 12 months from initial subscription |
| Redemption Fee | 1% if < 24 months; 0.5% if 24–36 months; 0% if > 36 months |
| Side Pockets | Applied to illiquid investments (capex, IP) — 3-year realization |
| NAV Calculation | Monthly (administrator), audited quarterly |
| Cut-Off | 15th of month preceding quarter-end |
| Settlement | T+15 |

### 3.5 AUM & Return Projections ($M)

| Year | Beginning AUM | Inflows | Outflows | Performance | Ending AUM | NAV/Unit | Cumulative Return |
|---|---|---|---|---|---|---|---|
| Y3 | — | 25.0 | — | — | 25.0 | $100.00 | — |
| Y4 | 25.0 | 30.0 | — | 3.0 | 58.0 | $116.00 | +16.0% |
| Y5 | 58.0 | 20.0 | 3.0 | 8.7 | 83.7 | $139.50 | +39.5% |
| Y6 | 83.7 | 15.0 | 5.0 | 16.7 | 110.4 | $184.00 | +84.0% |
| Y7 | 110.4 | 10.0 | 8.0 | 22.1 | 134.5 | $224.17 | +124.2% |
| Y8 | 134.5 | 5.0 | 10.0 | 26.9 | 156.4 | $260.67 | +160.7% |
| Y9 | 156.4 | 5.0 | 12.0 | 31.3 | 180.7 | $301.17 | +201.2% |
| Y10 | 180.7 | 5.0 | 15.0 | 36.1 | 206.8 | $344.67 | +244.7% |

### 3.6 Investor Types & Target Allocations

| Investor Type | Target % | Ticket Size | Lock-Up | Geographic Focus |
|---|---|---|---|---|
| Family Offices | 30% | $2–5M | 24 months | US, UAE, KSA |
| High-Net-Worth Individuals | 20% | $0.5–2M | 12 months | US, EU, GCC |
| Sovereign Wealth / Public Funds | 20% | $5–15M | 36 months | GCC, SE Asia |
| Pension Funds (Endowment Model) | 15% | $3–8M | 36 months | US, EU |
| DFI / Development Finance | 10% | $2–5M | 48 months | Global |
| Corporate / Strategic | 5% | $1–3M | 24 months | GCC, Africa |
| **Total** | **100%** | — | — | — |

---

## 4. CEI Income Fund (Closed-End REIT, $50M Target)

### 4.1 Fund Parameters

| Parameter | Specification |
|---|---|
| Structure | Closed-End Real Estate Investment Trust (REIT) — US Delaware |
| Target Equity | $50.0M |
| Leverage Target | 50% LTV (max 60%) |
| Total Asset Value | $100.0M |
| Base Currency | USD |
| Investment Focus | AISTA Corridor real estate, logistics hubs, cold chain facilities, retail properties, mineral extraction sites |
| Domicile | Delaware, USA |
| Property Manager | Corleone Real Estate SPV |
| Administrator | SS&C Technologies |
| Custodian | State Street |
| Auditor | KPMG |
| Regulatory | SEC (US-REIT), FCA (UK notification) |
| IPO / Listing | Y5 — OTC or small-cap exchange |
| Term | 7 years with 2-year extension |

### 4.2 Portfolio Allocation (Y5)

| Property Type | Properties | Location | Acquisition Cost ($M) | LTV | Equity | Yield Target | Occupancy |
|---|---|---|---|---|---|---|---|
| Logistics Hubs | 3 | Dubai, Jeddah, Hargeisa | 25.0 | 50% | 12.5 | 8.0% | 92% |
| Cold Chain Facilities | 2 | Berbera, Jeddah | 15.0 | 55% | 6.75 | 7.5% | 88% |
| Retail / Mixed-Use | 4 | Minneapolis, Columbus, Dubai, Riyadh | 20.0 | 45% | 11.0 | 7.0% | 85% |
| Mineral Extraction Sites | 2 | Lake Assal (Salt), Ainabo (Gypsum) | 10.0 | 40% | 6.0 | 9.0% | 95% (concession) |
| Development Land | 3 | AISTA Corridor nodes | 15.0 | 0% | 15.0 | 0% (appreciation) | N/A |
| **Total** | **14** | — | **85.0** | **46%** | **51.25** | **7.2% blended** | **89%** |

### 4.3 Fee Structure

| Fee Type | Rate | Base | Annual Amount (Y5, $M) | Annual Amount (Y10, $M) |
|---|---|---|---|---|
| Base Management Fee | 1.5% p.a. | Gross Asset Value | $1.28 | $2.25 |
| Performance Fee | 15% | NAV > 8% hurdle | $0.00 | $1.50 |
| Acquisition Fee | 1.5% | Purchase price | $0.75 | — |
| Disposition Fee | 1.0% | Sale price | — | $0.80 |
| Property Management Fee | 3.0% | Effective gross income | $0.18 | $0.30 |
| Financing Fee | 0.5% | Debt arranged | $0.20 | $0.15 |
| **Total Fee Burden (Y5)** | — | — | **$2.41M** | **$5.00M** |
| **Total Fee Burden (% NAV)** | — | — | **4.70%** | **4.00%** |

### 4.4 Distribution Policy

| Distribution Type | Frequency | Target | Y5 ($M) | Y10 ($M) |
|---|---|---|---|---|
| Ordinary Dividend | Quarterly | 90% of NOI | $2.80 | $5.20 |
| Special Dividend | Annual | 50% of asset sales | — | $2.00 |
| DRIP (Dividend Reinvestment) | Optional | 5% discount to NAV | — | — |
| **Total Distributions** | — | — | **$2.80M** | **$7.20M** |
| **Distribution Yield (% NAV)** | — | — | **5.50%** | **5.80%** |

### 4.5 AUM & NAV Projections ($M)

| Year | Beginning NAV | Capital Calls | Distributions | NOI | Appreciation | Ending NAV | NAV/Share | Distribution Yield |
|---|---|---|---|---|---|---|---|---|
| Y3 | — | 15.0 | — | — | — | 15.0 | $15.00 | — |
| Y4 | 15.0 | 20.0 | -0.5 | 1.2 | 0.8 | 36.5 | $36.50 | — |
| Y5 | 36.5 | 15.0 | -1.5 | 3.8 | 2.5 | 56.3 | $56.30 | 5.5% |
| Y6 | 56.3 | 10.0 | -2.8 | 5.5 | 3.5 | 72.5 | $72.50 | 5.2% |
| Y7 | 72.5 | — | -3.5 | 6.8 | 4.2 | 80.0 | $80.00 | 5.6% |
| Y8 | 80.0 | — | -4.0 | 7.5 | 4.5 | 88.0 | $88.00 | 5.7% |
| Y9 | 88.0 | — | -4.5 | 8.2 | 5.0 | 96.7 | $96.70 | 5.8% |
| Y10 | 96.7 | — | -5.0 | 9.0 | 5.5 | 106.2 | $106.20 | 5.8% |

---

## 5. CEI Emerging Markets Fund (PE-Style, $25M Target)

### 5.1 Fund Parameters

| Parameter | Specification |
|---|---|
| Structure | Private Equity Fund — Cayman Islands Limited Partnership |
| Target Committed Capital | $25.0M |
| Investment Period | 3 years |
| Harvest Period | 4 years |
| Total Term | 7 years + 2-year extension |
| Base Currency | USD |
| Investment Focus | Frontier-market SMEs, corridor logistics, ag-tech, mineral processing, halal supply chain |
| Domicile | Cayman Islands |
| GP | AISTA Capital Management (Pillar B) |
| LP | Institutional investors, family offices, DFI |
| Administrator | MUFG Fund Services |
| Custodian | Citibank |
| Auditor | EY Cayman |
| Regulatory | CIMA, AIFMD (EU marketing) |
| First Close | Y3 Q1 |
| Final Close | Y3 Q4 |
| Vintage Year | Y3 |

### 5.2 Investment Strategy & Allocation

| Sector | Target % | Min | Max | Geographic Focus | Y5 Deployed ($M) | Y10 Realized ($M) |
|---|---|---|---|---|---|---|
| Logistics & Transport | 25% | 20% | 30% | Somaliland, Ethiopia, Djibouti | 6.25 | 18.0 |
| Ag-Tech & Food Processing | 25% | 20% | 30% | Kenya, Uganda, Somaliland | 6.25 | 15.0 |
| Mineral Processing | 20% | 15% | 25% | Somaliland, Ethiopia | 5.00 | 12.0 |
| Halal Supply Chain | 15% | 10% | 20% | KSA, UAE, Egypt | 3.75 | 8.0 |
| Fintech / Trade Finance | 10% | 5% | 15% | East Africa, GCC | 2.50 | 5.0 |
| Reserve / Follow-On | 5% | 0% | 10% | Various | 1.25 | 3.0 |
| **Total** | **100%** | — | — | — | **25.0** | **61.0** |

### 5.3 Fee Structure (Standard 2/20 with Modifications)

| Fee Type | Rate | Base | Y5 Annual ($M) | Y10 Annual ($M) |
|---|---|---|---|---|
| Management Fee | 2.0% p.a. | Committed Capital (Y1–3), then Invested Capital | $0.50 | $0.40 |
| Management Fee (Step-Down) | 1.5% p.a. | Y4+ on invested capital | — | $0.30 |
| Performance Fee (Carried Interest) | 20% | Above 8% hurdle | $0.00 | $3.20 |
| Hurdle Rate | 8.0% p.a. | Preferred return, compounded | — | — |
| Catch-Up | 100% | GP receives 100% of profits until 20% of total profits | — | — |
| Clawback | 3-year | Look-back at final liquidation | — | — |
| Organization Expense | 1.0% | Committed capital (one-time) | $0.25 | — |
| Deal Sourcing Fee | 1.0% | Investment cost | $0.25 | — |
| Monitoring Fee | 1.0% p.a. | Portfolio company revenue | $0.15 | $0.30 |
| **Total Fee Burden (Y5)** | — | — | **$1.15M** | **$4.20M** |
| **Total Fee Burden (% Committed)** | — | — | **4.60%** | **16.80%** |

### 5.4 Waterfall & Distribution

| Tier | Return Threshold | Distribution Split |
|---|---|---|
| Return of Capital | 0% | 100% LP, 0% GP |
| Preferred Return | 8% p.a. | 100% LP, 0% GP |
| Catch-Up | 8%–10% | 100% GP until 20% share |
| Carried Interest | > 10% | 80% LP, 20% GP |
| GP Clawback | If final < 8% | GP returns excess |

### 5.5 Capital Call & Distribution Schedule ($M)

| Year | Committed Capital | Capital Called | Cumulative Invested | Realizations | Distributions | NAV |
|---|---|---|---|---|---|---|
| Y3 | 25.0 | 10.0 | 10.0 | — | — | 10.0 |
| Y4 | 25.0 | 8.0 | 18.0 | — | — | 18.5 |
| Y5 | 25.0 | 5.0 | 23.0 | — | — | 25.0 |
| Y6 | 25.0 | 2.0 | 25.0 | 2.0 | 1.5 | 28.0 |
| Y7 | 25.0 | — | 25.0 | 8.0 | 6.0 | 32.0 |
| Y8 | 25.0 | — | 25.0 | 15.0 | 12.0 | 28.0 |
| Y9 | 25.0 | — | 25.0 | 20.0 | 18.0 | 22.0 |
| Y10 | 25.0 | — | 25.0 | 16.0 | 20.0 | 12.0 |
| **Total** | **25.0** | **25.0** | — | **61.0** | **57.5** | — |

*MOIC: 61.0 / 25.0 = 2.44x; DPI: 57.5 / 25.0 = 2.30x; RVPI: 12.0 / 25.0 = 0.48x*

### 5.6 IRR Projections

| Scenario | MOIC | IRR | DPI | RVPI |
|---|---|---|---|---|
| Base Case | 2.44x | 22.0% | 2.30x | 0.48x |
| Upside Case | 3.50x | 32.0% | 3.20x | 0.30x |
| Downside Case | 1.60x | 12.0% | 1.40x | 0.20x |
| Stress Case | 0.80x | -5.0% | 0.70x | 0.10x |

---

## 6. Marketing Strategy & Investor Roadmap

### 6.1 Marketing Timeline

| Phase | Period | Activity | Target AUM ($M) |
|---|---|---|---|
| Phase 1: Seed / Anchor | Y1–Y2 | SSS Firm commitment, strategic cornerstone | 10.0 |
| Phase 2: First Close | Y3 Q1–Q2 | DFI, family offices, sovereign wealth | 40.0 |
| Phase 3: Final Close | Y3 Q3–Q4 | Institutional, pension, endowment | 60.0 |
| Phase 4: Follow-On / Top-Up | Y4–Y5 | Performance-based, co-investment rights | 75.0 |
| Phase 5: Harvest / Secondaries | Y6–Y10 | Secondary sales, fund-of-funds, evergreen | 100.0 |

### 6.2 Key Messaging by Investor Type

| Investor Type | Primary Message | Secondary Message | Channel |
|---|---|---|---|
| Sovereign Wealth | Sovereign trade architecture, strategic resources, GCC alignment | ESG, impact, mineral rights | Direct, bilateral |
| Family Offices | Generational wealth, halal-compliant, diversification | Tax efficiency, Luxembourg | Private banking, wealth advisors |
| Pension / Endowment | Long-horizon, inflation hedge, real assets | DFI co-investment, blended finance | Consultant-driven, RFP |
| DFI / Development | Impact, SDGs, SME development, corridor integration | Blended finance, catalytic first-loss | Direct, bilateral, MOU |
| HNWI / Retail (ETN) | Liquid exposure, 3.5% coupon, growth participation | Transparency, index methodology | Online, wealth platforms, advisors |
| Corporate / Strategic | Supply chain integration, vertical alignment, IP access | Joint venture, technology transfer | Corporate development, M&A |

### 6.3 AUM Consolidation & Projection ($M)

| Year | CEI Index (ETN) | Growth Fund | Income Fund | Emerging Markets | Total AUM | Fee Income |
|---|---|---|---|---|---|---|
| Y1 | 191.0 | — | — | — | 191.0 | 1.0 |
| Y2 | 342.8 | — | — | — | 342.8 | 1.8 |
| Y3 | 638.8 | 25.0 | 15.0 | 10.0 | 688.8 | 3.5 |
| Y4 | 1,054.3 | 58.0 | 36.5 | 18.5 | 1,167.3 | 5.8 |
| Y5 | 1,664.3 | 83.7 | 56.3 | 25.0 | 1,829.3 | 8.5 |
| Y6 | 2,158.3 | 110.4 | 72.5 | 28.0 | 2,369.2 | 11.0 |
| Y7 | 2,428.3 | 134.5 | 80.0 | 32.0 | 2,674.8 | 12.5 |
| Y8 | 2,686.3 | 156.4 | 88.0 | 28.0 | 2,958.7 | 13.8 |
| Y9 | 2,894.3 | 180.7 | 96.7 | 22.0 | 3,193.7 | 15.0 |
| Y10 | 2,965.3 | 206.8 | 106.2 | 12.0 | 3,290.3 | 15.5 |

---

## 7. Regulatory & Compliance Framework

| Jurisdiction | Registration | Regulator | Reporting | Key Requirement |
|---|---|---|---|---|
| USA (ETN) | SEC Reg D / 144A | SEC | Quarterly 10-K, annual | Accredited investors only (Y1–Y3) |
| USA (REIT) | SEC-registered | SEC | Quarterly 10-Q, annual 10-K | 90% distribution, 75% asset test |
| Luxembourg (Growth) | SICAV / Part II | CSSF | Annual, semi-annual | AIFMD, KIID, PRIIPs |
| Cayman Islands (EM) | Exempt LP | CIMA | Annual audited | Anti-money laundering, FATCA, CRS |
| UAE (Marketing) | DIFC / ADGM | DFSA / ADGM | Quarterly | Qualified investor, professional |
| KSA (Marketing) | CMA | CMA | Annual | Qualified investor, sovereign fund |
| EU (AIFMD) | AIFM notification | NCAs | Annual, periodic | Transparency, leverage, liquidity |
| UK (Marketing) | FCA temporary permission | FCA | Annual | Professional / eligible counterparty |

---

## 8. Key Formulas

```python
# CEI Index
cei_index = 100 * product(1 + r_t for t in 1..n)
r_t = (0.40 * rev_growth) + (0.30 * asset_growth) + (0.20 * ebitda_growth) + (0.10 * mineral_growth)

# ETN Liability
etn_liability = units_outstanding * index_level + accrued_coupon
accrued_coupon = units_outstanding * face_value * 0.035 * days / 365

# REIT NAV
nav = properties_fair_value - debt + cash - liabilities
nav_per_share = nav / shares_outstanding

# PE MOIC
moic = total_distributions / total_called_capital
irr = xirr(cash_flows)
dpi = cumulative_distributions / total_called_capital
rvpi = nav / total_called_capital

# Fee calculation
management_fee = nav * fee_rate
performance_fee = max(0, (nav - high_water_mark - hurdle)) * performance_rate
```

---

## 9. Reconciliation to SSS Ecosystem

| Pillar | Integration Point | Fund Vehicle | Value Flow |
|---|---|---|---|
| A (SSS Firm) | Anchor investor, governance | Growth Fund (20% anchor) | Capital + oversight |
| B (AISTA Corridor) | Infrastructure investment, logistics | Income Fund, EM Fund | Concession fees, tolls, leases |
| C (Corleone Enterprise) | Operating performance, dividend | ETN (index), Growth Fund | Revenue, EBITDA, asset growth |
| C (Corleone Enterprise) | Real estate, facilities | Income Fund | Rent, lease payments, NOI |
| C (Corleone Enterprise) | Frontier expansion, SME | EM Fund | JVs, acquisitions, technology |

---

## 10. Source Citations

| Benchmark | Source | Value Used |
|---|---|---|
| ETN issuance costs | Barclays / UBS ETN pricing | 0.50% hedging cost |
| Open-end fund fees | Morningstar / eVestment | 2.0% management, 20% performance |
| REIT fee structure | NAREIT / Green Street | 1.5% base, 15% performance |
| PE fund terms | Preqin / Cambridge Associates | 2.0% / 20.0%, 8% hurdle |
| REIT distribution yield | FTSE NAREIT | 5.0–6.0% |
| PE returns (frontier) | EMPEA / Preqin | 15–25% IRR, 1.8–2.5x MOIC |
| AUM projections | Internal model, SSS Board targets | As per tables |

---

*End of CEI Fund Architecture Model*
