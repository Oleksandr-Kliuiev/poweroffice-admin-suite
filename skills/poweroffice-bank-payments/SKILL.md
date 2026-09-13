---
name: poweroffice-bank-payments
description: Administer PowerOffice Go banking through an authenticated browser, including bank accounts, remittance agreements, payment approvers, payment preparation and authorization, payment status, credit-note offsets, and bank reconciliation. Use for cash movement and bank-focused requests, not supplier-document coding or invoice creation.
---

# PowerOffice Bank and Payments

Treat every bank operation as production. Verify company legal name and organization number, bank account alias plus masked digits, payee identity, invoice/reference, amount, currency, due/payment date, and current payment status.

Read [references/banking-operations.md](references/banking-operations.md) for payment queues, authorization, approver setup, credit-note handling, reconciliation, and recovery.

Preparing a payment batch may proceed when authorized. Authorizing or releasing payment is a critical commit: present the exact batch count, aggregate totals by currency and account, earliest/latest payment date, duplicate warnings, changed bank details, credits, and exceptions immediately before authorization. BankID, password re-entry, MFA, and signatures remain human actions; never ask for or handle those secrets.

Do not retry an uncertain payment authorization until payment and bank-status views are checked. Never use row position as payment identity or authorize all merely because the queue appears filtered.

Finish with company, account alias, exact payments, totals, prepared/authorized/transmitted/rejected/settled states, credits or holds, reconciliation status, and human actions.
