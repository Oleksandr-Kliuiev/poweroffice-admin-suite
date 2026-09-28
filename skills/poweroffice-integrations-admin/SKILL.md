---
name: poweroffice-integrations-admin
description: "PowerOffice Go integration activation, API access, imports, exports and sync troubleshooting. Use for integration work; ordinary report delivery belongs to reporting."
---

# PowerOffice Integrations Admin

Read the [Chrome contract](../poweroffice-admin-suite/references/browser-operation-contract.md) if absent from working context; retain it across related commands. Load only the relevant workflow section below, including its prerequisites and verification.

Use [integration operations](references/integrations.md): **Environments and credentials**, then **Browser activation or access change**, **Imports**, or **API writes and idempotency** as relevant. Verify company, registered integration/publisher, environment, scope and current activation; separate demo and production.

Keep credentials in an approved secret store; never expose keys/tokens in prompts, reports, tool output, shell history, catalogs or repositories. Activation, scope expansion, destructive imports and production writes require exact authorization. Before bulk execution, verify mapping, representative preview, date/currency formats, duplicates/idempotency, error handling and rollback.

Report masked identifiers, scopes, accepted/rejected/skipped/duplicate counts, sync state and needed rotation/human steps.
