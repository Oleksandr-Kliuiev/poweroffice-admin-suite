# Access operations

## Role model

PowerOffice Go access is role-based. Standard clients commonly include `Daglig leder`, `Regnskapsfører`, `Revisor`, and `Standard`; the immutable Administrator role has full client access. Other roles can expose no, read, full, or category-specific access depending on the category.

Role labels are not sufficient evidence. Open the role and inspect relevant privileges, especially:

- manage users and manage roles;
- payments and bank authorization;
- payroll administration and employee data;
- accounting posting and correction;
- invoice send/post permissions;
- reports, logs, and settings.

Access to role administration can allow self-escalation. Treat changes to that privilege and Administrator assignment as critical access commits.

## Invite or assign

1. Verify company and organization number.
2. Search all users by exact normalized email, including inactive or pending invitations.
3. If found, inspect current status and roles; update idempotently instead of inviting again.
4. If absent, create the invitation with the exact email and approved role.
5. Verify the resulting user row, role, and invitation status after refresh.

Do not claim the user has logged in or accepted the invitation unless the UI shows that state.

## Deactivate or remove access

Inventory the user's roles, privileged responsibilities, approval chains, client memberships, and special contacts. Reassign required responsibilities first. Use deactivation or access removal rather than deleting historical employee or accounting records.

Before retrying, search the user and inspect status. Report whether access is disabled immediately, pending, or blocked by an assigned responsibility.

## Complete-list handling

Use exact email search first. Clear previous filters, include inactive users, then use stable sorting and pagination. Track first and last visible emails per page; stop only when the target is found, the next-page control is disabled, or repeated boundaries prove exhaustion. For virtual lists, scroll the table container and track unique emails.

## Official references

- [Set up roles in PowerOffice](https://support.poweroffice.com/hc/no/articles/208468636-Sett-opp-roller-i-PowerOffice)
- [Role administration](https://support.poweroffice.com/hc/no/articles/208582866-Roller)
