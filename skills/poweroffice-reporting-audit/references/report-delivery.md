# Report export and email

Use for one-off report delivery. Live Chrome check on 2026-09-28 confirmed **Menu → Reports → Profit and Loss → Share → Email**, recipient/subject controls and an automatically generated PDF attachment. The unlabeled Share icon was in the bottom toolbar; resolve it from current semantics or a fresh screenshot, never saved coordinates. The dialog was cancelled without sending. Other report variants and delivery outcomes remain untested; confirm live labels/options.

## Resolve the request

Ground five items: company, report type, period/as-of date, optional customer/project filter, and output/destination. Reuse a visibly open report and its selected parameters when the user says “this report.” “Selected client” refers to the company in the client selector unless the request and selected customer row establish customer scope. If multiple interpretations remain, ask one concise clarification before changing scope or sending.

Use a full email address supplied by the user or an unambiguous authorized contact already verified in this session. “Send to me” requires a known verified address; do not infer it from a display name. Autocomplete is a candidate, not proof. A missing report type, accounting period, or recipient is a preparation blocker, not permission to guess. Previously approved workflow defaults can resolve these fields when explicitly established for this workflow.

## Short path

1. Verify the active company. If another company is named, open the client selector beside the menu, search by exact name/organization number where supported, select the match, and verify the new context. Do not add a client.
2. Stay in the intended report when already open. Otherwise use `Menu/Meny → Reports/Rapporter` and the requested report. Examples are `Profit and Loss/Resultatregnskap` for company profit/loss and `Customer Ledger/Kundereskontro` for customer ledger evidence. In the latter, verify the customer number and whether the request needs `Åpne poster` (open items) or `Kontoutskrift` (account statement). These have different bases; do not substitute one silently.
3. Apply the requested period and relevant filters once. Wait for the updated report and verify heading, parameter summary, customer when relevant, and a control total/count where exposed. Use visible parameters as evidence; reopen settings only if hidden or inconsistent. Profit/loss cannot span accounting years: prepare separate requested-year reports or clarify a requested cross-year presentation.
4. Use the report's `Share/Del` sharing/export control and choose the requested format. PowerOffice supports PDF, Excel, CSV and native `Email/E-post`; native email generates a PDF of the report view. Prefer native email for an authorized PDF send, avoiding download/reattach steps. Excel/CSV may include all available columns, so inspect scope/privacy instead of assuming hidden columns are excluded.
5. In the live email dialog, verify full recipient address(es), subject, company/customer, report name, period, and generated attachment(s) or preview when exposed. Remove unrelated prefilled recipients. Use a concise subject with report, company/customer, and period; invent neither personal data nor unrequested promises. Do not send if report identity/content cannot be established.
6. With an explicit matching send request, select Send once. Observe resulting status/acknowledgement and any available send history. Report application acceptance as “sent/queued by PowerOffice”; do not claim inbox delivery from a toast. If no durable status exists, state the observed acknowledgement and limit. If the result is ambiguous, do not resend automatically.

If `E-post` is unavailable for this view/role, determine whether an authorized export is available. Use a browser email service only when the requested recipient/purpose authorize that send and browser tools support attaching the actual verified file; follow the relevant mail skill only for that step. Never invent an attachment path, create a public file link, or install/configure another service to complete this task. Otherwise leave the generated private export ready and state the specific missing capability.

## Official sources

- [Report exports and native email](https://hjelpesenter.poweroffice.no/eksport-lister-rapporter): `Del`, PDF, Excel, CSV, and PDF-by-email.
- [Company selector](https://hjelpesenter.poweroffice.no/klientmeny-bytt-foretak): selected company, search, and company versus contact distinction.
- [Profit/loss report](https://hjelpesenter.poweroffice.no/resultatregnskap-visninger): report route and accounting-year limit.
- [Customer ledger views](https://hjelpesenter.poweroffice.no/matche-aapne-poster-reskontro): route and `Åpne poster` / `Kontoutskrift` labels. Its matching actions change accounting state and are outside this reporting workflow.
