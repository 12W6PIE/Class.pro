#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
    python3 -B "$SCRIPT_DIR/validate_phase1.py" "$@"
elif command -v python >/dev/null 2>&1; then
    python -B "$SCRIPT_DIR/validate_phase1.py" "$@"
else
    echo "[SKILL_FAIL] Python 3 not found on macOS/Linux PATH." >&2
    exit 1
fi
