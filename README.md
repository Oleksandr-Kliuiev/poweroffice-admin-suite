# PowerOffice Admin Suite

This Codex plugin provides focused skills for supervised PowerOffice Go administration through an already authenticated Chrome session. It is designed for real company work: exact company and object resolution, complete-list handling, idempotent changes, financial state awareness, and independent after-state verification.

## Included skills

- `poweroffice-admin-suite`: natural-language and voice task routing.
- `poweroffice-company-admin`: company settings, subscriptions, dimensions, and defaults.
- `poweroffice-access-admin`: users, invitations, roles, and permissions.
- `poweroffice-employee-lifecycle`: onboarding, transfer, and offboarding.
- `poweroffice-sales-invoicing`: customers, products, invoices, and credit notes.
- `poweroffice-purchases-approvals`: suppliers, incoming invoices, and approval flows.
- `poweroffice-bank-payments`: bank settings, payments, authorization, and reconciliation.
- `poweroffice-accounting-vat-close`: vouchers, ledger, VAT, and period close.
- `poweroffice-payroll-admin`: employee payroll data, payroll runs, and statutory reporting.
- `poweroffice-time-expenses-projects`: time, travel, expenses, and projects.
- `poweroffice-reporting-audit`: reporting, discrepancy review, export, and explicitly authorized report email through PowerOffice Share → Email.
- `poweroffice-integrations-admin`: integrations, PowerOffice API, and data exchange.
- `poweroffice-company-catalog`: private reusable company profiles.
- `poweroffice-partner-admin`: accounting-partner and multi-client administration.

Codex can select a focused skill from an ordinary spoken or written request that mentions PowerOffice Go. No skill name is required; the suite routes requests when needed. Explicit invocation remains available:

```text
$poweroffice-admin-suite conduct a complete onboarding for a new employee in PowerOffice Go
```

Install the complete `skills/` bundle together. Each task reads only its owning skill, needed workflow and shared Chrome contract; it does not load all 14 skills. Keep the authenticated browser session and verified task context across related voice commands. Skills do not provide a voice interface themselves; the host must support voice and browser tools.

## Company catalog

Copy `skills/poweroffice-company-catalog/assets/company-catalog.example.yaml` to `.poweroffice/company-catalog.yaml` in the administrator's working directory, then adapt it to the live company. Keep the real catalog private. It contains intended settings and aliases, never credentials, full bank details, identity numbers, or salary data.

Without a catalog, the selected skill discovers current state in the authenticated browser and asks only for decisions that materially change the result.

## Operating model

The administrator signs in to PowerOffice Go in Chrome, selects the intended company, and gives Codex the task. The skills reuse that session, execute authorized work, and verify persisted state. For an explicitly requested report email, they open the scoped report and use its own **Share/Del → Email/E-post** action. They verify the exact company/customer, report, period and full recipient, send once, and inspect PowerOffice's acknowledgement or available sharing history without repeating an already resolved approval. Submission is not proof of inbox delivery. Uncertain sends require checking state before any retry.

The same workflow serves Windows and macOS users in PowerOffice. It requires no downloaded file or separate mail service for ordinary report email. The native email dialog was observed in a live browser check; a completed send has not been validated end to end.

Invoice sending/posting, payments, statutory filing, payroll approval, period locks, destructive changes and broad multi-client access retain their exact critical review checkpoints unless already explicitly confirmed. MFA, BankID, electronic signatures, and other personal authentication remain human steps.
