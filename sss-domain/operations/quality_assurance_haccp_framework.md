---
artifact_id: SSTP-OPS-002
type: operations_document
title: Quality Assurance and HACCP Framework
status: draft
pillar: C - Corleone Enterprise
tags:
  - quality
  - food safety
  - HACCP
  - halal
  - audit
  - traceability
governance:
  owner: Chief Quality Officer
  approver: Board Risk Committee
  review_cycle: annual
  next_review: 2026-01-15
  document_control: controlled
created_date: 2025-04-01
version: 1.0
---

# Quality Assurance and HACCP Framework

## Document Control

| Field | Value |
|-------|-------|
| Document ID | SSTP-OPS-002 |
| Version | 1.0 |
| Author | Quality Assurance Department |
| Owner | Chief Quality Officer (CQO) |
| Approved By | Board Risk Committee |
| Classification | Restricted |
| Review Cycle | Annual |
| Next Review Date | 2026-01-15 |

---

## 1. Executive Summary

This document establishes the Quality Assurance (QA) and Hazard Analysis Critical Control Point (HACCP) framework for all food production and handling activities within the SSTP Corleone Enterprise ecosystem. It covers five operational entities: Don Vito's Pizza Oven (80 units Y5, $28M), Vito Corleone Bakery & Cafe (60 units Y5, $14M), Corleone Products CPG manufacturing (16 SKUs, $33M Y5), Vito Corleone Media & Licensing, and Corleone Halal Meats Somaliland SPV ($12M Y5, halal slaughterhouse and mineral extraction). The framework ensures compliance with Saudi SFDA, UAE MOHAP, Qatar MOPH, India FSSAI, Kenya KEBS, Egypt EOS, and Somaliland Ministry of Livestock requirements.

---

## 2. HACCP Plans by Production Facility

### 2.1 Don Vito's Pizza Oven — Central Commissary HACCP

| HACCP Element | Description |
|---------------|-------------|
| Product Description | Fresh and frozen pizza dough, sauces, pre-portioned toppings |
| Intended Use | Retail sale through 80 franchise units across 6 markets |
| Consumers | General public, including vulnerable groups |
| Flow Diagram | Receiving → Storage → Prep → Mixing → Proofing → Portioning → Packaging → Cold Storage → Distribution |

**Hazard Analysis Table:**

| Step | Hazard | Category | Likelihood | Severity | Risk | CCP? |
|------|--------|----------|------------|----------|------|------|
| Receiving flour | Allergen (gluten), mycotoxins | Chemical | Medium | High | High | CCP-1 |
| Receiving cheese | Pathogen (L. monocytogenes) | Biological | Medium | High | High | CCP-2 |
| Receiving toppings | Pathogen, allergens | Biological/Chemical | Medium | High | High | CCP-3 |
| Mixing dough | Foreign body (metal) | Physical | Low | Medium | Medium | No |
| Proofing | Pathogen growth (time/temp) | Biological | Medium | High | High | CCP-4 |
| Portioning | Cross-contamination | Biological | Medium | Medium | Medium | No (PRP) |
| Packaging | Seal integrity, labeling | Physical/Chemical | Low | High | Medium | CCP-5 |
| Cold storage | Pathogen growth (temp abuse) | Biological | Medium | High | High | CCP-6 |
| Distribution | Temperature abuse | Biological | Medium | High | High | CCP-7 |

### 2.2 Vito Corleone Bakery & Cafe — Central Commissary HACCP

| HACCP Element | Description |
|---------------|-------------|
| Product Description | Bread, pastries, cakes, cookies, sandwiches |
| Intended Use | Retail sale through 60 bakery units |
| Consumers | General public |
| Flow Diagram | Receiving → Storage → Weighing → Mixing → Baking → Decorating → Packaging → Display/Distribution |

**Hazard Analysis Table:**

| Step | Hazard | Category | Likelihood | Severity | Risk | CCP? |
|------|--------|----------|------------|----------|------|------|
| Receiving eggs | Salmonella spp. | Biological | Medium | High | High | CCP-B1 |
| Receiving dairy | Pathogen, antibiotic residue | Biological/Chemical | Low | High | High | CCP-B2 |
| Baking | Insufficient kill step | Biological | Low | High | Medium | No (time/temp PRP) |
| Decorating | Allergen cross-contact | Chemical | Medium | High | High | CCP-B3 |
| Cooling | Pathogen growth (S. aureus) | Biological | Medium | High | High | CCP-B4 |
| Packaging | Allergen labeling error | Chemical | Low | High | Medium | CCP-B5 |

