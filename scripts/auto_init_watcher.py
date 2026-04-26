from __future__ import annotations

import argparse
import time
from pathlib import Path

EXCLUDED_DIR_NAMES = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".nox",
    "dist",
    "build",
}


def should_handle_dir(path: Path) -> bool:
    return path.name not in EXCLUDED_DIR_NAMES and not path.name.startswith(".")


def iter_dirs(root: Path):
    for path in root.rglob("*"):
        if path.is_dir() and should_handle_dir(path):
            if any(part in EXCLUDED_DIR_NAMES for part in path.parts):
                continue
            if any(part.startswith(".") for part in path.parts):
                continue
            yield path


def ensure_init_file(directory: Path) -> bool:
    init_file = directory / "__init__.py"
    if init_file.exists():
        return False
    init_file.write_text("", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-create __init__.py for new directories")
    parser.add_argument("--root", default="api", help="Directory to monitor, default: api")
    parser.add_argument("--interval", type=float, default=1.0, help="Scan interval in seconds")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)

    # 初始化：先补齐已有目录
    known_dirs: set[Path] = set()
    created = 0
    for d in iter_dirs(root):
        known_dirs.add(d)
        if ensure_init_file(d):
            created += 1

    print(f"AUTO_INIT_WATCHER_STARTED root={root} created_initial={created}", flush=True)

    try:
        while True:
            current_dirs = set(iter_dirs(root))
            new_dirs = current_dirs - known_dirs
            for d in sorted(new_dirs):
                if ensure_init_file(d):
                    print(f"created: {d / '__init__.py'}", flush=True)
            known_dirs = current_dirs
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("AUTO_INIT_WATCHER_STOPPED", flush=True)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
