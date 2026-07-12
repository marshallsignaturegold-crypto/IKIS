# Contradiction Register

**Generated:** Template — will be auto-populated by `automation/contradiction_detector.py`  
**Last run:** Not yet executed  
**Status:** Pending first CI run

---

This register tracks all factual contradictions detected across the knowledge base by the automated contradiction detection system.

## How Contradictions Are Detected

The `contradiction_detector.py` script scans all knowledge base files for factual assertions in the following categories:
- Revenue / financial figures
- Capital stack amounts
- IRR percentages
- MOIC multiples
- EBITDA figures
- Engagement status claims
- Entity registration status
- Personnel roles

When two files assert different values for the same fact type, a contradiction is flagged with severity classification:
- **CRITICAL**: Revenue, capital stack, or IRR discrepancies
- **WARNING**: Status, engagement, or personnel role discrepancies
- **INFO**: Minor inconsistencies or edge cases

## Resolution Workflow

1. Contradiction detected by CI scan
2. GitHub Issue auto-created with full register
3. Knowledge owner reviews and validates correct value
4. Incorrect file(s) updated with corrected assertion
5. Re-run CI scan to confirm resolution
6. Issue closed with resolution note

## Register History

| Date | Total | Critical | Warning | Info | Status |
|------|-------|----------|---------|------|--------|
| — | — | — | — | — | Pending first run |

---

*This file is auto-generated. Do not edit manually — changes will be overwritten on next CI run.*
