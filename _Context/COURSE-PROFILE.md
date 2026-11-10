[[COURSE-PROFILE]]

COMMENT FOR AI: This document provide the base context for student project but can be overwritten by the students project profile if the student can justify otherwise (see STUDENT-PROFILE.md).

Even if students select project topic which is not scientific per se but rather domain specific applied AI project or domain engineering project the deliverables must be in scientific format like to teach them to communicate science and engineering style documents.

# **Course Profile: Syllabus, Constraints, & Administrative Rubric**

*This document defines the strict administrative boundaries, institutional requirements, grading criteria, and temporal logistics for the AI Engineering course. The AI CEO Agent must cross-reference all student ideas against this document to ensure feasibility and academic compliance.*

---

## **1. Course Identity & Temporal Logistics**
*   **Target Audience:** Undergraduate (Bachelor’s) and Graduate (Master’s) Engineering students.
*   **Semester Duration:** 3.5 months (14 weeks total).
*   **Class Format:** 3-hour laboratory/workshop classes per session.
*   **Core Objective:** Guide students from a vague idea to a functional AI-augmented project, culminating in a detailed AI tech utilization report and a structured scientific manuscript draft.
*   **The 6-Hour Ideation Constraint:** The first two classes (Weeks 1 & 2, max 6 hours total) are strictly insulated from empirical coding. They are entirely dedicated to moving from a "Vague Idea to Identified Topic, Domain, and Preliminary Title," culminating in the 1-Page Project Brief.

## **2. Institutional Competency Mandate**
All projects must rigorously enforce the formal institutional graduate learning outcome:
*   *"The graduate can retrieve, critically assess, and synthesize information from professional literature and specialized sources, including English-language databases (e.g., Web of Science, Scopus) as well as trust worthy online sources..."*
*   **Enforcement Rule:** No project idea can be approved unless its theoretical baseline can be cross-referenced and validated against English-language JCR Q1/Q2 indexed literature via Web of Science, Scopus, or OpenAlex or JCR Q3 or Q4 indexed literature or other peer-reviewed sources or other reliable online sources if project is domain specific and the domain does not have JCR Q1/Q2 indexed literature or the project is not explicitly/rigid scientific but rather domain specific applied AI or specific domain engineering. In delivered documents all substantial claims must reference sources unless they are self-evident or based on the student's own delivered software/code or research/analysis data. Text content of the document must be supported by visual material like tables graphs or images, screenshots, diagrams, code snippets, etc.

## **3. Physical Limits & Zero-Budget Strategy**
The AI CEO must reject any project proposal that requires massive enterprise compute or paid APIs unless student has an explicit paid access or student has access to such resources or systems or infrastructure. Projects are viable within the following basic constraints unless student can justify otherwise:
*   **Local Lab Compute:** University Computer Lab equipped with Nvidia RTX 4070 GPUs (12GB VRAM). (Requires aggressive quantization, SLMs, or smart routing for local inference).
*   **Student Hardware Reality:** Personal laptops (MacBook M-series, standard Windows machines).
*   **Approved Freemium/Student Tier Stack:** Google AI Studio (Gemini Pro), NotebookLM, GitHub Copilot Student Plan, Google Search AI Mode, Google Colab (Free), Docker (Local), and Ollama (Local open-weight models). 
*   **Archiving:** GitHub linked to Zenodo (strict 50GB limit for dataset/code archiving and DOI generation).

## **4. The Grading Rubric & Mandatory Deliverables**
To pass this course, students must successfully orchestrate the AI workshop and submit formal deliverables typeset in LaTeX (recommended via Overleaf/VS Code). Students who explicitly opt out of LaTeX due to lack of prior experience may submit in structured academic Markdown (`1-Page-Brief.md`), adhering strictly to formal publication structure and visual formatting. The AI CEO must trajectory-lock all students toward these exact outputs:

**Set 1: AI Technology & Methodology Track**
*   **1(a) AI Tech Utilization Report:** A highly detailed "how-to" manual documenting the exact AI tools, orchestration methods, sandboxing, and prompt frameworks used to build the project.
*   **1(b) AI Tech Draft Manuscript:** A draft publication manuscript focusing on the novel AI engineering methodologies built or utilized during the project.

**Set 2: The Project Domain Track**
*   **2(a) Domain Deliverables Report:** Formal documentation of the actual software/system deliverables of the chosen domain (e.g., the actual healthcare diagnostic app, or the climate model).
*   **2(b) Domain Draft Manuscript:** A draft publication manuscript focusing on the scientific findings or results within that specific topic scope.

*   **The AI Domain Exception Rule:** If a student’s entire project domain is purely "AI Technology" (e.g., they are researching MCP orchestration frameworks), Deliverable 1(a) fulfills the primary project requirement, and a single comprehensive manuscript may be generated from it.

## **5. The Publishing Level Assessment Rule**
This is a mandatory administrative requirement for the end-of-semester submission.
*   Every student manuscript must include a formal **Statement of Assessment** generated by the AI CEO evaluating against the 4-tier negotiation hierarchy:
    1. **Tier 1 (JCR Q1/Q2):** High-impact international peer-reviewed journals.
    2. **Tier 2 (JCR Q3/Q4):** Indexed peer-reviewed international journals.
    3. **Tier 3 (Proceedings):** International conference proceedings (e.g., OCETA Connect 2027).
    4. **Tier 4 (Course Repository):** Internal Semi-Scientific Course Publishing Service database (for applied domain engineering or solid methodology lacking novel SOTA breakthroughs).

## **6. Semester Milestone Schedule**
The AI CEO must govern the weekly `state.md` logs according to this pacing:
*   **Weeks 1 (Classes 1-2):** Ideation Phase. Completion of the Dual-Axis Profile, Socratic Grilling Loop & Dossier Convergence, TOON Tooling setup, and Final 1-Page Project Brief in LaTeX.
*   **Week 2 (Class 3):** In-Depth Research. Automated NotebookLM literature synthesis and finalizing the empirical baseline.
*   **Weeks 3 - 10:** The "Factory" Execution. Docker-sandboxed empirical coding, data gathering, and weekly Friday `state.md` checkpoints.
*   **Weeks 11 - 13:** Manuscript Drafting. Heavy use of Overleaf/LaTeX, Zotero citations, and continuous AI structural audits.
*   **Week 14:** Archiving & Final Submission. Zenodo DataCite DOIs minted, final Publishing Assessment attached, and dual-deliverables submitted for grading.
