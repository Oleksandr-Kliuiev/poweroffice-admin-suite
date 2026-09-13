# Repository guidance

Read `docs/AI_CONTEXT_MAP.md` before changing a skill. Work inside the smallest relevant skill folder and avoid loading unrelated references.

Keep every focused skill independently usable after plugin installation. Shared safety invariants may be stated concisely in each entrypoint; detailed procedures belong in that skill's `references/` directory.

Never commit company exports, employee lists, national identity numbers, bank account numbers, salary data, credentials, BankID material, API keys, session material, or a real `.poweroffice/company-catalog.yaml`. The public catalog is an example only.

Keep automatic invocation descriptions mutually discriminating. `poweroffice-admin-suite` applies only when explicitly named; focused skills own ordinary PowerOffice Go requests. Treat every company as production unless the user explicitly identifies a demo client.

Before any mutation, verify the selected company and exact object. Preserve authorization boundaries, idempotency, complete-list handling, financial state transitions, and independent after-state verification. Sending, posting, paying, submitting statutory reports, approving payroll, locking periods, and publishing multi-client access changes are critical commits.
