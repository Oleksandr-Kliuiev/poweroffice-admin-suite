---
name: poweroffice-company-admin
description: Administer PowerOffice Go company configuration through an authenticated browser, including company identity, subscriptions, numbering, dimensions, departments, document and invoice defaults, accounting defaults, and other company-level settings. Use for configuration-focused requests, not transaction entry or user access.
---

# PowerOffice Company Admin

Operate the exact PowerOffice Go company selected by legal name and organization number. Inspect current configuration and dependent modules before changing settings.

Read [references/company-settings.md](references/company-settings.md) for navigation, dependency checks, mutation boundaries, and verification.

Use `.poweroffice/company-catalog.yaml` when available for intended defaults. Verify the selected company and every referenced setting in the live UI; catalog values are not authorization.

Do not silently activate a paid subscription, alter historical numbering, replace bank details, change VAT registration, or modify accounting defaults that affect future postings. Explain the impact and obtain explicit authorization for those exact changes. Never infer legal or tax settings from a similarly named company.

For each completed change, report the company, setting, before value, after value, effective scope, dependencies, and any future-only behavior.
