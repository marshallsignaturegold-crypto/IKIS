---
artifact_id: COR-AISTA-FM-010
type: financial_model
title: AISTA Corridor Financial Model — Infrastructure, Revenue, DSCR, IRR, Blended Finance
status: draft
pillar: B
tags: [aista_corridor, infrastructure, capex, dscr, irr, blended_finance, eca, dfi, miga, dfc, AISTA]
governance: SSS-FIN-001
version: 1.0
author: Beta | Financial Modeler
reviewed_by: Alpha | Chief Architect
date: 2025-01-15
---

# AISTA Corridor Financial Model — Infrastructure, Revenue & Blended Finance (Y1–Y10)

## Document Control

| Field | Value |
|---|---|
| Artifact ID | COR-AISTA-FM-010 |
| Version | 1.0 |
| Status | Draft |
| Pillar | B — AISTA Corridor |
| Governance | SSS-FIN-001 |

---

## 1. Executive Summary

The AISTA (AI-Sovereign Trade Architecture) Corridor is the infrastructure backbone connecting the SSS Firm (Pillar A) to Corleone Enterprise (Pillar C). This model covers infrastructure capex, operating costs, revenue from tolls/leases/concessions, DSCR (Debt Service Coverage Ratio) analysis, IRR by node, and the blended-finance capital stack including ECA senior debt, DFI debt, MIGA/DFC political risk insurance (PRI), sponsor equity, local partner equity, and catalytic first-loss capital.

---

## 2. Corridor Architecture & Nodes

### 2.1 Node Map

| Node | Location | Type | Priority | Status | Opening Year |
|---|---|---|---|---|---|
| Node 1 | Minneapolis, MN, USA | Origin / HQ | 1 | Operational Y0 | Y0 |
| Node 2 | Columbus, OH, USA | Hub | 1 | Operational Y1 | Y1 |
| Node 3 | Nashville, TN, USA | Hub | 1 | Operational Y2 | Y2 |
| Node 4 | Austin, TX, USA | Hub | 2 | Operational Y2 | Y2 |
| Node 5 | Indianapolis, IN, USA | Spoke | 3 | Operational Y3 | Y3 |
| Node 6 | Charlotte, NC, USA | Spoke | 3 | Operational Y3 | Y3 |
| Node 7 | Dubai, UAE | GCC Hub | 1 | Operational Y3 | Y3 |
| Node 8 | Riyadh, KSA | GCC Hub | 1 | Operational Y3 | Y3 |
| Node 9 | Jeddah, KSA | Port / Logistics | 2 | Operational Y4 | Y4 |
| Node 10 | Hargeisa, Somaliland | Origin / Processing | 1 | Operational Y3 | Y3 |
| Node 11 | Berbera, Somaliland | Port / Export | 1 | Operational Y4 | Y4 |
| Node 12 | Djibouti City, Djibouti | Transit / Port | 2 | Operational Y4 | Y4 |
| Node 13 | Addis Ababa, Ethiopia | Hub | 3 | Operational Y5 | Y5 |
| Node 14 | Mombasa, Kenya | Port / Hub | 3 | Operational Y5 | Y5 |
| Node 15 | Mumbai, India | Origin / Hub | 3 | Operational Y6 | Y6 |
| Node 16 | Singapore | Financial / Trading | 4 | Operational Y7 | Y7 |
| **Total Nodes** | **16** | — | — | — | — |

### 2.2 Link Types & Distances

| Link | From | To | Mode | Distance (km) | Capacity | Status |
|---|---|---|---|---|---|---|
| L1 | Minneapolis | Columbus | Truck / Rail | 1,050 | 500 TEU / week | Active |
| L2 | Columbus | Nashville | Truck | 550 | 300 TEU / week | Active |
| L3 | Nashville | Austin | Truck | 1,200 | 250 TEU / week | Active |
| L4 | Austin | Hargeisa | Air / Sea | 14,500 | 50 TEU / week | Active |
| L5 | Dubai | Riyadh | Truck | 1,000 | 400 TEU / week | Active |
| L6 | Riyadh | Jeddah | Truck | 950 | 350 TEU / week | Active |
| L7 | Hargeisa | Berbera | Truck | 160 | 200 TEU / week | Active |
| L8 | Berbera | Jeddah | Sea | 1,200 | 500 TEU / week | Active |
| L9 | Berbera | Djibouti | Sea | 300 | 150 TEU / week | Active |
| L10 | Djibouti | Addis Ababa | Truck / Rail | 800 | 200 TEU / week | Active |
| L11 | Addis Ababa | Mombasa | Truck / Rail | 1,500 | 250 TEU / week | Planned Y5 |
| L12 | Mumbai | Dubai | Sea | 2,500 | 1,000 TEU / week | Active |
| L13 | Dubai | Singapore | Sea | 6,000 | 2,000 TEU / week | Active |
| L14 | Singapore | Minneapolis | Air / Sea | 15,000 | 100 TEU / week | Active |

