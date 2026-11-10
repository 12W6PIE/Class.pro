# Agentic Research Factory — Student Project Workspace (`Class.pro`)

Welcome to your AI Engineering research project workspace. This project repository operates strictly under the **Agent-First, Deterministic-First** engineering paradigm. 

Throughout this course, you will not perform routine manual development or boilerplate coding. Instead, you operate as the **Agent Governor**: orchestrating autonomous AI agents, defending scientific hypotheses under adversarial critique, and supervising deterministic skills within **Google Antigravity IDE**.

---

## 1. Operating Rules of Engagement

1. **Zero Manual Terminal Commands:** Do not run terminal scripts or Git commands by hand. All operational tasks (scaffolding, Git commits, phase validations) are executed by Agents invoking deterministic wrappers in `.agents/skills/`.
2. **Context Triad Grounding:** All agent reasoning is anchored in the three local context files located in `_Context/`:
   - `STUDENT-PROFILE.md`: Your technical baseline and career trajectory.
   - `KNOWLEDGEBASE.md`: Strategic engineering methodology and architectural patterns.
   - `COURSE-PROFILE.md`: University syllabus constraints, grading rubrics, and deliverable specifications.
3. **Strict TOON Protocol:** All structured agent handoffs, tooling configurations, and database queries must use **TOON (`application/toon`)**. JSON is strictly forbidden to eliminate token bloat and escaping errors.
4. **The 6-Hour Ideation Constraint:** During Classes 1 and 2, no empirical project code may be written. The focus is exclusively on problem scoping, SOTA benchmarking, and locking in the formal 1-Page Project Brief.
5. **Continuous Progress Rule:** Agents will not accept projects scoped only to your current baseline. You must identify and bridge a **Developmental Delta** (the technical gap between your current skills, your degree milestone, and your 3–5 year career target).

---

## 2. Workspace Directory Structure

```text
Class.pro/
├── AGENTS.md                   # Master Agent Manifest, lifecycle state, and skills registry
├── README.md                   # This operational guide
├── .gitignore                  # Git protection rules (tracks _X_Pros/ folder, ignores its contents)
├── .gitattributes              # Cross-platform line ending normalization (LF for .sh)
│
├── _Context/                   # Unified Context Triad & persistence state
│   ├── STUDENT-PROFILE.md      # Dual-axis intake audit (Skills vs. Domain)
│   ├── KNOWLEDGEBASE.md        # Strategic methodology and architectural patterns
│   ├── COURSE-PROFILE.md       # Administrative rubric, deliverables, and timeline
│   ├── Validated_Dossier.md    # Class 1 output (Interrogated baseline & candidate topics)
│   └── state.md                # Multi-turn persistence state across class sessions
│
├── _Deliverables/              # Formal course milestones and research artifacts
│   └── 1-Page-Brief.tex        # LaTeX project charter (Phase 1 gate requirement)
│
├── .agents/                    # Native Google Antigravity Agent & Skill Definitions
│   ├── agents/                 # Cognitive definitions, personas, and execution playbooks
│   │   ├── 00_project_init/    # Workspace scaffolding and maintenance agent
│   │   │   └── agent.md        # Antigravity agent specification with YAML frontmatter
│   │   └── 01_ideation_ceo/    # PhD Strategic Supervisor & Ideation Grilling Agent
│   │       ├── agent.md        # Antigravity agent specification with YAML frontmatter
│   │       ├── master-boot-prompt.md # 3-state boot sequence
│   │       ├── prompts-class-1.md    # Class 1 execution playbook (Prompts 1, 2, 3)
│   │       └── prompts-class-2.md    # Class 2 execution playbook (Prompts 4, 5, 6, 7)
│   │
│   └── skills/                 # OS-isolated deterministic execution engines
│       ├── skill_scaffold/     # Deploys upstream course templates non-destructively
│       ├── skill_git_sync/     # Validates gitignore, auto-configures author, commits & pushes
│       └── skill_gate_phase1/  # Deterministic validator for 1-Page-Brief.tex
│
└── _X_Pros/                    # Tracked external projects folder (contents ignored; contains Prime.pro clone)
```

---

## 3. Phase 1 Execution Workflow (Classes 1 & 2)

### Step 00: One-Time Workspace Bootstrap (Fresh Workspace Setup)
If your active workspace root does not yet have `.agents/` or `_Context/`:
In Antigravity default chat, submit:
- **On Windows:**
  `Run the scaffolding script at _X_Pros/Prime.pro/Class.pro-TMPL-0/.agents/skills/skill_scaffold/run_win.cmd --stage 0`
- **On macOS / Linux:**
  `Run the scaffolding script at _X_Pros/Prime.pro/Class.pro-TMPL-0/.agents/skills/skill_scaffold/run_mac.sh --stage 0`
*This deploys all templates and executes the automatic Stage 0 Git commit.*

### Step 0: Complete the Analog Intake (Class 1 — 15 Mins)
Before interacting with the AI CEO:
1. Open `_Context/STUDENT-PROFILE.md` in the Antigravity editor.
2. Complete your ratings (1–10 scale for Python, Git, Docker, Prompting), target milestones, and initial vague idea.
3. Save the file.

