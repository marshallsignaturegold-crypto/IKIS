# 12 — AI Context Protocols

> **How AI agents consume, produce, and interact with IKIS content.**

---

## 1. Context Loading Protocol

### Pre-Task Context Stack

AI agents should load context in this order:

```
1. AI_OPERATING_MANUAL.md (always)
2. sss-domain/00_sss_entity_index.md (for SSS tasks)
3. Relevant pillar files
4. Relevant portfolio entity profiles
5. Task-specific context injection files
6. Relevant templates
```

## 2. Content Production Protocol

All AI-produced content must:
- Include complete metadata block
- Follow appropriate template
- Apply legal gating rules (SSS materials)
- Tag confidence levels
- Cross-reference related artifacts

## 3. Context Injection Files

| File | Size | Load For |
|------|------|----------|
| `ai-agents/context_injection/sss_domain_context.md` | Medium | All SSS tasks |
| `ai-agents/context_injection/legal_gating_context.md` | Small | SSS-facing documents |
| `ai-agents/context_injection/visual_system_context.md` | Small | Document production |

## 4. Prompt Library

Reusable prompts in `ai-agents/prompt_library/`:

| File | Use Case |
|------|----------|
| `research_prompts.md` | Research tasks |
| `analysis_prompts.md` | Analysis tasks |
| `document_generation_prompts.md` | Document production |
| `validation_prompts.md` | Validation tasks |

---

*Last updated: 2026-07-05*  
*Artifact ID: IKIS-DOC-2026-012*  
*Owner: marshallwmorrison*
