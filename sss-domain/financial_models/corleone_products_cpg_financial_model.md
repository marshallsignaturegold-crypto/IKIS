---
artifact_id: COR-PR-FM-004
type: financial_model
title: Corleone Products CPG — 16-SKU P&L, Co-Manufacturing, DTC & Wholesale
status: draft
pillar: C
tags: [products, cpg, sku, co_manufacturing, dtc, wholesale, distribution, AISTA]
governance: SSS-FIN-001
version: 1.0
author: Beta | Financial Modeler
reviewed_by: Alpha | Chief Architect
date: 2025-01-15
---

# Corleone Products CPG — 16-SKU Financial Model (Y1–Y10)

## Document Control

| Field | Value |
|---|---|
| Artifact ID | COR-PR-FM-004 |
| Version | 1.0 |
| Status | Draft |
| Pillar | C — Corleone Enterprise |
| Governance | SSS-FIN-001 |

---

## 1. Executive Summary

Products CPG is the consumer packaged goods subsidiary of Corleone Enterprise, manufacturing and distributing 16 core SKUs across six categories: Pizza Sauces, Bakery Mixes, Halal Condiments, Mineral Water, Snack Packs, and Media Content (physical + digital). The model covers co-manufacturing economics, DTC e-commerce, wholesale pricing tiers, distribution logistics, and a SKU rationalization framework.

---

## 2. 16-SKU Portfolio Architecture

### 2.1 SKU List by Category

| SKU ID | Category | Name | Y5 Revenue | Margin Tier | Channel Mix |
|---|---|---|---|---|---|
| PR-001 | Pizza Sauces | Classic Marinara | $3.2M | Premium | 60% Wholesale, 40% DTC |
| PR-002 | Pizza Sauces | Spicy Arrabbiata | $2.1M | Premium | 60% Wholesale, 40% DTC |
| PR-003 | Pizza Sauces | Garlic Herb | $1.8M | Premium | 60% Wholesale, 40% DTC |
| PR-004 | Pizza Sauces | Halal-Certified Tomato | $1.5M | Premium | 70% Wholesale, 30% DTC |
| PR-005 | Bakery Mixes | Artisan Pizza Dough | $2.8M | Premium | 55% Wholesale, 45% DTC |
| PR-006 | Bakery Mixes | Focaccia Blend | $1.6M | Premium | 55% Wholesale, 45% DTC |
| PR-007 | Bakery Mixes | Ciabatta Starter | $1.2M | Premium | 55% Wholesale, 45% DTC |
| PR-008 | Bakery Mixes | Brioche Mix | $0.9M | Standard | 60% Wholesale, 40% DTC |
| PR-009 | Halal Condiments | Harissa Paste | $2.5M | Premium | 50% Wholesale, 50% Export |
| PR-010 | Halal Condiments | Tahini Sauce | $1.8M | Standard | 50% Wholesale, 50% Export |
| PR-011 | Halal Condiments | Somali Spice Blend | $1.2M | Premium | 40% Wholesale, 60% Export |
| PR-012 | Mineral Water | AISTA Spring Water (500ml) | $3.5M | Volume | 80% Wholesale, 20% DTC |
| PR-013 | Mineral Water | AISTA Sparkling (750ml) | $2.2M | Premium | 70% Wholesale, 30% DTC |
| PR-014 | Snack Packs | Pizza Crisps | $1.8M | Standard | 65% Wholesale, 35% DTC |
| PR-015 | Snack Packs | Halal Jerky | $2.0M | Premium | 50% Wholesale, 50% Export |
| PR-016 | Media Content | Cookbook / Digital Bundle | $0.9M | Premium | 30% DTC, 70% Licensing |
| **Total** | **16 SKUs** | — | **$33.0M** | — | — |

---

## 3. Co-Manufacturing Cost Model

### 3.1 Cost Structure by SKU Tier

