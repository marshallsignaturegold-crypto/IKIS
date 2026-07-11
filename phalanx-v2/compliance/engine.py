"""
Phalanx Swarm — Compliance Checker Engine
========================================
Validates documents against regulatory requirements per jurisdiction.
Checks completeness, consistency, recency, scores, reports, gaps,
and suggests remediation steps.
"""
from __future__ import annotations

import copy
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from enum import Enum, auto
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

from templates import (
    Jurisdiction,
    Template,
    TemplateRegistry,
    TemplateType,
    ValidationResult,
    TemplateValidator,
)


# ────────────────────────────────────────────────────────────────
# Compliance Status
# ────────────────────────────────────────────────────────────────
class ComplianceStatus(Enum):
    PASS = "pass"
    PARTIAL = "partial"
    FAIL = "fail"
    NOT_APPLICABLE = "not_applicable"


# ────────────────────────────────────────────────────────────────
# Check Result (single check)
# ────────────────────────────────────────────────────────────────
@dataclass
class CheckResult:
    check_id: str
    check_name: str
    category: str  # completeness | consistency | recency | jurisdiction
    status: ComplianceStatus
    score_contribution: float  # 0.0 – 1.0
    details: str
    remediation: Optional[str] = None
    evidence: List[str] = field(default_factory=list)


# ────────────────────────────────────────────────────────────────
# Compliance Report
# ────────────────────────────────────────────────────────────────
@dataclass
class ComplianceReport:
    document_id: str
    jurisdiction: Jurisdiction
    template_type: TemplateType
    overall_score: float  # 0 – 100
    status: ComplianceStatus
    checks: List[CheckResult] = field(default_factory=list)
    gaps: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    remediation_plan: List[str] = field(default_factory=list)
    critical_path_items: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "document_id": self.document_id,
            "jurisdiction": self.jurisdiction.value,
            "template_type": self.template_type.name,
            "overall_score": self.overall_score,
            "status": self.status.value,
            "checks": [
                {
                    "check_id": c.check_id,
                    "check_name": c.check_name,
                    "category": c.category,
                    "status": c.status.value,
                    "score_contribution": c.score_contribution,
                    "details": c.details,
                    "remediation": c.remediation,
                    "evidence": c.evidence,
                }
                for c in self.checks
            ],
            "gaps": self.gaps,
            "warnings": self.warnings,
            "generated_at": self.generated_at.isoformat(),
            "remediation_plan": self.remediation_plan,
            "critical_path_items": self.critical_path_items,
        }


# ────────────────────────────────────────────────────────────────
# Regulatory Requirement Database (per jurisdiction)
# ────────────────────────────────────────────────────────────────
class RegulatoryRequirement:
    """A single regulatory requirement that a document must satisfy."""

    def __init__(
        self,
        req_id: str,
        name: str,
        jurisdiction: Jurisdiction,
        template_types: Set[TemplateType],
        check_fn: Callable[[Dict[str, Any]], Tuple[bool, str]],
        weight: float = 1.0,
        remediation: str = "",
    ):
        self.req_id = req_id
        self.name = name
        self.jurisdiction = jurisdiction
        self.template_types = template_types
        self.check_fn = check_fn
        self.weight = weight
        self.remediation = remediation