---

## 3. Infrastructure Capex ($M)

### 3.1 Capex by Node

| Node | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Node 1 (Minneapolis) | 2.0 | 0.5 | 0.3 | 0.2 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 3.7 |
| Node 2 (Columbus) | 1.5 | 1.0 | 0.5 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 4.0 |
| Node 3 (Nashville) | — | 1.2 | 0.8 | 0.4 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 3.1 |
| Node 4 (Austin) | — | 1.0 | 0.6 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 2.6 |
| Node 5 (Indianapolis) | — | — | 0.8 | 0.5 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 2.0 |
| Node 6 (Charlotte) | — | — | 0.8 | 0.5 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 2.0 |
| Node 7 (Dubai) | — | — | 3.0 | 1.5 | 1.0 | 0.5 | 0.3 | 0.2 | 0.2 | 0.2 | 6.9 |
| Node 8 (Riyadh) | — | — | 2.5 | 1.2 | 0.8 | 0.5 | 0.3 | 0.2 | 0.2 | 0.2 | 5.9 |
| Node 9 (Jeddah) | — | — | — | 2.0 | 1.0 | 0.5 | 0.3 | 0.2 | 0.2 | 0.2 | 4.4 |
| Node 10 (Hargeisa) | 0.5 | 1.0 | 2.0 | 1.0 | 0.5 | 0.3 | 0.2 | 0.2 | 0.2 | 0.2 | 6.1 |
| Node 11 (Berbera) | — | — | — | 3.5 | 1.5 | 0.8 | 0.5 | 0.3 | 0.2 | 0.2 | 7.0 |
| Node 12 (Djibouti) | — | — | — | 1.5 | 1.0 | 0.5 | 0.3 | 0.2 | 0.2 | 0.2 | 3.9 |
| Node 13 (Addis Ababa) | — | — | — | — | 2.0 | 1.0 | 0.5 | 0.3 | 0.2 | 0.2 | 4.2 |
| Node 14 (Mombasa) | — | — | — | — | 1.5 | 1.0 | 0.5 | 0.3 | 0.2 | 0.2 | 3.7 |
| Node 15 (Mumbai) | — | — | — | — | — | 2.0 | 1.0 | 0.5 | 0.3 | 0.2 | 4.0 |
| Node 16 (Singapore) | — | — | — | — | — | — | 2.5 | 1.0 | 0.5 | 0.3 | 4.3 |
| **Total Node Capex** | **4.0** | **4.7** | **11.3** | **12.9** | **10.3** | **7.6** | **6.9** | **4.1** | **3.0** | **2.7** | **67.5** |

### 3.2 Capex by Link

| Link | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 (Minneapolis-Columbus) | 1.0 | 0.3 | 0.1 | 0.1 | — | — | — | — | — | — | 1.5 |
| L2 (Columbus-Nashville) | 0.5 | 0.5 | 0.2 | 0.1 | — | — | — | — | — | — | 1.3 |
| L3 (Nashville-Austin) | — | 0.8 | 0.3 | 0.1 | — | — | — | — | — | — | 1.2 |
| L4 (Austin-Hargeisa) | — | — | 1.5 | 0.5 | 0.2 | — | — | — | — | — | 2.2 |
| L5 (Dubai-Riyadh) | — | — | 1.0 | 0.5 | 0.2 | — | — | — | — | — | 1.7 |
| L6 (Riyadh-Jeddah) | — | — | 0.8 | 0.4 | 0.2 | — | — | — | — | — | 1.4 |
| L7 (Hargeisa-Berbera) | 0.3 | 0.5 | 0.5 | 0.2 | 0.1 | — | — | — | — | — | 1.6 |
| L8 (Berbera-Jeddah) | — | — | — | 1.5 | 0.5 | 0.2 | — | — | — | — | 2.2 |
| L9 (Berbera-Djibouti) | — | — | — | 0.8 | 0.3 | 0.1 | — | — | — | — | 1.2 |
| L10 (Djibouti-Addis) | — | — | — | 1.0 | 0.5 | 0.2 | — | — | — | — | 1.7 |
| L11 (Addis-Mombasa) | — | — | — | — | 1.0 | 0.5 | — | — | — | — | 1.5 |
| L12 (Mumbai-Dubai) | — | — | 1.0 | 0.5 | 0.2 | — | — | — | — | — | 1.7 |
| L13 (Dubai-Singapore) | — | — | — | — | — | 1.0 | 0.5 | — | — | — | 1.5 |
| L14 (Singapore-Minneapolis) | — | — | — | — | — | — | 1.0 | 0.5 | — | — | 1.5 |
| **Total Link Capex** | **1.8** | **2.1** | **5.9** | **6.2** | **4.7** | **2.5** | **1.5** | **0.5** | — | — | **25.2** |

### 3.3 Total Infrastructure Capex Summary

