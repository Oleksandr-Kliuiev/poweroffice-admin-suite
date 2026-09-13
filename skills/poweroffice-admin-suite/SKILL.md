---
name: poweroffice-admin-suite
description: Unified entrypoint for the PowerOffice Admin Suite. Use only when the user explicitly names poweroffice-admin-suite, with or without the $ prefix, to route and execute PowerOffice Go administration across company settings, access, employee lifecycle, sales, purchases, banking, accounting, VAT, payroll, projects, reporting, integrations, or partner clients.
---

# PowerOffice Admin Suite

Own the user's explicit `$poweroffice-admin-suite` request. Select the smallest applicable suite skill, read it completely, and carry out the work with the available browser tools. Do not stop after naming the route.

## Route the request

- Company identity, subscriptions, numbering, defaults, dimensions, or general configuration: read [poweroffice-company-admin](../poweroffice-company-admin/SKILL.md).
- Users, invitations, roles, permissions, or access removal: read [poweroffice-access-admin](../poweroffice-access-admin/SKILL.md).
- Complete employee onboarding, transfer, or offboarding: read [poweroffice-employee-lifecycle](../poweroffice-employee-lifecycle/SKILL.md).
- Customers, products, orders, invoices, credit notes, reminders, or recurring billing: read [poweroffice-sales-invoicing](../poweroffice-sales-invoicing/SKILL.md).
- Suppliers, incoming documents, supplier invoices, coding, or approval flows: read [poweroffice-purchases-approvals](../poweroffice-purchases-approvals/SKILL.md).
- Bank accounts, remittance, payment authorization, payment status, or bank reconciliation: read [poweroffice-bank-payments](../poweroffice-bank-payments/SKILL.md).
- Vouchers, journal entries, ledger, VAT, corrections, lock dates, or period close: read [poweroffice-accounting-vat-close](../poweroffice-accounting-vat-close/SKILL.md).
- Payroll setup, payroll runs, payslips, employment reporting, or A-melding: read [poweroffice-payroll-admin](../poweroffice-payroll-admin/SKILL.md).
- Timesheets, travel, expenses, absence, activities, or projects: read [poweroffice-time-expenses-projects](../poweroffice-time-expenses-projects/SKILL.md).
- Read-only reports, discrepancy investigation, audit evidence, or exports: read [poweroffice-reporting-audit](../poweroffice-reporting-audit/SKILL.md).
- Integrations, API activation, API keys, imports, or exports: read [poweroffice-integrations-admin](../poweroffice-integrations-admin/SKILL.md).
- Company-profile discovery, creation, comparison, or validation: read [poweroffice-company-catalog](../poweroffice-company-catalog/SKILL.md).
- Accounting-partner workspace, client portfolio, template roles, or multi-client access: read [poweroffice-partner-admin](../poweroffice-partner-admin/SKILL.md).

Choose one owner whenever possible. `poweroffice-employee-lifecycle` owns cross-domain onboarding and offboarding; do not load every related skill by default. Read a second skill only for a genuine independent operation not covered by the owner.

## Production and critical commits

Treat the selected company as production unless the user explicitly identifies a demo client. Before mutation, verify the visible company and organization number, exact object, current state, and intended period.

A draft may be created or edited when authorized. Immediately before a critical commit, present the exact company, object or batch, amount and currency when applicable, accounting or payroll period, effective date, and irreversible/external effects; obtain explicit confirmation unless that exact commit was separately confirmed in the current interaction. Critical commits include sending or posting invoices, authorizing payments, approving payroll, submitting statutory reports, locking periods, destructive corrections, and publishing access changes across clients.

MFA, BankID, electronic signatures, and personal authentication remain human steps. Never request, capture, or store their secrets.

## Company catalog and completion

Use `.poweroffice/company-catalog.yaml` when present or when the user supplies a path. Read only the selected company and relevant profile. The catalog is intended state, not authorization; verify every referenced object in the live company.

Finish with the selected route, company and organization number, exact targets, before/after state, drafts prepared, critical commits completed or awaiting confirmation, already-correct items, rejected or blocked items, and required human steps. A toast or button click alone is not proof of completion.
