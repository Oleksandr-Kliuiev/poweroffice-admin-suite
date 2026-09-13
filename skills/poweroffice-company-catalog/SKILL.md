---
name: poweroffice-company-catalog
description: Discover, create, compare, validate, and maintain a private PowerOffice Go company catalog containing verified company identities, approved access profiles, dimensions, approval chains, invoice and payroll defaults, protected users, integrations, and workflow conventions. Use to prepare reusable company-specific profiles; never treat the catalog as authorization.
---

# PowerOffice Company Catalog

Build a private intended-state catalog from administrator input and read-only PowerOffice Go discovery. The catalog accelerates other PowerOffice skills but never replaces live verification, accounting judgment, or task authorization.

## Location and privacy

Use a user-provided path or `.poweroffice/company-catalog.yaml` in the current working directory. Create the parent directory only when the user asks to create a catalog.

Never store passwords, BankID data, MFA secrets, API/application/client/subscription keys, tokens, certificates, national identity numbers, personal bank accounts, tax cards, salary amounts, payslip data, complete customer/supplier exports, or session material. Bank-account references must be aliases with masked last digits only.

Read [references/catalog-schema.md](references/catalog-schema.md) before creating or materially changing a catalog. Use [assets/company-catalog.example.yaml](assets/company-catalog.example.yaml) as the structural template.

## Discovery workflow

1. Confirm the authenticated PowerOffice user, workspace, active company, legal name, and organization number.
2. Inventory subscriptions, roles, departments, projects/activities, approval chains, invoice defaults, accounting periods/defaults, payroll calendar defaults, integrations, and protected responsibilities using read-only views.
3. Distinguish `observed` values from administrator-approved `intended` values. Ask for a decision only where the difference materially changes future work.
4. For each access or lifecycle profile, compare multiple representative users when available; record the common approved pattern, not one person's accidental privileges or sensitive data.
5. Record stable codes and masked aliases alongside human-readable names.
6. Add protected users, clients, roles, accounts, and workflows that automation must not modify without exact authorization.
7. Save the private catalog and run `scripts/validate_catalog.py` when Python and PyYAML are available.

Preserve administrator-authored comments and unknown forward-compatible keys when practical. Finish with companies/profiles added or changed, unresolved differences, unverified references, privacy exclusions, and validation results. Do not mutate the live company during catalog discovery unless separately requested.
