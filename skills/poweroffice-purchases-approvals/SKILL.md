---
name: poweroffice-purchases-approvals
description: Administer PowerOffice Go purchasing and document approval through an authenticated browser, including suppliers, incoming documents, supplier invoices and credit notes, coding, duplicate review, approval routing, approvers, and amount limits. Use before payment authorization; do not use to release money from a bank account.
---

# PowerOffice Purchases and Approvals

Verify company and organization number. Resolve suppliers by supplier number plus organization number, invoices by supplier invoice number/reference, and approvers by exact user identity.

Read [references/purchase-approval.md](references/purchase-approval.md) for duplicate controls, document states, coding, approval limits, queue handling, and verification.

Separate document capture, accounting coding, approval for posting, posting, and payment readiness. Never mark an invoice paid merely because it is approved or posted. Do not bypass configured approval levels, split a document to evade a limit, replace an approver without authorization, or change bank details based only on the invoice document.

Posting or final approval that creates an accounting liability is a critical commit. Final bank authorization belongs to `poweroffice-bank-payments` and requires a separate review.

Finish with supplier and document identifiers, duplicate-check evidence, gross/VAT/net totals, coding and dimensions, approval route and status, posting state, payment readiness, and exceptions.
