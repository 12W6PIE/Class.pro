#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path

def resolve_environment():
    current_file = Path(__file__).resolve()
    prime_root = None

    for parent in current_file.parents:
        if parent.name.startswith("Class.pro-TMPL-"):
            prime_root = parent.parent
            break
        if parent.name.lower() in ["prime.pro", "prime"]:
            prime_root = parent
            break

    if prime_root is not None:
        x_pros_dir = prime_root.parent
        workspace_root = x_pros_dir.parent if x_pros_dir.name.lower() in ["_x_pros", "_x_pro"] else prime_root.parent
    else:
        workspace_root = current_file.parents[3] if len(current_file.parents) > 3 else current_file.parents[2]
        for candidate in ["_X_Pros", "_X_PROs", "_x_pros"]:
            p = workspace_root / candidate / "Prime.pro"
            if p.exists():
                prime_root = p
                break
        if prime_root is None:
            prime_root = workspace_root / "_X_Pros" / "Prime.pro"

    return prime_root, workspace_root

def pull_upstream_prime(prime_root: Path):
    if (prime_root / ".git").exists():
        res = subprocess.run(
            ["git", "pull", "--ff-only"],
            cwd=prime_root,
            text=True,
            capture_output=True
        )
        if res.returncode == 0:
            print("[UPSTREAM_SYNC] Prime.pro is up to date.")
        else:
            print("[UPSTREAM_SYNC] Proceeding with local Prime.pro snapshot.")

def run_scaffold(stage: int):
    prime_root, workspace_root = resolve_environment()
    pull_upstream_prime(prime_root)
    stage_template = prime_root / f"Class.pro-TMPL-{stage}"

    print(f"[skill_scaffold] Stage:     {stage}")
    print(f"[skill_scaffold] Source:    {stage_template}")
    print(f"[skill_scaffold] Workspace: {workspace_root}")

    if not stage_template.exists():
        print(f"[SKILL_FAIL] Template directory not found: {stage_template}", file=sys.stderr)
        sys.exit(1)

    for folder in ["_Context", "_Deliverables", ".agents"]:
        (workspace_root / folder).mkdir(parents=True, exist_ok=True)

    protected_files = {
        Path("_Context/STUDENT-PROFILE.md"),
        Path("_Context/Validated_Dossier.md"),
        Path("_Context/state.md"),
        Path("_Deliverables/1-Page-Brief.tex"),
        Path("_Deliverables/1-Page-Brief.md"),
    }

    # Use os.walk to guarantee traversal into hidden folders (.agents) on all OS/Python versions
    for root, dirs, files in os.walk(stage_template):
        if "__pycache__" in root:
            continue

        for file_name in files:
            if file_name in {".DS_Store", "Thumbs.db", "desktop.ini"}:
                continue

            src_file = Path(root) / file_name
            rel_path = src_file.relative_to(stage_template)
            dest_path = workspace_root / rel_path

            # Preserve student-configured .gitignore
            if rel_path == Path(".gitignore") and dest_path.exists():
                if "_X_Pros" in dest_path.read_text(encoding="utf-8", errors="ignore"):
                    print(f"[PRESERVED] {rel_path}")
                    continue

            # Backup initial stub README
            if rel_path == Path("README.md") and dest_path.exists():
                existing_text = dest_path.read_text(encoding="utf-8", errors="ignore")
                if "Agentic Research Factory" in existing_text:
                    print(f"[PRESERVED] {rel_path}")
                    continue
                else:
                    backup_readme = workspace_root / "README.initial.md"
                    shutil.copy2(dest_path, backup_readme)
                    print("[BACKUP]    Backed up initial GitHub README.md -> README.initial.md")

            # Never overwrite student progress or deliverables
            if (rel_path in protected_files or "_Deliverables" in rel_path.parts) and dest_path.exists():
                print(f"[PRESERVED] {rel_path}")
                continue

            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Normalize line endings: LF for bash, CRLF for Windows cmd
            if src_file.suffix == ".sh":
                raw_text = src_file.read_text(encoding="utf-8").replace("\r\n", "\n")
                dest_path.write_text(raw_text, encoding="utf-8", newline="\n")
            elif src_file.suffix in [".cmd", ".bat"]:
                raw_text = src_file.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\n", "\r\n")
                dest_path.write_text(raw_text, encoding="utf-8", newline="\r\n")
            else:
                shutil.copy2(src_file, dest_path)

            print(f"[COPIED]    {rel_path}")

    print("[SKILL_PASS] Workspace scaffolding complete.")

    # Automatic Stage baseline Git checkpoint
    git_sync_script = workspace_root / ".agents" / "skills" / "skill_git_sync" / "git_sync.py"
    if git_sync_script.exists():
        print(f"[skill_scaffold] Triggering automatic Stage {stage} Git checkpoint...")
        commit_msg = f"feat: initialize Stage {stage} workspace baseline"
        res = subprocess.run([sys.executable, "-B", str(git_sync_script), "-m", commit_msg], cwd=workspace_root)
        if res.returncode != 0:
            print("[WARN] Automatic git checkpoint encountered non-zero status; verify with git status.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", type=int, default=0)
    args = parser.parse_args()
    run_scaffold(args.stage)
