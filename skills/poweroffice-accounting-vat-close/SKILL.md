---
name: poweroffice-accounting-vat-close
description: Administer PowerOffice Go accounting through an authenticated browser, including vouchers, journal entries, general ledger corrections, account and VAT coding, VAT reconciliation and reporting, lock dates, and period close. Use for bookkeeping and close requests, not payroll calculation or bank authorization.
---

# PowerOffice Accounting, VAT, and Close

Verify company and organization number, accounting period, document date, voucher number when present, account, VAT code, dimensions, currency, and debit/credit balance. Treat corrections as linked accounting events, not silent overwrites.

Read [references/accounting-vat-close.md](references/accounting-vat-close.md) for journal preparation, correction strategy, VAT reconciliation, filing, lock dates, close sequencing, and verification.

Preparing an unposted voucher or read-only reconciliation may proceed when authorized. Posting, reversing posted history, approving or submitting VAT, and changing a lock date are critical commits. Present the exact period, affected vouchers/accounts, debit/credit totals, VAT impact, reporting effect, and rollback/correction method before committing.

Do not provide tax or accounting judgment when the coding is ambiguous. Surface the evidence and require the responsible accountant's decision. Never backdate around a locked period or unlock one merely to make an edit easier.

Finish with company, period, voucher and account identifiers, balanced totals, posting state, VAT discrepancies, filed/approved state, lock date, unresolved judgments, and required accountant actions.