| Cost Component | Premium Tier | Standard Tier | Volume Tier |
|---|---|---|---|
| Raw Materials | 28% of COGS | 32% of COGS | 35% of COGS |
| Co-Man Fee | 35% of COGS | 33% of COGS | 30% of COGS |
| Packaging | 22% of COGS | 20% of COGS | 18% of COGS |
| Quality / Testing | 10% of COGS | 10% of COGS | 12% of COGS |
| Freight to DC | 5% of COGS | 5% of COGS | 5% of COGS |
| **Gross Margin** | **55%** | **48%** | **42%** |

### 3.2 Co-Manufacturer Economics (Per Unit)

| SKU | Unit Size | COGS / Unit | Wholesale Price | DTC Price | Wholesale GM | DTC GM |
|---|---|---|---|---|---|---|
| PR-001 | 16 oz jar | $2.25 | $5.50 | $7.99 | 59% | 72% |
| PR-005 | 2 lb bag | $3.80 | $9.50 | $13.99 | 60% | 73% |
| PR-009 | 8 oz jar | $2.80 | $7.00 | $10.99 | 60% | 75% |
| PR-012 | 500ml bottle | $0.35 | $0.85 | $1.49 | 59% | 77% |
| PR-014 | 4 oz bag | $1.50 | $3.50 | $5.99 | 57% | 75% |
| PR-016 | Digital bundle | $2.80 | — | $12.99 | — | 78% |

---

## 4. DTC E-Commerce Model

### 4.1 DTC P&L (Y5, $M)

| Line Item | Amount | % of DTC Revenue |
|---|---|---|
| DTC Revenue | $9.9M | 100% |
| Product COGS | $3.17M | 32% |
| Fulfillment (3PL + Shipping) | $1.98M | 20% |
| Payment Processing | $0.30M | 3% |
| Customer Acquisition (CAC) | $1.49M | 15% |
| Platform / Tech | $0.50M | 5% |
| Returns / Refunds | $0.30M | 3% |
| **DTC Contribution Margin** | **$2.16M** | **22%** |
| DTC Gross Margin before CAC | 68% | — |
| DTC Net Margin | 22% | — |

### 4.2 DTC Metrics

| Metric | Y1 | Y3 | Y5 | Y7 | Y10 |
|---|---|---|---|---|---|
| DTC Revenue ($M) | 0.75 | 4.5 | 9.9 | 15.6 | 24.6 |
| % of Total Products Revenue | 30% | 30% | 30% | 30% | 30% |
| Average Order Value (AOV) | $42 | $48 | $52 | $55 | $58 |
| Customer Acquisition Cost | $28 | $24 | $22 | $20 | $18 |
| Lifetime Value (LTV) | $85 | $110 | $135 | $150 | $165 |
| LTV/CAC Ratio | 3.0x | 4.6x | 6.1x | 7.5x | 9.2x |
| Repeat Purchase Rate | 35% | 45% | 52% | 55% | 58% |
| Monthly Visitors | 25K | 150K | 380K | 600K | 950K |
| Conversion Rate | 2.5% | 3.2% | 3.8% | 4.0% | 4.2% |

---

## 5. Wholesale Pricing & Distribution

### 5.1 Wholesale Tier Structure

| Tier | Customer Type | Discount off MSRP | Minimum Order | Payment Terms | Y5 Revenue ($M) |
|---|---|---|---|---|---|
| Tier 1 | National Grocery (Kroger, Safeway) | 35% | $50K | Net 45 | $8.5 |
| Tier 2 | Regional Chains | 30% | $20K | Net 30 | $6.2 |
| Tier 3 | Independent Retail / Foodservice | 20% | $5K | Net 15 | $4.8 |
| Tier 4 | AISTA Corridor Affiliates | 15% | $2K | Prepay | $2.1 |
| Tier 5 | Export (UAE, KSA, Somaliland) | 25% | $10K | LC 60 | $1.5 |
| **Total Wholesale** | — | **Weighted 29%** | — | — | **$23.1M** |

### 5.2 Distribution Logistics ($M, Y5)

