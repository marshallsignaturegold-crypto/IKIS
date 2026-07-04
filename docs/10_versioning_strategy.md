# 10 — Versioning Strategy

> **Versioning and release approach for IKIS.**

---

## 1. Semantic Versioning

IKIS uses semantic versioning: `MAJOR.MINOR.PATCH`

| Component | When to Increment |
|-----------|------------------|
| MAJOR | Breaking changes to schemas, governance, or structure |
| MINOR | New features, artifact types, or significant additions |
| PATCH | Bug fixes, corrections, minor updates |

## 2. Current Version

**Version: 1.0.0**

Initial release with complete repository structure, documentation, schemas, templates, governance, automation, and SSS domain artifacts.

## 3. Release Process

1. Update version in `.ikisrc`
2. Update `CHANGELOG.md`
3. Tag release in Git

## 4. Artifact Versioning

Individual artifacts are versioned via:
- Git history (temporal)
- `superseded_by` metadata (semantic)
- `related_artifacts` links (relationship)

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-010*  
*Owner: marshallwmorrison*
