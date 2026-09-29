---
name: poweroffice-admin-suite
description: "PowerOffice Go browser and voice task routing across finance, people, reports and administration. Use for mixed or unclear scope; choose specialists directly otherwise."
---

# PowerOffice Admin Suite

Reuse established context for related spoken or typed commands. Read the [Chrome contract](references/browser-operation-contract.md) if absent, then only the owning skill and needed reference section. Clear single-domain requests may start directly with that specialist.

| Requested work | Owner |
| --- | --- |
| Company settings, subscriptions, defaults, dimensions | [Company](../poweroffice-company-admin/SKILL.md) |
| Users, invitations, roles, access removal | [Access](../poweroffice-access-admin/SKILL.md) |
| Complete onboarding, changes, offboarding | [Employee lifecycle](../poweroffice-employee-lifecycle/SKILL.md) |
| Customers/products, orders, invoices, credits, reminders | [Sales](../poweroffice-sales-invoicing/SKILL.md) |
| Suppliers, incoming documents, coding, approvals | [Purchases](../poweroffice-purchases-approvals/SKILL.md) |
| Bank accounts, payments, approvers, reconciliation | [Bank](../poweroffice-bank-payments/SKILL.md) |
| Vouchers, ledger, VAT, locks, close | [Accounting](../poweroffice-accounting-vat-close/SKILL.md) |
| Payroll data, runs, payslips, A-melding | [Payroll](../poweroffice-payroll-admin/SKILL.md) |
| Time, absence, expenses/travel, projects | [Time/projects](../poweroffice-time-expenses-projects/SKILL.md) |
| Company/customer reports, exports/email, audit | [Reporting](../poweroffice-reporting-audit/SKILL.md) |
| Integration/API activation, imports, sync | [Integrations](../poweroffice-integrations-admin/SKILL.md) |
| Discover/create/compare/validate company profiles | [Catalog](../poweroffice-company-catalog/SKILL.md) |
| Partner workspace, template roles, multi-client access | [Partner](../poweroffice-partner-admin/SKILL.md) |

Choose one owner; lifecycle covers its cross-domain steps. Load another only for an independent operation the owner does not cover. Ordinary report export/email stays with reporting.

For a request such as “ta ut ein åpen post liste på leverandører og sende det til meg på epost”, route to Reporting, open the supplier open-items report, and send from that report with `Share/Del → Email/E-post`. Do not download the report merely to email it.

A catalog is optional: use the supplied path or `.poweroffice/company-catalog.yaml` only for needed company/profile fields, verify references live, and never infer authorization. For voice, finish with company, action/report, period/target, recipient if relevant, verified state and any blocker/human step. Keep detailed evidence for requested written summaries.
