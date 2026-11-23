

Here is the complete, step-by-step classroom guide for students. It takes them from an empty workspace to a fully scaffolded research repository and guides them through the Socratic Grilling Loop session—**strictly through prompting in Google Antigravity** (enforcing the *"Zero Manual Terminal Commands"* standard).

---

# Student Playbook: Workspace Setup & Ideation Grilling Loop in Google Antigravity

Welcome to the AI Engineering Research Factory. In this course, you operate as an **Agent Governor**. You do not write repetitive boilerplate or run manual commands in a separate terminal. Instead, you direct autonomous cognitive agents and deterministic skills directly inside **Google Antigravity**.

---

## Phase 0: Workspace Setup & Cloning `Prime.pro` via Prompt

### 1. Open Your Personal Project Root
1. Launch **Google Antigravity**.
2. Open your assigned project repository folder (e.g., `W6-AI-PUB` or `Class.pro`).
3. Ensure the **AI Chat** panel is open on the right sidebar.

### 2. Prompt Antigravity to Clone the Upstream Distribution
In the default Antigravity Chat input box, paste the following prompt (replace `<PRIME_REPO_URL>` with your instructor’s repository URL or local network path):

PRIME_REPO_URL: https://github.com/W6-Class/Prime.pro.git

```text
Create the directory `_X_Pros` if it does not already exist, and clone the Prime repository into `_X_Pros/Prime.pro` by running:
git clone <PRIME_REPO_URL> _X_Pros/Prime.pro
```

> **Verification:** In the Antigravity File Explorer, verify that `_X_Pros/Prime.pro/Class.pro-TMPL-0/` is now visible.

---

## Phase 1: One-Time Workspace Scaffolding (Stage 0 Bootstrap)

Because your root workspace does not yet have `.agents/` or `_Context/`, you will instruct Antigravity's default runner to execute the Stage 0 scaffolding skill.

### 1. Execute the Bootstrap Prompt
In the Antigravity Chat input box, submit the command matching your operating system:

* **On Windows:**
  ```text
  Run the scaffolding script at _X_Pros/Prime.pro/Class.pro-TMPL-0/.agents/skills/skill_scaffold/run_win.cmd --stage 0
  ```
* **On macOS / Linux:**
  ```text
  Run the scaffolding script at _X_Pros/Prime.pro/Class.pro-TMPL-0/.agents/skills/skill_scaffold/run_mac.sh --stage 0
  ```

### 2. Verify Output & Registry Refresh
1. Look for the success signature in the chat output:
   ```text
   [SKILL_PASS] Workspace scaffolding complete.
   [COMMITTED] feat: initialize Stage 0 workspace baseline
   ```
2. Your workspace root will now contain:
   - `_Context/` (`COURSE-PROFILE.md`, `KNOWLEDGEBASE.md`, `STUDENT-PROFILE.md`)
   - `.agents/` (`agents/` and `skills/`)
   - `_Deliverables/` (`1-Page-Brief.tex` and `.md`)
   - `AGENTS.md` and `README.md`
   - `.gitignore` and `.gitattributes`
3. **Registry Refresh:** To ensure Antigravity indexes the newly deployed agents, press **`Ctrl+Shift+P`** (Windows) or **`Cmd+Shift+P`** (macOS), search for **`Developer: Reload Window`**, and press **Enter** (or type `/agents` in chat).

---

## Phase 2: The 15-Minute Intake Exercise (Analog Profile)

Do not trigger the AI CEO yet. Radically honest data is required to calculate your Developmental Delta.

1. In the Antigravity editor, open **`_Context/STUDENT-PROFILE.md`**.
2. Complete every section:
   - **Student Identity:** Your Felix login ID and current degree semester.
   - **Axis 1 (AI Tech):** Rate your skills honestly from **1 to 10** for Python, Git/GitHub, Docker, and Prompting. Specify your hardware (e.g., personal laptop vs. university lab RTX 4070 12GB VRAM).
   - **Axis 2 (Domain):** Your scientific domain, thesis milestone, and 3–5 year career target.
   - **The Core Catalyst:** Your 1–2 sentence **Vague Idea** and your **Alignment Hypothesis** (how you believe this project connects your current baseline to your career target).
