# Repository guidance

Read `docs/AI_CONTEXT_MAP.md` before changing a skill. Work inside the smallest relevant skill folder and avoid loading unrelated references.

Install the complete suite so focused skills can reuse `poweroffice-admin-suite/references/browser-operation-contract.md`. Read that contract only when missing from the current context; keep detailed procedures in the owning skill's `references/` directory and load only the requested workflow.

Never commit company exports, employee lists, national identity numbers, bank account numbers, salary data, credentials, BankID material, API keys, session material, or a real `.poweroffice/company-catalog.yaml`. The public catalog is an example only.

Keep automatic invocation descriptions mutually discriminating. Focused skills own clear domain requests; `poweroffice-admin-suite` routes natural-language or voice requests when an owner needs to be selected. The user need not name a skill. Reuse authenticated Chrome unless the user specifies another browser. Treat every company as production unless the user explicitly identifies a demo client.

Before any mutation, verify the selected company and exact object. Preserve authorization boundaries, idempotency, complete-list handling, financial state transitions, and independent after-state verification. Invoice sending/posting, paying, submitting statutory reports, approving payroll, locking periods, and publishing multi-client access changes remain critical commits. A report email may be sent once when the exact company/customer, report, period, required attachment and full recipient are grounded and the user explicitly authorized that send; do not request redundant confirmation. Export from PowerOffice and send through Outlook on the web in the same authenticated Chrome profile, using the signed-in user's mailbox on Windows or macOS. Verify Sent Items, inspect uncertain outcomes before retrying, and do not equate a sent record with inbox delivery. Keep skills portable: no fixed sender/profile/path or native Outlook dependency.
