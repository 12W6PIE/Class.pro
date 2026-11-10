# Class 1 Execution Playbook (3 Hours)
**Goal:** From Vague Idea to Validated Research Dossier & Bounded Domain Selection.

> **Prerequisite:** Ensure you have booted `01_ideation_ceo` using Step 1 in `README.md`, and that you have filled out and saved `_Context/STUDENT-PROFILE.md`.

---

### PROMPT 1: STUDENT INTAKE & GRILLING LOOP INITIATION (CYCLE 1)
*(Copy and paste into Antigravity AI Chat after filling out and saving `_Context/STUDENT-PROFILE.md`)*

```text
@_Context/STUDENT-PROFILE.md @_Context/COURSE-PROFILE.md @_Context/KNOWLEDGEBASE.md
CEO, I have completed my Dual-Axis Professional Profile in `_Context/STUDENT-PROFILE.md`.

First, audit my profile for completeness. Then initiate the "Grilling Loop Protocol" (Cycle 1):
1. Expose my hand-waving assumptions and pinpoint my exact Developmental Delta at the intersection of Axis 1 (Tech) and Axis 2 (Domain/Milestones).
2. Stress-test my Alignment Hypothesis, compute constraints, and data modalities.
3. CRITICAL SCAFFOLDING MANDATE: For every exposed flaw, hardware mismatch, or skill gap, provide me with 3 to 4 concrete, scaffolded answer options (Option A, Option B, Option C, and Custom) based on the course stack and SOTA trends so I can evaluate trade-offs and defend my position.
4. Conclude your evaluation with a structured TOON `grilling_loop_status` payload listing:
   - cycle_number: 1
   - open_gaps_count: [INTEGER]
   - status: "ITERATING"
   - unresolved_issues: [LIST OF EXPOSED FLAWS]
   - convergence_achieved: false

Do not accept my baseline at face value. Interrogate me with options.
```

---

### PROMPT 1B: ITERATIVE DEFENSE & RE-AUDIT (LOOP TURN)
*(Copy and paste repeatedly for each interrogation cycle until CEO returns `convergence_achieved: true`)*

```text
CEO, here is my defense, selection of options, and architectural refinements for this grilling loop cycle:

1. DEFENSE & OPTION SELECTIONS:
   - Response to Issue 1: [Select Option A/B/C/Custom and defend your technical rationale]
   - Response to Issue 2: [Select Option A/B/C/Custom and defend your technical rationale]
   - Additional Gap Resolutions: [Address any further questions raised by the CEO]

2. HARDWARE & COMPUTE SANITY CHECK:
   - [Confirm how your selected approach strictly fits within your hardware baseline, e.g., local RTX 4070 12GB VRAM or free tiers]

3. TRAJECTORY ALIGNMENT:
   - [Confirm how this resolved baseline connects directly to your degree milestone and 3-5 year career target]

Re-audit my updated baseline against `COURSE-PROFILE.md` and `KNOWLEDGEBASE.md`.
Conclude with an updated TOON `grilling_loop_status` payload:
- If unresolved methodological flaws or contradictions remain: set `status: "ITERATING"`, update `unresolved_issues`, provide fresh 3-4 scaffolded options, and keep `convergence_achieved: false`.
- If and only if all gaps and contradictions are fully resolved: set `status: "CONVERGED"`, `open_gaps_count: 0`, and `convergence_achieved: true`, and instruct me to proceed to Prompt 2.
```

---

### PROMPT 2: DOSSIER FINALIZATION (LOOP CONVERGENCE GATE)
*(PRECONDITION: Send ONLY after the CEO has confirmed loop resolution with `convergence_achieved: true`)*

```text
@.agents/skills/skill_git_sync/SKILL.md
CEO, all grilling loop issues are resolved and `convergence_achieved: true` is confirmed.

1. Consolidate our final agreed baseline into a formal "Validated Research Dossier" and write it directly to `_Context/Validated_Dossier.md`. The dossier must record:
   - Validated Technical Baseline (Axis 1) and Domain Baseline (Axis 2).
   - Trajectory Alignment (Degree thesis milestone and 5-year target).
   - The specific "Developmental Delta" (the precise tools, architectures, and theoretical methodologies I MUST master this semester).
   - The Grilling Loop Audit Trail (number of completed cycles and resolved bottlenecks).
2. Read `.agents/skills/skill_git_sync/SKILL.md` and execute the safe git sync skill with message `"feat: lock in Validated_Dossier.md (grilling loop converged)"`.
```

---

### PROMPT 3: BOUNDED BRAINSTORMING & PERSISTENCE
*(Send once `_Context/Validated_Dossier.md` is saved and committed)*

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

Finally, append these 3 to 5 candidate ideas directly into `_Context/Validated_Dossier.md` under a new section `## Candidate Bounded Domains (Class 1 Output)` and execute `.agents/skills/skill_git_sync/SKILL.md` with message `"feat: append Class 1 candidate project ideas to Validated_Dossier.md"`.
```