| Category | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Nodes | 4.0 | 4.7 | 11.3 | 12.9 | 10.3 | 7.6 | 6.9 | 4.1 | 3.0 | 2.7 | 67.5 |
| Links | 1.8 | 2.1 | 5.9 | 6.2 | 4.7 | 2.5 | 1.5 | 0.5 | — | — | 25.2 |
| IT / Digital Platform | 0.5 | 0.8 | 1.2 | 1.5 | 1.0 | 0.8 | 0.6 | 0.4 | 0.3 | 0.2 | 7.3 |
| Contingency (10%) | 0.6 | 0.8 | 1.8 | 2.1 | 1.6 | 1.1 | 0.9 | 0.5 | 0.3 | 0.3 | 10.0 |
| **Total Capex** | **6.9** | **8.4** | **20.2** | **22.7** | **17.6** | **12.0** | **9.9** | **5.5** | **3.6** | **3.2** | **110.0** |

---

## 4. Operating Costs ($M, Y5)

### 4.1 Node Operating Costs

| Node | Staff | Utilities | Maintenance | Security | Insurance | IT / Comms | Admin | Total ($M) |
|---|---|---|---|---|---|---|---|---|
| Node 1 | 0.25 | 0.08 | 0.10 | 0.05 | 0.03 | 0.05 | 0.04 | 0.60 |
| Node 2 | 0.20 | 0.06 | 0.08 | 0.04 | 0.02 | 0.04 | 0.03 | 0.47 |
| Node 3 | 0.18 | 0.05 | 0.07 | 0.03 | 0.02 | 0.03 | 0.03 | 0.41 |
| Node 4 | 0.15 | 0.05 | 0.06 | 0.03 | 0.02 | 0.03 | 0.02 | 0.36 |
| Node 5 | 0.12 | 0.04 | 0.05 | 0.02 | 0.01 | 0.02 | 0.02 | 0.28 |
| Node 6 | 0.12 | 0.04 | 0.05 | 0.02 | 0.01 | 0.02 | 0.02 | 0.28 |
| Node 7 | 0.35 | 0.12 | 0.15 | 0.08 | 0.05 | 0.08 | 0.07 | 0.90 |
| Node 8 | 0.30 | 0.10 | 0.12 | 0.06 | 0.04 | 0.06 | 0.06 | 0.74 |
| Node 9 | 0.25 | 0.08 | 0.10 | 0.05 | 0.03 | 0.05 | 0.05 | 0.61 |
| Node 10 | 0.40 | 0.15 | 0.18 | 0.12 | 0.08 | 0.10 | 0.10 | 1.13 |
| Node 11 | 0.35 | 0.12 | 0.15 | 0.10 | 0.06 | 0.08 | 0.08 | 0.94 |
| Node 12 | 0.20 | 0.08 | 0.09 | 0.05 | 0.03 | 0.05 | 0.05 | 0.55 |
| Node 13 | 0.18 | 0.06 | 0.08 | 0.04 | 0.02 | 0.03 | 0.03 | 0.44 |
| Node 14 | 0.15 | 0.05 | 0.06 | 0.03 | 0.02 | 0.03 | 0.03 | 0.37 |
| Node 15 | 0.20 | 0.07 | 0.08 | 0.04 | 0.03 | 0.04 | 0.04 | 0.50 |
| Node 16 | 0.25 | 0.08 | 0.10 | 0.05 | 0.03 | 0.05 | 0.05 | 0.61 |
| **Total Nodes** | **3.65** | **1.23** | **1.52** | **0.77** | **0.48** | **0.72** | **0.65** | **9.22** |

### 4.2 Link Operating Costs

| Link | Transport | Fuel | Maintenance | Insurance | Tolls / Fees | IT / Tracking | Total ($M) |
|---|---|---|---|---|---|---|---|
| L1 | 0.12 | 0.08 | 0.05 | 0.02 | 0.01 | 0.02 | 0.30 |
| L2 | 0.08 | 0.05 | 0.03 | 0.01 | 0.01 | 0.01 | 0.19 |
| L3 | 0.10 | 0.06 | 0.04 | 0.02 | 0.01 | 0.01 | 0.24 |
| L4 | 0.15 | 0.10 | 0.05 | 0.03 | 0.02 | 0.02 | 0.37 |
| L5 | 0.12 | 0.08 | 0.04 | 0.02 | 0.01 | 0.01 | 0.28 |
| L6 | 0.10 | 0.07 | 0.04 | 0.02 | 0.01 | 0.01 | 0.25 |
| L7 | 0.08 | 0.05 | 0.03 | 0.01 | 0.01 | 0.01 | 0.19 |
| L8 | 0.20 | 0.15 | 0.08 | 0.04 | 0.02 | 0.02 | 0.51 |
| L9 | 0.10 | 0.07 | 0.04 | 0.02 | 0.01 | 0.01 | 0.25 |
| L10 | 0.12 | 0.08 | 0.05 | 0.02 | 0.01 | 0.01 | 0.29 |
| L11 | 0.15 | 0.10 | 0.06 | 0.03 | 0.02 | 0.01 | 0.37 |
| L12 | 0.18 | 0.12 | 0.06 | 0.03 | 0.02 | 0.02 | 0.43 |
| L13 | 0.25 | 0.18 | 0.08 | 0.04 | 0.02 | 0.02 | 0.59 |
| L14 | 0.15 | 0.10 | 0.05 | 0.03 | 0.02 | 0.02 | 0.37 |
| **Total Links** | **1.90** | **1.29** | **0.70** | **0.32** | **0.22** | **0.20** | **4.63** |

