# Company settings operations

## Resolve company context

Confirm the active company in the company selector and open company details to verify organization number. After a company switch or redirect, verify both again before editing. If multiple companies have similar names, use organization number as the discriminator.

PowerOffice navigation may vary by subscription and role. Current official routes commonly place configuration under `Menu > Manage/Administrer > Settings/Innstillinger`. Resolve controls by visible label and purpose rather than fixed screen coordinates.

## Dependency-aware changes

- Subscription: inspect status, billing consequence, dependent modules, and effective date. Activation is a paid external change.
- Company identity: verify legal name, organization number, addresses, VAT status, and contact fields independently; do not derive legal values.
- Number series: inspect the latest issued number and integrations before changing. Never create duplicate or backward sequences.
- Departments and dimensions: search inactive and active entries before creating; prefer reactivation where policy permits.
- Invoice defaults: inspect payment terms, delivery method, bank/OCR setup, templates, and VAT behavior together.
- Accounting defaults: inspect chart of accounts, rounding, VAT, lock date, and opening/conversion settings before mutation.

## Interaction and verification

Observe a fresh UI state, resolve the exact setting semantically, make one coherent change, wait for save completion, then reopen the setting and verify persisted state. Do not retry an uncertain save until the current value is read.

For lists, clear stale filters, search exact code or name, inspect inactive items, and traverse pagination or virtual scrolling to exhaustion before declaring an item absent.

## Official references

- [PowerOffice Go pricing and modules](https://www.poweroffice.no/priser)
- [PowerOffice Go invoicing setup](https://hjelpesenter.poweroffice.no/kom-i-gang-fakturering)
- [PowerOffice Go lock dates](https://hjelpesenter.poweroffice.no/laasedato-regnskapsperioder)