class RequirementRegistry:
    """Stores and queries regulatory requirements."""

    def __init__(self):
        self._requirements: List[RegulatoryRequirement] = []
        self._build_defaults()

    def add(self, req: RegulatoryRequirement) -> None:
        self._requirements.append(req)

    def for_document(
        self, jurisdiction: Jurisdiction, template_type: TemplateType
    ) -> List[RegulatoryRequirement]:
        return [
            r
            for r in self._requirements
            if r.jurisdiction == jurisdiction and template_type in r.template_types
        ]

    def _build_defaults(self) -> None:
        # ── India SEBI ──
        self.add(
            RegulatoryRequirement(
                req_id="SEBI-R01",
                name="Promoter shareholding disclosed",
                jurisdiction=Jurisdiction.INDIA_SEBI,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    "shareholding_pattern" in d and len(d.get("shareholding_pattern", "")) > 20,
                    "Promoter shareholding pattern missing or too short.",
                ),
                weight=1.0,
                remediation="Obtain latest shareholding pattern from registrar and attach.",
            )
        )
        self.add(
            RegulatoryRequirement(
                req_id="SEBI-R02",
                name="Related party transactions disclosed",
                jurisdiction=Jurisdiction.INDIA_SEBI,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    "related_party_transactions" in d,
                    "Related party transactions section missing.",
                ),
                weight=1.0,
                remediation="Compile related-party transaction register and include.",
            )
        )

        # ── Saudi SFDA ──
        self.add(
            RegulatoryRequirement(
                req_id="SFDA-R01",
                name="Local agent appointment documented",
                jurisdiction=Jurisdiction.SAUDI_SFDA,
                template_types={TemplateType.REGULATORY_FILING, TemplateType.CERTIFICATION_APPLICATION},
                check_fn=lambda d: (
                    "local_agent_appointment" in d and len(d.get("local_agent_appointment", "")) > 10,
                    "Local agent appointment not documented.",
                ),
                weight=1.0,
                remediation="Execute local agent agreement with SFDA-registered entity and attach.",
            )
        )
        self.add(
            RegulatoryRequirement(
                req_id="SFDA-R02",
                name="Arabic translation certified",
                jurisdiction=Jurisdiction.SAUDI_SFDA,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    "arabic_translation_certification" in d,
                    "Arabic translation certification missing.",
                ),
                weight=1.0,
                remediation="Engage certified translator and obtain notarized Arabic translation.",
            )
        )

        # ── Ethiopia WOAH ──
        self.add(
            RegulatoryRequirement(
                req_id="WOAH-R01",
                name="Import permit from Ministry of Agriculture present",
                jurisdiction=Jurisdiction.ETHIOPIA_WOAH,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    "import_permit_from_moa" in d,
                    "Import permit from Ministry of Agriculture missing.",
                ),
                weight=1.0,
                remediation="Apply to Ethiopian Ministry of Agriculture for import permit.",
            )
        )
        self.add(
            RegulatoryRequirement(
                req_id="WOAH-R02",
                name="GMP certificate attached",
                jurisdiction=Jurisdiction.ETHIOPIA_WOAH,
                template_types={TemplateType.REGULATORY_FILING, TemplateType.CERTIFICATION_APPLICATION},
                check_fn=lambda d: (
                    "manufacturing_gmp_certificate" in d,
                    "GMP certificate missing.",
                ),
                weight=1.0,
                remediation="Request updated GMP certificate from manufacturing facility and attach.",
            )
        )

        # ── US FinCEN ──
        self.add(
            RegulatoryRequirement(
                req_id="FINCEN-R01",
                name="BSA Officer contact provided",
                jurisdiction=Jurisdiction.US_FINCEN,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    "bsa_officer_contact" in d and "@" in d.get("bsa_officer_contact", ""),
                    "BSA Officer contact missing or invalid.",
                ),
                weight=1.0,
                remediation="Designate BSA Officer and provide name, email, phone.",
            )
        )
        self.add(
            RegulatoryRequirement(
                req_id="FINCEN-R02",
                name="SAR narrative within 12,000 chars",
                jurisdiction=Jurisdiction.US_FINCEN,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    len(d.get("suspicious_activity_narrative", "")) <= 12000,
                    "SAR narrative exceeds 12,000 characters.",
                ),
                weight=0.5,
                remediation="Trim narrative to 12,000 characters or split into multiple filings.",
            )
        )
        self.add(
            RegulatoryRequirement(
                req_id="FINCEN-R03",
                name="Compliance officer attestation present",
                jurisdiction=Jurisdiction.US_FINCEN,
                template_types={TemplateType.REGULATORY_FILING},
                check_fn=lambda d: (
                    "compliance_officer_attestation" in d,
                    "Compliance officer attestation missing.",
                ),
                weight=1.0,
                remediation="Obtain signed attestation from compliance officer.",
            )
        )

        # ── Global / Cross-cutting ──
        self.add(
            RegulatoryRequirement(
                req_id="GLOBAL-R01",
                name="Executive summary present",
                jurisdiction=Jurisdiction.GLOBAL,
                template_types={TemplateType.REGULATORY_FILING, TemplateType.AUDIT_REPORT},
                check_fn=lambda d: (
                    "executive_summary" in d and len(d.get("executive_summary", "")) > 50,
                    "Executive summary missing or too short.",
                ),
                weight=0.5,
                remediation="Draft executive summary covering scope, findings, and next steps.",
            )
        )