### 4.3 Total Operating Costs ($M)

| Category | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Node Operations | 1.5 | 2.8 | 4.5 | 6.2 | 9.2 | 10.5 | 11.8 | 12.5 | 13.0 | 13.5 |
| Link Operations | 0.8 | 1.5 | 2.5 | 3.5 | 4.6 | 5.2 | 5.8 | 6.2 | 6.5 | 6.8 |
| IT / Platform | 0.5 | 0.8 | 1.2 | 1.5 | 1.8 | 2.0 | 2.2 | 2.4 | 2.5 | 2.6 |
| G&A / Corporate | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 |
| **Total OpEx** | **3.0** | **5.5** | **8.8** | **12.0** | **16.6** | **18.8** | **21.0** | **22.4** | **23.4** | **24.4** |

---

## 5. Revenue Model — Tolls, Leases & Concessions

### 5.1 Toll Revenue by Link ($M, Y5)

| Link | Traffic (TEU/week) | Avg Toll / TEU | Weekly Revenue | Annual Revenue ($M) |
|---|---|---|---|---|
| L1 | 300 | $85 | $25,500 | $1.33 |
| L2 | 200 | $75 | $15,000 | $0.78 |
| L3 | 150 | $80 | $12,000 | $0.62 |
| L4 | 30 | $450 | $13,500 | $0.70 |
| L5 | 250 | $120 | $30,000 | $1.56 |
| L6 | 200 | $110 | $22,000 | $1.14 |
| L7 | 150 | $95 | $14,250 | $0.74 |
| L8 | 100 | $280 | $28,000 | $1.46 |
| L9 | 80 | $200 | $16,000 | $0.83 |
| L10 | 100 | $150 | $15,000 | $0.78 |
| L11 | 80 | $180 | $14,400 | $0.75 |
| L12 | 200 | $160 | $32,000 | $1.66 |
| L13 | 150 | $220 | $33,000 | $1.72 |
| L14 | 20 | $380 | $7,600 | $0.40 |
| **Total Tolls** | **2,010** | — | **$298,150** | **$15.47** |

### 5.2 Lease Revenue by Node ($M, Y5)

| Node | Leasable Space (sqm) | Avg Rent / sqm / yr | Occupancy | Annual Revenue ($M) |
|---|---|---|---|---|
| Node 1 | 5,000 | $180 | 85% | $0.77 |
| Node 2 | 4,000 | $160 | 80% | $0.51 |
| Node 3 | 3,500 | $150 | 75% | $0.39 |
| Node 4 | 3,000 | $140 | 70% | $0.29 |
| Node 5 | 2,500 | $130 | 65% | $0.21 |
| Node 6 | 2,500 | $130 | 65% | $0.21 |
| Node 7 | 8,000 | $220 | 90% | $1.58 |
| Node 8 | 7,000 | $200 | 85% | $1.19 |
| Node 9 | 6,000 | $190 | 80% | $0.91 |
| Node 10 | 4,000 | $80 | 70% | $0.22 |
| Node 11 | 5,000 | $90 | 75% | $0.34 |
| Node 12 | 3,000 | $100 | 70% | $0.21 |
| Node 13 | 3,500 | $85 | 65% | $0.19 |
| Node 14 | 3,000 | $90 | 70% | $0.19 |
| Node 15 | 4,000 | $110 | 75% | $0.33 |
| Node 16 | 5,000 | $250 | 90% | $1.13 |
| **Total Leases** | **69,000** | — | **76%** | **$9.67** |

### 5.3 Concession Revenue ($M, Y5)

| Concession | Type | Term | Annual Fee | Revenue Share | Y5 Revenue ($M) |
|---|---|---|---|---|---|
| Berbera Port Handling | Exclusive | 25 years | $0.50M | 5% of throughput | $0.80 |
| Hargeisa Processing Zone | Exclusive | 20 years | $0.30M | 3% of processing value | $0.45 |
| Dubai Logistics Hub | Non-exclusive | 15 years | $0.40M | 2% of logistics value | $0.60 |
| Riyadh Cold Chain | Non-exclusive | 15 years | $0.25M | 2% of throughput value | $0.35 |
| Mineral Extraction (Salt) | Exclusive | 25 years | $0.05M | 3% of gross | $0.15 |
| Mineral Extraction (Gypsum) | Exclusive | 20 years | $0.04M | 2.5% of gross | $0.12 |
| Water Bottling | Exclusive | 30 years | $0.03M | 1.5% of gross | $0.16 |
| AISTA Digital Platform | Exclusive | 10 years | $0.20M | 1% of transaction value | $0.25 |
| **Total Concessions** | — | — | **$1.77M** | — | **$2.88** |