### 2.3 Corleone Products CPG Manufacturing HACCP

| Facility | Products | HACCP Plan ID | Certifications |
|----------|----------|---------------|----------------|
| Jeddah Plant | Sauces, dressings, marinades | CPG-HACCP-001 | FSSC 22000, SFDA, Halal |
| Jeddah Plant 2 | Frozen appetizers, ready meals | CPG-HACCP-002 | FSSC 22000, SFDA, Halal |
| Dubai Contract Mfg | Snacks, seasonings | CPG-HACCP-003 | FSSC 22000, MOHAP, Halal |
| India Co-man | Spice blends, pickles | CPG-HACCP-004 | FSSAI, FSSC 22000 |

**CPG Critical Control Points:**

| CCP | Process Step | Hazard | Critical Limit | Monitoring | Frequency | Corrective Action | Verification |
|-----|-------------|--------|---------------|------------|-----------|-----------------|------------|
| CPG-1 | Receiving raw materials | Pathogen, chemicals, allergens | Certificate of analysis; allergen-free declaration | COA review, organoleptic | Per batch | Reject, quarantine, notify supplier | Quarterly supplier audit |
| CPG-2 | Metal detection | Metal fragments | Fe >1.5mm, Non-Fe >2.0mm, SS >2.5mm | Metal detector, test sticks | Every 2 hours | Stop line, isolate product, investigate | Daily calibration check |
| CPG-3 | Thermal processing (sauces) | Pathogen survival | >85°C core temp for >2 min | Chart recorder, temp probe | Continuous | Extend time/temp, reprocess, reject | Weekly calibration, annual validation |
| CPG-4 | pH control (acidified) | C. botulinum growth | pH <4.6 | pH meter | Per batch | Adjust acid, re-test, reject | Daily pH meter calibration |
| CPG-5 | Blast freezing | Pathogen growth | <-18°C within 4 hours of processing | Temp recorder | Continuous | Extend freezing, reject if exceeded | Weekly calibration |
| CPG-6 | Allergen control | Undeclared allergen | Dedicated lines or validated CIP | Swab testing, visual inspection | Per changeover | Re-clean, hold product, test | Weekly ELISA verification |
| CPG-7 | Label application | Incorrect allergen declaration | Match to approved spec | Vision system | Every pack | Stop line, reject, reprint | Daily vision system check |

### 2.4 Corleone Halal Meats — Somaliland Slaughterhouse HACCP

| HACCP Element | Description |
|---------------|-------------|
| Product Description | Fresh and frozen halal beef, lamb, goat, camel meat and offal |
| Intended Use | B2B export to GCC, local retail, Corleone Products ingredient |
| Consumers | Muslim and general consumers requiring halal certification |
| Flow Diagram | Animal receiving → Resting → Halal slaughter → Evisceration → Splitting → Chilling → Boning → Packaging → Freezing → Storage → Export |

**Hazard Analysis Table:**

| Step | Hazard | Category | Likelihood | Severity | Risk | CCP? |
|------|--------|----------|------------|----------|------|------|
| Animal receiving | Disease (FMD, BSE), antibiotic residue | Biological/Chemical | Medium | High | High | CCP-H1 |
| Resting | Pathogen shedding, stress | Biological | Medium | Medium | Medium | No (PRP) |
| Halal slaughter | Improper stunning, cross-contamination | Religious/Biological | Low | High | High | CCP-H2 |
| Evisceration | Fecal contamination (E. coli O157) | Biological | High | High | High | CCP-H3 |
| Chilling | Pathogen growth (time/temp) | Biological | Medium | High | High | CCP-H4 |
| Boning | Cross-contamination, foreign body | Biological/Physical | Medium | Medium | Medium | No (PRP) |
| Packaging | Label integrity, traceability | Chemical/Physical | Low | High | Medium | CCP-H5 |
| Freezing | Temperature abuse | Biological | Medium | High | High | CCP-H6 |

