---
name: skill_git_sync
description: OS-isolated Git checkpoint and synchronization utility. Enforces repository safety, verifies .gitignore and shields _X_Pros/ contents, auto-heals author configuration on lab computers, and stages, commits, and pushes changes to the remote.
---

# Skill: `skill_git_sync`

## 1. Overview & Purpose
The `skill_git_sync` tool is an OS-isolated Git checkpoint and synchronization utility. It guarantees repository safety before and during every commit:
- **Vendor Shielding:** Confirms `.gitignore` exists at the workspace root and explicitly un-indexes any accidental tracking of `_X_Pros/` contents (and its casing variants) while preserving folder tracking via `.gitkeep`.
- **Environment Self-Healing:** On shared or fresh university lab computers, it verifies `.git` exists (runs `git init` if missing) and provides project-scoped author credentials (`user.name` and `user.email`) if not configured globally.
- **Atomic Staging & Push:** Stages all workspace modifications, checks for changes, commits with the specified message, and pushes to remote setting upstream tracking (`git push -u origin HEAD`).

---

## 2. Environment & OS Execution Protocol

The executing Agent must detect the host operating system (`Windows` vs. `macOS/Linux`) and invoke the corresponding OS wrapper script:

### Arguments
- `-m "<COMMIT_MESSAGE>"`: The Git commit message describing the phase milestone (default: `"chore: agent checkpoint sync"`).

### Invocation Commands
- **Windows:**
  ```cmd
  cmd /c .agents\skills\skill_git_sync\run_win.cmd -m "<COMMIT_MESSAGE>"
  ```
- **macOS / Linux:**
  ```bash
  bash ".agents/skills/skill_git_sync/run_mac.sh" -m "<COMMIT_MESSAGE>"
  ```

---

## 3. Deterministic Output & Exit Verification

### Success Signature (Exit Code: `0`)
The output must indicate success via one of the pass signatures:
```text
[SKILL_PASS] Successfully committed and pushed to remote.
```
or
```text
[SKILL_PASS] Committed locally (remote push skipped: ...).
```
or
```text
[SKILL_PASS] Working tree already clean. Nothing new to commit.
```

### Failure Signature (Exit Code: `1` or non-zero)
```text
[SKILL_FAIL] .gitignore missing at workspace root! Aborting to protect _X_Pros contents.
```
or
```text
[SKILL_FAIL] git commit failed: ...
```

If a failure occurs, the agent must halt, diagnose whether `.gitignore` is missing or file locks exist, and report the issue to the student.
