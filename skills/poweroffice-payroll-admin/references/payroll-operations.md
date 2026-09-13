# Payroll operations

## Prepare a payroll run

1. Verify company, period, payment date, run type, payroll subscription, and integrations.
2. Search existing draft and approved runs for the same period/type/date before creating.
3. Inspect active employment relationships and the employment report; resolve unexpected active, ended, or missing employees.
4. Select intended inputs: fixed lines, travel claims, time through date, imported payroll bases, and exact employee inclusion/exclusion.
5. Reconcile warnings and aggregate gross, taxable benefits, deductions, tax, employer cost, and net payment.
6. Compare with the prior comparable run and investigate material variances rather than assuming they are correct.
7. Save the unapproved run and reopen it independently.

Do not expose employee-level sensitive amounts unless the task specifically requires authorized investigation. Prefer aggregate evidence and identifiers.

## Critical commit: approve

Approval can send A-melding, post accounting entries, prepare salary/tax payments, and generate payslips. Present the period, type, payment date, employee count, aggregate totals, excluded employees, warnings, and all side effects immediately before approval. Obtain explicit confirmation unless that exact approval was separately confirmed.

After approval, verify each independent state: run approved, A-melding sent, acknowledgement received or pending, posting created, payslips generated/delivery scheduled, and payments awaiting authorization. Do not report salaries as paid until bank status confirms settlement.

## Corrections and no-pay reporting

Never edit an approved historical run as if it were a draft. Use the supported correction workflow and identify which prior report/posting is affected. A no-pay A-melding still reports employment relationships and is a statutory submission requiring the same critical checkpoint.

## Complete-list handling and recovery

Clear year, status, and run-type filters. Traverse pages or virtual rows using period/run identifiers. Before retrying approval or submission after a timeout, inspect run state, A-melding history, posting, and payment queues to prevent duplicate reporting.

## Official references

- [Payroll runs in PowerOffice Go](https://hjelpesenter.poweroffice.no/loennskjoering)
- [Submit A-melding without paid salary](https://hjelpesenter.poweroffice.no/sende-a-melding-uten-loenn)
- [Get started with payroll](https://hjelpesenter.poweroffice.no/kom-i-gang-poweroffice-go-loenn)
