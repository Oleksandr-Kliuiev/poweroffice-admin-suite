# Changelog

## Unreleased — 2026-09-29

- Send requested reports with PowerOffice Share/Del → Email/E-post, including supplier open items. Download only for a requested file, and verify the native send acknowledgement or history.
- Confirm the Supplier Ledger → Open Items view and its native email dialog with `Supplier Ledger.pdf`; avoid reusing a stale email dialog for a new request.

## 0.1.2 — 2026-09-28

- Export PowerOffice reports and deliver through Outlook on the web in the same authenticated Chrome profile.
- Use each Windows/macOS user's signed-in mailbox, verified recipient and actual exported file without native Outlook or fixed machine/account assumptions.
- Verify uploaded attachments and Outlook Sent Items; report unsupported file access and uncertain sends without silent mail-service fallbacks.

## 0.1.1 — 2026-09-28

- Route spoken or written requests without requiring a skill name and reuse authenticated Chrome.
- Reduce entrypoint context with a shared browser contract and selected workflow references.
- Add grounded native report export/email navigation, exact recipient and scope checks, and safe handling of uncertain sends.
- Preserve financial commit checkpoints, complete-list handling, and verified outcomes.
