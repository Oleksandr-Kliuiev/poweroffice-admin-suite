# Time, expense, travel, and project operations

## Timesheets and absence

Resolve employee, week/date, customer, project/subproject, activity, department, hour type, billable flag, quantity, and comments. Search existing transactions for the same date and dimensions before adding. Internal activity, vacation, and absence commonly have no customer; do not force a customer or project.

Before submission or approval, reconcile expected normal hours, totals by day, billable/non-billable classification, absence, and duplicate entries. Verify status after refresh.

## Expenses and travel

Inspect the company's treatment before approval: reimbursement may be prepared immediately, split between direct reimbursement and payroll reporting, or handled in a payroll run. Verify employee, purpose, dates, receipts, expense type, account/VAT mapping, currency, exchange rate source, mileage/rates, approvers, and totals.

Approval with payment or payroll consequences is a critical commit. Present the treatment and aggregate effect. Never infer a missing receipt, expense purpose, tax treatment, or employee bank detail.

## Projects

Resolve projects by code plus customer and inspect inactive and subproject records. Verify name, customer, project manager, department, start/end dates, billing method, budget hours/amount, activities, participants, and invoice linkage. Search before create or copy.

Closing or deactivating a project requires checking unapproved time, unbilled transactions, open orders, supplier documents, and remaining responsibilities. Preserve posted history.

## Complete-list handling

Clear employee/project/status/date filters. Use exact codes and bounded date ranges, then traverse all pages or virtual rows while tracking stable transaction or project identifiers. A current-week view is not an exhaustive search.

## Official references

- [Web timesheet entry](https://hjelpesenter.poweroffice.no/timeregistrering-timeliste)
- [Time reports](https://hjelpesenter.poweroffice.no/timerapporter-oversikt)
- [Travel-expense settings](https://hjelpesenter.poweroffice.no/reiseregning-innstillinger)
- [Project report](https://hjelpesenter.poweroffice.no/prosjektrapport-oversikt)