### Step 1: Boot the Ideation CEO (Antigravity AI Chat)
Switch Antigravity AI Chat to **Agent Mode** and activate `01_ideation_ceo` (via the `/agents` menu, dropdown, or direct mention):
```text
@01_ideation_ceo @.agents/agents/01_ideation_ceo/master-boot-prompt.md
Initialize Phase 1 Ideation CEO using master boot prompt.
```
The CEO will inspect `_Context/` and respond with a TOON status report confirming system readiness.

### Step 2: Execute Class 1 Playbook (From Vague Idea to Validated Dossier)
Open `.agents/agents/01_ideation_ceo/prompts-class-1.md` and execute the prompts sequentially in the chat, engaging with the iterative Grilling Loop:
- **Prompt 1 (Intake & Grilling Loop Trigger):** Initiates Cycle 1 of the adversarial Socratic Grilling Loop. The CEO audits your baseline, identifies critical methodological flaws and hardware mismatches, and provides 4-option scaffolded alternatives.
- **Prompt 1B (Iterative Defense & Counter-Audit):** Your repeating loop turn. Defend your engineering choices, evaluate trade-offs, or pivot. Continue cycling through Prompt 1B iterations until the CEO confirms all critical flaws and Developmental Delta gaps are fully resolved (`convergence_achieved: true`).
- **Prompt 2 (Loop Convergence & Dossier Finalization):** Triggered only after the grilling loop converges. Compiles resolved defenses and locks in `_Context/Validated_Dossier.md` (committed via `skill_git_sync`).
- **Prompt 3 (Bounded Brainstorming & Persistence):** Generates 3 to 5 publication-targeted candidate ideas bridging your resolved Developmental Delta, appends them to your dossier, and commits the state.

---

### Step 3: Execute Class 2 Playbook (SOTA Alignment & Deliverable Gate)
*Note: If starting Class 2 in a fresh chat window, repeat Step 1 to boot the CEO. It will automatically detect `Validated_Dossier.md` and resume in State 1B.*

Open `.agents/agents/01_ideation_ceo/prompts-class-2.md` and execute the prompts sequentially:
- **Prompt 4 (SOTA Alignment & MCP Queries):** Formulates academic Working Titles and Boolean search queries for Web of Science, Scopus, and OpenAlex, outputting structured TOON payloads for literature indexing.
- **Prompt 5 (Tooling Strategy & Sandboxing):** Formulates local compute limits, Docker isolation, and Zenodo DOI archiving plans.
- **Prompt 6 (1-Page Project Brief & Gate Verification):** Writes the compilable LaTeX charter to `_Deliverables/1-Page-Brief.tex` and executes `skill_gate_phase1` to deterministically verify all sections.
- **Prompt 7 (State Persistence & Checkpoint):** Freezes project state into `_Context/state.md` and syncs your repository via `skill_git_sync`.

---

## 4. Phase Gating & Maintenance

### Phase Gate Check (Unlocking Phase 2)
To advance to Phase 2 (Literature Synthesis & Empirical Setup in Class 3), your project brief must pass deterministic inspection:
- The LaTeX file `_Deliverables/1-Page-Brief.tex` must compile cleanly without missing blocks.
- All 7 mandatory structural sections must be present.
- All template placeholders (`[INSERT ...]`, `[YES/NO ...]`) must be replaced with approved technical text.
- `.agents/skills/skill_gate_phase1/` must return `[SKILL_PASS]`.

### Upstream Course Material Updates
When the instructor releases new course phases or tools (e.g., `Class.pro-TMPL-1`), instruct Antigravity AI Chat:
```text
Execute skill_scaffold for stage 1.
```
The agent will pull upstream changes from `_X_Pros/Prime.pro` and deploy the new stage files while strictly preserving your work in `_Context/` and `_Deliverables/`.

---

## 5. Troubleshooting & Support

- **Script Permissions on macOS/Linux:** If wrapper scripts fail to run, instruct Antigravity:  
  `Run chmod +x on all .sh files in .agents/skills/`.
- **Git Author Warnings:** If Git throws identity warnings on lab workstations, `skill_git_sync` will automatically fall back to local project-scoped defaults (`AI Engineering Student`).
- **LaTeX Compilation Issues:** The `1-Page-Brief.tex` template uses standard packages (`geometry`, `titlesec`, `enumitem`). It is designed to compile out-of-the-box in both local TeX installations and Overleaf.

---

## 6. How to Call & Govern Agents in Google Antigravity

All course engineering is governed through the Antigravity AI Chat interface using the native `.agents/` workspace architecture.

### Activating an Agent (Interactive Switch)
* **Via Slash Command:** In the chat input box, type `/agents` and press `Enter`. Use the arrow keys (`↑` / `↓`) to highlight the desired agent (e.g., `00_project_init`, `01_ideation_ceo`) and press `Enter`.
* **Via UI Dropdown:** In the Antigravity Chat panel, click the **Agent Selector dropdown** next to the model picker in the prompt bar and select the agent.

### Direct Chat Routing (`@` Mention)
Within an active chat session, route a specific command or file review directly to an agent:
```text
@01_ideation_ceo Review my _Context/STUDENT-PROFILE.md and initiate the Socratic Grill.
```
