#!/usr/bin/env python3
"""Bump the '🚀 Version YYYY.MM.DD.N' line in changed blueprint files.

Files without an existing version line are left untouched -- this only
maintains versions in blueprints that have opted in to the convention.
"""
import datetime
import re
import sys

VERSION_RE = re.compile(
    r"^(?P<indent>\s*)🚀 Version (?P<version>\d{4}\.\d{2}\.\d{2}(?:\.\d+)?)\s*$"
)


def bump(path: str, today: str) -> bool:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    changed = False
    for i, line in enumerate(lines):
        m = VERSION_RE.match(line.rstrip("\n"))
        if not m:
            continue

        parts = m.group("version").split(".")
        date_str = ".".join(parts[:3])
        counter = int(parts[3]) if len(parts) > 3 else 0
        new_version = f"{today}.{counter + 1}" if date_str == today else f"{today}.1"

        lines[i] = f'{m.group("indent")}🚀 Version {new_version}\n'
        changed = True
        break  # only one version line expected per file

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)
    return changed


def main(argv: list[str]) -> None:
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d")
    any_changed = False
    for path in argv:
        if not path.strip():
            continue
        if bump(path, today):
            print(f"Bumped version in {path}")
            any_changed = True
    if not any_changed:
        print("No version lines found to bump.")


if __name__ == "__main__":
    main(sys.argv[1:])