---

## 3. Prerequisite Programs (PRPs)

### 3.1 Good Manufacturing Practices (GMP)

| GMP Element | Standard | Frequency | Responsible |
|-------------|----------|-----------|-------------|
| Personnel hygiene | SOP-QA-001 | Daily | Production Supervisor |
| Uniform and PPE | SOP-QA-002 | Daily | Production Supervisor |
| Hand washing | SOP-QA-003 | Every entry, every break | All employees |
| Illness policy | SOP-QA-004 | Ongoing | HR + QA |
| Visitor control | SOP-QA-005 | Per visit | QA Manager |
| Training | SOP-QA-006 | Monthly | QA Training |
| Building maintenance | SOP-QA-007 | Weekly | Facilities |
| Equipment maintenance | SOP-QA-008 | Per schedule | Maintenance |
| Calibration program | SOP-QA-009 | Per instrument | QA Technician |

### 3.2 Sanitation and Pest Control

| Program | Scope | Provider | Frequency | Documentation |
|---------|-------|----------|-----------|---------------|
| Master sanitation | All facilities | Internal + third-party | Daily/weekly/monthly | Sanitation log |
| ATP bioluminescence | Contact surfaces | Internal | Post-sanitation | ATP meter readings |
| Microbiological swabs | High-risk zones | Third-party lab | Weekly | Lab reports |
| Pest control | All facilities | Rentokil / local | Monthly service + daily checks | Pest sighting log, service reports |
| Water quality | Potable water, process water | Third-party lab | Monthly | Water analysis certificates |
| Air quality | Production zones | Third-party | Quarterly | Air quality reports |

### 3.3 Supplier Approval Program

| Supplier Category | Approval Requirements | Audit Frequency | Risk Rating |
|-------------------|---------------------|---------------|-------------|
| A: Raw meat (Somaliland) | On-site audit, COA, halal cert, veterinary cert | Quarterly | High |
| B: Dairy, eggs | COA, third-party audit, allergen statement | Annual | High |
| C: Flour, grains | COA, third-party cert (FSSC/BRC) | Bi-annual | Medium |
| D: Packaging (food contact) | Migration testing, COA, food contact declaration | Annual | Medium |
| E: Chemicals, cleaning | COA, SDS, approved supplier list | Annual | Medium |
| F: Indirect materials | Basic qualification, COA | Bi-annual | Low |

---

## 4. Hazard Analysis Detail

### 4.1 Biological Hazards

| Hazard | Source | Control Measures | CCP |
|--------|--------|-----------------|-----|
| Salmonella spp. | Poultry, eggs, raw ingredients | Cooking, supplier control, cross-contamination prevention | CPG-3, CCP-B1 |
| E. coli O157:H7 | Beef, leafy greens | Cooking, supplier control, separation | CCP-H3, CPG-3 |
| L. monocytogenes | Dairy, ready-to-eat foods | Cold chain control, sanitation, shelf-life management | CCP-6, CCP-B4 |
| S. aureus | Human handling, cooling | Time/temp control, personnel hygiene, rapid cooling | CCP-B4, CCP-H4 |
| C. perfringens | Cooked meats, slow cooling | Rapid cooling, hot holding >63°C | CPG-5, CCP-H4 |
| C. botulinum | Low-acid canned/VP foods | pH control, thermal processing, refrigeration | CPG-4 |
| FMD virus | Livestock (Somaliland) | Veterinary inspection, quarantine, geographic sourcing | CCP-H1 |

### 4.2 Chemical Hazards

| Hazard | Source | Control Measures | CCP |
|--------|--------|-----------------|-----|
| Mycotoxins (aflatoxin, DON) | Grains, spices | Supplier COA, testing, specification | CCP-1, CPG-1 |
| Antibiotic residues | Dairy, meat | Veterinary cert, supplier audit, testing | CCP-H1, CCP-B2 |
| Allergens (undeclared) | Cross-contact, labeling | Allergen management plan, dedicated lines, label verification | CCP-B3, CPG-6, CPG-7 |
| Pesticide residues | Spices, vegetables | Supplier COA, country of origin control, testing | CPG-1 |
| Cleaning chemicals | Sanitation | SDS, training, rinse verification, storage control | PRP |
| Heavy metals (mineral cross-contamination) | Mineral extraction | Geographic separation, dedicated transport, testing | SPV-QA-001 |

