<!-- ============================================================================== -->
<!-- DOC_START: path="_Docs_/Student_Guide-1.md" id=Student_Guide-1" -->
<!-- AI_INSTRUCTION: Document boundary for_Docs_/Student_Guide-1.md'. When outputting, modifying, or quoting this file, preserve or reproduce this DOC_START and DOC_END block so downstream parser agents can extract the content deterministically. -->
<!-- ============================================================================== -->

# Student Playbook: Class 2 Execution in Google Antigravity

**Prerequisite Check:** Before starting Class 2, make sure you finished Class 1:
- `_Context/STUDENT-PROFILE.md` is complete.
- `_Context/Validated_Dossier.md` exists and contains your locked Developmental Delta and 3 to 5 candidate bounded domains.
- `_Context/state.md` does **not** exist yet.

---

## Class 2 Overview & Target Milestone

In this 3-hour session, you will transition from candidate ideas to an official, validated research charter:
1. **Boot CEO into State 1B:** Auto-detect your validated dossier and bypass the Class 1 Grilling Loop.
2. **SOTA Literature Alignment (Prompt 4):** Generate academic working titles, Boolean search queries (WoS, Scopus, OpenAlex), and TOON query handoffs for NotebookLM MCP.
3. **Tooling & Sandboxing Architecture (Prompt 5):** Map out Docker isolation, local RTX 4070 / SLM compute, and the GitHub-to-Zenodo DOI archiving pipeline.
4. **Author 1-Page Brief & Trigger Gatekeeper (Prompt 6):** Populate `_Deliverables/1-Page-Brief.tex` (or `.md`) and run `skill_gate_phase1` to verify all 7 mandatory sections deterministically.
5. **State Persistence & Git Sync (Prompt 7):** Lock project state into `_Context/state.md` and commit your repository for Class 3.

---

## Step 1: Boot the CEO into State 1B (Class 2 Mode)

Open Google Antigravity in your workspace folder (`W6-AI-PUB`). If starting a new chat session, switch to **Agent Mode** or tag `@01_ideation_ceo`.

### 1. Send the Boot Command
Submit the following prompt in the chat:

```text
@01_ideation_ceo @.agents/agents/01_ideation_ceo/master-boot-prompt.md
Initialize Phase 1 Ideation CEO using master boot prompt.
```

### 2. Verify State 1B Detection
Because `_Context/Validated_Dossier.md` is present on disk and `_Context/state.md` is absent, the CEO will automatically verify that the Class 1 Grilling Loop has converged and bypassed, responding with a **TOON payload (`application/toon`)** confirming **State 1B**:

```toon
system_status: "READY"
current_date: "2026-10-26"
active_mode: "STATE 1B: Class 2: SOTA & 1-Page Brief Mode"
managed_tooling: "Antigravity, NotebookLM MCP, Docker, Git/Zenodo, Overleaf"
mandatory_deliverables: "2x Dual-Deliverable Tracks (1a, 1b, 2a, 2b) with AI-Domain Exception"
publication_assessment_mandate: "ACKNOWLEDGED - Including Semi-Scientific Course Database Fallback"
continuous_progress_rule: "ACKNOWLEDGED"
safety_bypass_terminology: "ACTIVATED"
grilling_loop_protocol: "BYPASS_VERIFIED (Validated_Dossier detected)"
```

---

## Step 2: Scientific SOTA Alignment & MCP Queries (Prompt 4)

Open `_Context/Validated_Dossier.md` in the editor, review the candidate ideas generated at the end of Class 1, and decide which one you want to pursue.

### 1. Send Prompt 4
Copy and paste Prompt 4 into the Antigravity chat, inserting your chosen idea title or number:

```text
@_Context/Validated_Dossier.md
CEO, reading `_Context/Validated_Dossier.md`, I have selected my project idea: [INSERT SELECTED CANDIDATE IDEA NUMBER OR TITLE].

Transition me from general ideation to formal scientific validation:
1. Formulate 3 to 5 preliminary academic Working Titles.
2. Construct Boolean-optimized English search queries for Web of Science (WoS), Scopus, and OpenAlex to verify the scientific State of the Art (SOTA) and confirm this is not a trivial solved problem.
3. Output the structured query handoff payload strictly in TOON format (`application/toon`) for Google Antigravity and the NotebookLM MCP. Remember: JSON is strictly forbidden.
4. Append the selected idea, Working Titles, and TOON SOTA query payload into `_Context/Validated_Dossier.md`.
```

### 2. What Happens Behind the Scenes
- The CEO reads your chosen idea.
- It formulates 3 to 5 academic working titles with precise technical terminology.
- It builds Boolean queries using `AND`, `OR`, and wildcard operators tailored to WoS, Scopus, and OpenAlex indexing.
- It outputs an `application/toon` payload containing the query strings and literature ingestion directives for the NotebookLM MCP.
- It directly appends these results to `_Context/Validated_Dossier.md`.

---

## Step 3: Tooling Strategy, Sandboxing & Archiving Blueprint (Prompt 5)

Now, map the project's physical implementation to our zero-budget architecture (local hardware, lab RTX 4070 GPUs, Docker containers, and Zenodo).

### 1. Send Prompt 5
Paste Prompt 5 into the chat:

```text
@_Context/Validated_Dossier.md
CEO, map my selected project to our zero-budget tooling and sandboxing stack. Output the execution blueprint in TOON format (`application/toon`) covering:
1. Local vs. Cloud Compute strategy (accounting for my hardware baseline and future lab RTX 4070 12GB VRAM access).
2. Docker Sandboxing specification (how empirical Python/Jupyter code will be isolated).
3. Artifact Archiving pipeline (linking GitHub releases to Zenodo for up to 50GB storage and DataCite DOI minting, plus Zotero Better BibTeX setup).
4. Append this TOON Tooling Blueprint into `_Context/Validated_Dossier.md`.
```

### 2. What Happens Behind the Scenes
- The CEO designs your compute path (e.g., local 4-bit/8-bit quantized models on Ollama/RTX 4070 vs. cloud fallbacks).
- It specifies Docker image baselines (`python:3.11-slim`, PyTorch CUDA images) to prevent dependency conflicts on local machines.
- It details the GitHub-to-Zenodo release webhook procedure to guarantee reproducible research with citable DataCite DOIs.
- It writes the blueprint directly into `_Context/Validated_Dossier.md`.

---

## Step 4: 1-Page Project Brief & Phase 1 Gate Verification (Prompt 6)

This step produces the formal charter for Phase 1. 

*(Note: The default standard is LaTeX `_Deliverables/1-Page-Brief.tex`. If you explicitly opted out of LaTeX, mention in your prompt to populate `_Deliverables/1-Page-Brief.md` instead).*

### 1. Send Prompt 6
Paste Prompt 6 into the chat:

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

### 2. Autonomous Gatekeeper Audit
The CEO will:
1. Populate `_Deliverables/1-Page-Brief.tex`, writing complete technical paragraphs for all 7 sections.
2. Detect your host operating system and invoke the gatekeeper script:
   - **Windows:** `cmd /c .agents\skills\skill_gate_phase1\run_win.cmd`
   - **macOS / Linux:** `bash ".agents/skills/skill_gate_phase1/run_mac.sh"`
3. Parse the return code and stdout:
   ```text
   [skill_gate_phase1] Validating deliverable: 1-Page-Brief.tex
   [SKILL_PASS] 1-Page-Brief.tex passed all Phase 1 structural and content checks.
   ```

> **Troubleshooting a `[SKILL_FAIL]`:** If the script reports exit code 2 (missing sections) or exit code 3 (unreplaced placeholders like `[INSERT ...]`), the CEO will identify the offending lines, rewrite the section, and re-run the check until it returns `[SKILL_PASS]`.

---

## Step 5: Multi-Turn State Persistence (`state.md`) & Phase 1 Git Checkpoint (Prompt 7)

To prevent context window bloat and memory loss across the 14-week semester, freeze the project state into `_Context/state.md`.

### 1. Send Prompt 7
Paste Prompt 7 into the chat:

```text
@_Context/Validated_Dossier.md @_Deliverables/1-Page-Brief.tex @.agents/skills/skill_git_sync/SKILL.md
CEO, generate our Multi-Turn Persistence file and save it to `_Context/state.md`.
Include:
- Student Dual-Axis Baseline & Developmental Delta.
- Approved Working Title, Bounded Domain, and Core Hypothesis.
- Target Deliverables Mapping & Publishing Level Assessment.
- SOTA Search Queries (TOON) & Next Actions for Class 3 (Phase 2 Literature Synthesis).

Once `_Context/state.md` is saved, execute `.agents/skills/skill_git_sync/SKILL.md` with message "feat: complete Phase 1 1-Page-Brief.tex and state.md".
```

### 2. Verify Output & Remote Sync
1. The CEO compiles and saves `_Context/state.md`.
2. The CEO executes `skill_git_sync` (`run_win.cmd` or `run_mac.sh`).
3. Confirm stdout reports:
   ```text
   [COMMITTED] feat: complete Phase 1 1-Page-Brief.tex and state.md
   [SKILL_PASS] Successfully committed and pushed to remote.
   ```

---

## Final Phase 1 Exit Audit (Class 2 Complete)

Check your workspace root in Antigravity to confirm Phase 1 completion:

| Artifact | Location | Expected State |
| :--- | :--- | :--- |
| **Project Charter** | `_Deliverables/1-Page-Brief.tex` | Fully filled (all 7 sections intact, zero placeholders, compilable in Overleaf or VS Code). |
| **Validated Dossier** | `_Context/Validated_Dossier.md` | Contains SOTA queries, candidate topics, and TOON tooling architecture. |
| **State Persistence** | `_Context/state.md` | Exists on disk (will unlock **State 2: Active Execution Mode** in Class 3). |
| **Gatekeeper Status** | `skill_gate_phase1` | Executed with `[SKILL_PASS]`. |
| **Git Baseline** | Remote Repository | Clean working tree; Phase 1 committed and pushed. |

**You are now cleared to advance to Phase 2 (Class 3: Deep Literature Synthesis & Benchmarking with `02_literature_coo`).**


<!-- ============================================================================== -->
<!-- DOC_END: path="_Docs_/Student_Guide-1.md" id=Student_Guide-1                   -->
<!-- ============================================================================== -->