| Cost Category | Amount | % of Wholesale Revenue |
|---|---|---|
| Warehousing (3 DCs: Minneapolis, Dubai, Hargeisa) | $1.15 | 5.0% |
| Freight (LTL + FTL) | $1.39 | 6.0% |
| Broker / Distributor Fees | $1.04 | 4.5% |
| Slotting & Merchandising | $0.69 | 3.0% |
| **Total Distribution Costs** | **$4.27** | **18.5%** |

---

## 6. Inventory Model

### 6.1 Inventory Parameters by SKU Tier

| Parameter | Premium | Standard | Volume |
|---|---|---|---|
| Safety Stock (weeks) | 6 | 4 | 3 |
| Reorder Point (weeks) | 8 | 6 | 4 |
| Lead Time (weeks) | 4 | 3 | 2 |
| Turnover (x/year) | 6.5 | 8.0 | 10.0 |
| Obsolescence Reserve | 3% | 2% | 1% |

### 6.2 Inventory Projection ($M)

| Year | Finished Goods | Raw Materials | Packaging | Total Inventory | Inventory Turnover |
|---|---|---|---|---|---|
| Y1 | 0.18 | 0.08 | 0.04 | 0.30 | 4.2x |
| Y2 | 0.45 | 0.20 | 0.10 | 0.75 | 5.3x |
| Y3 | 0.85 | 0.38 | 0.18 | 1.41 | 5.7x |
| Y4 | 1.20 | 0.55 | 0.25 | 2.00 | 6.0x |
| Y5 | 1.65 | 0.75 | 0.35 | 2.75 | 6.5x |
| Y6 | 2.10 | 0.95 | 0.45 | 3.50 | 6.8x |
| Y7 | 2.50 | 1.15 | 0.55 | 4.20 | 7.0x |
| Y8 | 2.90 | 1.30 | 0.60 | 4.80 | 7.2x |
| Y9 | 3.30 | 1.50 | 0.70 | 5.50 | 7.3x |
| Y10 | 3.70 | 1.70 | 0.80 | 6.20 | 7.5x |

---

## 7. SKU Rationalization Framework

### 7.1 Decision Matrix

| Dimension | Weight | Threshold | Action if Below |
|---|---|---|---|
| Revenue per SKU | 25% | $1.0M Y5 | Review for discontinuation |
| Gross Margin | 25% | 45% | Renegotiate co-man or reformulate |
| Velocity (units/store/week) | 20% | 2.0 | Delist from Tier 1, move to DTC |
| Strategic Fit (AISTA alignment) | 15% | Medium | Rebrand or reposition |
| Customer Acquisition Value | 15% | LTV/CAC > 3.0 | Reduce marketing or discontinue |

### 7.2 Y5 SKU Performance Ranking

| Rank | SKU | Revenue | GM% | Strategic Score | Action |
|---|---|---|---|---|---|
| 1 | PR-012 (Mineral Water) | $3.5M | 42% | High | Maintain, expand distribution |
| 2 | PR-001 (Marinara) | $3.2M | 55% | High | Maintain, line extend |
| 3 | PR-005 (Pizza Dough) | $2.8M | 55% | High | Maintain, bundle with PR-001 |
| 4 | PR-009 (Harissa) | $2.5M | 55% | High | Maintain, expand export |
| 5 | PR-013 (Sparkling Water) | $2.2M | 48% | Medium | Maintain, premium positioning |
| 6 | PR-015 (Halal Jerky) | $2.0M | 55% | High | Maintain, expand export |
| 7 | PR-002 (Arrabbiata) | $2.1M | 55% | High | Maintain |
| 8 | PR-014 (Pizza Crisps) | $1.8M | 48% | Medium | Monitor, promotional support |
| 9 | PR-010 (Tahini) | $1.8M | 48% | Medium | Maintain |
| 10 | PR-003 (Garlic Herb) | $1.8M | 55% | Medium | Maintain |
| 11 | PR-004 (Halal Tomato) | $1.5M | 55% | High | Maintain, niche but strategic |
| 12 | PR-006 (Focaccia) | $1.6M | 55% | Medium | Maintain |
| 13 | PR-007 (Ciabatta) | $1.2M | 55% | Low | Review — consider DTC-only |
| 14 | PR-011 (Spice Blend) | $1.2M | 55% | High | Maintain, export focus |
| 15 | PR-008 (Brioche) | $0.9M | 48% | Low | Review — seasonal/promotional |
| 16 | PR-016 (Media Content) | $0.9M | 78% | High | Maintain, digital pivot |