### 4.3 Physical Hazards

| Hazard | Source | Control Measures | CCP |
|--------|--------|-----------------|-----|
| Metal fragments | Equipment wear, processing | Metal detection, X-ray, sieving, maintenance | CPG-2, CCP-H3 |
| Glass/plastic | Packaging, lighting | Shatterproof policy, glass register, inspection | PRP |
| Stones/soil | Raw materials (spices, grains) | Supplier control, sieving, sorting | CPG-1 |
| Bone fragments | Meat processing | Deboning SOP, visual inspection, X-ray | CCP-H3 |
| Personal effects | Human handling | Jewelry policy, uniform checks, metal detectors | PRP |

### 4.4 Allergen Management

| Allergen | Presence in Products | Control Status | Label Declaration |
|----------|---------------------|----------------|-------------------|
| Gluten (wheat) | Pizza dough, bread, pastries | Controlled | All units |
| Milk/dairy | Cheese, baked goods | Controlled | All units |
| Eggs | Baked goods, pasta | Controlled | All units |
| Soy | Sauces, marinades | Controlled | CPG only |
| Sesame | Baked goods, Middle Eastern items | Controlled | All units |
| Nuts | Selected bakery items | Controlled | Bakery + CPG |
| Shellfish | Selected sauces (fish sauce) | Controlled | CPG only |
| Sulphites | Dried fruits, wine | Controlled | CPG only |

---

## 5. Critical Control Points (CCPs) with Monitoring Procedures

### 5.1 CCP Monitoring Summary

| CCP ID | Location | Process Step | Critical Limit | Monitoring Method | Frequency | Responsibility | Record |
|--------|----------|-------------|---------------|-------------------|-----------|---------------|--------|
| CCP-1 | Pizza commissary | Receiving flour | COA + allergen decl | Document review | Per batch | Receiving clerk | Receiving log |
| CCP-2 | Pizza commissary | Receiving cheese | <4°C, COA, use-by | Temp check + doc review | Per batch | Receiving clerk | Receiving log |
| CCP-3 | Pizza commissary | Receiving toppings | <4°C, COA, allergen | Temp check + doc review | Per batch | Receiving clerk | Receiving log |
| CCP-4 | Pizza commissary | Proofing | <25°C for <4 hours | Temp + time recorder | Continuous | Baker | Proofing log |
| CCP-5 | Pizza commissary | Packaging | Seal integrity, correct label | Vision system + operator check | Every pack | Packaging operator | Packaging log |
| CCP-6 | Pizza commissary | Cold storage | <4°C | Digital temp recorder | Continuous | Cold store operator | Temp chart |
| CCP-7 | All units | Distribution | <4°C (refrigerated), <-18°C (frozen) | Digital temp logger | Continuous | Logistics | Delivery temp log |
| CCP-B1 | Bakery commissary | Receiving eggs | COA, Salmonella neg, <4°C | Doc review + temp | Per batch | Receiving clerk | Receiving log |
| CCP-B2 | Bakery commissary | Receiving dairy | COA, antibiotic neg, <4°C | Doc review + temp | Per batch | Receiving clerk | Receiving log |
| CCP-B3 | Bakery commissary | Decorating | Allergen segregation | Visual + swab testing | Per changeover | Baker + QA | Allergen log |
| CCP-B4 | Bakery commissary | Cooling | <21°C within 2 hours | Temp probe | Every batch | Baker | Cooling log |
| CCP-B5 | Bakery commissary | Labeling | Correct allergen declaration | Vision system | Every pack | Operator | Label verification |
| CPG-1 | CPG plants | Receiving | COA, spec compliance | Doc review | Per batch | QA inspector | Receiving log |
| CPG-2 | CPG plants | Metal detection | Fe>1.5mm, NFe>2.0mm, SS>2.5mm | Metal detector | Every 2 hours | Operator | Metal detector log |
| CPG-3 | CPG plants | Thermal processing | >85°C core for >2 min | Chart recorder | Continuous | Process operator | Process chart |
| CPG-4 | CPG plants | pH control | pH <4.6 | pH meter | Per batch | QA technician | pH log |
| CPG-5 | CPG plants | Blast freezing | <-18°C within 4 hours | Temp recorder | Continuous | Freezing operator | Freezing log |
| CPG-6 | CPG plants | Allergen control | No detectable allergen cross-contact | Swab ELISA + visual | Per changeover | QA technician | Allergen verification |
| CPG-7 | CPG plants | Label application | Match approved spec | Vision system | Every pack | Operator | Vision system log |
| CCP-H1 | Somaliland | Animal receiving | FMD-free cert, veterinary inspection, 24h quarantine | Vet inspection + doc review | Every batch | Veterinarian | Animal receiving log |
| CCP-H2 | Somaliland | Halal slaughter | Hand slaughter, tasmiya, no stunning | Religious supervisor + video | Every animal | Halal supervisor | Halal slaughter log |
| CCP-H3 | Somaliland | Evisceration | Zero visible fecal contamination, zero bone | Visual inspection + knife check | Every carcass | Line inspector | Evisceration log |
| CCP-H4 | Somaliland | Chilling | <7°C within 24h, <3°C within 48h | Temp recorder | Continuous | Chilling operator | Chilling chart |
| CCP-H5 | Somaliland | Packaging | Correct label, RFID tag, seal integrity | Visual + RFID scan | Every pack | Packer | Packaging log |
| CCP-H6 | Somaliland | Freezing | <-18°C within 24h of slaughter | Temp recorder | Continuous | Freezing operator | Freezing chart |

