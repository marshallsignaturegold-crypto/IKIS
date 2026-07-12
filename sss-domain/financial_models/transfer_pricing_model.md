---
artifact_id: COR-TP-FM-009
type: financial_model
title: Corleone Enterprise Transfer Pricing Model — OECD Arm's-Length Analysis
status: draft
pillar: C
tags: [transfer_pricing, oecd, arms_length, cup, profit_split, cost_plus, functional_analysis, AISTA]
governance: SSS-FIN-001
version: 1.0
author: Beta | Financial Modeler
reviewed_by: Alpha | Chief Architect
date: 2025-01-15
---

# Corleone Enterprise Transfer Pricing Model — OECD Arm's-Length Analysis (Y5)

## Document Control

| Field | Value |
|---|---|
| Artifact ID | COR-TP-FM-009 |
| Version | 1.0 |
| Status | Draft |
| Pillar | C — Corleone Enterprise |
| Governance | SSS-FIN-001 |

---

## 1. Executive Summary

This document presents the OECD-aligned transfer pricing documentation for Corleone Enterprise's five-subsidiary architecture. It covers functional analysis, risk analysis, asset analysis, and the application of three transfer pricing methodologies: Comparable Uncontrolled Price (CUP), Profit Split (for brand IP), and Cost Plus (for manufacturing). Documentation requirements are specified for five jurisdictions: USA, UAE, Somaliland, India, and Saudi Arabia.

---

## 2. Intercompany Transaction Matrix (Y5)

### 2.1 Transaction Overview

| Transaction ID | Supplier | Recipient | Product / Service | Volume (Y5) | Market Price | Transfer Price | Discount / Premium | Subsidy Value ($M) |
|---|---|---|---|---|---|---|---|---|
| TP-001 | Halal Meats SPV (Somaliland) | Products (USA) | Halal meat (frozen) | 180 MT | $4.20/kg | $2.80/kg | -33.3% | $0.252 |
| TP-002 | Halal Meats SPV (Somaliland) | Products (USA) | Mineral water | 2.4M bottles | $0.85/bottle | $0.55/bottle | -35.3% | $0.720 |
| TP-003 | Halal Meats SPV (Somaliland) | Products (USA) | Salt / gypsum | 450 tons | $120/ton | $72/ton | -40.0% | $0.022 |
| TP-004 | Products (USA) | Pizza Oven (USA) | Pizza sauces | 320K units | $12.50/unit | $10.65/unit | -14.8% | $0.592 |
| TP-005 | Products (USA) | Bakery (USA) | Bakery mixes | 180K units | $8.20/unit | $6.97/unit | -15.0% | $0.221 |
| TP-006 | Media (USA) | Pizza Oven (USA) | Marketing services | 80 units | $2.50/unit | $1.75/unit | -30.0% | $0.060 |
| TP-007 | Media (USA) | Bakery (USA) | Marketing services | 60 units | $1.80/unit | $1.26/unit | -30.0% | $0.032 |
| TP-008 | Products (USA) | Pizza Oven (USA) | Branded packaging | 80K units | $3.50/unit | $2.80/unit | -20.0% | $0.056 |
| TP-009 | Products (USA) | Bakery (USA) | Branded packaging | 60K units | $2.80/unit | $2.24/unit | -20.0% | $0.034 |
| TP-010 | Halal Meats SPV (Somaliland) | Products (USA) | Halal certification services | 1,200 certificates | $150/cert | $105/cert | -30.0% | $0.054 |
| TP-011 | Corporate (USA) | All subsidiaries | Management services | 5 entities | $2.80M total | $2.24M total | -20.0% | $0.560 |
| TP-012 | Corporate (USA) | All subsidiaries | IT / platform services | 5 entities | $1.20M total | $0.96M total | -20.0% | $0.240 |
| TP-013 | Corporate (USA) | All subsidiaries | Brand IP licensing | 5 entities | $1.50M total | $1.20M total | -20.0% | $0.300 |
| TP-014 | Pizza Oven (USA) | Products (USA) | Recipe / menu IP | 12 recipes | $25K/recipe | $20K/recipe | -20.0% | $0.060 |
| TP-015 | Bakery (USA) | Products (USA) | Recipe / menu IP | 8 recipes | $20K/recipe | $16K/recipe | -20.0% | $0.032 |
| **Total Cross-Subsidy** | — | — | — | — | — | — | — | **$3.174M** |
| **Implicit Brand / Shared Services** | — | — | — | — | — | — | — | **$1.676M** |
| **Total Intercompany Subsidy** | — | — | — | — | — | — | — | **$4.850M** |

