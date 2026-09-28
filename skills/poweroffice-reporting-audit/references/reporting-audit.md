# Reporting and audit operations

## Scope the evidence

Record company/legal entity, organization number, report name, period, as-of timestamp, posted/draft basis, currency, comparison period, dimensions, status filters, and user-visible timezone. Verify parameters in the generated report; reopen settings only when the report does not expose them or they appear inconsistent.

## Reconcile and drill down

- Ledger: reconcile account opening, movements, and closing; drill to voucher and source attachment.
- Receivables/payables: reconcile control totals to customer/supplier ledger and payment status.
- VAT: compare ledger VAT accounts, VAT codes, VAT specification, reconciliation warnings, and submitted return.
- Payroll: use aggregate totals and run/report identifiers; minimize employee-level disclosure.
- Bank: compare PowerOffice book/bank view with available bank statement evidence; do not infer settlement from approval.
- Time/projects: record whether unapproved or unbilled time is included; drill from project totals to transactions.

Classify each discrepancy as timing, filter/basis mismatch, missing/unposted item, duplicate, mapping/coding issue, external-state mismatch, or unresolved.

## Complete lists and exports

Preserve requested filters and remove conflicting stale filters. Prefer a verified all-results report/export instead of scanning every page. When the UI is the only complete source, use stable sorting, traverse every page or virtual row, and track first/last stable identifiers and result counts. For Excel/CSV/PDF, verify date range, row count when applicable, total, and file name; CSV/Excel may include columns hidden in the report view. Store sensitive exports only in the user-approved private location.

## Evidence quality

A screenshot proves what was visible, not completeness. Pair it with report parameters, counts/totals, stable source identifiers, and drilldown evidence. State when a result is sampled rather than exhaustive.

Official references: [VAT specification](https://hjelpesenter.poweroffice.no/mva-spesifikasjon) and [PowerOffice project reports](https://hjelpesenter.poweroffice.no/prosjektrapport-oversikt).
