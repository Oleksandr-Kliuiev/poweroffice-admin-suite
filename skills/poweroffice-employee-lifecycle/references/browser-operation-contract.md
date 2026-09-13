# Browser operation contract

## Company and object identity

Confirm company legal name and organization number before every mutation batch and after any company switch. Resolve people by exact email plus employee number when available; never use display name alone. Resolve customers, suppliers, projects, invoices, vouchers, and payroll runs by stable number plus secondary attributes.

## Stable interaction loop

1. Observe a fresh accessibility/UI state.
2. Resolve controls by semantic role, accessible name, visible value, or stable identifier. Avoid coordinates and row positions.
3. Perform one coherent action or fill one unchanged form.
4. Wait for a meaningful readiness signal: loading completion, changed count, heading, URL, status, or message.
5. Observe again and verify the persisted object independently.

Discard old element references after navigation, modal changes, refresh, sorting, or asynchronous updates. Before retrying any mutation, reread current state to determine whether the first attempt succeeded.

## Search, filters, and pagination

Clear old filters and date ranges. Use exact server-side search, then relevant status filters, then stable sorting, then pagination. Track page boundaries by stable identifiers; stop only when found, Next is disabled, or repeated boundaries prove exhaustion. For virtual tables, scroll the table container and track unique identifiers. Never report `not found` after inspecting only the first page or current date range.

## Critical commit checkpoint

Drafts and reversible preparation may proceed within the authorized request. Immediately before sending, posting, paying, approving payroll, filing statutory reports, locking a period, deleting/reversing history, or publishing multi-client access changes, show a concise transaction summary and obtain explicit confirmation unless that exact commit was separately confirmed in the current interaction.

MFA, BankID, electronic signatures, and personal authentication remain human actions. Do not ask for or handle their secrets.

## Evidence and recovery

Keep a compact record of before state, requested change, UI acknowledgement, independently observed after state, and downstream dependencies. A toast is provisional. Use bounded retries for loading or eventual consistency; never create duplicate users, employees, invoices, payments, vouchers, projects, or payroll runs to compensate for uncertainty.
