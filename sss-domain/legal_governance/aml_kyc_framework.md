---
artifact_id: SSTP-OPS-005
type: operations_document
title: Anti-Money Laundering and Know-Your-Customer Framework
status: draft
pillar: A - SSS Firm Advisory
  - B - AISTA Corridor Infrastructure
  - C - Corleone Enterprise
tags:
  - AML
  - KYC
  - compliance
  - FATF
  - sanctions
  - PEP
  - transaction monitoring
  - suspicious activity
governance:
  owner: Chief Compliance Officer
  approver: Board Risk Committee
  review_cycle: annual
  next_review: 2026-01-15
  document_control: controlled
created_date: 2025-04-01
version: 1.0
---

# Anti-Money Laundering and Know-Your-Customer Framework

## Document Control

| Field | Value |
|-------|-------|
| Document ID | SSTP-OPS-005 |
| Version | 1.0 |
| Author | Compliance Office |
| Owner | Chief Compliance Officer (CCO) |
| Approved By | Board Risk Committee |
| Classification | Confidential |
| Review Cycle | Annual |
| Next Review Date | 2026-01-15 |

---

## 1. Executive Summary

This document establishes the Anti-Money Laundering (AML) and Know-Your-Customer (KYC) framework for the Sovereign SafeTrade Program (SSTP) Corleone ecosystem. It applies to all legal entities, subsidiaries, franchisees, joint venture partners, and counterparties across all jurisdictions. The framework ensures compliance with applicable laws including the USA PATRIOT Act, FinCEN regulations, EU AML Directives (4AMLD/5AMLD/6AMLD), UAE Central Bank regulations, Saudi SAMA AML rules, India Prevention of Money Laundering Act (PMLA), and FATF Recommendations. The framework covers customer onboarding, ongoing monitoring, suspicious activity reporting, record keeping, and training.

---

## 2. Applicable Laws and Regulations

| Jurisdiction | Authority | Key Regulation | Scope | Applicability |
|-------------|-----------|---------------|-------|---------------|
| United States | FinCEN / OFAC | USA PATRIOT Act; BSA; 31 CFR 1010 | US persons, USD transactions, US banking | AISTA corridor if USD nexus; US investors |
| European Union | ECB / national regulators | 4AMLD, 5AMLD, 6AMLD; EU Sanctions | EU persons, EUR transactions, EU banking | EU franchisees; EU investors; EUR trade |
| UAE | Central Bank of UAE | AML/CFT Regulations 2019; Cabinet Decision 10/2019 | UAE entities, AED transactions | Corleone UAE entities; franchisees; AISTA |
| Saudi Arabia | SAMA | SAMA AML Rules; Royal Decree M/20 | SAR transactions, Saudi entities | Corleone KSA entities; franchisees; AISTA |
| Qatar | QCB | QCB AML/CFT Regulations | QAR transactions, Qatar entities | Qatar franchisees |
| India | RBI / ED | PMLA 2002; RBI KYC Master Direction | INR transactions, Indian entities | India operations; franchisees; co-manufacturer |
| Egypt | CBE | CBE AML/CFT Guidelines | EGP transactions, Egyptian entities | Egypt franchisees |
| Kenya | CBK | CBK AML Regulations | KES transactions, Kenyan entities | Kenya franchisees |
| Somaliland | Central Bank of Somaliland | Local AML guidelines | Local transactions | SPV operations; herder payments |
| International | FATF | FATF 40 Recommendations | Global standard | All entities |
| UN | UN Security Council | UN Sanctions Resolutions | Global | All entities |

---

## 3. Risk-Based Approach

### 3.1 Risk Classification Methodology

```
Risk Score = (Customer Risk + Geography Risk + Product Risk + Transaction Risk) / 4

Score Range:
  1.0 - 2.0 = LOW RISK     (Simplified due diligence)
  2.1 - 3.5 = MEDIUM RISK  (Standard due diligence)
  3.6 - 5.0 = HIGH RISK    (Enhanced due diligence)
```

### 3.2 Customer Risk Rating

| Factor | Weight | Low (1) | Medium (2) | High (3) | Very High (4) |
|--------|--------|---------|------------|----------|---------------|
| Entity type | 20% | Listed company | Private company, NGO | Trust, partnership | Shell company, bearer shares |
| Ownership transparency | 20% | >25% UBO known | 10-25% UBO known | <10% UBO known | No UBO identifiable |
| Business purpose clarity | 15% | Clear, documented | Understandable but complex | Complex structure | Unclear / no business purpose |
| Source of funds | 15% | Documented, legitimate | Partially documented | Unclear origin | Suspicious origin |
| Expected activity | 15% | Predictable, low value | Moderate, some variation | High value, complex | Unpredictable, high risk |
| PEP / sanctions exposure | 15% | None | Minor (local PEP) | Senior PEP | Sanctioned / close associate |