---

## 3. Functional Analysis (OECD Guidelines §1.42)

### 3.1 Functions Performed by Entity

| Function | Corporate (USA) | Pizza Oven (USA) | Bakery (USA) | Products (USA) | Media (USA) | Halal Meats (Somaliland) |
|---|---|---|---|---|---|---|
| Strategic Management | ★★★ | ★ | ★ | ★★ | ★ | ★ |
| R&D / Innovation | ★★ | ★ | ★ | ★★★ | ★ | ★ |
| Manufacturing / Processing | — | ★★★ | ★★★ | ★★ | ★ | ★★★ |
| Sourcing / Procurement | ★★ | ★★ | ★★ | ★★★ | ★ | ★★★ |
| Quality Control | ★ | ★★★ | ★★★ | ★★★ | ★ | ★★★ |
| Marketing & Branding | ★★★ | ★ | ★ | ★★ | ★★★ | ★ |
| Sales & Distribution | — | ★★★ | ★★★ | ★★★ | ★ | ★★★ |
| Logistics & Transport | ★ | ★ | ★ | ★★ | ★ | ★★★ |
| Customer Service | — | ★★★ | ★★★ | ★★ | ★ | ★ |
| Financial Management | ★★★ | ★ | ★ | ★★ | ★ | ★ |
| Legal / Regulatory | ★★★ | ★ | ★ | ★★ | ★★ | ★★★ |
| IT / Digital Platform | ★★★ | ★ | ★ | ★★ | ★★ | ★ |
| **Total Functions** | **High** | **Medium-High** | **Medium-High** | **High** | **Medium** | **High** |

### 3.2 Risk Analysis (OECD Guidelines §1.43)

| Risk Type | Corporate | Pizza Oven | Bakery | Products | Media | Halal Meats |
|---|---|---|---|---|---|---|
| Market / Demand Risk | ★ | ★★★ | ★★★ | ★★★ | ★★ | ★★ |
| Credit / Counterparty Risk | ★★ | ★★ | ★★ | ★★★ | ★ | ★★ |
| Inventory / Obsolescence Risk | — | ★★★ | ★★★ | ★★★ | ★ | ★★★ |
| Foreign Exchange Risk | ★★ | ★ | ★ | ★★ | ★ | ★★★ |
| Commodity Price Risk | ★ | ★★ | ★★ | ★★★ | ★ | ★★★ |
| Operational / Production Risk | ★ | ★★★ | ★★★ | ★★ | ★★ | ★★★ |
| Regulatory / Compliance Risk | ★★★ | ★★ | ★★ | ★★★ | ★★ | ★★★ |
| Environmental / Climate Risk | ★ | ★ | ★ | ★★ | ★ | ★★★ |
| Political / Country Risk | ★ | ★ | ★ | ★ | ★ | ★★★ |
| Technology / IP Risk | ★★★ | ★ | ★ | ★★ | ★★★ | ★ |
| Financial / Funding Risk | ★★★ | ★ | ★ | ★★ | ★ | ★ |
| **Total Risk Profile** | **Medium-High** | **High** | **High** | **High** | **Medium** | **Very High** |

### 3.3 Asset Analysis (OECD Guidelines §1.44)

| Asset Type | Corporate | Pizza Oven | Bakery | Products | Media | Halal Meats |
|---|---|---|---|---|---|---|
| Tangible Assets (PP&E) | ★ | ★★★ | ★★★ | ★★ | ★ | ★★★ |
| Inventory | — | ★★★ | ★★★ | ★★★ | ★ | ★★★ |
| Intangible Assets (Brand) | ★★★ | ★ | ★ | ★★ | ★★★ | ★ |
| Intangible Assets (IP / Patents) | ★★★ | ★ | ★ | ★★★ | ★★★ | ★ |
| Intangible Assets (Recipes) | ★★ | ★★★ | ★★★ | ★★ | ★ | ★ |
| Human Capital / Know-How | ★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★ |
| Customer Relationships | — | ★★★ | ★★★ | ★★★ | ★★ | ★★ |
| Mineral Concessions | — | — | — | — | — | ★★★ |
| Digital Platform / Data | ★★★ | ★ | ★ | ★★ | ★★★ | ★ |
| **Total Asset Intensity** | **Medium** | **High** | **High** | **High** | **Medium** | **Very High** |

