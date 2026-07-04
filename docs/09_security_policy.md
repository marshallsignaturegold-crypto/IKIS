# 09 — Security Policy

> **Security and access policy for IKIS.**

---

## 1. Access Control

### Repository Access

| Role | Permissions |
|------|-------------|
| Owner | Full control |
| Maintainer | Write + admin |
| Contributor | Write |
| Reader | Read |

### Classification-Based Access

| Classification | Access Level |
|---------------|-------------|
| public | Anyone |
| internal | Contributors and above |
| confidential | Maintainers and above |
| restricted | Named individuals only |

## 2. Content Security

Do NOT commit:
- Passwords or credentials
- Private keys
- Personal information (PII)
- Unpublished financial data
- Active negotiation details

## 3. Incident Response

If sensitive information is committed:
1. Remove immediately
2. Notify SSS leadership
3. Rotate any exposed credentials

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-009*  
*Owner: marshallwmorrison*