### 3.3 Geography Risk Rating

| Risk Level | Jurisdictions | Corresponding Measures |
|------------|--------------|-------------------------|
| Very Low | EU, UK, US, Canada, Australia, Japan, Singapore | Simplified CDD allowed for low-risk |
| Low | GCC (Saudi, UAE, Qatar, Bahrain, Kuwait, Oman), Malaysia, South Korea | Standard CDD |
| Medium | India, Egypt, Kenya, Turkey, Mexico, South Africa | Standard CDD, enhanced monitoring |
| High | Pakistan, Bangladesh, Nigeria, Philippines, Indonesia | Enhanced due diligence |
| Very High | Iran, DPRK, Syria, Myanmar, Afghanistan, Somalia (non-Somaliland), FATF grey list | Prohibited or enhanced EDD with MLRO approval; Somaliland treated as medium with enhanced monitoring |

### 3.4 Product Risk Rating

| Product / Service | Risk Level | Rationale | Mitigation |
|-------------------|------------|-----------|------------|
| Franchise license sale | Medium | Cash-intensive, multiple locations | Source of funds verification, ongoing monitoring |
| Franchise royalty payments | Low | Recurring, predictable | Standard monitoring |
| CPG wholesale sales | Medium | B2B, cross-border, cash possible | Customer CDD, transaction monitoring |
| CPG e-commerce | Low-Medium | Card payments, consumer | Standard CDD, chargeback monitoring |
| AISTA trade settlement | High | Cross-border, multiple jurisdictions, correspondent banking | Full EDD, blockchain monitoring, trade doc verification |
| Somaliland livestock purchase | High | Cash payments to herders, limited formal banking | Enhanced controls, herder registration, biometric KYC |
| Somaliland mineral offtake | High | Cross-border, extractive sector, limited transparency | Full EDD, assay verification, chain-of-custody |
| Media licensing | Low | Intellectual property, contractual | Standard CDD |
| Employee payroll | Very Low | Salary, documented | Minimal |
| Supplier payments | Low-Medium | B2B, invoice-based | Standard CDD for new suppliers |

### 3.5 Transaction Risk Rating

| Indicator | Low Risk | Medium Risk | High Risk |
|-----------|----------|-------------|-----------|
| Transaction size | <$10K/month | $10K-$100K/month | >$100K/month |
| Frequency | Predictable, regular | Some variation | Unpredictable, spiking |
| Counterparty | Known, verified | New, verified | Unknown, high-risk |
| Purpose | Documented, logical | Generally logical | Unexplained, unusual |
| Payment method | Bank transfer, card | Mixed | Cash, crypto, informal |
| Geography | Domestic or low-risk | Medium-risk | High-risk or sanctions-adjacent |
| Structuring | None | Suspected | Confirmed |
| Velocity | Consistent with profile | Slightly elevated | Far exceeds profile |

---

## 4. Customer Due Diligence (CDD)

### 4.1 CDD Procedures

| Step | Action | Documentation | Responsible | Timeline |
|------|--------|--------------|-------------|----------|
| 1 | Identify customer | Name, legal form, registration, address | Onboarding officer | Day 0 |
| 2 | Verify identity | Government-issued ID, corporate registry, certificate of incorporation | Onboarding officer | Day 0-1 |
| 3 | Verify address | Utility bill, bank statement, lease, or site visit | Onboarding officer | Day 0-3 |
| 4 | Identify beneficial owners | >25% ownership or control; senior managing official if no UBO | Onboarding officer | Day 0-3 |
| 5 | Verify beneficial owners | ID, PEP/sanctions screening, source of wealth | Onboarding officer | Day 0-3 |
| 6 | Understand purpose | Business description, expected transactions, source of funds | Relationship manager | Day 0-3 |
| 7 | Risk assessment | Apply risk scoring model, assign risk rating | Compliance officer | Day 1-3 |
| 8 | Approval | Low/Medium: automated; High: MLRO approval | MLRO | Day 3-5 |
| 9 | Account opening | System setup, monitoring parameters, limits | Operations | Day 3-5 |
| 10 | Ongoing monitoring | Transaction monitoring, periodic review, trigger events | Compliance | Continuous |

### 4.2 Identification and Verification Requirements