### 5.4 Ancillary Revenue ($M, Y5)

| Revenue Stream | Description | Y5 ($M) | Y10 ($M) |
|---|---|---|---|
| Insurance Services | Cargo, transit, political risk | $0.80 | $1.50 |
| Customs Brokerage | Documentation, clearance | $0.60 | $1.20 |
| Trade Finance Facilitation | Letters of credit, factoring | $0.50 | $1.00 |
| Data & Analytics | Corridor intelligence, market data | $0.30 | $0.80 |
| Training & Certification | Halal, logistics, compliance | $0.20 | $0.50 |
| **Total Ancillary** | — | **$2.40** | **$5.00** |

### 5.5 Total Revenue Summary ($M)

| Revenue Category | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Tolls | 1.5 | 3.0 | 6.0 | 10.0 | 15.5 | 18.0 | 20.5 | 22.0 | 23.5 | 25.0 |
| Leases | 0.8 | 1.5 | 3.0 | 5.5 | 9.7 | 11.5 | 13.0 | 14.0 | 15.0 | 16.0 |
| Concessions | 0.2 | 0.5 | 1.0 | 1.8 | 2.9 | 3.5 | 4.0 | 4.5 | 5.0 | 5.5 |
| Ancillary | 0.1 | 0.3 | 0.6 | 1.2 | 2.4 | 3.0 | 3.8 | 4.5 | 5.2 | 5.8 |
| **Total Revenue** | **2.6** | **5.3** | **10.6** | **18.5** | **30.5** | **36.0** | **41.3** | **45.0** | **48.7** | **52.3** |

---

## 6. P&L Summary — AISTA Corridor ($M)

| Line Item | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Total Revenue** | **2.6** | **5.3** | **10.6** | **18.5** | **30.5** | **36.0** | **41.3** | **45.0** | **48.7** | **52.3** |
| Operating Costs | 3.0 | 5.5 | 8.8 | 12.0 | 16.6 | 18.8 | 21.0 | 22.4 | 23.4 | 24.4 |
| **EBITDA** | **-0.4** | **-0.2** | **1.8** | **6.5** | **13.9** | **17.2** | **20.3** | **22.6** | **25.3** | **27.9** |
| EBITDA Margin | -15.4% | -3.8% | 17.0% | 35.1% | 45.6% | 47.8% | 49.2% | 50.2% | 52.0% | 53.3% |
| D&A | 0.5 | 1.0 | 2.0 | 3.0 | 4.5 | 5.0 | 5.5 | 6.0 | 6.5 | 7.0 |
| **EBIT** | **-0.9** | **-1.2** | **-0.2** | **3.5** | **9.4** | **12.2** | **14.8** | **16.6** | **18.8** | **20.9** |
| Interest Expense | 0.2 | 0.5 | 1.0 | 1.8 | 2.8 | 3.2 | 3.5 | 3.8 | 4.0 | 4.2 |
| **EBT** | **-1.1** | **-1.7** | **-1.2** | **1.7** | **6.6** | **9.0** | **11.3** | **12.8** | **14.8** | **16.7** |
| Taxes | — | — | — | — | 1.0 | 1.4 | 1.7 | 1.9 | 2.2 | 2.5 |
| **Net Income** | **-1.1** | **-1.7** | **-1.2** | **1.7** | **5.6** | **7.6** | **9.6** | **10.9** | **12.6** | **14.2** |
| Net Margin | -42.3% | -32.1% | -11.3% | 9.2% | 18.4% | 21.1% | 23.2% | 24.2% | 25.9% | 27.1% |

---

## 7. Debt Service Coverage Ratio (DSCR) Analysis

### 7.1 Debt Schedule

| Tranche | Lender | Amount ($M) | Interest Rate | Term | Grace Period | Repayment Start | Security |
|---|---|---|---|---|---|---|---|
| Senior Debt (ECA) | US EXIM / Euler Hermes | 40.0 | 5.5% (fixed) | 12 years | 3 years | Y4 | Sovereign guarantee, project assets |
| Senior Debt (DFI) | IFC / DEG / FMO | 30.0 | 6.0% (fixed) | 10 years | 2 years | Y3 | Project assets, assignment of revenues |
| Subordinated Debt | AfDB / EBRD | 15.0 | 7.5% (fixed) | 10 years | 4 years | Y5 | Second lien, sponsor guarantee |
| Local Currency | Somaliland Central Bank | 5.0 | 8.0% (fixed) | 8 years | 2 years | Y3 | Local assets, concession |
| **Total Debt** | — | **90.0** | **6.0% blended** | — | — | — | — |

