#!/usr/bin/env python3
"""Check structural and context-budget invariants for the skill package."""

from __future__ import annotations

import re
import sys
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def yaml_scalar(block: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", block)
    if not match:
        return None
    return match.group(1).strip().strip('"\'')


def main() -> int:
    errors: list[str] = []
    descriptions: dict[str, str] = {}

    for skill_dir in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        entry = skill_dir / "SKILL.md"
        interface = skill_dir / "agents" / "openai.yaml"
        if not entry.is_file():
            errors.append(f"missing {entry.relative_to(ROOT)}")
            continue
        if not interface.is_file():
            errors.append(f"missing {interface.relative_to(ROOT)}")

        text = entry.read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            errors.append(f"invalid frontmatter: {entry.relative_to(ROOT)}")
            continue
        name = yaml_scalar(match.group(1), "name")
        description = yaml_scalar(match.group(1), "description")
        if name != skill_dir.name:
            errors.append(f"name mismatch in {entry.relative_to(ROOT)}: {name!r}")
        if not description:
            errors.append(f"missing description in {entry.relative_to(ROOT)}")
        elif description in descriptions:
            errors.append(
                f"duplicate description in {skill_dir.name} and {descriptions[description]}"
            )
        else:
            descriptions[description] = skill_dir.name
        if description and len(description) > 220:
            errors.append(f"description budget exceeded in {skill_dir.name}: {len(description)} > 220")

        if interface.is_file():
            interface_text = interface.read_text(encoding="utf-8")
            if re.search(r"(?m)^\s*allow_implicit_invocation:\s*false\b", interface_text):
                errors.append(f"automatic invocation disabled in {skill_dir.name}")
            if f"${skill_dir.name}" not in interface_text:
                errors.append(
                    f"default prompt does not name ${skill_dir.name}: "
                    f"{interface.relative_to(ROOT)}"
                )

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        for target in LOCAL_LINK.findall(markdown.read_text(encoding="utf-8")):
            local_target = target.split("#", 1)[0]
            if local_target and not (markdown.parent / local_target).resolve().exists():
                errors.append(
                    f"broken local link in {markdown.relative_to(ROOT)}: {target}"
                )

    for path in ROOT.rglob("*"):
        if (
            path.is_file()
            and ".git" not in path.parts
            and path.suffix in {".md", ".yaml", ".yml", ".py", ".json"}
        ):
            line_count = len(path.read_text(encoding="utf-8").splitlines())
            if line_count > 700:
                errors.append(f"context ceiling exceeded: {path.relative_to(ROOT)} ({line_count})")

    try:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        if manifest.get("name") != "poweroffice-admin-suite":
            errors.append("plugin manifest name must be poweroffice-admin-suite")
        if manifest.get("skills") != "./skills/":
            errors.append("plugin manifest skills path must be ./skills/")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid plugin manifest: {exc}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Package valid: {len(descriptions)} skills; all active files <= 700 lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
