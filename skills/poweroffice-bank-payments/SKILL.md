---
name: poweroffice-bank-payments
description: "PowerOffice Go bank accounts, payment preparation and authorization, approvers, payment status and reconciliation. Use for banking and cash movement."
---

# PowerOffice Bank and Payments

Read the [Chrome contract](../poweroffice-admin-suite/references/browser-operation-contract.md) if absent from working context; retain it across related commands. Load only the relevant workflow section below, including its prerequisites and verification.

Use [banking operations](references/banking-operations.md): **Review and authorize**, **Approver setup**, or **Credits and reconciliation**, with **Payment-state discipline**.

Treat bank work as production. Resolve payments by payee, document/reference, account alias/masked digits, amount, currency and payment date; never by row position. Before release, include batch count, totals per account/currency, earliest/latest date, changed bank details, credits, duplicates and exceptions in the critical checkpoint.

Check payment history and bank status before any uncertain retry. Report each requested prepared/authorized/transmitted/rejected/settled state accurately; BankID/MFA/signatures remain human steps.