### 7.2 DSCR Calculation ($M, Y5)

| Item | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|
| EBITDA | 1.8 | 6.5 | 13.9 | 17.2 | 20.3 | 22.6 | 25.3 | 27.9 |
| Less: Cash Taxes | — | — | 1.0 | 1.4 | 1.7 | 1.9 | 2.2 | 2.5 |
| Less: Maintenance Capex | 1.5 | 2.0 | 2.5 | 2.8 | 3.0 | 3.2 | 3.4 | 3.6 |
| Less: Working Capital Change | 0.5 | 0.8 | 1.0 | 0.8 | 0.6 | 0.5 | 0.4 | 0.3 |
| **Cash Available for Debt Service (CAFDS)** | **-0.2** | **3.7** | **9.4** | **12.2** | **15.0** | **17.0** | **19.3** | **21.5** |
| Principal Repayment | — | 2.5 | 5.0 | 6.0 | 7.0 | 8.0 | 8.5 | 9.0 |
| Interest Expense | 1.8 | 2.8 | 2.8 | 3.2 | 3.5 | 3.8 | 4.0 | 4.2 |
| **Total Debt Service** | **1.8** | **5.3** | **7.8** | **9.2** | **10.5** | **11.8** | **12.5** | **13.2** |
| **DSCR (CAFDS / TDS)** | **-0.11** | **0.70** | **1.21** | **1.33** | **1.43** | **1.44** | **1.54** | **1.63** |
| **Minimum Required DSCR** | 1.20 | 1.20 | 1.20 | 1.20 | 1.20 | 1.20 | 1.20 | 1.20 |
| **DSCR Covenant Compliance** | **Fail** | **Fail** | **Pass** | **Pass** | **Pass** | **Pass** | **Pass** | **Pass** |

*Note: DSCR fails in Y3 and Y4 due to construction-phase capex and ramp-up. DSCR reserve account (6 months debt service) and standby equity commitment cover shortfalls. ECA/DFI forbearance provisions triggered for Y3–Y4.*

### 7.3 LLCR (Loan Life Cover Ratio)

| Year | NPV of CAFDS (Remaining) | Outstanding Debt | LLCR | Threshold |
|---|---|---|---|---|
| Y3 | 45.0 | 88.0 | 0.51 | 1.20 |
| Y4 | 52.0 | 82.0 | 0.63 | 1.20 |
| Y5 | 58.0 | 75.0 | 0.77 | 1.20 |
| Y6 | 62.0 | 68.0 | 0.91 | 1.20 |
| Y7 | 65.0 | 60.0 | 1.08 | 1.20 |
| Y8 | 66.0 | 51.0 | 1.29 | 1.20 |
| Y9 | 64.0 | 41.0 | 1.56 | 1.20 |
| Y10 | 58.0 | 30.0 | 1.93 | 1.20 |

*LLCR breaches Y3–Y7. Remedial actions: equity cure rights, cash sweep, standby equity.*

---

## 8. IRR by Node & Project

### 8.1 Node-Level IRR (Unlevered, 10-year)

| Node | Capex ($M) | NPV of FCF ($M) | IRR (Unlevered) | IRR (Levered) | Equity Invested ($M) | Equity IRR |
|---|---|---|---|---|---|---|
| Node 1 (Minneapolis) | 3.7 | 8.5 | 28.5% | 32.0% | 1.5 | 38.0% |
| Node 2 (Columbus) | 4.0 | 7.2 | 24.0% | 28.0% | 1.6 | 34.0% |
| Node 3 (Nashville) | 3.1 | 5.8 | 22.5% | 26.0% | 1.2 | 31.0% |
| Node 4 (Austin) | 2.6 | 4.5 | 20.0% | 24.0% | 1.0 | 28.0% |
| Node 7 (Dubai) | 6.9 | 15.0 | 26.0% | 30.0% | 2.8 | 36.0% |
| Node 8 (Riyadh) | 5.9 | 12.0 | 24.5% | 28.5% | 2.4 | 34.0% |
| Node 9 (Jeddah) | 4.4 | 8.5 | 25.0% | 29.0% | 1.8 | 35.0% |
| Node 10 (Hargeisa) | 6.1 | 10.0 | 18.0% | 22.0% | 2.5 | 26.0% |
| Node 11 (Berbera) | 7.0 | 12.5 | 20.5% | 25.0% | 2.8 | 30.0% |
| Node 12 (Djibouti) | 3.9 | 6.5 | 21.0% | 25.5% | 1.6 | 31.0% |
| Node 13 (Addis Ababa) | 4.2 | 7.0 | 19.5% | 24.0% | 1.7 | 29.0% |
| Node 14 (Mombasa) | 3.7 | 6.0 | 20.0% | 24.5% | 1.5 | 29.5% |
| Node 15 (Mumbai) | 4.0 | 8.0 | 24.0% | 28.0% | 1.6 | 34.0% |
| Node 16 (Singapore) | 4.3 | 9.0 | 25.5% | 30.0% | 1.7 | 36.0% |
| **Blended Corridor** | **67.5** | **130.5** | **23.0%** | **27.0%** | **27.0** | **32.0%** |