| Entity Type | Identification Documents | Verification Method | Re-verification |
|-------------|--------------------------|-------------------|---------------|
| Individual | Passport / national ID; proof of address | Document verification (Onfido/Jumio); biometric selfie | Every 3 years (medium), annually (high) |
| Sole proprietor | Business license; personal ID; tax ID | Registry check; site visit if high-risk | Annually |
| Private company | Certificate of incorporation; MOA/AOA; registry extract; tax ID | Registry check; legal opinion if complex | Every 2 years |
| Public company | Stock exchange listing; annual report; registry extract | Exchange verification; public filings | Every 3 years |
| Partnership | Partnership agreement; partner IDs; registry extract | Registry check; partner verification | Every 2 years |
| Trust | Trust deed; settlor/beneficiary IDs; trustee appointment | Legal review; beneficiary verification | Every 2 years |
| Foundation | Charter; founder ID; council member IDs | Registry check; purpose verification | Every 2 years |
| Franchisee (individual) | Personal ID; business license; lease; franchise agreement | ID verification + site visit | Annually |
| Franchisee (corporate) | Full corporate CDD + franchise agreement + financial statements | Full corporate verification + site visit | Annually |
| Somaliland herder | Biometric registration; clan/guarantor reference; livestock ownership proof | Biometric + community verification | Per season |
| Somaliland mineral buyer | Full corporate CDD + mining license + export permit + assay records | Full verification + site visit + third-party reference | Every 6 months |

### 4.3 Beneficial Ownership Verification

| Ownership Threshold | Identification Required | Verification | Exception |
|---------------------|--------------------------|-------------|-----------|
| >25% direct | Full CDD on individual | ID, PEP, sanctions, source of wealth | None |
| >25% indirect (through entity) | Full CDD on intermediate entity + ultimate individual | Full chain verification | None |
| Senior managing official | Full CDD if no UBO identified | ID, PEP, sanctions | Document rationale |
| Nominee arrangements | Full CDD on nominee + nominator + economic owner | Legal opinion + declaration | Prohibited if concealing |
| Politically exposed person (PEP) | Enhanced CDD; senior management approval | Source of wealth, source of funds, ongoing monitoring | Required for all PEPs |

### 4.4 PEP Screening

| PEP Category | Definition | Screening Source | Action Required |
|--------------|------------|-----------------|-----------------|
| Head of state / government | President, prime minister, monarch | Dowson, World-Check, internal | EDD + senior management approval |
| Senior politician | Minister, deputy minister, MP, mayor of major city | Dowson, World-Check | EDD + senior management approval |
| Senior military / judicial | Chief of defense, supreme court judge | Dowson, World-Check | EDD + senior management approval |
| Senior executive (SOE) | CEO, board member of state-owned enterprise | Dowson, Orbis, internal | EDD + senior management approval |
| International organization | Senior leader of UN, World Bank, IMF, etc. | Dowson, internal | EDD + senior management approval |
| Family member (close) | Spouse, partner, children, parents, siblings | Dowson, World-Check | EDD + senior management approval |
| Close associate | Known close business associate, advisor | Dowson, media, internal | EDD + senior management approval |
| Domestic PEP | Same categories but sub-national | Dowson, local lists | EDD required; management approval if high-risk |
| International PEP | Same categories, foreign | Dowson, World-Check, sanctions | EDD + senior management approval |

### 4.5 Sanctions Screening

| Sanctions List | Source | Screening Frequency | System |
|---------------|--------|---------------------|--------|
| OFAC SDN | US Treasury | Real-time | Dowson, internal |
| OFAC Consolidated | US Treasury | Real-time | Dowson, internal |
| EU Consolidated | EU | Real-time | Dowson, internal |
| UN Security Council | UN | Real-time | Dowson, internal |
| UK HMT | UK Treasury | Real-time | Dowson, internal |
| HMT Consolidated | UK | Real-time | Dowson, internal |
| Saudi SAMA sanctions | SAMA | Real-time | Internal + local |
| UAE Central Bank | CBUAE | Real-time | Internal + local |
| India UN Act | MHA | Real-time | Internal + local |
| FATF Public Statements | FATF | Monthly | Manual review |
| Local sanctions (Somaliland) | CBSL | Real-time | Internal |
| Internal watchlist | Internal | Real-time | Internal |

---

## 5. Enhanced Due Diligence (EDD)

### 5.1 EDD Triggers