# ────────────────────────────────────────────────────────────────
# Consistency Checker
# ────────────────────────────────────────────────────────────────
class ConsistencyChecker:
    """Detects contradictions between sections of a document."""

    @staticmethod
    def check(data: Dict[str, Any]) -> List[CheckResult]:
        results: List[CheckResult] = []

        # Check 1: date ranges (period start <= period end)
        start = data.get("audit_period_start") or data.get("period_start")
        end = data.get("audit_period_end") or data.get("period_end")
        if start and end:
            try:
                ds = datetime.fromisoformat(start.replace("Z", "+00:00"))
                de = datetime.fromisoformat(end.replace("Z", "+00:00"))
                if ds > de:
                    results.append(
                        CheckResult(
                            check_id="CON-001",
                            check_name="Period start before end",
                            category="consistency",
                            status=ComplianceStatus.FAIL,
                            score_contribution=0.0,
                            details="Period start is after period end.",
                            remediation="Correct period dates to ensure chronological order.",
                        )
                    )
                else:
                    results.append(
                        CheckResult(
                            check_id="CON-001",
                            check_name="Period start before end",
                            category="consistency",
                            status=ComplianceStatus.PASS,
                            score_contribution=1.0,
                            details="Period dates are consistent.",
                        )
                    )
            except Exception:
                pass

        # Check 2: entity name consistency across sections
        names = []
        for key in ["entity_identification", "applicant_details", "reporting_entity_cik"]:
            if key in data:
                val = data[key]
                if isinstance(val, str):
                    names.append(val.split()[0] if val.split() else val)
                elif isinstance(val, dict) and "name" in val:
                    names.append(val["name"])
        if len(set(names)) > 1:
            results.append(
                CheckResult(
                    check_id="CON-002",
                    check_name="Entity name consistency",
                    category="consistency",
                    status=ComplianceStatus.FAIL,
                    score_contribution=0.0,
                    details=f"Entity names differ across sections: {names}",
                    remediation="Standardize entity name across all sections.",
                )
            )
        elif len(names) > 1:
            results.append(
                CheckResult(
                    check_id="CON-002",
                    check_name="Entity name consistency",
                    category="consistency",
                    status=ComplianceStatus.PASS,
                    score_contribution=1.0,
                    details="Entity name is consistent across sections.",
                )
            )

        # Check 3: attachments referenced vs provided
        for key, val in data.items():
            if key.endswith("_attachments"):
                base = key.replace("_attachments", "")
                if base in data and not val:
                    results.append(
                        CheckResult(
                            check_id=f"CON-ATT-{base}",
                            check_name=f"Attachment presence for {base}",
                            category="consistency",
                            status=ComplianceStatus.FAIL,
                            score_contribution=0.0,
                            details=f"Section '{base}' references attachments but list is empty.",
                            remediation=f"Upload attachments for '{base}' or remove attachment requirement.",
                        )
                    )

        return results