---

## 4. Transfer Pricing Methodology Selection

### 4.1 Methodology by Transaction Type

| Transaction | Method | OECD Category | Justification | Reliability |
|---|---|---|---|---|
| TP-001 (Halal meat) | CUP | Traditional | Active market for halal meat, published price indices | High |
| TP-002 (Mineral water) | CUP | Traditional | Comparable bottled water brands, retail and wholesale data | High |
| TP-003 (Salt/gypsum) | CUP | Traditional | Commodity exchanges, mineral price indices | High |
| TP-004 (Pizza sauces) | CUP | Traditional | Comparable co-manufactured sauces, industry benchmarks | Medium-High |
| TP-005 (Bakery mixes) | CUP | Traditional | Comparable dry mix products, wholesale pricing | Medium-High |
| TP-006 (Marketing services) | CUP | Traditional | Comparable agency rates, hourly benchmarks | Medium |
| TP-007 (Marketing services) | CUP | Traditional | Comparable agency rates, hourly benchmarks | Medium |
| TP-008 (Branded packaging) | Cost Plus | Traditional | Limited comparable packaging transactions, cost-based approach | Medium |
| TP-009 (Branded packaging) | Cost Plus | Traditional | Limited comparable packaging transactions, cost-based approach | Medium |
| TP-010 (Certification services) | Cost Plus | Traditional | Internal cost allocation with comparable margin | Medium |
| TP-011 (Management services) | Cost Plus | Traditional | Arm's-length management fee benchmarks (4.5–6.0% of revenue) | High |
| TP-012 (IT services) | Cost Plus | Traditional | Comparable IT outsourcing rates, cost-plus 10–15% | Medium-High |
| TP-013 (Brand IP) | Profit Split | Transactional | Unique brand value, no direct comparables, residual profit split | Medium |
| TP-014 (Recipe IP) | CUP | Traditional | Comparable recipe licensing, franchise systems | Medium |
| TP-015 (Recipe IP) | CUP | Traditional | Comparable recipe licensing, franchise systems | Medium |

---

## 5. Comparable Uncontrolled Price (CUP) Analysis

### 5.1 CUP — Halal Meat (TP-001)

| Comparable | Source | Price ($/kg) | Volume (MT) | Quality Grade | Delivery Terms | Adjustment | Adjusted Price |
|---|---|---|---|---|---|---|---|
| GCC Wholesale Halal Lamb | Dubai Meat Market | $4.50 | 500 | Premium | CIF Jeddah | -0.20 (logistics) | $4.30 |
| Brazilian Halal Beef Export | BRF / Minerva | $4.10 | 2,000 | Standard | FOB Santos | +0.15 (Africa premium) | $4.25 |
| Australian Halal Lamb Export | Meat & Livestock Aus | $4.80 | 1,000 | Premium | CIF Jeddah | -0.30 (origin premium) | $4.50 |
| Somaliland Live Export (live) | FAO Trade Data | $2.80 | 5,000 | Variable | FOB Berbera | +1.40 (processing value-add) | $4.20 |
| Indian Buffalo Meat (frozen) | APEDA | $3.50 | 10,000 | Standard | CIF | +0.80 (quality upgrade) | $4.30 |
| **Median Comparable** | — | **$4.20** | — | — | — | — | **$4.20** |
| **Transfer Price** | — | **$2.80** | — | — | — | — | — |
| **Discount** | — | **33.3%** | — | — | — | — | — |
| **Justification** | — | Vertical integration, volume commitment, captive market, long-term contract | — | — | — | — | — |

### 5.2 CUP — Mineral Water (TP-002)