### 5.2 Corrective Actions Matrix

| CCP Deviation | Immediate Action | Root Cause Analysis | Preventive Action | Timeline |
|---------------|-----------------|--------------------|--------------------|----------|
| Temp exceed critical limit | Quarantine product, adjust equipment | Equipment failure, operator error, power | Repair, retrain, backup power | <24h |
| Metal detection reject | Stop line, isolate lot, investigate | Equipment wear, process error | Maintenance, SOP review | <4h |
| Allergen cross-contact detected | Hold product, re-clean, re-test | Changeover error, equipment design | Retrain, equipment modification | <8h |
| Halal procedure deviation | Stop line, segregate affected animals | Supervision lapse, training gap | Retrain, additional supervisor | Immediate |
| FMD suspicion | Quarantine, notify authorities, stop receiving | Sourcing breach, certificate fraud | Source investigation, vet audit | Immediate |
| pH out of spec | Reprocess or reject, adjust formulation | Ingredient error, measurement error | Retrain, formula lock | <4h |

---

## 6. Verification and Validation

### 6.1 Verification Schedule

| Activity | Frequency | Method | Responsible |
|----------|-----------|--------|-------------|
| CCP monitoring record review | Daily | QA review of all CCP logs | QA Technician |
| Calibration verification | Weekly | Reference standards against instruments | QA Technician |
| Internal audit | Monthly | Full GMP + HACCP audit | Internal Auditor |
| Supplier audit | Quarterly/Annual | On-site assessment | QA Manager |
| Third-party certification | Annual | FSSC 22000, BRC, Halal | Certification body |
| Regulatory inspection | As scheduled | SFDA, MOHAP, FSSAI, etc. | Regulatory Affairs |
| HACCP plan review | Annual | Full team review | HACCP Team |
| Validation of control measures | Annual | Challenge studies, scientific evidence | QA + Technical |

### 6.2 Validation Studies

| Study | Purpose | Method | Frequency |
|-------|---------|--------|-----------|
| Thermal process validation | Confirm lethality of cooking step | Heat penetration + microbiological | Annual, new product |
| Cold chain validation | Confirm temperature maintenance | Temperature mapping + data logger | Annual, new route |
| Shelf-life study | Confirm safe shelf life | Microbiological + sensory | New product, annual verification |
| Allergen cleaning validation | Confirm effective cleaning | ELISA + swab testing | New product, quarterly |
| Halal slaughter validation | Confirm religious compliance | Religious scholar review + video | Annual |
| Water activity validation | Confirm safety of ambient products | aW measurement + challenge | New product |

---