# ────────────────────────────────────────────────────────────────
# Recency Checker
# ────────────────────────────────────────────────────────────────
class RecencyChecker:
    """Verifies that permits, certifications, and dates are still valid."""

    DEFAULT_CERT_VALIDITY_DAYS = 365
    DEFAULT_PERMIT_VALIDITY_DAYS = 730

    def __init__(self, now: Optional[datetime] = None):
        self.now = now or datetime.now(timezone.utc)

    def _parse_date(self, val: Any) -> Optional[datetime]:
        if isinstance(val, datetime):
            return val
        if isinstance(val, str):
            try:
                return datetime.fromisoformat(val.replace("Z", "+00:00"))
            except Exception:
                pass
        return None

    def check(self, data: Dict[str, Any]) -> List[CheckResult]:
        results: List[CheckResult] = []

        # Certifications
        certs = data.get("certifications", [])
        if isinstance(certs, dict):
            certs = [certs]
        if not isinstance(certs, list):
            certs = []
        for cert in certs:
            if isinstance(cert, dict):
                name = cert.get("name", "Unknown")
                issued = self._parse_date(cert.get("issued_date"))
                expiry = self._parse_date(cert.get("expiry_date"))
                if issued and expiry:
                    if expiry < self.now:
                        results.append(
                            CheckResult(
                                check_id=f"REC-CERT-{name}",
                                check_name=f"Certification '{name}' validity",
                                category="recency",
                                status=ComplianceStatus.FAIL,
                                score_contribution=0.0,
                                details=f"Certification '{name}' expired on {expiry.date()}.",
                                remediation=f"Renew certification '{name}' immediately.",
                            )
                        )
                    elif (expiry - self.now).days < 30:
                        results.append(
                            CheckResult(
                                check_id=f"REC-CERT-{name}",
                                check_name=f"Certification '{name}' validity",
                                category="recency",
                                status=ComplianceStatus.PARTIAL,
                                score_contribution=0.5,
                                details=f"Certification '{name}' expires in {(expiry - self.now).days} days.",
                                remediation=f"Initiate renewal for certification '{name}'.",
                            )
                        )
                    else:
                        results.append(
                            CheckResult(
                                check_id=f"REC-CERT-{name}",
                                check_name=f"Certification '{name}' validity",
                                category="recency",
                                status=ComplianceStatus.PASS,
                                score_contribution=1.0,
                                details=f"Certification '{name}' is valid until {expiry.date()}.",
                            )
                        )

        # Permits
        permits = data.get("permits", [])
        if isinstance(permits, dict):
            permits = [permits]
        if not isinstance(permits, list):
            permits = []
        for permit in permits:
            if isinstance(permit, dict):
                name = permit.get("name", "Unknown")
                expiry = self._parse_date(permit.get("expiry_date"))
                if expiry:
                    if expiry < self.now:
                        results.append(
                            CheckResult(
                                check_id=f"REC-PERM-{name}",
                                check_name=f"Permit '{name}' validity",
                                category="recency",
                                status=ComplianceStatus.FAIL,
                                score_contribution=0.0,
                                details=f"Permit '{name}' expired on {expiry.date()}.",
                                remediation=f"Renew permit '{name}' immediately; operations may be halted.",
                            )
                        )
                    elif (expiry - self.now).days < 30:
                        results.append(
                            CheckResult(
                                check_id=f"REC-PERM-{name}",
                                check_name=f"Permit '{name}' validity",
                                category="recency",
                                status=ComplianceStatus.PARTIAL,
                                score_contribution=0.5,
                                details=f"Permit '{name}' expires in {(expiry - self.now).days} days.",
                                remediation=f"Initiate renewal for permit '{name}'.",
                            )
                        )
                    else:
                        results.append(
                            CheckResult(
                                check_id=f"REC-PERM-{name}",
                                check_name=f"Permit '{name}' validity",
                                category="recency",
                                status=ComplianceStatus.PASS,
                                score_contribution=1.0,
                                details=f"Permit '{name}' is valid until {expiry.date()}.",
                            )
                        )

        # Filing / submission date recency
        filing_date = self._parse_date(data.get("filing_date"))
        if filing_date:
            age_days = (self.now - filing_date).days
            if age_days > 365:
                results.append(
                    CheckResult(
                        check_id="REC-FILING-AGE",
                        check_name="Filing date recency",
                        category="recency",
                        status=ComplianceStatus.FAIL,
                        score_contribution=0.0,
                        details=f"Filing is {age_days} days old; may be stale.",
                        remediation="Update filing with current data or re-file.",
                    )
                )
            elif age_days > 180:
                results.append(
                    CheckResult(
                        check_id="REC-FILING-AGE",
                        check_name="Filing date recency",
                        category="recency",
                        status=ComplianceStatus.PARTIAL,
                        score_contribution=0.5,
                        details=f"Filing is {age_days} days old; consider refresh.",
                        remediation="Review filing for material changes.",
                    )
                )
            else:
                results.append(
                    CheckResult(
                        check_id="REC-FILING-AGE",
                        check_name="Filing date recency",
                        category="recency",
                        status=ComplianceStatus.PASS,
                        score_contribution=1.0,
                        details=f"Filing is {age_days} days old; current.",
                    )
                )

        return results


