# Accounting, VAT, and close operations

## Voucher and journal preparation

1. Verify company, period, source document, currency, transaction date, and whether the period is locked.
2. Search by voucher number, external reference, amount, date, and counterparty to prevent duplicates.
3. Resolve accounts and dimensions by exact code; inspect active dates and VAT configuration.
4. Enter lines and verify total debit equals total credit in transaction currency and base currency where shown.
5. Save as unposted/draft when available and reopen independently.
6. Before posting, summarize all lines, totals, VAT effect, dimensions, source attachment, and period.

Correct posted entries through the supported correction or reversal workflow so the audit trail remains intact. Never overwrite source evidence or delete history to hide an error.

## VAT reconciliation and filing

PowerOffice commonly exposes VAT reconciliation under `Menu > Reports/Rapporter > VAT reconciliation/Mva-avstemming`.

1. Select the exact year and VAT period.
2. Review the summary, output VAT, input VAT, unposted documents, unusual VAT codes, and prior-period balances.
3. Drill into every discrepancy and classify it as corrected, explained, or unresolved.
4. Re-run the reconciliation after corrections.
5. Before approving or submitting, present period totals, discrepancies, unposted documents, attachments/comments, and expected payable/refundable amount.
6. After submission, verify status, receipt/acknowledgement, posted VAT settlement entries, and resulting lock date where applicable.

Do not submit while unexplained discrepancies or unposted in-period documents remain unless the responsible accountant explicitly accepts them.

## Period close and lock date

Confirm all expected bank, customer, supplier, payroll, VAT, accrual, depreciation, and reconciliation work is complete. Changing the lock date is a critical commit. Verify the new date, affected users, reason/history field, and correction procedure before saving. Never move the lock date backward without exact authorization and documented purpose.

## Complete-list handling

Clear date and status filters, include posted and unposted states as relevant, and traverse all pages or virtual rows. Track stable voucher numbers or report row keys. A zero-result current-period view does not prove historical absence.

## Official references

- [Perform VAT reconciliation](https://hjelpesenter.poweroffice.no/utfoer-mva-avstemming-i-poweroffice-go-steg-for-steg)
- [VAT specification](https://hjelpesenter.poweroffice.no/mva-spesifikasjon)
- [Lock dates and accounting periods](https://hjelpesenter.poweroffice.no/laasedato-regnskapsperioder)