## 7. Traceability and Recall Procedures

### 7.1 Traceability System

| Level | Granularity | System | Response Time |
|-------|------------|--------|---------------|
| Tier 1: Ingredient to supplier | Batch/lot | ERP + AISTA blockchain | <30 minutes |
| Tier 2: Production to ingredient | Production run | ERP + MES | <2 hours |
| Tier 3: Finished goods to customer | Unit/pallet | ERP + WMS + POS | <4 hours |
| Tier 4: Customer to finished goods | Transaction | POS + CRM + loyalty | <1 hour |
| Tier 5: Livestock to herder | Individual animal | RFID + blockchain | <1 hour |
| Tier 6: Mineral batch to extraction point | Batch + GPS | SCADA + blockchain | <2 hours |

### 7.2 Recall Classification

| Class | Risk Level | Trigger | Timeline | Action |
|-------|-----------|---------|----------|--------|
| Class I | Life-threatening | Pathogen, undeclared allergen, toxin | <24h | Full recall, media notification, regulatory |
| Class II | Health hazard unlikely | Off-spec, labeling error (minor) | <72h | Trade recall, correction |
| Class III | Unlikely health hazard | Quality defect, minor labeling | <7 days | Customer notification, withdrawal |

### 7.3 Recall Procedure

```
Recall Activation Flow
======================
[Trigger Identified] → [Risk Assessment] → [Classify: I/II/III] → [Activate Recall Team]
       │                      │                      │                    │
       ▼                      ▼                      ▼                    ▼
[Notify Regulatory]    [Identify Scope]      [Draft Communication]  [Notify Customers]
       │                      │                      │                    │
       ▼                      ▼                      ▼                    ▼
[Product Retrieval]    [Traceability]        [Media (if Class I)]   [Monitor/Verify]
       │                      │                      │                    │
       ▼                      ▼                      ▼                    ▼
[Quarantine]          [Root Cause]           [Effectiveness Check]  [Close-Out Report]
```

| Role | Responsibility | Contact |
|------|---------------|---------|
| Recall Coordinator | Overall coordination, regulatory liaison | CQO |
| QA Lead | Technical assessment, root cause | QA Manager |
| Legal/Regulatory | Regulatory notification, legal exposure | General Counsel |
| Communications | Media, customer, franchisee communication | CMO |
| Operations | Product retrieval, logistics, destruction | COO |
| Finance | Insurance, financial tracking | CFO |
| IT | Traceability data, system support | CTO |

---

## 8. Halal Certification Management

### 8.1 Halal Certification Scope

| Entity | Certifying Body | Certificate Number | Valid Until | Scope |
|--------|----------------|-------------------|-------------|-------|
| Pizza Oven | SFDA Halal Center | HC-PO-2024-001 | 2026-03-15 | Pizza, dough, toppings |
| Bakery & Cafe | SFDA Halal Center | HC-BK-2024-001 | 2026-03-15 | Bread, pastries, cakes |
| CPG Jeddah | SFDA Halal Center | HC-CPG-2024-001 | 2026-03-15 | Sauces, dressings, frozen foods |
| CPG Dubai | ESMA Halal | HC-CPG-DXB-2024-001 | 2025-12-20 | Snacks, seasonings |
| Halal Meats SPV | GAC / Local Somaliland | HC-HM-2024-001 | 2025-09-10 | Slaughter, processing, export |
| India Co-man | Jamiat Ulama Halal | HC-IND-2024-001 | 2025-11-30 | Spice blends, pickles |

### 8.2 Slaughter Procedures (Somaliland SPV)

| Step | Requirement | Verification | Documentation |
|------|-------------|------------|---------------|
| Animal receiving | FMD-free, healthy, no visible disease | Vet inspection | Veterinary certificate |
| Resting | 24-hour minimum rest, water access | Visual, records | Resting log |
| Slaughter method | Hand slaughter (dhabh), sharp knife | Religious supervisor, CCTV | Slaughter video archive |
| Invocation | Tasmiya (Bismillah Allahu Akbar) | Religious supervisor | Supervisor sign-off |
| Stunning | NOT permitted for halal certification | Supervisor verification | Nil |
| Bleeding | Complete bleeding, severing carotid + jugular | Visual inspection | Inspector sign-off |
| Evisceration | No cross-contamination with digestive tract | Visual + procedure | Evisceration log |
| Chilling | Immediate chilling post-slaughter | Temp recording | Chilling chart |

