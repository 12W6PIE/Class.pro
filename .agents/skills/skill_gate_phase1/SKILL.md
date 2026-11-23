---
name: skill_gate_phase1
description: Deterministic phase-gate inspection engine. Verifies whether Phase 1 (Classes 1 & 2) is completed by auditing the structural integrity, mandatory sections, and placeholder completeness of ./_Deliverables/1-Page-Brief.tex. Use before proceeding to Phase 2.
---

# Skill: `skill_gate_phase1`

## 1. Overview & Purpose
The `skill_gate_phase1` tool is a deterministic phase-gate inspection engine. It verifies whether the student researcher has formally completed Phase 1 (Classes 1 & 2) by auditing the structural integrity and content completeness of `./_Deliverables/1-Page-Brief.tex`.

Downstream agents (such as `02_literature_coo` in Phase 2) must execute this skill before booting to prevent hallucinating on unanchored or incomplete research briefs.

---

## 2. Environment & OS Execution Protocol

The executing Agent must identify the host operating system (`Windows` vs. `macOS/Linux`) and invoke the corresponding OS wrapper script:

### Arguments
None. The script automatically targets `./_Deliverables/1-Page-Brief.tex`.

### Invocation Commands
- **Windows:**
  ```cmd
  cmd /c .agents\skills\skill_gate_phase1\run_win.cmd
  ```
- **macOS / Linux:**
  ```bash
  bash ".agents/skills/skill_gate_phase1/run_mac.sh"
  ```

---

## 3. Verification Criteria

The validator checks for three critical invariants:
1. **Valid LaTeX Structure:** Presence of `\documentclass` and `\end{document}`.
2. **All 7 Mandatory Sections:**
   - Section 1: Working Titles
   - Section 2: Project Idea & Motivation
   - Section 3: Bounded Domain & Scientific Delta (SOTA Alignment)
   - Section 4: Developmental Delta (Continuous Progress Rule)
   - Section 5: Tooling Architecture & Automated Pipelines
   - Section 6: Course Deliverables Mapping
   - Section 7: Statement of Publishing Level Assessment
3. **Zero Unreplaced Placeholders:** Ensures no template tokens remain (e.g., `[INSERT ...]`, `[YES/NO ...]`, `[TODO ...]`, `[CHOOSE ...]`).

---

## 4. Deterministic Output & Exit Verification

### Success Signature (Exit Code: `0`)
```text
[SKILL_PASS] 1-Page-Brief.tex passed all Phase 1 structural and content checks.
```

### Failure Signature (Exit Code: non-zero)
- **Exit Code 1:** File missing or invalid LaTeX root syntax.
- **Exit Code 2:** Missing one or more required sections.
- **Exit Code 3:** Unreplaced template placeholders detected.

```text
[SKILL_FAIL] Missing required sections in 1-Page-Brief.tex: ...
```
or
```text
[SKILL_FAIL] Found N unreplaced placeholders in 1-Page-Brief.tex: ...
```

If a failure occurs, the agent must output the exact missing sections or placeholder names and instruct the student to complete them before proceeding to Phase 2.
