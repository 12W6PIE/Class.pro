# Class 2 Execution Playbook (3 Hours)
**Goal:** SOTA Alignment, Tooling Blueprint, Overleaf 1-Page Project Brief & Gate Verification.

> **Important (If opening a new Chat Window for Class 2):** First boot `01_ideation_ceo` by activating `01_ideation_ceo` in Antigravity Chat and running `@01_ideation_ceo @.agents/agents/01_ideation_ceo/master-boot-prompt.md Initialize Phase 1 Ideation CEO using master boot prompt`. It will detect `_Context/Validated_Dossier.md` and enter State 1B. Then proceed with Prompt 4 below.

---

### PROMPT 4: SCIENTIFIC SOTA ALIGNMENT & MCP QUERIES
*(Send at the start of Class 2 after choosing your project idea from `_Context/Validated_Dossier.md`)*

```text
@_Context/Validated_Dossier.md
CEO, reading `_Context/Validated_Dossier.md`, I have selected my project idea: [STATE SELECTED IDEA NUMBER/TITLE].

Transition me from general ideation to formal scientific validation:
1. Formulate 3 to 5 preliminary academic Working Titles.
2. Construct Boolean-optimized English search queries for Web of Science (WoS), Scopus, and OpenAlex to verify the scientific State of the Art (SOTA) and confirm this is not a trivial solved problem.
3. Output the structured query handoff payload strictly in TOON format (`application/toon`) for Google Antigravity and the NotebookLM MCP. Remember: JSON is strictly forbidden.
4. Append the selected idea, Working Titles, and TOON SOTA query payload into `_Context/Validated_Dossier.md`.
```

---

### PROMPT 5: TOOLING STRATEGY, SANDBOXING & ARCHIVING BLUEPRINT
*(Send after reviewing the SOTA queries)*

```text
@_Context/Validated_Dossier.md
CEO, map my selected project to our zero-budget tooling and sandboxing stack. Output the execution blueprint in TOON format (`application/toon`) covering:
1. Local vs. Cloud Compute strategy (accounting for my hardware baseline and future lab RTX 4070 12GB VRAM access).
2. Docker Sandboxing specification (how empirical Python/Jupyter code will be isolated).
3. Artifact Archiving pipeline (linking GitHub releases to Zenodo for up to 50GB storage and DataCite DOI minting, plus Zotero Better BibTeX setup).
4. Append this TOON Tooling Blueprint into `_Context/Validated_Dossier.md`.
```

---

### PROMPT 6: 1-PAGE PROJECT BRIEF GENERATION & GATE VERIFICATION
*(Generates the Charter in LaTeX or Markdown and runs deterministic validation. Note: If you opted out of LaTeX, instruct the CEO to populate `_Deliverables/1-Page-Brief.md` instead of `.tex`)*

```text
@_Context/Validated_Dossier.md @_Deliverables/1-Page-Brief.tex @.agents/skills/skill_gate_phase1/SKILL.md
CEO, consolidate all our decisions from `_Context/Validated_Dossier.md` and directly update `_Deliverables/1-Page-Brief.tex` with clean, compilable LaTeX code (replacing all `[INSERT ...]` and `[YES/NO ...]` placeholders).

Keep the exact 7 `\section{...}` headings intact and populate:
1. Working Titles (Primary + 2 alternatives).
2. Project Idea & Motivation.
3. Bounded Domain & Scientific Delta (SOTA Alignment).
4. Developmental Delta (Continuous Progress Rule).
5. Tooling Architecture & Automated Pipelines.
6. Course Deliverables Mapping (Tracks 1a, 1b, 2a, 2b, and whether the AI Domain Exception applies).
7. Statement of Publishing Level Assessment (evaluating JCR Q1–Q4 / OCETA Connect 2027 target vs. internal Semi-Scientific Course Publishing Service fallback).

Once written, immediately read and execute `.agents/skills/skill_gate_phase1/SKILL.md` to deterministically verify that `_Deliverables/1-Page-Brief.tex` passes all Phase 1 gate checks with `[SKILL_PASS]`.
```

---

### PROMPT 7: CONTEXT PRESERVATION (`state.md`) & PHASE 1 SYNC
*(Final step of Class 2)*

```text
@_Context/Validated_Dossier.md @_Deliverables/1-Page-Brief.tex @.agents/skills/skill_git_sync/SKILL.md
CEO, generate our Multi-Turn Persistence file and save it to `_Context/state.md`.
Include:
- Student Dual-Axis Baseline & Developmental Delta.
- Approved Working Title, Bounded Domain, and Core Hypothesis.
- Target Deliverables Mapping & Publishing Level Assessment.
- SOTA Search Queries (TOON) & Next Actions for Class 3 (Phase 2 Literature Synthesis).

Once `_Context/state.md` is saved, execute `.agents/skills/skill_git_sync/SKILL.md` with message `"feat: complete Phase 1 1-Page-Brief.tex and state.md"`.
```