| Trigger | Description | EDD Level | Approval |
|---------|-------------|-----------|----------|
| High-risk geography | Customer from FATF grey list or high-risk jurisdiction | Full EDD | MLRO |
| PEP identified | Any politically exposed person or associate | Full EDD | MLRO + senior management |
| Complex ownership | Layered structures, trusts, nominees, bearer shares | Full EDD | MLRO |
| Unusual activity | Transactions inconsistent with profile | Event-driven EDD | MLRO |
| Negative media | Adverse media suggesting criminal activity | Event-driven EDD | MLRO |
| Sanctions match | Close match or related party to sanctioned entity | Full EDD + legal | MLRO + General Counsel |
| Cash-intensive business | High cash turnover, limited banking history | Full EDD | MLRO |
| Somaliland operations | Herder, small trader, informal sector | Context-specific EDD | MLRO + SPV GM |
| Mineral sector | Extractive industry, cross-border trade | Full EDD + third-party reference | MLRO + senior management |
| Correspondent banking | Banking relationship with foreign bank | Full EDD | MLRO |
| Franchisee >5 units | Large franchisee with significant capital | Full EDD | MLRO |
| FIV member | Franchisee Investment Vehicle member | Full EDD + financial verification | MLRO |

### 5.2 EDD Procedures

| Element | Standard CDD | Enhanced EDD |
|---------|-------------|-------------|
| Identity verification | Standard documents | Additional documents; notarized; apostilled if foreign |
| Source of funds | Self-declaration | Documented evidence: tax returns, bank statements, sale contracts, audited accounts |
| Source of wealth | Self-declaration | Documented evidence: employment history, business ownership, inheritance, investment |
| PEP screening | Real-time + periodic | Real-time + daily; enhanced monitoring; close associate screening |
| Sanctions screening | Real-time + periodic | Real-time + daily; fuzzy matching; related party screening |
| Adverse media | Periodic | Daily; local language; social media; litigation databases |
| Site visit | Not required | Required for high-risk; unannounced if concerns |
| Third-party reference | Not required | Bank reference, professional reference, public records |
| Ongoing monitoring | Standard thresholds | Reduced thresholds; enhanced reporting; monthly review |
| Re-verification | 2-3 years | Annually or event-driven |
| Approval | Automated or compliance officer | MLRO + senior management |
| Record keeping | 5 years | 10 years |

---

## 6. Ongoing Monitoring

### 6.1 Transaction Monitoring

| Risk Level | Monitoring Frequency | Threshold | Review | Escalation |
|------------|---------------------|-----------|--------|------------|
| Low | Monthly | 2x expected volume | Automated | Quarterly |
| Medium | Weekly | 1.5x expected volume | Semi-automated | Monthly |
| High | Daily | Any unusual pattern | Manual review | Immediate |
| Very High | Real-time | Any transaction | Pre-approval required | Immediate |

### 6.2 Suspicious Activity Indicators

| Category | Indicator | Risk Level | Action |
|----------|-----------|------------|--------|
| Structuring | Multiple transactions just below reporting threshold | High | Investigate, potential SAR |
| Velocity | Sudden increase in transaction volume/frequency | Medium-High | Review, enhanced monitoring |
| Counterparty | Transactions with sanctioned or high-risk jurisdictions | Very High | Block, investigate, SAR |
| Purpose | Transactions with no apparent business purpose | High | Investigate, potential SAR |
| Round-tripping | Funds transferred out and back with no purpose | High | Investigate, SAR |
| Layering | Complex series of transfers obscuring origin | High | Investigate, SAR |
| Cash intensity | Unusual cash deposits/withdrawals | Medium-High | Investigate, source verification |
| Geographic | Transactions to/from unexpected jurisdictions | Medium-High | Enhanced monitoring |
| PEP | Transactions involving PEP without clear purpose | High | EDD, senior review, potential SAR |
| Negative media | Customer mentioned in corruption/fraud investigation | High | Review, enhanced monitoring, potential SAR |
| Franchisee | Unusual royalty payments (too high or too low) | Medium | Investigate, potential fraud |
| AISTA trade | Trade documents inconsistent with payment | High | Investigate, documentary check, potential SAR |
| Somaliland | Herder payments inconsistent with livestock count | Medium | Verify, biometric check, potential SAR |
| Mineral offtake | Assay values inconsistent with payment | High | Third-party verification, SAR if confirmed |

### 6.3 Threshold Setting