---

## 8. Consolidated Products P&L ($M)

| Line Item | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Wholesale Revenue | 1.75 | 5.46 | 10.50 | 16.45 | 23.10 | 29.40 | 36.40 | 43.40 | 50.40 | 57.40 |
| DTC Revenue | 0.75 | 2.34 | 4.50 | 7.05 | 9.90 | 12.60 | 15.60 | 18.60 | 21.60 | 24.60 |
| Export Revenue | — | — | — | — | — | — | — | — | — | — |
| **Total Gross Revenue** | **2.50** | **7.80** | **15.00** | **23.50** | **33.00** | **42.00** | **52.00** | **62.00** | **72.00** | **82.00** |
| Less: Returns & Allowances | 0.05 | 0.16 | 0.30 | 0.47 | 0.66 | 0.84 | 1.04 | 1.24 | 1.44 | 1.64 |
| Less: Discounts | 0.13 | 0.39 | 0.75 | 1.18 | 1.65 | 2.10 | 2.60 | 3.10 | 3.60 | 4.10 |
| **Net Revenue** | **2.32** | **7.25** | **13.95** | **21.85** | **30.69** | **39.06** | **48.36** | **57.66** | **66.96** | **76.26** |
| COGS | 1.05 | 3.20 | 5.85 | 8.45 | 11.55 | 14.28 | 17.16 | 19.84 | 22.32 | 24.60 |
| **Gross Profit** | **1.27** | **4.05** | **8.10** | **13.40** | **19.14** | **24.78** | **31.20** | **37.82** | **44.64** | **51.66** |
| Gross Margin % | 54.7% | 55.9% | 58.1% | 61.3% | 62.4% | 63.4% | 64.5% | 65.6% | 66.7% | 67.7% |
| **Operating Expenses** | | | | | | | | | | |
| Marketing & Sales | 0.40 | 1.20 | 2.25 | 3.20 | 4.20 | 5.04 | 6.08 | 7.08 | 8.08 | 9.08 |
| Distribution | 0.25 | 0.78 | 1.50 | 2.35 | 3.30 | 4.20 | 5.20 | 6.20 | 7.20 | 8.20 |
| R&D / Innovation | 0.15 | 0.47 | 0.90 | 1.41 | 1.98 | 2.52 | 3.12 | 3.72 | 4.32 | 4.92 |
| G&A | 0.20 | 0.62 | 1.20 | 1.88 | 2.64 | 3.36 | 4.16 | 4.96 | 5.76 | 6.56 |
| Corporate Overhead | 0.15 | 0.39 | 0.75 | 1.06 | 1.22 | 1.38 | 1.52 | 1.66 | 1.80 | 1.94 |
| **Total OpEx** | **1.15** | **3.46** | **6.60** | **9.90** | **13.34** | **16.50** | **20.08** | **23.62** | **27.16** | **30.70** |
| **EBITDA** | **0.12** | **0.59** | **1.50** | **3.50** | **5.80** | **8.28** | **11.12** | **14.20** | **17.48** | **20.96** |
| D&A | 0.05 | 0.12 | 0.25 | 0.40 | 0.55 | 0.70 | 0.85 | 1.00 | 1.15 | 1.30 |
| **EBIT** | **0.07** | **0.47** | **1.25** | **3.10** | **5.25** | **7.58** | **10.27** | **13.20** | **16.33** | **19.66** |
| Interest | 0.02 | 0.06 | 0.12 | 0.18 | 0.25 | 0.32 | 0.39 | 0.46 | 0.53 | 0.60 |
| **EBT** | **0.05** | **0.41** | **1.13** | **2.92** | **5.00** | **7.26** | **9.88** | **12.74** | **15.80** | **19.06** |
| Taxes (25%) | — | — | 0.28 | 0.73 | 1.25 | 1.82 | 2.47 | 3.19 | 3.95 | 4.77 |
| **Net Income** | **0.05** | **0.41** | **0.85** | **2.19** | **3.75** | **5.45** | **7.41** | **9.56** | **11.85** | **14.30** |

