---
name: poweroffice-employee-lifecycle
description: Execute end-to-end PowerOffice Go employee onboarding, employment changes, and safe offboarding through an authenticated browser, coordinating employee records, user access, roles, approvers, time and expense access, project responsibilities, and payroll readiness. Use for lifecycle requests spanning at least two of these areas.
---

# PowerOffice Employee Lifecycle

Own the complete lifecycle workflow and keep one evidence record for the exact person. A PowerOffice user, employee record, payroll employment, and approver assignment are distinct objects; link them only after verifying stable fields such as email, employee number, and employment dates.

## Establish context

1. Attach to the user-mentioned PowerOffice Go tab when present; otherwise reuse the authenticated PowerOffice session.
2. Confirm the active company, organization number, signed-in administrator, and exact employee.
3. Inspect current user and employee state before mutation. Continue partial workflows idempotently.
4. Use `.poweroffice/company-catalog.yaml` when available for approved profiles and defaults. Verify every referenced role, department, approver, activity, project, and payroll setting live.
5. Read [references/browser-operation-contract.md](references/browser-operation-contract.md).

## Choose one workflow

- New employee: read [references/onboarding.md](references/onboarding.md).
- Departing employee: read [references/offboarding.md](references/offboarding.md).
- Department, manager, employment, role, or responsibility change: read [references/employee-change.md](references/employee-change.md).

## Authorization

A request for complete onboarding, transfer, or safe offboarding authorizes ordinary reversible changes for the named person and stated profile. It does not authorize Administrator access, payment authority, payroll approval, deletion of historical records, submission of A-melding, disclosure of sensitive payroll data, or unrelated company-wide changes.

Do not enter or persist national identity numbers, personal bank accounts, tax details, salary amounts, or other sensitive employment data unless the user provides the exact value through an appropriate secure workflow and the task requires it. Never repeat those values in the completion report.

## Finish

Report company, exact employee and email, employee/user linkage, verified roles, approvers, time/expense/project setup, payroll readiness without sensitive values, completed and already-correct steps, pending invitations, blocked items, and human actions. Distinguish `record created`, `invited`, `linked`, `configured`, `reported`, and `paid`.
