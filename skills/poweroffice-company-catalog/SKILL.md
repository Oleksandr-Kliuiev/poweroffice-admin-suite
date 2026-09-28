---
name: poweroffice-company-catalog
description: "PowerOffice Go private company catalogs and approved profiles: discover, create, compare or validate selected settings. Catalogs never authorize live changes."
---

# PowerOffice Company Catalog

For browser discovery, read the [Chrome contract](../poweroffice-admin-suite/references/browser-operation-contract.md) only if absent from working context. Local catalog comparison/validation needs no browser session.

Use the supplied path or `.poweroffice/company-catalog.yaml`. Read only the requested company/profile/fields; create or rebuild a catalog only when requested. Intended state never replaces live verification, accounting judgment or authorization.

For creation/material changes, read [catalog schema](references/catalog-schema.md) and use the [synthetic example](assets/company-catalog.example.yaml). Preserve comments and unknown compatible keys when practical; run `scripts/validate_catalog.py` if Python/PyYAML are available.

Discover only requested scope read-only after verifying administrator/workspace/company. Depending on scope, inspect subscriptions, roles, dimensions/projects/activities, approval chains, invoice/accounting/payroll defaults, integrations or protected responsibilities. Mark observed versus approved intended values; resolve material differences. For access/lifecycle profiles, compare representative users where available rather than copying accidental privileges. Record stable codes, approved patterns, protected objects/workflows and masked bank aliases.

Keep the catalog private. Never store credentials/keys/tokens/certificates, BankID/MFA/session data, identity numbers, personal banking/tax/salary/payslip data or complete customer/supplier exports; company bank references use aliases/last digits only.

Report changed companies/profiles, unresolved differences, unverified references and validation results. Catalog discovery does not authorize live mutation.
