# Report sharing and email in PowerOffice

Use this workflow for one-off report delivery. When the user asks to email a report, send it from the report's own `Share/Del → Email/E-post` action in PowerOffice. Do not download the report or switch to Outlook for that request. Export a file only when the user asks to download or save one, or when a native email action is unavailable and the user authorizes another delivery method.

The native email dialog was observed for `Menu → Reports → Profit and Loss → Share` on 2026-09-28 and for `Reports → Supplier Ledger → Open Items` on 2026-09-29. The latter showed an attached `Supplier Ledger.pdf`. Neither observation is proof of a completed send. Verify current controls and the send result at runtime.

## Resolve the request

Ground company, report type, period/as-of date, optional supplier/customer/project filter, and the exact destination. Reuse a visibly open report and its selected parameters when the user says “this report.” “Selected client” refers to the company in the client selector unless the request and selected row establish a narrower scope. If multiple interpretations remain, ask one concise clarification before changing scope or sending.

Use the exact full email address supplied by the user or an unambiguous authorized contact already verified in this session. Never infer an address from a display name, a previous administrator, an example or an owner-specific default. Autocomplete is a candidate, not proof. A missing recipient blocks sending only; prepare the scoped report while resolving the address. Previously approved workflow defaults apply only when explicitly established for the current user and workflow.

## Prepare the report

1. Verify the active company. If another company is named, use the client selector, search by exact name/organization number where supported, select the match, and verify the new context. Do not add a client.
2. Stay in the intended report when already open. Otherwise use `Menu/Meny → Reports/Rapporter` and the requested report. For an open supplier items list, use **Supplier Ledger / Leverandørreskontro → Open Items / Åpne poster** and retain supplier, date and status filters. The observed report also offered **Statement**; do not switch to it for an open-items request. For customer ledger, distinguish `Åpne poster` from `Kontoutskrift`; they have different bases.
3. Apply the requested period/as-of date and relevant filters once. Wait for the updated report and verify heading, parameter summary, supplier/customer when relevant, and a control total/count where exposed. Use visible parameters as evidence; reopen settings only if hidden or inconsistent. Profit/loss cannot span accounting years: prepare separate requested-year reports or clarify a requested cross-year presentation.

## Send with Share → Email

1. Open the report's `Share/Del` control and choose `Email/E-post` from that menu. Do not choose PDF, Excel, CSV or Download for an email request unless the user separately requested a saved file. If an old email dialog is already open, verify that it belongs to the current request; otherwise cancel it and open a new one from the verified report.
2. Before opening the email dialog, verify the report's company, Open Items view, as-of date and filters in the report itself. In the dialog, verify the report attachment or report identity (the observed supplier dialog named `Supplier Ledger.pdf`). Do not require every filter to be repeated in the dialog when it is already verified in the report. Enter the exact full recipient address and verify it after entry. Remove unrelated prefilled recipients. Use a concise subject and message identifying the report, company and period if the dialog provides those fields.
3. Before sending, verify every recipient and the report or attachment shown in the dialog. If the dialog cannot identify the report or destination reliably, stop before sending and state what could not be verified. Do not silently switch to another mail service.
4. With an explicit matching send request, select `Send/Send e-post` once without redundant confirmation. Observe PowerOffice's acknowledgement or available sharing/history record and verify the recipient/report when shown. Report exactly what PowerOffice confirms; accepted or queued does not prove inbox delivery.

If sending times out or the result is ambiguous, inspect the dialog and available PowerOffice sharing/history or status before deciding whether it submitted. Do not automatically resend. Retry at most once only when evidence establishes that no submission occurred; otherwise report the uncertain outcome.

## File export when requested

If the user asks to download or save a report, choose the requested PDF, Excel or CSV format from `Share/Del`, preserve the complete scoped report, and verify the export identity, format and parameters. Excel/CSV may include all available columns, so check scope and privacy rather than assuming hidden columns are excluded. Obtain any file location from the active tool runtime; never invent a Downloads path.

## Official references

- [Report sharing and export formats](https://hjelpesenter.poweroffice.no/eksport-lister-rapporter): `Del`, email, PDF, Excel and CSV.
- [Company selector](https://hjelpesenter.poweroffice.no/klientmeny-bytt-foretak): selected company and company versus contact distinction.
- [Profit/loss report](https://hjelpesenter.poweroffice.no/resultatregnskap-visninger): report route and accounting-year limit.
- [Customer ledger views](https://hjelpesenter.poweroffice.no/matche-aapne-poster-reskontro): `Åpne poster` and `Kontoutskrift` labels. Matching actions change accounting state and are outside this reporting workflow.
