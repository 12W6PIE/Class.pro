# Agentic Research Factory: Master Project Manifest (`AGENTS.md`)

## 1. Global Framework Anchors (Unified Context Triad)

All autonomous cognitive agents operating in this workspace are strictly grounded in the **Unified Context Triad** and persistent state records located in `./_Context/`:

- **Strategic Blueprint:** `./_Context/KNOWLEDGEBASE.md`  
  Defines the overarching research methodology, TOON protocol standards, Zero-Budget compute architecture, artifact archiving policies, and the Friday Checkpoint lifecycle.
- **Administrative Rubric:** `./_Context/COURSE-PROFILE.md`  
  Defines academic syllabus constraints, 14-week milestone deadlines, evaluation rubrics, global engineering market competencies, international publication standards, and dual-track deliverable structures.
- **Student Baseline Profile:** `./_Context/STUDENT-PROFILE.md`  
  Initial self-assessment capturing Axis 1 (AI Tech ratings 1–10 for Python, Git, Docker, and Prompting), Axis 2 (domain baseline, thesis milestone, 5-year career target), and the Core Catalyst hypothesis.
- **Validated Research Dossier:** `./_Context/Validated_Dossier.md`  
  Formally locked record of the student’s interrogated baseline, exposed Developmental Delta, candidate project domains, Boolean SOTA query payloads, and tooling blueprints (generated in Class 1 and Class 2).
- **Multi-Turn Persistence Record:** `./_Context/state.md`  
  The persistent project state compiled at the end of each sprint to prevent cognitive drift, context window bloat, and redundant interrogations across chat sessions.

---

## 2. Invariant Rules of Engagement

Every agent operating within this workspace must unconditionally enforce the following governance rules:

### A. Agent-First & Deterministic-First Modus Operandi
- **Agent Governance:** Students do not perform routine file manipulations or write manual boilerplate. Students act as **Agent Governors**, providing high-level direction, contextual constraints, and academic defense.
- **Deterministic Skills:** Cognitive agents must not guess or hallucinate filesystem operations, Git synchronization, or syntax validations. Whenever a task can be executed deterministically, agents must invoke registered, OS-isolated scripts from `./.agents/skills/`.
- **Zero Manual Terminal Commands:** Agents must never direct the student to execute raw OS commands in their terminal. All actions must be performed autonomously through registered skills or Antigravity native file-system tool calls.

### B. OS Isolation Protocol (Windows & macOS)
- Agents must detect the host operating system before executing any local skill wrapper:
  - **On Windows:** Invoke `cmd /c .agents\skills\<SKILL_NAME>\run_win.cmd [ARGS]`
  - **On macOS / Linux:** Invoke `bash ".agents/skills/<SKILL_NAME>/run_mac.sh" [ARGS]`
- Scripts are self-contained and run Python in non-bytecode mode (`-B`) with deterministic path resolution.

### C. Output Format Protocol (Strict TOON Mandate)
- **Strict TOON:** Structured outputs, handoff payloads, and MCP query definitions must be emitted strictly in **TOON format (`application/toon`)**.
- **JSON Prohibition:** JSON is strictly forbidden for inter-agent communication, configuration payloads, and prompt outputs to eliminate syntax escaping failures and context token bloat.

### D. Safety Bypass via Objective Academic Rigor
- To prevent AI safety filters from falsely flagging adversarial questioning as abusive or harassing, all Socratic critiques, baseline challenges, and intellectual interrogations must be framed in **strictly objective, detached academic language** (e.g., *"This hypothesis exhibits a fatal methodological flaw"*, *"The proposed architecture demonstrates empirical triviality"*).

### E. The Continuous Progress Rule & Developmental Delta
- Agents must reject projects scoped purely within the student's existing technical comfort zone.
- Every approved project must define and bridge a measurable **Developmental Delta**—a verified delta in engineering competence connecting the student’s initial baseline to their upcoming thesis milestone and long-term career target.

