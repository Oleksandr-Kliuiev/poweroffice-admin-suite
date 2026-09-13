# Integration operations

## Environments and credentials

PowerOffice API demo and production use distinct base URLs and credentials. Never mix environments. API v2 requires a valid access token; production access is tied to an integration application and a client-specific activation/key.

Treat all keys and tokens as secrets. Use a secret manager or environment injection that does not echo values. Store only integration name, environment, scopes, masked key identifier, activation state, owner, and last verified date in the private catalog.

## Browser activation or access change

1. Verify company and organization number.
2. Resolve the integration by exact registered name and publisher.
3. Inspect environment, requested permissions/scopes, owner, status, and affected data domains.
4. Explain write, payroll, bank, employee, and accounting access explicitly.
5. Obtain exact authorization for activation or scope expansion.
6. Verify active state and perform a least-privilege read test without exposing secrets.

## Imports

Before production import, verify source provenance, encoding, delimiter, locale/date/decimal formats, company identity, field mapping, required codes, duplicate keys, and behavior for unknown references. Use preview/validation when available. Keep an input checksum and row count outside the public repository.

Do not re-run an uncertain import until imported objects and import history are checked. Report accepted, rejected, skipped, and duplicate counts separately.

## API writes and idempotency

Prefer stable external references and supported idempotency behavior. Before retrying after timeout, query by stable key and compare intended values. Respect pagination and continuation metadata; do not treat one response page as complete.

## Official references

- [PowerOffice API authentication and environments](https://developer.poweroffice.net/documentation/authentication)
- [PowerOffice API getting started](https://developer.poweroffice.net/gettingstarted/1)
