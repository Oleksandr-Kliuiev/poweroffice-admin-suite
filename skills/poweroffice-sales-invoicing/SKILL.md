---
name: poweroffice-sales-invoicing
description: Administer PowerOffice Go sales and invoicing through an authenticated browser, including customers, contacts, products, orders, invoice drafts, recurring invoices, sending, reminders, and full or partial credit notes. Use for accounts-receivable and customer-billing requests, not supplier invoices or bank authorization.
---

# PowerOffice Sales and Invoicing

Verify the active company and organization number, then resolve customers by customer number and organization number, products by product number, and invoices by invoice number. Search existing drafts and recurring orders before creating anything.

Read [references/invoicing-operations.md](references/invoicing-operations.md) for invoice states, validation, sending, crediting, duplicate prevention, pagination, and verification.

Creating or editing a draft is reversible. Sending an invoice or credit note generates, posts, and externally delivers an accounting document; treat Send and bulk generation as critical commits. Immediately before committing, summarize customer, delivery method, invoice date, due terms, currency, line totals, VAT, total, project/department, attachments, and affected draft count.

Do not infer VAT exemption, alternate revenue account, delivery method, bank/OCR setup, or customer email. Use the company catalog only as intended defaults and verify them live.

Finish with exact customer and document numbers, draft/confirmed/sent state, totals without unnecessary personal data, delivery result, posting state, outstanding warnings, and any human approval required.