| Comparable | Source | Price ($/bottle) | Volume | Channel | Adjustment | Adjusted Price |
|---|---|---|---|---|---|---|
| Evian (500ml retail) | Retail scan | $1.20 | 10M | Retail | -0.40 (wholesale) | $0.80 |
| Fiji (500ml wholesale) | Wholesale data | $0.75 | 5M | Wholesale | +0.05 (premium) | $0.80 |
| Local UAE brand (wholesale) | Trade data | $0.55 | 2M | Wholesale | +0.05 (AISTA premium) | $0.60 |
| Coca-Cola (Dasani, wholesale) | Coca-Cola financials | $0.45 | 50M | Wholesale | +0.15 (premium) | $0.60 |
| **Median Comparable** | — | **$0.60** | — | — | — | **$0.60** |
| **Transfer Price** | — | **$0.55** | — | — | — | — |
| **Discount** | — | **8.3%** | — | — | — | — |
| **Justification** | — | Bulk volume (2.4M units), long-term contract, captive buyer, shared logistics | — | — | — | — |

### 5.3 CUP — Pizza Sauces (TP-004)

| Comparable | Source | Price ($/unit) | Volume | Channel | Adjustment | Adjusted Price |
|---|---|---|---|---|---|---|
| Rao's Homemade (16oz wholesale) | Retail scan | $7.50 | 1M | Wholesale | +2.00 (premium brand) | $9.50 |
| Barilla (16oz wholesale) | Trade data | $5.50 | 5M | Wholesale | +3.00 (artisan premium) | $8.50 |
| Private Label (co-man) | Industry data | $4.50 | 10M | Wholesale | +4.00 (brand premium) | $8.50 |
| Whole Foods 365 (organic) | Retail scan | $6.50 | 2M | Wholesale | +3.00 (artisan premium) | $9.50 |
| **Median Comparable** | — | **$8.50** | — | — | — | **$8.50** |
| **Transfer Price** | — | **$10.65** | — | — | — | — |
| **Premium** | — | **+25.3%** | — | — | — | — |
| **Justification** | — | Corleone brand premium, halal certification, exclusive recipes, integrated supply chain | — | — | — | — |

---

## 6. Profit Split Methodology (Brand IP — TP-013)

### 6.1 Residual Profit Split Analysis

| Step | Calculation | Amount ($M) |
|---|---|---|
| Combined Profit (CE Consolidated Y5) | EBITDA | 18.1 |
| Less: Routine Functions | Market return on routine functions | 12.5 |
| Residual Profit | Brand IP, intangibles, synergies | 5.6 |
| Brand IP Contribution | 40% of residual | 2.24 |
| Technology / Platform Contribution | 25% of residual | 1.40 |
| Mineral Concession Contribution | 20% of residual | 1.12 |
| Organizational Synergy | 15% of residual | 0.84 |
| **Total Residual** | — | **5.6** |

### 6.2 Brand IP Allocation by Subsidiary

| Subsidiary | Brand Value Contribution | Routine Return | Residual Allocation | Brand IP Fee ($M) |
|---|---|---|---|---|
| Pizza Oven | High (flagship, customer touchpoint) | 2.0 | 0.80 | 0.80 |
| Bakery | Medium (secondary brand) | 1.5 | 0.40 | 0.40 |
| Products | High (CPG brand power) | 3.0 | 0.72 | 0.72 |
| Media | Very High (brand creation, content) | 1.5 | 0.56 | 0.56 |
| Halal Meats | Medium (halal certification, origin) | 2.5 | 0.56 | 0.56 |
| Corporate | Very High (strategic management, IP ownership) | 2.0 | 0.40 | 0.40 |
| **Total** | — | **12.5** | **3.44** | **3.44** |

*Note: Total brand IP fees of $3.44M exceed the $1.20M intercompany charge. The difference reflects implicit brand value not charged as a fee but embedded in cross-subsidies. The documented TP-013 charge of $1.20M is the explicit, arm's-length fee; the residual $2.24M is captured through product pricing and operational allocations.*

---

## 7. Cost Plus Methodology (Manufacturing & Services)

### 7.1 Cost Plus — Management Services (TP-011)

