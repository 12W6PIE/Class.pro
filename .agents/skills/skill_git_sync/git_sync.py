#!/usr/bin/env python3
import sys
import subprocess
import argparse
from pathlib import Path

def resolve_workspace_root():
    current_file = Path(__file__).resolve()
    for parent in current_file.parents:
        if parent.name.startswith("Class.pro-TMPL-"):
            prime_root = parent.parent
            x_pros = prime_root.parent
            return x_pros.parent if x_pros.name.lower() in ["_x_pros", "_x_pro"] else prime_root.parent

    for parent in current_file.parents:
        if (parent / ".git").exists() or (parent / "AGENTS.md").exists():
            return parent

    return current_file.parents[3] if len(current_file.parents) > 3 else current_file.parents[2]

def run_cmd(cmd, cwd):
    res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def ensure_git_ready(workspace_root: Path):
    if not (workspace_root / ".git").exists():
        run_cmd(["git", "init"], workspace_root)
        print("[GIT_INIT] Initialized local Git repository.")

    code_name, name_out, _ = run_cmd(["git", "config", "user.name"], workspace_root)
    if code_name != 0 or not name_out:
        run_cmd(["git", "config", "user.name", "AI Engineering Student"], workspace_root)
        print("[GIT_CONFIG] Set fallback local git user.name")

    code_email, email_out, _ = run_cmd(["git", "config", "user.email"], workspace_root)
    if code_email != 0 or not email_out:
        run_cmd(["git", "config", "user.email", "student@class.pro.local"], workspace_root)
        print("[GIT_CONFIG] Set fallback local git user.email")

def safe_git_sync(message: str):
    workspace_root = resolve_workspace_root()
    gitignore_path = workspace_root / ".gitignore"

    if not gitignore_path.exists():
        print("[SKILL_FAIL] .gitignore missing at workspace root! Aborting to protect _X_Pros contents.", file=sys.stderr)
        sys.exit(1)

    ensure_git_ready(workspace_root)

    for variant in ["_X_Pros", "_X_PROs", "_x_pros"]:
        run_cmd(["git", "rm", "-r", "--cached", "--ignore-unmatch", variant], workspace_root)

    code, _, err = run_cmd(["git", "add", "."], workspace_root)
    if code != 0:
        print(f"[SKILL_FAIL] git add failed: {err}", file=sys.stderr)
        sys.exit(1)

    _, status_out, _ = run_cmd(["git", "status", "--porcelain"], workspace_root)
    if not status_out:
        print("[SKILL_PASS] Working tree already clean. Nothing new to commit.")
        sys.exit(0)

    code, _, err = run_cmd(["git", "commit", "-m", message], workspace_root)
    if code != 0:
        print(f"[SKILL_FAIL] git commit failed: {err}", file=sys.stderr)
        sys.exit(1)

    print(f"[COMMITTED] {message}")
    code, _, err = run_cmd(["git", "push", "-u", "origin", "HEAD"], workspace_root)
    if code == 0:
        print("[SKILL_PASS] Successfully committed and pushed to remote.")
    else:
        print(f"[SKILL_PASS] Committed locally (remote push skipped: {err}).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", default="chore: agent checkpoint sync")
    args = parser.parse_args()
    safe_git_sync(args.message)
