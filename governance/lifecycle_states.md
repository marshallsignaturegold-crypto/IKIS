# Lifecycle States

## States

| State | Description | Terminal |
|-------|-----------|----------|
| draft | Initial creation | No |
| under_review | Under active review | No |
| revision_requested | Changes requested | No |
| validated | Reviewed and approved | No |
| deprecated | Superseded | Yes |
| archived | Retained for history | Yes |

## Transitions

| From | To | Trigger |
|------|-----|---------|
| draft | under_review | Author submits |
| under_review | validated | Reviewer approves |
| under_review | revision_requested | Reviewer requests changes |
| revision_requested | under_review | Author resubmits |
| validated | deprecated | Newer artifact supersedes |
| validated | archived | Explicit decision |