### 8.3 Ingredient Verification

| Ingredient Category | Verification | Halal Status | Certificate |
|--------------------|-------------|------------|-------------|
| Meat | Source animal, slaughter method, cert | Must be halal-certified | Halal cert |
| Dairy | Animal source, rennet type | Must be halal or vegetarian | Halal cert / COA |
| Enzymes | Source, fermentation media | Must be halal or microbial | Halal cert |
| Additives | E-number, source | Must be halal | Halal cert |
| Flavorings | Carrier, alcohol content | Must be halal, <0.1% alcohol | Halal cert / COA |
| Colorings | Source, carrier | Must be halal | Halal cert |

### 8.4 Audit Schedule

| Audit Type | Frequency | Auditor | Scope |
|------------|-----------|---------|-------|
| Internal halal audit | Monthly | Internal Halal Officer | All halal-handling areas |
| Third-party halal audit | Annual | Certifying body | Full facility, documentation, procedures |
| Supplier halal verification | Annual | QA + certifying body | Supplier facilities, certificates |
| Unannounced audit | Bi-annual | Certifying body | Spot-check halal compliance |
| Religious scholar review | Annual | Board of Islamic scholars | Slaughter procedures, new products |

---

## 9. Customer Complaint Handling

### 9.1 Complaint Categories

| Category | Severity | Examples | Response Time |
|----------|----------|----------|---------------|
| Food safety | Critical | Illness, foreign object, allergen reaction | <2 hours |
| Quality | High | Off-taste, spoilage, incorrect product | <24 hours |
| Service | Medium | Long wait, incorrect order, rude staff | <48 hours |
| Packaging | Low | Damaged pack, missing item, labeling error | <72 hours |

### 9.2 Complaint Handling Process

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Receive complaint (phone, app, social, email) | Customer Service | Immediate |
| 2 | Log in CRM, assign severity | Customer Service | <15 min |
| 3 | Notify relevant team (QA, ops, legal if severe) | Customer Service | <30 min |
| 4 | Investigate, trace product, review records | QA Manager | <24h (critical) |
| 5 | Respond to customer, compensation if appropriate | Customer Service | <48h |
| 6 | Root cause analysis, corrective action | QA + Operations | <5 days |
| 7 | Trend analysis, management review | CQO | Monthly |

### 9.3 Y5 Complaint Targets

| Metric | Target | Actual |
|--------|--------|--------|
| Total complaints per 1M transactions | <50 | TBD |
| Food safety complaints | 0 | TBD |
| Complaint resolution time | <48h | TBD |
| Customer satisfaction (post-complaint) | >80% | TBD |
| Repeat complaint rate | <5% | TBD |

---

## 10. Quality Audits

### 10.1 Audit Program

| Audit Type | Frequency | Auditor | Scope | Reporting |
|------------|-----------|---------|-------|-----------|
| Internal GMP | Monthly | Internal QA | All facilities | QA Manager |
| Internal HACCP | Quarterly | Internal HACCP team | All CCPs, PRPs | CQO |
| Franchise operations | Monthly | RDO + QA | 20% of units rotating | COO |
| Mystery shopper | Monthly | Third-party | All units | COO |
| Third-party food safety | Annual | Certification body (FSSC/BRC) | All manufacturing | Board |
| Third-party halal | Annual | Halal certifier | All halal products | Board |
| Regulatory | As scheduled | SFDA, MOHAP, FSSAI, etc. | Per jurisdiction | Regulatory Affairs |
| Supplier | Annual/bi-annual | QA team | All A/B/C suppliers | QA Manager |
| ESG/sustainability | Annual | Third-party | Environmental, social | ESG Officer |

### 10.2 Audit Scoring

| Score | Rating | Action Required |
|-------|--------|----------------|
| 90-100 | Excellent | Maintain, share best practices |
| 80-89 | Good | Minor corrective actions, 30-day close |
| 70-79 | Satisfactory | Major corrective actions, 60-day close, re-audit |
| 60-69 | Unsatisfactory | Immediate action, stop operations if critical, 30-day re-audit |
| <60 | Critical | Immediate stop, senior management action, certification at risk |

