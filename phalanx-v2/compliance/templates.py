"""
Phalanx Swarm — Regulatory Filing Template Engine
===============================================
Defines template types, inheritance hierarchies, jurisdiction-specific
variations, validation rules, versioning, and JSON-to-markdown rendering.

Jurisdictions: India (SEBI), Saudi Arabia (SFDA), Ethiopia (WOAH), US (FinCEN)
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import textwrap
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Set, Tuple, Union


# ────────────────────────────────────────────────────────────────
# Template Types
# ────────────────────────────────────────────────────────────────
class TemplateType(Enum):
    REGULATORY_FILING = auto()
    LEGAL_CONTRACT = auto()
    COMPLIANCE_CHECKLIST = auto()
    AUDIT_REPORT = auto()
    CERTIFICATION_APPLICATION = auto()


# ────────────────────────────────────────────────────────────────
# Jurisdictions
# ────────────────────────────────────────────────────────────────
class Jurisdiction(Enum):
    GLOBAL = "global"
    INDIA_SEBI = "in_sebi"
    SAUDI_SFDA = "sa_sfda"
    ETHIOPIA_WOAH = "et_woah"
    US_FINCEN = "us_fincen"


# ────────────────────────────────────────────────────────────────
# Section Definition
# ────────────────────────────────────────────────────────────────
@dataclass
class SectionDef:
    name: str
    mandatory: bool = True
    max_length_chars: Optional[int] = None
    min_length_chars: Optional[int] = None
    requires_attachments: bool = False
    allowed_attachment_types: List[str] = field(default_factory=list)
    conditional_on: Optional[str] = None  # section name that must exist if this one does
    repeatable: bool = False
    jurisdiction_override: Optional[Dict[Jurisdiction, Dict[str, Any]]] = None

    def get_for_jurisdiction(self, j: Jurisdiction) -> "SectionDef":
        if self.jurisdiction_override and j in self.jurisdiction_override:
            ov = self.jurisdiction_override[j]
            return SectionDef(
                name=self.name,
                mandatory=ov.get("mandatory", self.mandatory),
                max_length_chars=ov.get("max_length_chars", self.max_length_chars),
                min_length_chars=ov.get("min_length_chars", self.min_length_chars),
                requires_attachments=ov.get("requires_attachments", self.requires_attachments),
                allowed_attachment_types=ov.get("allowed_attachment_types", self.allowed_attachment_types),
                conditional_on=ov.get("conditional_on", self.conditional_on),
                repeatable=ov.get("repeatable", self.repeatable),
            )
        return self


# ────────────────────────────────────────────────────────────────
# Validation Rule
# ────────────────────────────────────────────────────────────────
@dataclass
class ValidationRule:
    rule_id: str
    description: str
    applies_to_types: Optional[Set[TemplateType]] = None
    applies_to_jurisdictions: Optional[Set[Jurisdiction]] = None
    predicate: Optional[callable] = None  # fn(template, rendered) -> bool
    severity: str = "error"  # error | warning | info
    max_pages: Optional[int] = None
    must_have_sections: Optional[List[str]] = None
    must_not_have_sections: Optional[List[str]] = None
    section_order_matters: bool = False
    required_section_order: Optional[List[str]] = None

    def applies(self, tt: TemplateType, jj: Jurisdiction) -> bool:
        if self.applies_to_types and tt not in self.applies_to_types:
            return False
        if self.applies_to_jurisdictions and jj not in self.applies_to_jurisdictions:
            return False
        return True


# ────────────────────────────────────────────────────────────────
# Template Version
# ────────────────────────────────────────────────────────────────
@dataclass
class TemplateVersion:
    major: int = 1
    minor: int = 0
    patch: int = 0
    released_at: Optional[datetime] = None
    changelog: str = ""

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def bump(self, level: str) -> "TemplateVersion":
        now = datetime.now(timezone.utc)
        if level == "major":
            return TemplateVersion(self.major + 1, 0, 0, now, "")
        if level == "minor":
            return TemplateVersion(self.major, self.minor + 1, 0, now, "")
        return TemplateVersion(self.major, self.minor, self.patch + 1, now, "")


# ────────────────────────────────────────────────────────────────
# Template Registry Entry
# ────────────────────────────────────────────────────────────────
@dataclass
class Template:
    template_id: str
    name: str
    template_type: TemplateType
    jurisdiction: Jurisdiction
    version: TemplateVersion
    parent_template_id: Optional[str] = None
    sections: List[SectionDef] = field(default_factory=list)
    validation_rules: List[ValidationRule] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    _checksum: Optional[str] = None

    def compute_checksum(self) -> str:
        payload = json.dumps({
            "id": self.template_id,
            "name": self.name,
            "type": self.template_type.name,
            "jurisdiction": self.jurisdiction.value,
            "version": str(self.version),
            "sections": [s.name for s in self.sections],
            "rules": [r.rule_id for r in self.validation_rules],
        }, sort_keys=True)
        self._checksum = hashlib.sha256(payload.encode()).hexdigest()[:16]
        return self._checksum

    def all_sections(self, registry: "TemplateRegistry") -> List[SectionDef]:
        """Return inherited + own sections, merged by name."""
        inherited: Dict[str, SectionDef] = {}
        if self.parent_template_id:
            parent = registry.get(self.parent_template_id)
            if parent:
                for s in parent.all_sections(registry):
                    inherited[s.name] = s
        for s in self.sections:
            inherited[s.name] = s
        return list(inherited.values())

    def all_rules(self, registry: "TemplateRegistry") -> List[ValidationRule]:
        inherited: Dict[str, ValidationRule] = {}
        if self.parent_template_id:
            parent = registry.get(self.parent_template_id)
            if parent:
                for r in parent.all_rules(registry):
                    inherited[r.rule_id] = r
        for r in self.validation_rules:
            inherited[r.rule_id] = r
        return list(inherited.values())


# ────────────────────────────────────────────────────────────────
# Template Registry
# ────────────────────────────────────────────────────────────────
class TemplateRegistry:
    def __init__(self):
        self._templates: Dict[str, Template] = {}

    def register(self, template: Template) -> None:
        template.compute_checksum()
        template.updated_at = datetime.now(timezone.utc)
        self._templates[template.template_id] = template

    def get(self, template_id: str) -> Optional[Template]:
        return self._templates.get(template_id)

    def list_by_type(self, tt: TemplateType) -> List[Template]:
        return [t for t in self._templates.values() if t.template_type == tt]

    def list_by_jurisdiction(self, jj: Jurisdiction) -> List[Template]:
        return [t for t in self._templates.values() if t.jurisdiction == jj]

    def lineage(self, template_id: str) -> List[Template]:
        chain: List[Template] = []
        t = self.get(template_id)
        while t:
            chain.append(t)
            t = self.get(t.parent_template_id) if t.parent_template_id else None
        return list(reversed(chain))


# ────────────────────────────────────────────────────────────────
# Validation Engine
# ────────────────────────────────────────────────────────────────
@dataclass
class ValidationResult:
    template_id: str
    jurisdiction: Jurisdiction
    template_type: TemplateType
    passed: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    missing_sections: List[str] = field(default_factory=list)
    extra_sections: List[str] = field(default_factory=list)
    page_estimate: Optional[int] = None


class TemplateValidator:
    def __init__(self, registry: TemplateRegistry):
        self.registry = registry

    def _estimate_pages(self, content: str) -> int:
        # rough: ~3000 chars per page of dense text
        return max(1, len(content) // 3000)

    def validate(self, template_id: str, data: Dict[str, Any], content: str) -> ValidationResult:
        template = self.registry.get(template_id)
        if not template:
            return ValidationResult(
                template_id=template_id,
                jurisdiction=Jurisdiction.GLOBAL,
                template_type=TemplateType.REGULATORY_FILING,
                passed=False,
                errors=["Template not found in registry."],
            )

        sections = template.all_sections(self.registry)
        rules = template.all_rules(self.registry)
        errors, warnings, info = [], [], []
        missing, extra = [], []
        data_sections = set(data.keys())
        required_sections = {s.name for s in sections if s.mandatory}
        present_sections = data_sections & required_sections
        missing_sections = list(required_sections - data_sections)
        missing.extend(missing_sections)

        for s in sections:
            if s.name not in data:
                if s.mandatory:
                    errors.append(f"Mandatory section '{s.name}' is missing.")
                continue
            val = data[s.name]
            if isinstance(val, str):
                if s.min_length_chars and len(val) < s.min_length_chars:
                    errors.append(f"Section '{s.name}' below minimum length ({s.min_length_chars}).")
                if s.max_length_chars and len(val) > s.max_length_chars:
                    warnings.append(f"Section '{s.name}' exceeds recommended length ({s.max_length_chars}).")
            if s.requires_attachments and not data.get(f"{s.name}_attachments"):
                warnings.append(f"Section '{s.name}' expects attachments but none provided.")

        for rule in rules:
            if not rule.applies(template.template_type, template.jurisdiction):
                continue
            if rule.must_have_sections:
                for sec in rule.must_have_sections:
                    if sec not in data_sections:
                        errors.append(f"Rule {rule.rule_id}: must have section '{sec}'.")
            if rule.must_not_have_sections:
                for sec in rule.must_not_have_sections:
                    if sec in data_sections:
                        errors.append(f"Rule {rule.rule_id}: must NOT have section '{sec}'.")
            if rule.max_pages is not None:
                est = self._estimate_pages(content)
                if est > rule.max_pages:
                    errors.append(f"Rule {rule.rule_id}: exceeds {rule.max_pages} pages (estimated {est}).")
            if rule.section_order_matters and rule.required_section_order:
                order = [s for s in rule.required_section_order if s in data_sections]
                if order != rule.required_section_order:
                    warnings.append(f"Rule {rule.rule_id}: section order may not match required order.")
            if rule.predicate and not rule.predicate(template, content):
                if rule.severity == "error":
                    errors.append(f"Rule {rule.rule_id}: {rule.description}")
                elif rule.severity == "warning":
                    warnings.append(f"Rule {rule.rule_id}: {rule.description}")
                else:
                    info.append(f"Rule {rule.rule_id}: {rule.description}")

        return ValidationResult(
            template_id=template_id,
            jurisdiction=template.jurisdiction,
            template_type=template.template_type,
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            info=info,
            missing_sections=missing,
            extra_sections=list(data_sections - {s.name for s in sections}),
            page_estimate=self._estimate_pages(content),
        )


# ────────────────────────────────────────────────────────────────
# Renderer: JSON data → Markdown document
# ────────────────────────────────────────────────────────────────
class TemplateRenderer:
    def __init__(self, registry: TemplateRegistry):
        self.registry = registry

    def _format_section(self, name: str, value: Any, level: int = 2) -> str:
        prefix = "#" * level
        if isinstance(value, dict):
            body = "\n".join(f"- **{k}**: {v}" for k, v in value.items())
            return f"{prefix} {name}\n\n{body}\n"
        if isinstance(value, list):
            body = "\n".join(f"- {item}" for item in value)
            return f"{prefix} {name}\n\n{body}\n"
        return f"{prefix} {name}\n\n{value}\n"

    def render(self, template_id: str, data: Dict[str, Any], meta: Optional[Dict[str, Any]] = None) -> str:
        template = self.registry.get(template_id)
        if not template:
            raise ValueError(f"Template '{template_id}' not found.")

        sections = template.all_sections(self.registry)
        out_lines: List[str] = []
        out_lines.append(f"# {template.name}")
        out_lines.append(f"<!-- Template: {template.template_id} | Version: {template.version} | Jurisdiction: {template.jurisdiction.value.upper()} -->")
        if meta:
            out_lines.append(f"<!-- Meta: {json.dumps(meta, default=str)} -->")
        out_lines.append("")

        for s in sections:
            if s.name in data:
                out_lines.append(self._format_section(s.name, data[s.name], level=2))
            elif s.mandatory:
                out_lines.append(f"## {s.name}\n\n> **[PLACEHOLDER — MANDATORY SECTION MISSING]**\n")

        return "\n".join(out_lines)


# ────────────────────────────────────────────────────────────────
# Change Tracking
# ────────────────────────────────────────────────────────────────
@dataclass
class TemplateChange:
    change_id: str
    template_id: str
    from_version: str
    to_version: str
    changed_at: datetime
    changed_by: str
    diff_summary: str


class TemplateChangeLog:
    def __init__(self):
        self._entries: List[TemplateChange] = []

    def record(self, entry: TemplateChange) -> None:
        self._entries.append(entry)

    def history(self, template_id: str) -> List[TemplateChange]:
        return [e for e in self._entries if e.template_id == template_id]

    def diff(self, template_id: str, v1: str, v2: str) -> Optional[str]:
        changes = [e for e in self._entries if e.template_id == template_id and {v1, v2} <= {e.from_version, e.to_version}]
        if not changes:
            return None
        return "\n".join(c.diff_summary for c in changes)


# ────────────────────────────────────────────────────────────────
# Pre-built Templates (Factory)
# ────────────────────────────────────────────────────────────────
class TemplateFactory:
    """Bootstraps the registry with base templates and jurisdiction variants."""

    @staticmethod
    def build_registry() -> TemplateRegistry:
        reg = TemplateRegistry()

        # ── Base Regulatory Filing ──
        base_regulatory = Template(
            template_id="base.regulatory_filing",
            name="Base Regulatory Filing",
            template_type=TemplateType.REGULATORY_FILING,
            jurisdiction=Jurisdiction.GLOBAL,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            sections=[
                SectionDef("executive_summary", mandatory=True, max_length_chars=5000),
                SectionDef("entity_identification", mandatory=True, min_length_chars=50),
                SectionDef("scope_of_filing", mandatory=True),
                SectionDef("supporting_evidence", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf", ".xlsx", ".csv"]),
                SectionDef("risk_assessment", mandatory=True),
                SectionDef("compliance_statement", mandatory=True),
                SectionDef("appendices", mandatory=False, repeatable=True),
                SectionDef("disclaimers", mandatory=False),
            ],
            validation_rules=[
                ValidationRule("R001", "Must have executive summary <= 5000 chars", max_pages=50,
                               must_have_sections=["executive_summary", "compliance_statement"]),
                ValidationRule("R002", "Supporting evidence must have attachments", must_have_sections=["supporting_evidence"]),
            ],
            metadata={"owner": "phalanx-legal", "category": "regulatory"},
        )
        reg.register(base_regulatory)

        # ── India SEBI Regulatory Filing ──
        india_sebi = Template(
            template_id="in_sebi.regulatory_filing",
            name="SEBI Regulatory Filing (India)",
            template_type=TemplateType.REGULATORY_FILING,
            jurisdiction=Jurisdiction.INDIA_SEBI,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            parent_template_id="base.regulatory_filing",
            sections=[
                SectionDef("sebi_specific_disclosures", mandatory=True,
                           jurisdiction_override={Jurisdiction.INDIA_SEBI: {"mandatory": True}}),
                SectionDef("shareholding_pattern", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf", ".xlsx"]),
                SectionDef("related_party_transactions", mandatory=True),
                SectionDef("corporate_governance_report", mandatory=True),
            ],
            validation_rules=[
                ValidationRule("R-IN-001", "SEBI filings must include shareholding pattern",
                               applies_to_jurisdictions={Jurisdiction.INDIA_SEBI},
                               must_have_sections=["shareholding_pattern"]),
                ValidationRule("R-IN-002", "SEBI filing max 100 pages",
                               applies_to_jurisdictions={Jurisdiction.INDIA_SEBI}, max_pages=100),
            ],
            metadata={"regulator": "SEBI", "form_reference": "SEBI Circular CIR/CFD/DCR/2/2013"},
        )
        reg.register(india_sebi)

        # ── Saudi SFDA Regulatory Filing ──
        saudi_sfda = Template(
            template_id="sa_sfda.regulatory_filing",
            name="SFDA Regulatory Filing (Saudi Arabia)",
            template_type=TemplateType.REGULATORY_FILING,
            jurisdiction=Jurisdiction.SAUDI_SFDA,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            parent_template_id="base.regulatory_filing",
            sections=[
                SectionDef("product_classification", mandatory=True),
                SectionDef("safety_profile", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf", ".docx"]),
                SectionDef("local_agent_appointment", mandatory=True),
                SectionDef("sfda_fee_receipt", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf"]),
                SectionDef("arabic_translation_certification", mandatory=True),
            ],
            validation_rules=[
                ValidationRule("R-SA-001", "SFDA requires Arabic translation certification",
                               applies_to_jurisdictions={Jurisdiction.SAUDI_SFDA},
                               must_have_sections=["arabic_translation_certification"]),
                ValidationRule("R-SA-002", "SFDA filing max 75 pages",
                               applies_to_jurisdictions={Jurisdiction.SAUDI_SFDA}, max_pages=75),
            ],
            metadata={"regulator": "SFDA", "language": "ar+en"},
        )
        reg.register(saudi_sfda)

        # ── Ethiopia WOAH Regulatory Filing ──
        ethiopia_woah = Template(
            template_id="et_woah.regulatory_filing",
            name="WOAH / Animal Health Regulatory Filing (Ethiopia)",
            template_type=TemplateType.REGULATORY_FILING,
            jurisdiction=Jurisdiction.ETHIOPIA_WOAH,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            parent_template_id="base.regulatory_filing",
            sections=[
                SectionDef("veterinary_product_description", mandatory=True),
                SectionDef("manufacturing_gmp_certificate", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf"]),
                SectionDef("import_permit_from_moa", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf"]),
                SectionDef("batch_release_certification", mandatory=True),
                SectionDef("residue_depletion_study", mandatory=False),
            ],
            validation_rules=[
                ValidationRule("R-ET-001", "WOAH filing requires import permit from Ministry of Agriculture",
                               applies_to_jurisdictions={Jurisdiction.ETHIOPIA_WOAH},
                               must_have_sections=["import_permit_from_moa"]),
                ValidationRule("R-ET-002", "WOAH filing max 60 pages",
                               applies_to_jurisdictions={Jurisdiction.ETHIOPIA_WOAH}, max_pages=60),
            ],
            metadata={"regulator": "WOAH / MoA Ethiopia", "priority": "agriculture"},
        )
        reg.register(ethiopia_woah)

        # ── US FinCEN Regulatory Filing ──
        us_fincen = Template(
            template_id="us_fincen.regulatory_filing",
            name="FinCEN BSA / AML Filing (US)",
            template_type=TemplateType.REGULATORY_FILING,
            jurisdiction=Jurisdiction.US_FINCEN,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            parent_template_id="base.regulatory_filing",
            sections=[
                SectionDef("reporting_entity_cik", mandatory=True),
                SectionDef("suspicious_activity_narrative", mandatory=True, max_length_chars=12000),
                SectionDef("financial_transaction_records", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".csv", ".xlsx", ".pdf"]),
                SectionDef("compliance_officer_attestation", mandatory=True),
                SectionDef("bsa_officer_contact", mandatory=True),
            ],
            validation_rules=[
                ValidationRule("R-US-001", "FinCEN requires compliance officer attestation",
                               applies_to_jurisdictions={Jurisdiction.US_FINCEN},
                               must_have_sections=["compliance_officer_attestation"]),
                ValidationRule("R-US-002", "FinCEN SAR narrative max 12000 chars",
                               applies_to_jurisdictions={Jurisdiction.US_FINCEN}, max_pages=30),
                ValidationRule("R-US-003", "Section order must follow BSA format",
                               applies_to_jurisdictions={Jurisdiction.US_FINCEN},
                               section_order_matters=True,
                               required_section_order=["reporting_entity_cik", "suspicious_activity_narrative",
                                                       "financial_transaction_records", "compliance_officer_attestation"]),
            ],
            metadata={"regulator": "FinCEN", "form": "SAR / CTR"},
        )
        reg.register(us_fincen)

        # ── Base Legal Contract ──
        base_contract = Template(
            template_id="base.legal_contract",
            name="Base Legal Contract",
            template_type=TemplateType.LEGAL_CONTRACT,
            jurisdiction=Jurisdiction.GLOBAL,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            sections=[
                SectionDef("parties", mandatory=True),
                SectionDef("recitals", mandatory=True),
                SectionDef("definitions", mandatory=True),
                SectionDef("obligations", mandatory=True),
                SectionDef("representations_and_warranties", mandatory=True),
                SectionDef("liability_and_indemnity", mandatory=True),
                SectionDef("termination", mandatory=True),
                SectionDef("governing_law", mandatory=True),
                SectionDef("dispute_resolution", mandatory=True),
                SectionDef("signature_blocks", mandatory=True),
                SectionDef("schedules", mandatory=False, repeatable=True),
            ],
            validation_rules=[
                ValidationRule("C001", "Contract must have signature blocks", must_have_sections=["signature_blocks"]),
                ValidationRule("C002", "Contract must specify governing law", must_have_sections=["governing_law"]),
            ],
            metadata={"owner": "phalanx-legal", "category": "contract"},
        )
        reg.register(base_contract)

        # ── Compliance Checklist ──
        base_checklist = Template(
            template_id="base.compliance_checklist",
            name="Base Compliance Checklist",
            template_type=TemplateType.COMPLIANCE_CHECKLIST,
            jurisdiction=Jurisdiction.GLOBAL,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            sections=[
                SectionDef("checklist_metadata", mandatory=True),
                SectionDef("control_items", mandatory=True, repeatable=True),
                SectionDef("evidence_references", mandatory=True),
                SectionDef("self_assessment_scores", mandatory=True),
                SectionDef("gap_summary", mandatory=True),
                SectionDef("remediation_plan", mandatory=False),
            ],
            validation_rules=[
                ValidationRule("CL001", "Checklist must have at least one control item", must_have_sections=["control_items"]),
            ],
            metadata={"owner": "phalanx-compliance", "category": "checklist"},
        )
        reg.register(base_checklist)

        # ── Audit Report ──
        base_audit = Template(
            template_id="base.audit_report",
            name="Base Audit Report",
            template_type=TemplateType.AUDIT_REPORT,
            jurisdiction=Jurisdiction.GLOBAL,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            sections=[
                SectionDef("audit_scope", mandatory=True),
                SectionDef("audit_period", mandatory=True),
                SectionDef("auditor_credentials", mandatory=True),
                SectionDef("findings", mandatory=True, repeatable=True),
                SectionDef("management_response", mandatory=True),
                SectionDef("corrective_action_plan", mandatory=True),
                SectionDef("opinion", mandatory=True),
                SectionDef("distribution_list", mandatory=False),
            ],
            validation_rules=[
                ValidationRule("A001", "Audit report must have findings and opinion",
                               must_have_sections=["findings", "opinion"]),
                ValidationRule("A002", "Audit report max 200 pages", max_pages=200),
            ],
            metadata={"owner": "phalanx-audit", "category": "audit"},
        )
        reg.register(base_audit)

        # ── Certification Application ──
        base_cert = Template(
            template_id="base.certification_application",
            name="Base Certification Application",
            template_type=TemplateType.CERTIFICATION_APPLICATION,
            jurisdiction=Jurisdiction.GLOBAL,
            version=TemplateVersion(1, 0, 0, datetime.now(timezone.utc)),
            sections=[
                SectionDef("applicant_details", mandatory=True),
                SectionDef("certification_sought", mandatory=True),
                SectionDef("technical_documentation", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf", ".zip"]),
                SectionDef("test_reports", mandatory=True, requires_attachments=True,
                           allowed_attachment_types=[".pdf"]),
                SectionDef("quality_management_system", mandatory=True),
                SectionDef("previous_certifications", mandatory=False),
                SectionDef("declaration_of_conformity", mandatory=True),
            ],
            validation_rules=[
                ValidationRule("CERT001", "Cert application must include declaration of conformity",
                               must_have_sections=["declaration_of_conformity"]),
                ValidationRule("CERT002", "Cert application max 150 pages", max_pages=150),
            ],
            metadata={"owner": "phalanx-certification", "category": "certification"},
        )
        reg.register(base_cert)

        return reg


# ────────────────────────────────────────────────────────────────
# CLI / module test harness
# ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    reg = TemplateFactory.build_registry()
    renderer = TemplateRenderer(reg)
    validator = TemplateValidator(reg)

    # Example: render a US FinCEN filing
    data = {
        "executive_summary": "This SAR documents suspicious wire transfers...",
        "entity_identification": "Acme Bank NA, CIK 0001234567",
        "scope_of_filing": "Suspicious Activity Report for Q3 2025",
        "supporting_evidence": "Wire transfer logs and KYC records reviewed.",
        "supporting_evidence_attachments": ["wires_Q3.csv", "kyc_review.pdf"],
        "risk_assessment": "High risk due to rapid movement of funds.",
        "compliance_statement": "This filing is made in good faith.",
        "reporting_entity_cik": "0001234567",
        "suspicious_activity_narrative": "Subject transferred $4.2M across 12 jurisdictions...",
        "financial_transaction_records": "See attached CSV.",
        "compliance_officer_attestation": "I, Jane Doe, attest to the accuracy.",
        "bsa_officer_contact": "Jane Doe, jane.doe@acmebank.com, +1-555-0100",
    }

    md = renderer.render("us_fincen.regulatory_filing", data, meta={"submitted_by": "Agent-7", "case_id": "SAR-2025-0042"})
    print(md)

    result = validator.validate("us_fincen.regulatory_filing", data, md)
    print("\n--- Validation ---")
    print(json.dumps(result.__dict__, default=str, indent=2))