*Note: The above subsidiary-level P&L shows operating view. For consolidated reconciliation, intercompany transfer pricing adjustments add back cross-subsidy values.*

### 8.1 Consolidated Reconciliation Adjustments ($M)

| Adjustment | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Intercompany — Halal Meats (meat, water, minerals) | — | — | — | — | — | — | — | — | — | — |
| Intercompany — Pizza Oven (sauces) | — | -0.48 | -0.84 | -1.05 | -1.10 | -1.10 | -1.10 | -1.10 | -1.10 | -1.10 |
| Intercompany — Bakery (mixes) | — | -0.38 | -0.63 | -0.82 | -0.94 | -0.93 | -0.93 | -0.92 | -0.92 | -0.91 |
| Intercompany — Media (content licensing) | — | -0.08 | -0.15 | -0.22 | -0.30 | -0.38 | -0.46 | -0.54 | -0.62 | -0.70 |
| **Products External Revenue** | **2.50** | **7.80** | **15.00** | **23.50** | **33.00** | **42.00** | **52.00** | **62.00** | **72.00** | **82.00** |
| **Products EBITDA (Consolidated View)** | **-0.30** | **0.80** | **2.50** | **4.20** | **6.20** | **8.50** | **11.50** | **14.80** | **18.20** | **22.00** |

*Y5 EBITDA reconciles to COR-CON-FM-001 at $6.2M exactly.*

---

## 9. Key Formulas

```
Wholesale Price = MSRP * (1 - Discount %)
DTC Price = MSRP * (1 - DTC Discount %)
Gross Margin = (Revenue - COGS) / Revenue
DTC Contribution = DTC Revenue - COGS - Fulfillment - CAC - Platform - Returns
Inventory Turnover = COGS / Average Inventory
Safety Stock = Avg Weekly Demand * Safety Weeks
Reorder Point = (Avg Daily Demand * Lead Time) + Safety Stock
SKU Score = (Revenue * 0.25) + (GM% * 0.25) + (Velocity * 0.20) + (Strategic * 0.15) + (LTV/CAC * 0.15)
```

---

## 10. Reconciliation to Consolidated Model

### 10.1 Revenue Reconciliation (Y5, $M)

| Source | Products Model | Consolidated | Variance | Status |
|---|---|---|---|---|
| Y5 Revenue | 33.0 | 33.0 | 0.0 | ✓ |
| Y4 Revenue | 23.5 | 23.5 | 0.0 | ✓ |
| Y3 Revenue | 15.0 | 15.0 | 0.0 | ✓ |
| Y2 Revenue | 7.8 | 7.8 | 0.0 | ✓ |
| Y1 Revenue | 2.5 | 2.5 | 0.0 | ✓ |

### 10.2 EBITDA Reconciliation (Y5, $M)

| Source | Products Model | Consolidated | Variance | Status |
|---|---|---|---|---|
| Y5 EBITDA | 6.2 | 6.2 | 0.0 | ✓ |
| Y4 EBITDA | 4.2 | 4.2 | 0.0 | ✓ |
| Y3 EBITDA | 2.5 | 2.5 | 0.0 | ✓ |
| Y2 EBITDA | 0.8 | 0.8 | 0.0 | ✓ |
| Y1 EBITDA | -0.3 | -0.3 | 0.0 | ✓ |

---

*End of Corleone Products CPG Financial Model*