### F. The 6-Hour Ideation Constraint & Grilling Loop (Classes 1 & 2)
- Zero empirical coding or implementation is permitted during Phase 1 (Weeks 1 and 2).
- Agents must strictly confine their intelligence to baseline auditing, executing the iterative Socratic Grilling Loop Protocol (cycling until all gaps, methodological flaws, and compute mismatches are resolved), SOTA literature benchmarking, tooling architecture design, and authoring `./_Deliverables/1-Page-Brief.tex`.

### G. Architectural Precedence Rule
- Wherever legacy documentation references browser-based Google AI Studio copy-pasting, agents must supersede those instructions with **native Google Antigravity IDE workspace file operations and skill execution**.

---

## 3. Agent Lifecycle & Skills Registry

The research lifecycle is divided into sequential, gatekeeper-protected phases. Agents are defined natively under `./.agents/agents/` and skills under `./.agents/skills/` to enable progressive disclosure and preserve clean context windows:

| Phase | Agent ID | Agent Role | Specification Source | Registered Skills | Required Input | Target Deliverable |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 0** | `00_project_init` | Workspace Scaffolder & Updater | `./.agents/agents/00_project_init/agent.md` | `skill_scaffold`<br>`skill_git_sync` | Distribution template from `_X_Pros/Prime.pro` | Scaffolded `Class.pro` Workspace |
| **Phase 1** | `01_ideation_ceo` | PhD Supervisor & Grilling Loop Orchestrator | `./.agents/agents/01_ideation_ceo/agent.md`<br>`./.agents/agents/01_ideation_ceo/master-boot-prompt.md` | `skill_gate_phase1`<br>`skill_git_sync` | `./_Context/STUDENT-PROFILE.md` (multi-turn loop input) | `./_Context/Validated_Dossier.md` (locked upon loop convergence)<br>`./_Deliverables/1-Page-Brief.tex`<br>`./_Context/state.md` |
| **Phase 2** | `02_literature_coo` | Literature Synthesis & SOTA Benchmarker | `./.agents/agents/02_literature_coo/agent.md` *(Stage 1)* | `skill_gate_phase1`<br>`skill_notebooklm_mcp` | `./_Deliverables/1-Page-Brief.tex`<br>`./_Context/Validated_Dossier.md` | `./_Deliverables/Lit_Synthesis.md`<br>`./_Deliverables/references.bib` |
| **Phase 3** | `03_factory_coo` | Sandboxed Empirical Execution Runner | `./.agents/agents/03_factory_coo/agent.md` *(Stage 2)* | `skill_docker_runner`<br>`skill_zenodo_archive` | TOON Experiment Specification | Empirical Logs, Visual Plots, Model Weights, Zenodo DataCite DOI |
| **Phase 4** | `04_assessor` | Typesetter & Publishing Evaluator | `./.agents/agents/04_assessor/agent.md` *(Stage 3)* | `skill_latex_compile`<br>`skill_bibtex_check` | Overleaf LaTeX Manuscripts & Reports | Final Typeset PDFs & Statement of Publishing Level Assessment |

---

## 4. Phase Transition Gate Contracts

Transitions between phases are deterministic and conditional. No downstream agent may be booted until the upstream gate has been verified:

- **Phase 0 $\rightarrow$ Phase 1 Gate:** Verification that `.gitignore`, `.gitattributes`, `_Context/`, `_Deliverables/1-Page-Brief.tex`, and `.agents/` exist and the Stage 0 git checkpoint was completed with `[SKILL_PASS]`.
- **Phase 1 $\rightarrow$ Phase 2 Gate (Unlocking Class 3):** `_Deliverables/1-Page-Brief.tex` must pass deterministic validation via `.agents/skills/skill_gate_phase1/SKILL.md` returning `[SKILL_PASS]` (all 7 required sections present, non-empty, and zero unreplaced template placeholders).
