# AI context map

Use this map to load the smallest sufficient context.

| Task | Start here | Load next only when needed |
|---|---|---|
| Natural-language/voice routing or explicit `$poweroffice-admin-suite` request | `skills/poweroffice-admin-suite/SKILL.md` | Exactly one owning skill; lifecycle may span related domains |
| Company setup and subscriptions | `skills/poweroffice-company-admin/SKILL.md` | `references/company-settings.md` |
| Users, invitations, roles, permissions | `skills/poweroffice-access-admin/SKILL.md` | `references/access-operations.md` |
| Employee onboarding, transfer, offboarding | `skills/poweroffice-employee-lifecycle/SKILL.md` | Browser contract and one lifecycle reference |
| Customers, products, invoices, credit notes | `skills/poweroffice-sales-invoicing/SKILL.md` | `references/invoicing-operations.md` |
| Suppliers, incoming invoices, approvals | `skills/poweroffice-purchases-approvals/SKILL.md` | `references/purchase-approval.md` |
| Bank accounts, payments, reconciliation | `skills/poweroffice-bank-payments/SKILL.md` | `references/banking-operations.md` |
| Vouchers, ledger, VAT, period close | `skills/poweroffice-accounting-vat-close/SKILL.md` | `references/accounting-vat-close.md` |
| Payroll run or reporting | `skills/poweroffice-payroll-admin/SKILL.md` | `references/payroll-operations.md` |
| Time, expenses, travel, projects | `skills/poweroffice-time-expenses-projects/SKILL.md` | `references/time-expense-project.md` |
| Reports, export and authorized Outlook web email on Windows/macOS | `skills/poweroffice-reporting-audit/SKILL.md` | `references/report-delivery.md`; audit reference only for investigation |
| Integrations, API, import/export | `skills/poweroffice-integrations-admin/SKILL.md` | `references/integrations.md` |
| Company profile discovery/catalog | `skills/poweroffice-company-catalog/SKILL.md` | Schema, example, validator |
| Partner portal and multi-client roles | `skills/poweroffice-partner-admin/SKILL.md` | `references/partner-operations.md` |

Do not load the complete `skills/` tree for a domain change. Route directly to a clear specialist, then read only the reference required for the operation. Reuse `skills/poweroffice-admin-suite/references/browser-operation-contract.md` once per active context; the complete suite must remain installed for shared links to resolve.

Before publishing, run `python3 scripts/check_package.py` for package metadata, local links, automatic invocation, description length (220 characters), and the 700-line active-file ceiling. Scenario fixtures in `tests/` guide semantic review; they do not prove live browser behavior.
