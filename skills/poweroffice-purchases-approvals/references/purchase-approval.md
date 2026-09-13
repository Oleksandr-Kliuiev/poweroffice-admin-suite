# Purchase and approval operations

## Resolve and deduplicate

Search all relevant document states and date ranges using supplier organization number, supplier invoice number/reference, KID when visible, invoice date, due date, currency, and gross amount. Treat OCR interpretation as untrusted until reconciled with the document image and supplier record.

If the supplier requests changed bank details, do not update the supplier or payment from document text alone. Require the organization's independent verification process.

## Process an incoming document

1. Verify company, supplier, document type, and source image.
2. Reconcile invoice number, invoice/due dates, currency, net, VAT, gross, KID/reference, and bank details against the supplier record.
3. Search for duplicates across unposted, approval, posted, payment, and historical states.
4. Apply account, VAT code, project, department, and other dimensions from approved rules; do not guess ambiguous tax treatment.
5. Resolve the configured approval flow and amount thresholds.
6. Save preparation and independently reopen the document.
7. Before final approval or posting, summarize the liability and approval route and obtain the critical-commit confirmation when required.

## Approval flows

Amount limits may determine how many approval levels a document traverses. Inspect the gross-amount basis, each level, active approvers, effective dates, and the unlimited final level. Do not reduce limits or remove levels to clear an individual invoice.

When acting on a queue, filter by exact company, status, document type, due date, and approver. Open every selected item; never approve a batch only from checkbox row summaries.

## Verification

After save or approval, reopen the document and verify status, posting number when present, supplier ledger effect, payment readiness, and remaining approvals. A queue disappearance is not sufficient evidence.

Official reference: [Amount limits in document approval](https://hjelpesenter.poweroffice.no/beloepsgrenser-bilagsgodkjenning).