| Cost Category | Annual Cost ($M) | Allocation Basis | Allocated to Subsidiaries ($M) |
|---|---|---|---|
| Executive Compensation | 0.80 | Revenue | 0.80 |
| Legal & Compliance | 0.30 | Revenue | 0.30 |
| Finance & Treasury | 0.40 | Revenue | 0.40 |
| Strategy & BD | 0.50 | Revenue | 0.50 |
| HR & Administration | 0.40 | Headcount | 0.40 |
| Board & Governance | 0.20 | Equal | 0.20 |
| Insurance | 0.20 | Asset value | 0.20 |
| **Total Cost Base** | **2.80** | — | **2.80** |
| **Arm's-Length Mark-Up** | **5.0%** | — | **0.14** |
| **Total Fee Charged** | **2.94** | — | **2.94** |
| **Actual Fee (TP-011)** | **2.24** | — | — |
| **Discount / Subsidy** | **23.8%** | Volume commitment, long-term, integrated | — |

### 7.2 Cost Plus — IT Services (TP-012)

| Cost Category | Annual Cost ($M) | Allocation Basis | Allocated ($M) |
|---|---|---|---|
| Platform Development | 0.40 | Users / transactions | 0.40 |
| Cloud Infrastructure | 0.30 | Data volume | 0.30 |
| Cybersecurity | 0.20 | Risk exposure | 0.20 |
| Support & Maintenance | 0.20 | Tickets / users | 0.20 |
| Data Analytics | 0.10 | Usage | 0.10 |
| **Total Cost Base** | **1.20** | — | **1.20** |
| **Arm's-Length Mark-Up** | **12.0%** | — | **0.144** |
| **Total Fee Charged** | **1.344** | — | — |
| **Actual Fee (TP-012)** | **0.96** | — | — |
| **Discount / Subsidy** | **28.6%** | Shared platform, captive users, volume | — |

---

## 8. Documentation Requirements by Jurisdiction

### 8.1 USA (IRS — Section 482, Treas. Reg. §1.6662)

| Document | Requirement | Deadline | Penalty for Non-Compliance |
|---|---|---|---|
| Master File | CE group structure, business overview, TP policy | Annual, contemporaneous | 20% underpayment penalty |
| Local File | US-specific transactions, detailed CUP/Cost Plus | Annual, contemporaneous | 20% underpayment penalty |
| CbCR (Country-by-Country Report) | Revenue, profit, tax, employees by jurisdiction | 12 months after year-end | $25,000 penalty |
| Form 5472 | Related-party transactions | With tax return | $10,000 per form |
| APA (Advance Pricing Agreement) | Optional, recommended for TP-001, TP-002 | 3-year negotiation | N/A |
| BEPS Action 13 | Full documentation package | As above | As above |

### 8.2 UAE (Federal Tax Authority — Corporate Tax, 9%)

| Document | Requirement | Deadline | Notes |
|---|---|---|---|
| TP Documentation | Master File + Local File if revenue > AED 200M | Annual, with tax return | New CT regime (2023+) |
| CbCR | If group revenue > AED 3.15B | 12 months after year-end | OECD standard |
| Economic Substance | Demonstration of real activity in UAE | Annual declaration | Relevant for Media, Products |
| CT Return | Filed with FTA | 9 months after year-end | 9% rate, free zone 0% if qualifying |
| TP Adjustments | Arm's-length adjustments permitted | As part of return | Penalty 50% of underpaid tax |

### 8.3 Somaliland (Ministry of Finance — Informal, Developing)

| Document | Requirement | Deadline | Notes |
|---|---|---|---|
| Transfer Pricing Disclosure | Voluntary, recommended for MNE | Annual tax return | No formal TP rules; OECD-aligned best practice |
| Tax Return | Corporate income tax (10% rate) | 6 months after year-end | Limited enforcement capacity |
| Concession Reports | Mineral extraction royalties | Quarterly to Ministry | 1.5–3.0% of gross |
| Customs Documentation | Export declarations, origin certificates | Per shipment | Critical for halal certification |
| BEPS Readiness | Prepare for future adoption | Ongoing | Somalia federal may assert TP |
| DTA Network | No treaties currently; negotiate with UAE, KSA | Long-term | Priority for AISTA |

### 8.4 India (CBDT — Income Tax Act, Section 92)

| Document | Requirement | Deadline | Penalty |
|---|---|---|---|
| TP Study / Report | Mandatory if international transactions > INR 10M | 30 November | 2% of transaction value |
| Form 3CEB | Accountant's certification of TP study | 30 November | INR 100,000 |
| CbCR | If group revenue > EUR 750M | 12 months after year-end | INR 5,000–50,000 |
| APA | Optional, unilateral / bilateral / multilateral | 3–5 year negotiation | N/A |
| Safe Harbour | Available for IT, BPO, R&D | Annual election | Limits audit risk |
| BEPS Action 13 | Full documentation | As above | As above |