| Transaction Type | Low Risk Threshold | Medium Risk Threshold | High Risk Threshold | Action |
|----------------|-------------------|----------------------|--------------------|--------|
| Cash deposit | >$5,000 | >$10,000 | >$25,000 | Review / SAR |
| Wire transfer (out) | >$25,000 | >$50,000 | >$100,000 | Review / SAR |
| Wire transfer (in) | >$50,000 | >$100,000 | >$250,000 | Review / SAR |
| Currency exchange | >$10,000 | >$25,000 | >$50,000 | Review / SAR |
| Trade payment (AISTA) | >$100,000 | >$250,000 | >$500,000 | Enhanced doc check |
| Franchisee payment | >$5,000/month | >$10,000/month | >$25,000/month | Review |
| Royalty (to franchisee) | >$5,000/month | >$10,000/month | >$25,000/month | Review |
| Herder payment (Somaliland) | >$2,000/season | >$5,000/season | >$10,000/season | Biometric + verification |
| Mineral offtake payment | >$50,000 | >$100,000 | >$250,000 | Third-party verification |

---

## 7. Suspicious Activity Reporting (SAR)

### 7.1 SAR Decision Matrix

| Finding | Confidence | Action | Timeline | Escalation |
|---------|------------|--------|----------|------------|
| Confirmed suspicious activity | High | File SAR immediately; freeze if required | <24h | MLRO + General Counsel |
| Probable suspicious activity | Medium | Further investigation; preliminary SAR | <48h | MLRO |
| Possible suspicious activity | Low | Enhanced monitoring; document rationale | <5 days | Compliance officer |
| Unusual but not suspicious | N/A | Document; no SAR; continue monitoring | Ongoing | File note |

### 7.2 SAR Filing Procedure

| Step | Action | Responsible | Timeline | Documentation |
|------|--------|-------------|----------|---------------|
| 1 | Detect / receive alert | Transaction monitoring system / staff | Real-time | System alert |
| 2 | Initial assessment | Compliance officer | <4 hours | Investigation memo |
| 3 | Detailed investigation | Compliance officer + MLRO | <24 hours | Full investigation file |
| 4 | SAR determination | MLRO | <48 hours | SAR or no-SAR decision |
| 5 | SAR preparation | Compliance officer | <24 hours | SAR form (see Appendix C) |
| 6 | Legal review | General Counsel | <12 hours | Privilege review |
| 7 | SAR filing | MLRO | <72 hours from detection | Filed with FIU |
| 8 | Internal notification | MLRO | <24 hours after filing | CEO, CRO, Board Risk Committee |
| 9 | Customer handling | Relationship manager | Ongoing | No tipping off; maintain normal relationship |
| 10 | Record keeping | Compliance | 10 years | Investigation file, SAR copy, outcome |

### 7.3 Tipping Off Prohibition

| Action | Permitted | Prohibited |
|--------|-----------|------------|
| Inform customer of SAR filing | NEVER | Informing customer or anyone else that SAR filed |
| Continue normal business | Yes | Must not alert customer to investigation |
| Decline transaction | Yes, with plausible business reason | Declining because of SAR/suspicion |
| Close account | Yes, with business reason unrelated to suspicion | Closing because of SAR |
| Record keeping | Yes, internal documentation | Leaving records accessible to customer |
| Staff communication | Yes, need-to-know only | Discussing SAR in open office, email, messaging |
| Board reporting | Yes, at appropriate level | Naming customer in unencrypted communication |
| External legal advice | Yes, under privilege | Discussing with non-privileged advisors |

---

## 8. Record Keeping

### 8.1 Record Retention Requirements

| Record Category | Retention Period | Format | Location | Access Control |
|-----------------|-----------------|--------|----------|----------------|
| CDD files | 10 years from relationship end | Digital + physical | Document management system | Restricted |
| Transaction records | 10 years from transaction | Digital | ERP + data warehouse | Restricted |
| SARs and investigations | 10 years from filing | Digital | Secure compliance system | Confidential |
| Risk assessments | 10 years from creation | Digital | Compliance system | Restricted |
| Training records | Duration of employment + 10 years | Digital | LMS | Internal |
| PEP screening results | 10 years from screening | Digital | Screening system | Restricted |
| Sanctions screening results | 10 years from screening | Digital | Screening system | Restricted |
| Correspondence with regulators | 15 years | Digital + physical | Legal system | Confidential |
| AISTA trade records | 10 years from trade | Blockchain + digital | Corda + document system | Restricted |
| Franchisee KYC | 10 years from franchise end | Digital + physical | Document system | Restricted |
| Somaliland herder records | 10 years from registration | Digital + biometric | Custom system | Restricted |
| Mineral offtake records | 10 years from transaction | Digital + physical | SPV system + document system | Restricted |
| FIV member records | 10 years from membership end | Digital | Legal + compliance system | Confidential |

---

## 9. Compliance Program and Training

### 9.1 Training Program