### 8.2 Link-Level IRR

| Link | Capex ($M) | NPV of FCF ($M) | IRR (Unlevered) | Equity IRR |
|---|---|---|---|---|
| L1 | 1.5 | 3.2 | 26.0% | 35.0% |
| L2 | 1.3 | 2.5 | 22.0% | 30.0% |
| L3 | 1.2 | 2.0 | 19.0% | 26.0% |
| L8 (Berbera-Jeddah) | 2.2 | 5.5 | 28.0% | 38.0% |
| L12 (Mumbai-Dubai) | 1.7 | 3.8 | 27.0% | 36.0% |
| L13 (Dubai-Singapore) | 1.5 | 3.5 | 28.0% | 37.0% |
| **Blended Links** | **25.2** | **52.0** | **24.0%** | **33.0%** |

---

## 9. Blended-Finance Capital Stack

### 9.1 Capital Structure ($M, Y5)

| Layer | Source | Amount | % of Total | Terms | Risk Profile | Expected Return |
|---|---|---|---|---|---|---|
| Senior Debt (ECA) | US EXIM, Euler Hermes, Coface | 40.0 | 36.4% | 5.5% fixed, 12-year, sovereign guarantee | Lowest | 5.5% |
| Senior Debt (DFI) | IFC, DEG, FMO, AfDB | 30.0 | 27.3% | 6.0% fixed, 10-year, project finance | Low | 6.0% |
| Subordinated Debt | AfDB, EBRD, local banks | 15.0 | 13.6% | 7.5% fixed, 10-year, second lien | Medium | 7.5% |
| Local Currency Debt | Somaliland Central Bank | 5.0 | 4.5% | 8.0% fixed, 8-year, local assets | Medium-High | 8.0% |
| **Total Debt** | — | **90.0** | **81.8%** | — | — | **6.0% blended** |
| Sponsor Equity (SSS Firm) | Pillar A | 12.0 | 10.9% | Common equity, 25% ownership | High | 18.0% |
| Sponsor Equity (CE) | Pillar C | 8.0 | 7.3% | Common equity, 15% ownership | High | 18.0% |
| **Total Equity** | — | **20.0** | **18.2%** | — | — | **18.0% blended** |
| **Total Project Cost** | — | **110.0** | **100%** | — | — | **8.0% WACC** |

### 9.2 Catalytic First-Loss Capital

| Tranche | Provider | Amount ($M) | Structure | Trigger | Return |
|---|---|---|---|---|---|
| First-Loss Equity | DFC (US) | 5.0 | Equity, subordinate to sponsor | DSCR < 1.0 for 2 consecutive quarters | 12.0% preferred return |
| First-Loss Guarantee | MIGA | 10.0 | Political risk insurance | Expropriation, political violence, currency inconvertibility | 1.5% premium |
| First-Loss Guarantee | AfDB | 5.0 | Partial risk guarantee | Sovereign default, payment delay | 1.0% premium |
| Technical Assistance | USAID | 2.0 | Grant, non-repayable | Corridor development, capacity building | N/A |
| Concessional Loan | IDA / World Bank | 8.0 | 2.0% fixed, 20-year, 10-year grace | Frontier market infrastructure | 2.0% |
| **Total Catalytic** | — | **30.0** | — | — | — |

### 9.3 Blended-Finance Impact

| Metric | Without Catalytic | With Catalytic | Improvement |
|---|---|---|---|
| Senior Debt Interest Rate | 7.5% | 5.5% | -200 bps |
| Debt Tenor | 8 years | 12 years | +4 years |
| Grace Period | 1 year | 3 years | +2 years |
| Equity Required | $35.0M | $20.0M | -$15.0M |
| DSCR (Y5) | 0.95 | 1.21 | +26% |
| Project IRR | 19.0% | 23.0% | +400 bps |
| Equity IRR | 24.0% | 32.0% | +800 bps |
| Viability | Marginal | Robust | — |

---

## 10. MIGA / DFC Political Risk Insurance (PRI)

### 10.1 PRI Coverage