# ────────────────────────────────────────────────────────────────
# Gap Analyzer
# ────────────────────────────────────────────────────────────────
class GapAnalyzer:
    """Identifies what's missing, what's wrong, and what's expired."""

    @staticmethod
    def analyze(report: ComplianceReport, data: Dict[str, Any]) -> List[str]:
        gaps: List[str] = []
        for check in report.checks:
            if check.status in (ComplianceStatus.FAIL, ComplianceStatus.PARTIAL):
                gaps.append(f"[{check.category.upper()}] {check.check_name}: {check.details}")
        if report.gaps:
            gaps.extend(report.gaps)
        return gaps


# ────────────────────────────────────────────────────────────────
# Remediation Suggester
# ────────────────────────────────────────────────────────────────
class RemediationSuggester:
    """Generates specific remediation steps from check results."""

    @staticmethod
    def suggest(checks: List[CheckResult]) -> List[str]:
        steps: List[str] = []
        for check in checks:
            if check.status != ComplianceStatus.PASS and check.remediation:
                steps.append(f"[{check.check_id}] {check.remediation}")
        return steps


# ────────────────────────────────────────────────────────────────
# Compliance Engine (orchestrator)
# ────────────────────────────────────────────────────────────────
class ComplianceEngine:
    def __init__(
        self,
        template_registry: TemplateRegistry,
        requirement_registry: Optional[RequirementRegistry] = None,
        now: Optional[datetime] = None,
    ):
        self.template_registry = template_registry
        self.requirement_registry = requirement_registry or RequirementRegistry()
        self.validator = TemplateValidator(template_registry)
        self.consistency_checker = ConsistencyChecker()
        self.recency_checker = RecencyChecker(now=now)
        self.gap_analyzer = GapAnalyzer()
        self.remediation_suggester = RemediationSuggester()

    def evaluate(
        self,
        document_id: str,
        template_id: str,
        data: Dict[str, Any],
        content: str,
        jurisdiction: Optional[Jurisdiction] = None,
    ) -> ComplianceReport:
        template = self.template_registry.get(template_id)
        if not template:
            return ComplianceReport(
                document_id=document_id,
                jurisdiction=jurisdiction or Jurisdiction.GLOBAL,
                template_type=TemplateType.REGULATORY_FILING,
                overall_score=0.0,
                status=ComplianceStatus.FAIL,
                checks=[],
                gaps=[f"Template '{template_id}' not found."],
                remediation_plan=["Register template before evaluation."],
            )

        jj = jurisdiction or template.jurisdiction
        tt = template.template_type
        checks: List[CheckResult] = []

        # 1. Template validation (completeness proxy)
        val_result = self.validator.validate(template_id, data, content)
        val_status = ComplianceStatus.PASS if val_result.passed else ComplianceStatus.FAIL
        if val_result.warnings:
            val_status = ComplianceStatus.PARTIAL if val_result.passed else ComplianceStatus.FAIL
        checks.append(
            CheckResult(
                check_id="TMPL-VAL",
                check_name="Template structural validation",
                category="completeness",
                status=val_status,
                score_contribution=1.0 if val_result.passed else 0.0,
                details=f"Missing: {val_result.missing_sections}; Warnings: {len(val_result.warnings)}; Errors: {len(val_result.errors)}",
                remediation="Address missing sections and warnings before submission." if not val_result.passed else None,
                evidence=val_result.errors + val_result.warnings,
            )
        )

        # 2. Jurisdiction-specific requirements
        reqs = self.requirement_registry.for_document(jj, tt)
        for req in reqs:
            passed, detail = req.check_fn(data)
            status = ComplianceStatus.PASS if passed else ComplianceStatus.FAIL
            score = 1.0 if passed else 0.0
            checks.append(
                CheckResult(
                    check_id=req.req_id,
                    check_name=req.name,
                    category="jurisdiction",
                    status=status,
                    score_contribution=score * req.weight,
                    details=detail if not passed else f"Requirement '{req.name}' satisfied.",
                    remediation=req.remediation if not passed else None,
                )
            )

        # 3. Consistency
        checks.extend(self.consistency_checker.check(data))

        # 4. Recency
        checks.extend(self.recency_checker.check(data))

        # Score calculation
        total_weight = sum(c.score_contribution for c in checks if c.status != ComplianceStatus.NOT_APPLICABLE)
        max_weight = len([c for c in checks if c.status != ComplianceStatus.NOT_APPLICABLE])
        score = (total_weight / max_weight * 100) if max_weight > 0 else 0.0

        # Determine status
        if all(c.status == ComplianceStatus.PASS for c in checks if c.status != ComplianceStatus.NOT_APPLICABLE):
            status = ComplianceStatus.PASS
        elif any(c.status == ComplianceStatus.FAIL for c in checks):
            status = ComplianceStatus.FAIL
        else:
            status = ComplianceStatus.PARTIAL

        gaps = self.gap_analyzer.analyze(
            ComplianceReport(document_id=document_id, jurisdiction=jj, template_type=tt, overall_score=0, status=status),
            data,
        )
        # enrich gaps from checks
        for c in checks:
            if c.status in (ComplianceStatus.FAIL, ComplianceStatus.PARTIAL) and c.details not in gaps:
                gaps.append(c.details)

        remediation = self.remediation_suggester.suggest(checks)

        # Critical path items: any FAIL or PARTIAL with weight >= 1.0
        critical = [c.check_name for c in checks if c.status in (ComplianceStatus.FAIL, ComplianceStatus.PARTIAL) and c.score_contribution >= 1.0]

        return ComplianceReport(
            document_id=document_id,
            jurisdiction=jj,
            template_type=tt,
            overall_score=round(score, 2),
            status=status,
            checks=checks,
            gaps=gaps,
            warnings=[c.details for c in checks if c.status == ComplianceStatus.PARTIAL],
            remediation_plan=remediation,
            critical_path_items=critical,
        )