| Audience | Course | Frequency | Duration | Delivery | Assessment |
|----------|--------|-----------|----------|--------|------------|
| All employees | AML awareness | Annual | 30 min | E-learning | Quiz (80% pass) |
| Customer-facing staff | CDD basics | Annual | 1 hour | E-learning + workshop | Quiz + case study |
| Compliance team | AML technical | Quarterly | 4 hours | In-person + external | Exam + case studies |
| MLRO | Advanced AML + leadership | Quarterly | 8 hours | External + conference | Certification |
| Senior management | AML governance | Annual | 2 hours | Board presentation | Discussion |
| Board | AML oversight | Annual | 1 hour | Briefing | Discussion |
| Franchisees | AML basics | Onboarding + biennial | 1 hour | E-learning | Quiz |
| SPV staff | Somaliland-specific AML | Quarterly | 2 hours | In-person | Case study |
| AISTA trade desk | Trade-based AML | Quarterly | 4 hours | In-person + external | Case study |
| New hires | AML induction | Within 30 days | 1 hour | E-learning | Quiz |
| Post-incident | Targeted refresher | Event-driven | 1-2 hours | In-person | Case study |

### 9.2 Compliance Program Governance

| Element | Description | Frequency | Owner |
|---------|-------------|-----------|-------|
| Risk assessment | Enterprise-wide AML risk assessment | Annual | MLRO |
| Policies & procedures | Framework update, new regulation integration | Annual | CCO |
| Independent audit | External audit of AML program | Annual | Internal Audit |
| Regulatory reporting | FIU returns, regulatory returns | Quarterly | MLRO |
| Management information | AML MI dashboard for Board | Quarterly | MLRO |
| Quality assurance | Sampling and testing of CDD files | Quarterly | QA Compliance |
| System tuning | Transaction monitoring rule tuning | Quarterly | MLRO + vendor |
| Look-back reviews | Historical review triggered by new intelligence | Event-driven | MLRO |
| Compliance culture | Tone from the top, whistleblower program | Ongoing | CEO + CCO |

---

## 10. Franchisee KYC

### 10.1 Franchisee Risk Assessment

| Factor | Low Risk | Medium Risk | High Risk |
|--------|----------|-------------|-----------|
| Number of units | 1-2 | 3-5 | 6+ |
| Geography | Low-risk market | Medium-risk market | High-risk market |
| Ownership structure | Individual, transparent | Corporate, some complexity | Complex, opaque, trust |
| Source of funds | Documented, legitimate | Partially documented | Unclear, cash-intensive |
| PEP/sanctions | None | Minor | Confirmed or close associate |
| Business history | Established, verifiable | New but documented | No verifiable history |
| Payment method | Bank transfer | Mixed | Cash, informal |

### 10.2 Franchisee KYC Process

| Step | Action | Documentation | Responsible | Timeline |
|------|--------|--------------|-------------|----------|
| 1 | Application | Franchisee KYC form (Appendix A), business plan, financial statements | Franchise development | Day 0 |
| 2 | Initial screening | PEP, sanctions, adverse media | Compliance | Day 1-2 |
| 3 | Identity verification | ID, corporate registry, UBO declaration | Compliance | Day 2-3 |
| 4 | Source of funds | Bank statements, tax returns, sale documentation | Compliance | Day 3-5 |
| 5 | Site visit | Unannounced or scheduled visit to existing business | Franchise development | Day 5-10 |
| 6 | Financial verification | Accountant reference, credit check, bank reference | Finance | Day 5-10 |
| 7 | Risk rating | Apply franchisee risk model | Compliance | Day 10 |
| 8 | Approval | Low: automated; Medium: compliance; High: MLRO | Varies | Day 10-15 |
| 9 | Ongoing monitoring | Quarterly review, annual re-KYC, event-driven | Compliance | Ongoing |
| 10 | Exit KYC | Final review, record retention | Compliance | Post-exit |

---

## 11. Somaliland Partner KYC

### 11.1 Herder KYC

| Step | Action | Documentation | Technology | Responsible |
|------|--------|--------------|------------|-------------|
| 1 | Registration | Herder KYC form (simplified), clan affiliation, livestock ownership | Biometric app | SPV field officer |
| 2 | Biometric capture | Fingerprint + photo (ISO template) | Android biometric scanner | SPV field officer |
| 3 | GPS registration | Home location, grazing areas, water points | GPS + GIS mapping | SPV field officer |
| 4 | Community verification | Clan elder / cooperative reference | Paper reference + phone verification | SPV field officer |
| 5 | Livestock tagging | RFID ear tag assignment, linking to herder | RFID scanner | SPV field officer |
| 6 | Risk assessment | Low (cooperative member) / Medium (independent) / High (new, no reference) | Custom app | SPV field officer |
| 7 | Blockchain registration | Herder identity hash on AISTA Corda | Corda node | AISTA trade desk |
| 8 | Ongoing verification | Seasonal re-registration, livestock count verification | Biometric + RFID | SPV field officer |
| 9 | Payment linkage | Biometric verification for payment collection | Biometric POS | SPV finance |
| 10 | Record retention | Digital + blockchain, 10 years | Custom system + Corda | Compliance |

