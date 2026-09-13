---
name: poweroffice-access-admin
description: Administer PowerOffice Go users, invitations, roles, permissions, administrator access, and user deactivation through an authenticated browser. Use for access-focused requests within one company. Do not use for employee payroll records or full lifecycle workflows spanning access and employment.
---

# PowerOffice Access Admin

Resolve the active company by legal name and organization number, then resolve the target user by exact email. Treat a PowerOffice user and an employee record as distinct objects unless their linkage is verified.

Read [references/access-operations.md](references/access-operations.md) for role semantics, invitation and deactivation workflows, privilege-escalation checks, list handling, and verification.

Use least privilege and an approved profile from `.poweroffice/company-catalog.yaml` when available. Verify the live role definition before assignment. Never assign Administrator, access to manage roles/users, payment approval, payroll administration, or broad report access merely because a similarly titled user has it.

Before removing access, verify responsibility ownership, approval chains, active sessions where visible, and whether the user is a security contact, subscription administrator, or another protected owner. Preserve accounting history; do not delete an employee record to remove login access.

Report exact email, company, role before/after, invitation status, privileged capabilities affected, reassigned responsibilities, and any acceptance or MFA step left to the user.