### 8.5 Saudi Arabia (ZATCA — Transfer Pricing Bylaws, 2019)

| Document | Requirement | Deadline | Penalty |
|---|---|---|---|
| TP Documentation | Master File + Local File if revenue > SAR 100M | Annual, with tax return | 2.5% of underpaid tax |
| CbCR | If group revenue > SAR 3.2B | 12 months after year-end | SAR 10,000–100,000 |
| Form TP-1 | Related-party transactions disclosure | With tax return | SAR 25,000 |
| APA | Optional, unilateral / bilateral | 2–3 year negotiation | N/A |
| Thin Capitalization | 3:1 debt-to-equity | Ongoing | Disallowed interest |
| Withholding Tax | 5% on royalties, 5% on services | Per payment | 2.5% of underpaid |
| BEPS Alignment | Full OECD compliance expected | Ongoing | Increasing scrutiny |

---

## 9. Key Formulas

```python
# CUP Adjustment
adjusted_price = comparable_price + sum(adjustments for differences)
arm's_length_range = interquartile_range(adjusted_prices)
transfer_price = selected_point_in_range (typically median)

# Profit Split
combined_profit = sum(subsidiary_profits)
routine_return = routine_assets * market_return_rate
residual_profit = combined_profit - routine_return
contribution_weights = based_on_functional_analysis
allocation = residual_profit * contribution_weights

# Cost Plus
total_cost = direct_costs + indirect_costs + overhead
mark_up = arm's_length_margin (comparable companies or transactions)
arm's_length_price = total_cost * (1 + mark_up)

# Interquartile Range (IQR)
q1 = 25th percentile of comparables
q3 = 75th percentile of comparables
iqr = [q1, q3]
arm's_length_range = iqr
```

---

## 10. Reconciliation to Consolidated Financials

| Transfer | Subsidy Value ($M) | Consolidated Impact | Treatment |
|---|---|---|---|
| TP-001 (Halal meat) | 0.252 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-002 (Mineral water) | 0.720 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-003 (Salt/gypsum) | 0.022 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-004 (Pizza sauces) | 0.592 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-005 (Bakery mixes) | 0.221 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-006/007 (Marketing) | 0.092 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-008/009 (Packaging) | 0.090 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-010 (Certification) | 0.054 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-011 (Management) | 0.560 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-012 (IT) | 0.240 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-013 (Brand IP) | 0.300 | Eliminated in consolidation | Gross presentation, net in CE |
| TP-014/015 (Recipe IP) | 0.092 | Eliminated in consolidation | Gross presentation, net in CE |
| **Total Documented** | **3.174** | **Eliminated** | **—** |
| Implicit / Shared Services | 1.676 | Eliminated in consolidation | Net presentation |
| **Total Intercompany** | **4.850** | **Eliminated in consolidation** | **—** |

*Reconciles to COR-CON-FM-001 Interco Elimination of $5.2M Y5. Difference of $0.35M reflects timing, inventory in transit, and currency translation.*

---

## 11. Source Citations

| Benchmark | Source | Application |
|---|---|---|
| OECD Transfer Pricing Guidelines | OECD 2022 edition | Primary framework |
| Halal meat prices | Dubai Meat Market / FAO / ITC | CUP comparables |
| Mineral water prices | Euromonitor / Nielsen | CUP comparables |
| Pizza sauce prices | IRi / SPINS / industry data | CUP comparables |
| Management fee benchmarks | Bloomberg / RoyaltyStat | Cost Plus mark-up |
| IT outsourcing rates | Gartner / ISG | Cost Plus mark-up |
| Brand valuation | Interbrand / Brand Finance | Profit Split allocation |
| US TP regulations | Treas. Reg. §1.482, §1.6662 | US documentation |
| UAE CT / TP | Federal Decree-Law 47/2022 | UAE compliance |
| Saudi TP bylaws | ZATCA Transfer Pricing Bylaws 2019 | KSA compliance |
| India TP | Income Tax Act, Section 92 | India compliance |
| BEPS Action 13 | OECD / G20 | Global documentation |

---

*End of Corleone Enterprise Transfer Pricing Model*
