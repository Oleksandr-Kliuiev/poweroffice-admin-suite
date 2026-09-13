# Invoicing operations

## Document states

PowerOffice Go commonly exposes invoice work under `Menu > Invoices/Fakturaer` with states such as Draft, Confirmed, Recurring, Unpaid, and Paid. Treat state changes precisely:

- Draft: editable and not issued.
- Confirmed: prepared for later or bulk generation; not necessarily sent.
- Sent/Unpaid: generated, posted, and delivered; a legal accounting document now exists.
- Paid: customer ledger matching indicates settlement.

Do not describe Confirmed as sent or a successful Send click as paid.

## Create or edit a draft

1. Verify company and search customer by customer number or organization number.
2. Search drafts, confirmed orders, recurring orders, unpaid invoices, and recent sent documents for the same reference, date, amount, and customer.
3. Resolve product by exact number; inspect revenue account, alternate account, unit, price, and VAT behavior.
4. Enter customer reference, invoice and delivery dates, payment terms, currency, project, department, lines, discounts, VAT, and attachments exactly as authorized.
5. Preview and reconcile subtotal, VAT, total, currency, delivery method, and attachment list.
6. Save as Draft or Confirmed and independently reopen it.

## Critical commit: send or bulk generate

Before Send, list customer, document type, date, due date/terms, delivery method, currency, subtotal, VAT, total, and attachment names. For bulk work, include count and aggregate amount plus outliers. Obtain explicit confirmation unless this exact commit was separately confirmed in the current interaction.

After committing, verify generated invoice/credit-note number, posted state, delivery result, and location under Unpaid or the relevant ledger. Do not resend after an uncertain response until those states are searched.

## Credit note

Resolve the original invoice and create a linked credit-note draft from it where possible. For partial credit, verify removed or adjusted lines and the net amount. Preserve the original reference. Sending the credit note is a separate critical commit.

## Complete-list handling

Clear status, date, and customer filters. Search exact number first, then customer plus amount/date/reference. Traverse pages or virtual rows to exhaustion and track stable document numbers. Include archived or paid states when investigating duplicates.

## Official references

- [Create invoices and credit notes](https://hjelpesenter.poweroffice.no/lag-faktura-kreditnota)
- [Credit an invoice](https://hjelpesenter.poweroffice.no/kreditere-faktura)
- [Set up invoicing](https://hjelpesenter.poweroffice.no/kom-i-gang-fakturering)