| Risk Type | Coverage ($M) | Premium (% of coverage) | Annual Premium ($M) | Provider |
|---|---|---|---|---|
| Expropriation | 15.0 | 0.8% | 0.120 | MIGA |
| Political Violence | 10.0 | 1.2% | 0.120 | MIGA |
| Currency Inconvertibility | 8.0 | 1.0% | 0.080 | MIGA |
| Breach of Contract | 12.0 | 1.5% | 0.180 | DFC |
| Non-Honoring of Sovereign Guarantee | 10.0 | 1.0% | 0.100 | MIGA |
| War & Civil Disturbance | 5.0 | 2.0% | 0.100 | DFC |
| **Total PRI Coverage** | **60.0** | **1.17% avg** | **0.70** | — |

### 10.2 PRI Claim Scenarios

| Scenario | Probability | Potential Loss ($M) | Coverage ($M) | Net Loss ($M) |
|---|---|---|---|---|
| Somaliland political instability | 15% | 8.0 | 6.0 | 2.0 |
| Berbera port concession dispute | 8% | 5.0 | 4.0 | 1.0 |
| Currency inconvertibility (SLL) | 12% | 3.0 | 2.5 | 0.5 |
| Expropriation of mineral assets | 5% | 10.0 | 8.0 | 2.0 |
| Breach of contract (KSA) | 5% | 6.0 | 5.0 | 1.0 |
| War / civil disturbance | 3% | 15.0 | 12.0 | 3.0 |
| **Expected Loss (uninsured)** | — | — | — | **$1.45M** |
| **Expected Loss (insured)** | — | — | — | **$0.35M** |

---

## 11. Key Formulas

```python
# DSCR
dscr = (ebitda - cash_taxes - maintenance_capex - wc_change) / (principal_repayment + interest_expense)

# LLCR
llcr = npv(remaining_cafds, discount_rate) / outstanding_debt

# IRR
irr = np.irr(cash_flows)

# WACC (project)
wacc = (debt / total_capital) * cost_of_debt * (1 - tax_rate) + (equity / total_capital) * cost_of_equity

# Blended return
blended_return = sum(layer_amount * layer_return for layer in capital_stack) / total_capital

# Revenue per TEU
revenue_per_teu = total_toll_revenue / total_teu_volume

# Concession revenue
concession_revenue = fixed_fee + (revenue_share * throughput_value)
```

---

## 12. Reconciliation to Consolidated Model

### 12.1 AISTA Corridor Revenue to Consolidated

| Year | AISTA Corridor Revenue | Consolidated Revenue | CE Share (Intercompany) | External Revenue | Status |
|---|---|---|---|---|---|
| Y1 | 2.6 | 5.7 | 2.0 | 3.7 | ✓ |
| Y2 | 5.3 | 19.1 | 4.5 | 14.6 | ✓ |
| Y3 | 10.6 | 37.9 | 7.0 | 30.9 | ✓ |
| Y4 | 18.5 | 60.2 | 10.0 | 50.2 | ✓ |
| Y5 | 30.5 | 85.8 | 12.0 | 73.8 | ✓ |

*Note: AISTA Corridor revenue is not fully consolidated into Corleone Enterprise P&L. The CE share represents intercompany charges for use of corridor infrastructure (tolls, leases, logistics). These are eliminated in consolidated reporting. The AISTA Corridor operates as a separate Pillar B entity with its own financials, though integrated with CE operations.*

### 12.2 AISTA Corridor EBITDA to Consolidated

| Year | AISTA Corridor EBITDA | Consolidated EBITDA | CE Allocation (OpEx) | Net Corridor Contribution | Status |
|---|---|---|---|---|---|
| Y3 | 1.8 | 4.9 | -0.8 | 1.0 | ✓ |
| Y4 | 6.5 | 10.6 | -1.5 | 5.0 | ✓ |
| Y5 | 13.9 | 18.1 | -2.5 | 11.4 | ✓ |

*Note: AISTA Corridor's positive EBITDA is partially offset by CE's allocation of infrastructure costs. The net corridor contribution to consolidated EBITDA is positive and growing, reflecting the strategic value of the corridor infrastructure.*

---

## 13. Source Citations

| Benchmark | Source | Value Used |
|---|---|---|
| Infrastructure capex benchmarks | World Bank PPI / FDI Markets | $67.5M nodes, $25.2M links |
| ECA lending terms | US EXIM, Euler Hermes, Coface | 5.5% fixed, 12-year |
| DFI project finance | IFC, DEG, FMO pricing | 6.0% fixed, 10-year |
| MIGA PRI premiums | MIGA pricing grid | 0.8–2.0% |
| DFC political risk | DFC exposure fee schedule | 1.0–2.0% |
| Toll rates | Global toll road data, ADB | $75–450/TEU |
| Logistics lease rates | CBRE / JLL / local brokers | $80–250/sqm |
| Concession terms | IFC concession database | 15–30 years |
| DSCR thresholds | Project finance bank standards | 1.20x minimum |
| IRR benchmarks | Infrastructure Investor / Preqin | 15–25% unlevered |
| Blended finance | OECD DAC / Convergence | Catalytic 30% of project |

---

*End of AISTA Corridor Financial Model*