3. **Save the file** (`Ctrl+S` / `Cmd+S`).

---

## Phase 3: Booting the Course CEO (`01_ideation_ceo`)

Now that `_Context/STUDENT-PROFILE.md` is populated, activate the PhD Supervisor Agent.

### 1. Send the Master Boot Command
In the Antigravity Chat, tag the agent and reference the boot prompt:

```text
@01_ideation_ceo @.agents/agents/01_ideation_ceo/master-boot-prompt.md
Initialize Phase 1 Ideation CEO using master boot prompt.
```

### 2. Verify the TOON System Status
The CEO will inspect `_Context/`, confirm that `state.md` and `Validated_Dossier.md` are absent, and output an acknowledgment strictly formatted in **TOON** (`application/toon`):

```toon
system_status: "READY"
current_date: "2026-10-26"
active_mode: "STATE 1A (Class 1: Intake & Grilling Loop Mode)"
managed_tooling: "Antigravity, NotebookLM MCP, Docker, Git/Zenodo, Overleaf"
mandatory_deliverables: "2x Dual-Deliverable Tracks (1a, 1b, 2a, 2b) with AI-Domain Exception"
publication_assessment_mandate: "ACKNOWLEDGED - Including Semi-Scientific Course Database Fallback"
continuous_progress_rule: "ACKNOWLEDGED"
safety_bypass_terminology: "ACTIVATED"
grilling_loop_protocol: "ACTIVATED"
loop_convergence_gate: "ENFORCED"
```

---

## Phase 4: Running the Socratic Grilling Loop Protocol (Prompts 1 & 1B)

### 1. Trigger the Adversarial Grilling Loop (Prompt 1)
Copy and paste this prompt directly into Antigravity Chat:

```text
@_Context/STUDENT-PROFILE.md @_Context/COURSE-PROFILE.md @_Context/KNOWLEDGEBASE.md
CEO, I have completed my Dual-Axis Professional Profile in `_Context/STUDENT-PROFILE.md`.

First, audit my profile for completeness. Then initiate the "Grilling Loop Protocol":
1. Expose my hand-waving assumptions and pinpoint my exact Developmental Delta at the intersection of Axis 1 (Tech) and Axis 2 (Domain/Milestones).
2. Stress-test my Alignment Hypothesis and hardware reality.
3. CRITICAL: For each challenge or question you pose, provide me with 3 to 4 concrete, scaffolded answer options (Option A, Option B, Option C, and Custom) based on the course stack, hardware constraints, and SOTA trends so I can evaluate the engineering trade-offs and defend my position.
4. Output your evaluation including a structured `grilling_loop_status` TOON block tracking open issues and convergence status.

Do not accept my baseline at face value. Interrogate me with options and enter Loop Cycle 1.
```

### 2. How to Read and Handle the CEO's Attack
- **Safety Bypass Phrasing:** The CEO will use detached, objective academic critiques (e.g., *"This hypothesis exhibits empirical triviality"*, *"Hardware allocation mismatch detected"*). Do not take it personally; this is designed to bypass UI safety filters and maintain scientific rigor.
- **Scaffolded Navigation:** For every exposed flaw, the CEO will provide:
  - **Option A:** Architectural pattern (e.g., RAG / MCP pipeline).
  - **Option B:** Compute-efficient pattern (e.g., local quantized SLM fine-tuning on RTX 4070).
  - **Option C:** Applied domain benchmark or empirical evaluation suite.
  - **Option D:** Custom / Hybrid defense of your own formulation.
- **The Grilling Loop Header:** The CEO will prefix responses with a loop status block:
  ```toon
  grilling_loop_status:
    cycle_number: 1
    open_gaps_count: 2
    status: "ITERATING"
    convergence_achieved: false
  ```

### 3. Iterating the Defense Loop (Prompt 1B)
You will not exit after turn 1. If `convergence_achieved: false`, evaluate the scaffolding options, make engineering trade-offs, and execute **Prompt 1B** to defend and counter-audit:

```text
CEO, here is my defense and gap resolution for Grilling Loop Cycle [INSERT CYCLE NUMBER]:

[TYPE YOUR DETAILED DEFENSE FOR EACH CHALLENGE, STATING WHICH SCAFFOLDED OPTIONS (A, B, C, or Custom) YOU ADOPT AND WHY]

Re-evaluate my project baseline against the Context Triad. If critical flaws or developmental gaps remain, issue the next interrogation cycle with scaffolded options. If all issues and gaps are resolved, confirm loop convergence with `convergence_achieved: true`.
```
*(Repeat Prompt 1B until the CEO emits `convergence_achieved: true` and confirms all gaps are resolved.)*

---

## Phase 5: Concluding the Loop & Locking the Dossier (Prompt 2)

### 1. The Loop Convergence Gate
Do NOT execute Prompt 2 until the CEO explicitly outputs `convergence_achieved: true` in the `grilling_loop_status` block. Executing Prompt 2 prematurely will be rejected by the CEO.

### 2. Lock In the Validated Research Dossier (Prompt 2)
Once convergence is verified, submit **Prompt 2** to write and commit your dossier:

```text
@.agents/skills/skill_git_sync/SKILL.md
CEO, based on my defenses and our discussion above:
1. Compile our findings into a formal "Validated Research Dossier" and write it directly to `_Context/Validated_Dossier.md`. The dossier must record:
   - Validated Technical Baseline (Axis 1) and Domain Baseline (Axis 2).
   - Trajectory Alignment (Degree thesis milestone and 5-year target).
   - The specific "Developmental Delta" (the precise tools, architectures, and theoretical methodologies I MUST master this semester).
2. Read `.agents/skills/skill_git_sync/SKILL.md` and execute the safe git sync skill with message "feat: lock in Validated_Dossier.md".
```

> **Verification:** Confirm that `_Context/Validated_Dossier.md` has been created in your editor and that the agent output displays `[SKILL_PASS] Successfully committed and pushed to remote.`

---

## Phase 6: Bounded Brainstorming (Prompt 3)

Complete the final stage of Class 1 by deriving 3 to 5 viable project ideas grounded in your newly validated dossier.

### 1. Run Candidate Domain Ideation
Paste **Prompt 3** into the chat:

```text
@_Context/Validated_Dossier.md @.agents/skills/skill_git_sync/SKILL.md
CEO, reading my validated dossier, brainstorm 3 to 5 Bounded Domains and Project Ideas for this semester.

Constraints:
1. Each idea must force me to bridge the gaps in my Developmental Delta.
2. Each idea must have realistic potential for publication in English-language JCR Q1–Q4 journals, conference proceedings (e.g., OCETA Connect 2027), or the internal Semi-Scientific Course Publishing Service repository.
3. If my domain is "AI Technology" itself, structure the idea so the AI Tech Utilization Report forms the primary empirical foundation of the manuscript.

For each idea, define:
- Bounded Domain (In-scope vs. out-of-scope boundaries).
- Core Hypothesis & Expected Scientific Delta.
- How it advances my career trajectory.

Finally, append these 3 to 5 candidate ideas directly into `_Context/Validated_Dossier.md` under a new section `## Candidate Bounded Domains (Class 1 Output)` and execute `.agents/skills/skill_git_sync/SKILL.md` with message "feat: append Class 1 candidate project ideas to Validated_Dossier.md".
```

---

## Summary Checklist: Are You Done with Class 1?

Before closing your laptop for Class 1, verify:
- [ ] `_Context/STUDENT-PROFILE.md` contains your honest ratings and goals.
- [ ] The **Grilling Loop** ran through full iteration until `convergence_achieved: true`.
- [ ] `_Context/Validated_Dossier.md` exists and contains your locked Developmental Delta plus 3–5 bounded candidate domains.
- [ ] Antigravity executed `skill_git_sync` with `[SKILL_PASS]`.
- [ ] **No empirical code was written** (strictly observing the 6-Hour Ideation Constraint).

*You are now fully prepared for Class 2 (SOTA Literature Queries, Tooling Blueprints, and `1-Page-Brief.tex` compilation).*

