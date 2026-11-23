---
name: skill_scaffold
description: Deterministic workspace provisioning engine. Deploys configuration files, agent instructions, context templates, and skills from a specified course template stage (Class.pro-TMPL-<STAGE>) into the student's root workspace non-destructively.
---

# Skill: `skill_scaffold`

## 1. Overview & Purpose
The `skill_scaffold` tool is a deterministic workspace provisioning engine. It deploys configuration files, agent instructions, context templates, and skills from a specified course template stage (`Class.pro-TMPL-<STAGE>`) located inside `_X_Pros/Prime.pro` into the student's root repository workspace.

### Core Behaviors
- **Upstream Auto-Sync:** Before copying files, it inspects `_X_Pros/Prime.pro` and executes a safe `git pull --ff-only` to ensure the local distribution snapshot has the latest updates and blueprints pushed by the instructor.
- **Non-Destructive Scaffolding:** Preserves student progress. It will **never** overwrite protected files (`_Context/STUDENT-PROFILE.md`, `_Context/Validated_Dossier.md`, `_Context/state.md`) or any existing deliverables inside `_Deliverables/`.
- **Gitignore Protection:** Preserves student-customized root `.gitignore` files as long as `_X_Pros` is configured (folder versioned, contents ignored).
- **README Safety:** Backs up any 1-line GitHub initial stub `README.md` to `README.initial.md` before writing the course manual `README.md`.
- **Cross-Platform Normalization:** Automatically converts `.sh` shell scripts to Unix line endings (`LF` / `\n`) during file copy, preventing macOS/Linux `bash` runtime crashes when template repositories are prepared on Windows.

---

## 2. Environment & OS Execution Protocol

The executing Agent must identify the host operating system (`Windows` vs. `macOS/Linux`) and invoke the corresponding OS wrapper script. The agent must **never** execute raw inline terminal logic or arbitrary commands.

### Arguments
- `--stage <INT>`: The numeric stage of the course template to deploy (default: `0`).

### Invocation Commands

#### Scenario A: Bootstrap Invocation (Before root workspace scaffolding exists)
When called by `project-init` immediately after cloning `Prime.pro`:
- **Windows:**
  ```cmd
  cmd /c _X_Pros\Prime.pro\Class.pro-TMPL-0\.agents\skills\skill_scaffold\run_win.cmd --stage 0
  ```
- **macOS / Linux:**
  ```bash
  bash "_X_Pros/Prime.pro/Class.pro-TMPL-0/.agents/skills/skill_scaffold/run_mac.sh" --stage 0
  ```

#### Scenario B: In-Workspace Invocation (After workspace has been scaffolded)
When called for progressive stage updates (e.g., `--stage 1` in subsequent weeks):
- **Windows:**
  ```cmd
  cmd /c .agents\skills\skill_scaffold\run_win.cmd --stage <STAGE>
  ```
- **macOS / Linux:**
  ```bash
  bash ".agents/skills/skill_scaffold/run_mac.sh" --stage <STAGE>
  ```

---

## 3. Deterministic Output & Exit Verification

The agent must parse stdout and stderr to verify execution success:

### Success Signature (Exit Code: `0`)
The output must terminate with:
```text
[SKILL_PASS] Workspace scaffolding complete.
```

### Failure Signature (Exit Code: `1` or non-zero)
Any execution returning non-zero indicates an environment or path error:
```text
[SKILL_FAIL] Template directory not found: ...
```
or
```text
[SKILL_FAIL] Python 3 not found on ... PATH.
```

If a failure occurs, the agent must abort subsequent operations, report the exact error output to the student, and ask them to verify Python installation or repository paths.

---

## 4. Protected Files Manifest

The following file paths are permanently write-protected against overwriting during any scaffold run:
- `_Context/STUDENT-PROFILE.md`
- `_Context/Validated_Dossier.md`
- `_Context/state.md`
- `_Deliverables/*` (All files inside the deliverables folder)
