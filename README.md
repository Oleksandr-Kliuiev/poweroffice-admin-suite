# PowerOffice Admin Suite

This Codex plugin provides focused skills for supervised PowerOffice Go administration through an already authenticated browser session. It is designed for real company work: exact company and object resolution, complete-list handling, idempotent changes, financial state awareness, and independent after-state verification.

## Included skills

- `poweroffice-admin-suite`: explicit unified entrypoint and dispatcher.
- `poweroffice-company-admin`: company settings, subscriptions, dimensions, and defaults.
- `poweroffice-access-admin`: users, invitations, roles, and permissions.
- `poweroffice-employee-lifecycle`: onboarding, transfer, and offboarding.
- `poweroffice-sales-invoicing`: customers, products, invoices, and credit notes.
- `poweroffice-purchases-approvals`: suppliers, incoming invoices, and approval flows.
- `poweroffice-bank-payments`: bank settings, payments, authorization, and reconciliation.
- `poweroffice-accounting-vat-close`: vouchers, ledger, VAT, and period close.
- `poweroffice-payroll-admin`: employee payroll data, payroll runs, and statutory reporting.
- `poweroffice-time-expenses-projects`: time, travel, expenses, and projects.
- `poweroffice-reporting-audit`: read-only reporting, discrepancy review, and evidence export.
- `poweroffice-integrations-admin`: integrations, PowerOffice API, and data exchange.
- `poweroffice-company-catalog`: private reusable company profiles.
- `poweroffice-partner-admin`: accounting-partner and multi-client administration.

Codex can select a focused skill from an ordinary request that clearly mentions PowerOffice Go. Use the stable suite entrypoint for explicit routing:

```text
$poweroffice-admin-suite conduct a complete onboarding for a new employee in PowerOffice Go
```

## Company catalog

Copy `skills/poweroffice-company-catalog/assets/company-catalog.example.yaml` to `.poweroffice/company-catalog.yaml` in the administrator's working directory, then adapt it to the live company. Keep the real catalog private. It contains intended settings and aliases, never credentials, full bank details, identity numbers, or salary data.

Without a catalog, the selected skill discovers current state in the authenticated browser and asks only for decisions that materially change the result.

## Operating model

The administrator signs in to PowerOffice Go, selects the intended company, and gives Codex the task. The skills execute routine authorized work and verify persisted state. They stop at a review checkpoint before sending, posting, paying, filing statutory reports, approving payroll, locking periods, or publishing broad multi-client access changes. MFA, BankID, electronic signatures, and other personal authentication remain human steps.