---

## 11. Continuous Improvement

### 11.1 Six Sigma Program

| Project | Belt Level | Sponsor | Target | Timeline |
|---------|-----------|---------|--------|----------|
| Reduce dough waste (Pizza) | Green Belt | Commissary Manager | -20% waste | 6 months |
| Reduce pastry defect rate (Bakery) | Green Belt | Bakery Manager | -30% defects | 6 months |
| Reduce CPG line changeover time | Black Belt | Plant Manager | -40% changeover | 12 months |
| Reduce halal slaughter yield loss | Green Belt | SPV Operations | -10% yield loss | 6 months |
| Improve forecast accuracy | Black Belt | Supply Chain | MAPE <12% | 12 months |

### 11.2 Lean Manufacturing

| Lean Initiative | Application | Target | Method |
|----------------|-------------|--------|--------|
| 5S | All production facilities | Standardized work areas | Sort, Set, Shine, Standardize, Sustain |
| Value Stream Mapping | CPG production lines | Eliminate non-value-added steps | VSM workshops |
| Kaizen Events | Monthly across all facilities | Continuous small improvements | Kaizen blitz teams |
| TPM | All manufacturing equipment | >90% OEE | Autonomous + planned maintenance |
| Kanban | Inventory replenishment | Reduce stockouts by 25% | Pull-based replenishment |
| SMED | CPG line changeovers | <30 min changeover | Quick changeover techniques |

### 11.3 Y5 Quality KPIs

| KPI | Target | Measurement Frequency | Owner |
|-----|--------|----------------------|-------|
| Food safety incidents | 0 | Real-time | CQO |
| Product recall events | 0 | Annual | CQO |
| Customer complaint rate | <50 per 1M transactions | Monthly | QA Manager |
| Internal audit score | >85 average | Monthly | QA Manager |
| Third-party audit score | >90 | Annual | CQO |
| Supplier audit score | >80 average | Quarterly | QA Manager |
| HACCP deviation rate | <2% of CCP checks | Weekly | QA Technician |
| Training completion | 100% | Quarterly | QA Training |
| Halal certification maintenance | 100% | Annual | Halal Officer |
| Microbiological test pass rate | >99.5% | Weekly | Lab Manager |
| Allergen management incidents | 0 | Real-time | QA Manager |
| Cold chain compliance | >99.0% | Daily | Logistics Manager |

---

## 12. Appendices

### Appendix A: HACCP Team Members

| Name | Role | Responsibility | Training |
|------|------|---------------|----------|
| TBD | HACCP Team Leader | Overall plan, validation | Level 4 HACCP |
| TBD | QA Manager | CCP monitoring, verification | Level 3 HACCP |
| TBD | Production Manager | Operational controls | Level 2 HACCP |
| TBD | Engineering Manager | Equipment, calibration | Engineering |
| TBD | Procurement Manager | Supplier approval | Supplier quality |
| TBD | Microbiologist | Technical support, validation | Food science |
| TBD | Religious Supervisor | Halal compliance | Islamic scholarship |

### Appendix B: Regulatory Alignment Matrix

| Market | Regulator | Relevant Standard | Compliance Status |
|--------|-----------|-------------------|-------------------|
| Saudi Arabia | SFDA | Food Law, Halal Regulations, HACCP | Compliant |
| UAE | MOHAP | Food Safety Law, Halal Regulations | Compliant |
| Qatar | MOPH | Food Control Law, Halal Standards | Compliant |
| India | FSSAI | FSS Act 2006, FSSR 2011 | Compliant |
| Egypt | EOS / NFA | Food Safety Standards | Compliant |
| Kenya | KEBS / KRA | Food Safety Standards | Compliant |
| Somaliland | Ministry of Livestock | Local veterinary + halal | Compliant |
| International | Codex Alimentarius | CODEX HACCP Guidelines | Aligned |

---

*End of Document*
*SSTP-OPS-002 v1.0 | Quality Assurance and HACCP Framework*
*Classification: Restricted | © 2025 SSTP Corleone Ecosystem*
