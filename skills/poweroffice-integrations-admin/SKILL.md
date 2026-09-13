---
name: poweroffice-integrations-admin
description: Administer PowerOffice Go integrations and data exchange, including integration activation, API client access, PowerOffice API environment selection, import/export preparation, mapping validation, and integration troubleshooting. Use for integration-focused requests; do not store or expose credentials and do not substitute API use for an unauthorized browser mutation.
---

# PowerOffice Integrations Admin

Verify company, organization number, integration name, environment, requested scope, and current activation. Keep demo and production credentials, endpoints, and client contexts strictly separated.

Read [references/integrations.md](references/integrations.md) for browser activation, API authentication boundaries, imports, exports, duplicate prevention, secret handling, and verification.

Never write application keys, client keys, subscription keys, access tokens, certificates, or passwords to a skill, catalog, prompt, report, shell history, or source repository. Use an approved secret store and masked identifiers. Do not display tool output that could contain tokens.

Integration activation, scope expansion, destructive import, and production writes require exact authorization. For bulk data exchange, validate a representative preview, field mapping, company identity, date/currency formats, idempotency key or duplicate strategy, error handling, and rollback before execution.

Finish with company, integration and environment, masked key identifiers only, authorized scopes, records accepted/rejected, duplicate handling, resulting sync state, and rotation or human steps. Never report a token value.
