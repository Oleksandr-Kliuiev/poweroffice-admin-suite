# Employee onboarding

## Required identity and employment facts

Establish exact legal/display name, work email, employment start date, department, position, access profile, payroll inclusion, time/expense requirements, and approver relationships. Ask only for missing facts that materially affect the configuration. Sensitive values such as bank account, national identity number, salary, and tax details require a secure user-provided source and must not be invented.

## Idempotent workflow

1. Search employees across active and inactive records by email and name; inspect likely matches.
2. Search users and pending invitations by exact email.
3. Create or update the employee record with verified non-sensitive employment facts.
4. Create or update user access and assign the approved role; never infer elevated privileges.
5. Link the user and employee records, then verify the linkage from both views where possible.
6. Configure department, normal working time, employment dates, approvers, and permitted time/expense/travel functions.
7. Add project or activity responsibilities only when the profile requires them.
8. Prepare payroll fields and identify missing secure data; do not approve a payroll run as part of onboarding.
9. Refresh and verify employee status, invitation, role, linkage, approvers, and enabled modules.

If an object already exists, reconcile it rather than creating a duplicate. If identity is ambiguous, stop before mutation.

## Completion states

Report `employee record created/updated`, `user invited/existing`, `role assigned`, `records linked`, `approvers configured`, `time/expense/project access configured`, and `payroll ready/missing secure data` separately.

Official reference: [Create employees in PowerOffice Go](https://hjelpesenter.poweroffice.no/opprett-ansatte).