# ────────────────────────────────────────────────────────────────
# CLI / module test harness
# ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from templates import TemplateFactory

    reg = TemplateFactory.build_registry()
    engine = ComplianceEngine(reg)

    data = {
        "executive_summary": "This SAR documents suspicious wire transfers...",
        "entity_identification": "Acme Bank NA",
        "scope_of_filing": "Suspicious Activity Report for Q3 2025",
        "supporting_evidence": "Wire transfer logs reviewed.",
        "supporting_evidence_attachments": ["wires_Q3.csv"],
        "risk_assessment": "High risk due to rapid movement of funds.",
        "compliance_statement": "This filing is made in good faith.",
        "reporting_entity_cik": "0001234567",
        "suspicious_activity_narrative": "Subject transferred $4.2M across 12 jurisdictions..." * 50,
        "financial_transaction_records": "See attached CSV.",
        "compliance_officer_attestation": "I, Jane Doe, attest.",
        "bsa_officer_contact": "Jane Doe, jane.doe@acmebank.com",
        "certifications": [
            {"name": "SOC2", "issued_date": "2023-01-01", "expiry_date": "2024-01-01"},  # expired
            {"name": "ISO27001", "issued_date": "2024-01-01", "expiry_date": "2025-06-01"},  # soon
        ],
        "permits": [
            {"name": "MSB License", "expiry_date": "2026-01-01"},
        ],
        "filing_date": "2024-01-01",
    }

    content = "\n".join(f"{k}: {v}" for k, v in data.items())
    report = engine.evaluate("DOC-2025-001", "us_fincen.regulatory_filing", data, content)
    print(json.dumps(report.to_dict(), indent=2))