### 11.2 Mineral Buyer / Offtaker KYC

| Step | Action | Documentation | Verification | Responsible |
|------|--------|--------------|-------------|-------------|
| 1 | Corporate KYC | Full corporate CDD (see Section 4) | Full verification | Compliance |
| 2 | Mining license verification | Copy of license, validity check, regulatory confirmation | Government registry + legal | SPV GM + Legal |
| 3 | Export permit verification | Copy of permit, destination confirmation | Government registry | SPV GM |
| 4 | Assay verification | Independent lab assay, chain of custody | Third-party lab | CQO |
| 5 | Site visit | Mine site visit, processing facility inspection | Unannounced + scheduled | SPV GM + Compliance |
| 6 | Financial verification | Bank reference, credit check, trade reference | Bank + trade reference | Finance |
| 7 | EDD if high-risk | Source of wealth, beneficial owners, PEP screening | Full EDD | MLRO |
| 8 | Contract review | Offtake agreement, payment terms, delivery schedule | Legal review | General Counsel |
| 9 | Ongoing monitoring | Quarterly review, assay trend analysis, payment reconciliation | Custom dashboard | Compliance + SPV GM |
| 10 | Exit | Contract termination, final reconciliation, record retention | Standard | Compliance |

---

## 12. Appendices

### Appendix A: KYC Form Template (Individual / Franchisee)

```
═══════════════════════════════════════════════════════════════════
           SSTP CORLEONE KYC FORM — INDIVIDUAL / FRANCHISEE
═══════════════════════════════════════════════════════════════════

Form ID: KYC-[ENTITY]-[DATE]-[SEQUENCE]
Version: 1.0
Classification: Confidential

SECTION 1: PERSONAL INFORMATION
─────────────────────────────────────────────────────────────────
Full Legal Name: ________________________________________________
Date of Birth: ____/____/________    Place of Birth: ____________
Nationality: ____________________    Second Nationality: ________
Gender: [ ] Male  [ ] Female  [ ] Other
Marital Status: [ ] Single  [ ] Married  [ ] Divorced  [ ] Widowed

SECTION 2: CONTACT INFORMATION
─────────────────────────────────────────────────────────────────
Residential Address: ____________________________________________
________________________________________________________________
City: _______________________  Country: _________________________
Postal Code: ________________  Telephone: _______________________
Mobile: _____________________  Email: ____________________________

SECTION 3: IDENTIFICATION
─────────────────────────────────────────────────────────────────
ID Type: [ ] Passport  [ ] National ID  [ ] Driver's License  [ ] Other
ID Number: _______________________  Issuing Country: _______________
Issue Date: ____/____/________    Expiry Date: ____/____/________
ID Copy Attached: [ ] Yes  [ ] No

SECTION 4: OCCUPATION & INCOME
─────────────────────────────────────────────────────────────────
Occupation: _______________________  Employer: ____________________
Employer Address: ________________________________________________
Annual Income (USD): ________________  Source of Income: ____________
[ ] Salary  [ ] Business  [ ] Investment  [ ] Inheritance  [ ] Other: ____

SECTION 5: PEP / SANCTIONS DECLARATION
─────────────────────────────────────────────────────────────────
Are you or any immediate family member a politically exposed person?
[ ] Yes  [ ] No
If yes, provide details: __________________________________________

Are you or any related party subject to sanctions?
[ ] Yes  [ ] No
If yes, provide details: __________________________________________

SECTION 6: FRANCHISEE INFORMATION (if applicable)
─────────────────────────────────────────────────────────────────
Proposed Units: _______    Market: ______________________________
Source of Franchise Capital: ______________________________________
Estimated Initial Investment: _______________ USD
Bank Reference: _______________________  Account Number: __________

SECTION 7: DECLARATION
─────────────────────────────────────────────────────────────────
I declare that all information provided is true and complete.
I consent to background checks, PEP/sanctions screening, and credit checks.
I understand that false information may result in rejection or termination.

Signature: _______________________  Date: ____/____/________

SECTION 8: INTERNAL USE
─────────────────────────────────────────────────────────────────
Risk Score: _____    Risk Rating: [ ] Low  [ ] Medium  [ ] High
Screening Results: PEP [ ] Clear [ ] Match    Sanctions [ ] Clear [ ] Match
Adverse Media [ ] Clear [ ] Match    Credit Check [ ] Clear [ ] Concern
Approved By: _______________________  Date: ____/____/________
═══════════════════════════════════════════════════════════════════
```

