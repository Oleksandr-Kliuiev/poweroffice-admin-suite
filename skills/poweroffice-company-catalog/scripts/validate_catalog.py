#!/usr/bin/env python3
"""Validate structural and privacy invariants of a PowerOffice company catalog."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - dependency error is user-facing
    yaml = None


FORBIDDEN_KEY = re.compile(
    r"(^|_)(password|passwd|secret|token|access_token|refresh_token|private_key|"
    r"client_key|client_secret|application_key|subscription_key|bankid|mfa_secret|"
    r"national_id|identity_number|fodselsnummer|birth_number|tax_card|salary|payslip|"
    r"iban|bic|swift|bank_account_number)s?($|_)",
    re.IGNORECASE,
)
SLUG = re.compile(r"[a-z0-9][a-z0-9-]*")
ORG_NUMBER = re.compile(r"\d{9}")
LAST4 = re.compile(r"\d{4}")


def load_catalog(path: Path) -> Any:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required. Install scripts/requirements.txt in an isolated environment."
        )
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def walk_for_forbidden_keys(value: Any, location: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}" if location else str(key)
            if FORBIDDEN_KEY.search(str(key)):
                errors.append(f"sensitive key is forbidden: {child_location}")
            walk_for_forbidden_keys(child, child_location, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk_for_forbidden_keys(child, f"{location}[{index}]", errors)


def validate_profiles(company_path: str, profiles: Any, errors: list[str]) -> None:
    if profiles is None:
        return
    if not isinstance(profiles, dict):
        errors.append(f"{company_path}.access_profiles must be a mapping")
        return

    for name, profile in profiles.items():
        path = f"{company_path}.access_profiles.{name}"
        if not isinstance(name, str) or not SLUG.fullmatch(name):
            errors.append(f"invalid profile name at {path}")
        if not isinstance(profile, dict):
            errors.append(f"{path} must be a mapping")
            continue
        parents = profile.get("extends", [])
        if isinstance(parents, str):
            parents = [parents]
        if not isinstance(parents, list) or not all(isinstance(x, str) for x in parents):
            errors.append(f"{path}.extends must be a list of profile names")
            continue
        for parent in parents:
            if parent not in profiles:
                errors.append(f"{path}.extends references unknown profile {parent!r}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str, trail: list[str]) -> None:
        if name in visiting:
            errors.append(
                f"profile inheritance cycle in {company_path}: "
                + " -> ".join(trail + [name])
            )
            return
        if name in visited:
            return
        visiting.add(name)
        profile = profiles.get(name, {})
        parents = profile.get("extends", []) if isinstance(profile, dict) else []
        if isinstance(parents, str):
            parents = [parents]
        if isinstance(parents, list):
            for parent in parents:
                if isinstance(parent, str) and parent in profiles:
                    visit(parent, trail + [name])
        visiting.remove(name)
        visited.add(name)

    for profile_name in profiles:
        if isinstance(profile_name, str):
            visit(profile_name, [])


def validate_bank_aliases(company_path: str, accounts: Any, errors: list[str]) -> None:
    if accounts is None:
        return
    if not isinstance(accounts, dict):
        errors.append(f"{company_path}.bank_accounts must be a mapping")
        return
    for alias, account in accounts.items():
        path = f"{company_path}.bank_accounts.{alias}"
        if not isinstance(alias, str) or not SLUG.fullmatch(alias):
            errors.append(f"invalid bank alias at {path}")
        if not isinstance(account, dict):
            errors.append(f"{path} must be a mapping")
            continue
        last4 = account.get("last4")
        if not isinstance(last4, str) or not LAST4.fullmatch(last4):
            errors.append(f"{path}.last4 must contain exactly four digits")


def validate_catalog(data: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        return ["catalog root must be a mapping"], warnings
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    workspace = data.get("workspace")
    if not isinstance(workspace, dict):
        errors.append("workspace must be a mapping")
    elif not workspace.get("display_name"):
        warnings.append("workspace.display_name is missing")

    companies = data.get("companies")
    if not isinstance(companies, dict) or not companies:
        errors.append("companies must be a non-empty mapping")
    else:
        seen_org_numbers: dict[str, str] = {}
        for slug, company in companies.items():
            company_path = f"companies.{slug}"
            if not isinstance(slug, str) or not SLUG.fullmatch(slug):
                errors.append(f"invalid company slug: {slug!r}")
            if not isinstance(company, dict):
                errors.append(f"{company_path} must be a mapping")
                continue
            if not company.get("legal_name"):
                errors.append(f"{company_path}.legal_name is required")
            org_number = company.get("organization_number")
            if not isinstance(org_number, str) or not ORG_NUMBER.fullmatch(org_number):
                errors.append(f"{company_path}.organization_number must contain nine digits")
            elif org_number in seen_org_numbers:
                errors.append(
                    f"duplicate organization_number {org_number} in {company_path} "
                    f"and companies.{seen_org_numbers[org_number]}"
                )
            else:
                seen_org_numbers[org_number] = str(slug)
            currency = company.get("currency")
            if not isinstance(currency, str) or not re.fullmatch(r"[A-Z]{3}", currency):
                errors.append(f"{company_path}.currency must be a three-letter uppercase code")
            validate_profiles(company_path, company.get("access_profiles"), errors)
            validate_bank_aliases(company_path, company.get("bank_accounts"), errors)

    walk_for_forbidden_keys(data, "", errors)
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    args = parser.parse_args()

    try:
        data = load_catalog(args.catalog)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate_catalog(data)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Catalog invalid: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"Catalog valid: {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
