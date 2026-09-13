# Banking operations

## Payment-state discipline

Distinguish `ready for approval`, `authorized`, `sent/transmitted`, `accepted by bank`, `rejected`, and `settled`. Do not call a payment complete until the requested observable state is verified.

PowerOffice commonly exposes pending payments under `Purchases/Kjøp > Payments/Betalinger > Waiting for approval/Venter på godkjenning`. Verify the visible route instead of depending on fixed coordinates.

## Review and authorize

1. Verify company and source bank account using alias plus masked digits.
2. Clear stale filters and select the intended status and payment-date range.
3. Resolve each item by supplier/payee, source document number, amount, currency, KID/reference, destination account mask, and payment date.
4. Check duplicates, overdue items, credits, holds, changed bank details, and unexpected currencies.
5. Reconcile batch count and totals independently from selected rows.
6. Present the critical-commit summary and obtain explicit confirmation unless separately confirmed.
7. Allow the administrator to complete BankID/password/MFA.
8. Refresh payment history and verify state per item; capture rejection reasons.

For `Pay all`, inspect the entire filtered result, all pages, and aggregate totals before invoking it.

## Approver setup

Verify that the user has the required payment role, the account has an active remittance agreement, identity verification is complete, and effective dates are correct. Adding payment authority is a privileged financial-access commit; summarize the user, account, start date, and scope before saving.

## Credits and reconciliation

Credit-note offset behavior may depend on account number and KID matching. If offset fails, investigate both documents and perform manual ledger matching only when authorized; never delete the credit or alter references to force payment.

During bank reconciliation, match amount, date, currency, reference, and counterpart. Leave ambiguous many-to-one or one-to-many matches unresolved with an explanation.

## Official references

- [Approve and pay invoices](https://hjelpesenter.poweroffice.no/betale-faktura)
- [Create payment authorization](https://hjelpesenter.poweroffice.no/betalingsgodkjenning-opprett)
- [Payments involving credit notes](https://hjelpesenter.poweroffice.no/kreditnota-betaling)