### Appendix B: Risk Assessment Matrix

| Risk Factor | Weight | Score | Weighted Score |
|-------------|--------|-------|---------------|
| Customer type | 20% | 1-4 | _____ |
| Ownership transparency | 20% | 1-4 | _____ |
| Geography | 15% | 1-4 | _____ |
| Product/service | 15% | 1-4 | _____ |
| Transaction profile | 15% | 1-4 | _____ |
| PEP/sanctions | 15% | 1-4 | _____ |
| **Total** | **100%** | | **_____** |

| Total Score | Risk Rating | Due Diligence Level | Approval |
|-------------|-------------|---------------------|----------|
| 1.0 - 2.0 | Low | Simplified | Automated |
| 2.1 - 3.5 | Medium | Standard | Compliance Officer |
| 3.6 - 5.0 | High | Enhanced | MLRO |
| >5.0 or sanctions match | Prohibited | Decline | MLRO + General Counsel |

### Appendix C: Suspicious Activity Report (SAR) Template

```
═══════════════════════════════════════════════════════════════════
         SUSPICIOUS ACTIVITY REPORT (SAR) — INTERNAL TEMPLATE
═══════════════════════════════════════════════════════════════════

SAR ID: SAR-[YYYY]-[SEQUENCE]
Filing Date: ____/____/________
Filing Jurisdiction: _____________________________________________
FIU Reference (if filed): ________________________________________

SECTION 1: SUBJECT INFORMATION
─────────────────────────────────────────────────────────────────
Subject Name: ____________________________________________________
Subject Type: [ ] Individual  [ ] Corporate  [ ] Other: _________
Account/Relationship ID: __________________________________________
Risk Rating: [ ] Low  [ ] Medium  [ ] High  [ ] Very High
Relationship Start Date: ____/____/________

SECTION 2: SUSPICIOUS ACTIVITY DESCRIPTION
─────────────────────────────────────────────────────────────────
Date(s) of Activity: ____/____/________ to ____/____/________
Activity Type: [ ] Structuring  [ ] Layering  [ ] Terrorist financing
              [ ] Tax evasion  [ ] Fraud  [ ] Sanctions evasion
              [ ] Corruption  [ ] Other: _______________________

Detailed Description:
________________________________________________________________
________________________________________________________________
________________________________________________________________

Amount Involved (USD): _________________  Currency: ______________
Number of Transactions: _________________  Transaction IDs: ______
________________________________________________________________

SECTION 3: WHY SUSPICIOUS
─────────────────────────────────────────────────────────────────
[ ] No apparent economic purpose
[ ] Inconsistent with known business/profile
[ ] Involves high-risk jurisdiction
[ ] Involves PEP or sanctioned party
[ ] Complex structure with no clear purpose
[ ] Unusual cash activity
[ ] Round-tripping
[ ] Structuring/smurfing
[ ] Trade-based money laundering indicators
[ ] Other: ______________________________________________________

SECTION 4: INVESTIGATION SUMMARY
─────────────────────────────────────────────────────────────────
Date Investigation Started: ____/____/________
Investigating Officer: __________________________________________
Investigation Summary:
________________________________________________________________
________________________________________________________________
________________________________________________________________

Documents Reviewed: ______________________________________________
________________________________________________________________

SECTION 5: DISPOSITION
─────────────────────────────────────────────────────────────────
[ ] SAR filed with FIU
[ ] Internal investigation ongoing
[ ] Law enforcement notified
[ ] Account frozen/closed
[ ] No SAR filed (documented rationale below)
Rationale if no SAR: _____________________________________________
________________________________________________________________

SECTION 6: APPROVALS
─────────────────────────────────────────────────────────────────
Prepared By: _______________________  Date: ____/____/________
MLRO Review: _______________________  Date: ____/____/________
Legal Review: ______________________  Date: ____/____/________
CEO Notification: __________________  Date: ____/____/________

Classification: Confidential — Tipping Off Prohibited
═══════════════════════════════════════════════════════════════════
```

---

*End of Document*
*SSTP-OPS-005 v1.0 | Anti-Money Laundering and Know-Your-Customer Framework*
*Classification: Confidential | © 2025 SSTP Corleone Ecosystem*
