# Company catalog schema

The catalog is YAML with `schema_version: 1`. Keep values human-reviewable and company references stable. The public example is synthetic; real catalogs must remain private.

## Top-level keys

- `schema_version`: required integer, currently `1`.
- `workspace`: required map with `display_name`, optional `partner_mode`, and `verified_at`.
- `companies`: required non-empty map keyed by a short stable slug.
- `partner`: optional partner-level template-role and protected-client settings.

## Company identity

Every company requires:

- `legal_name`;
- `organization_number`, stored as nine digits;
- `currency`;
- optional `verified_at`, `subscriptions`, and `status`.

Do not use display name as the only selector. Live skills must verify legal name and organization number before mutation.

## Optional company sections

- `access_profiles`: approved roles, employment defaults, time/expense/project access, and approver aliases.
- `departments`, `activities`, and `projects`: stable codes and names, not transaction exports.
- `approval_flows`: named approver aliases, levels, and gross-amount thresholds.
- `invoicing_defaults`: payment terms, delivery method, currency, and masked bank alias.
- `accounting_defaults`: fiscal year, VAT period, lock-date policy, standard dimension rules, and responsible accountant alias.
- `payroll_defaults`: normal hours, default pay day, included sources, and responsible payroll alias. Never store salaries or employee tax/bank data.
- `integrations`: name, environment, owner alias, scope summary, masked key identifier, and status. Never store keys or tokens.
- `safety`: protected users, roles, bank aliases, projects, clients, and critical workflows.

## Profile inheritance

An access profile may use `extends` with one or more profile names from the same company. Apply parents before the child; merge maps recursively, append unique list items, and let child scalar values override parent values. Reject unknown parents and cycles.

Profiles are intended state. They do not authorize role assignment, prove that a live role still has the expected privileges, or permit critical financial commits.

## Masked identifiers and forbidden data

Use aliases plus `last4` for company bank accounts. Never include full account number, IBAN, BIC, employee bank details, national identity number, tax card, salary, credentials, BankID material, API keys, tokens, certificates, or session data under any key.
