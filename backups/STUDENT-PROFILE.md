<!-- 
COMMENT FOR AI AGENT: 
This document serves as Round 0 Input for the iterative Grilling Loop Protocol.
Students are at an early stage and cannot be expected to know advanced AI Engineering architectures or tooling workflows upfront. Their target goals and initial ideas may be vague or technically naive. 
Your role during the Grilling Loop Protocol is NOT to reject them, but to aggressively expose gaps across iterative inquiry cycles AND simultaneously scaffold them by suggesting concrete technical architectures, methodologies, and tooling options (based on KNOWLEDGEBASE.md and COURSE-PROFILE.md) until all project handling and deliverable gaps are fully resolved.
-->

# Student Dual-Axis Professional Profile

> **Instruction:** Complete this form during the 15-minute intake exercise. Be radically honest about your current skill levels and hardware constraints. This profile serves as Round 0 Input for the iterative Grilling Loop Protocol: your AI Project CEO will cross-examine your baseline across multiple interrogation cycles to identify and resolve your Developmental Delta before locking in your research dossier.
> 
> *Privacy Notice:* Do not enter your real name or personal contact data. Use only your university Felix server login ID.

---

### **Student Identity & Study Level**
- Felix Login ID: 12
- Current Degree & Semester: Bachelor's degree (Computer Science), 3rd year, 5th Semester

---

### **Axis 1: AI Technology & Engineering Stack**

#### 1. Current Technical Baseline (Scale: 1 = Beginner to 10 = Expert)
*Core Stack (Mandatory to rate):*
- Python: [7/10]
- Git / GitHub: [8/10]
- Docker: [3/10]
- Prompt Engineering & LLM Utilization: [9/10]

*Additional Languages, Frameworks & Libraries:*
- PyTorch: [6/10]
- Scikit-Learn: [6/10]
- SQL: [6/10]
- Linux / Bash: [5/10]

*Not yet practised (target skills for this semester):*
- IR / RAG evaluation (Recall@k, MRR, nDCG, RAGAS-style faithfulness): [new]
- LLM-as-judge calibration & statistical testing (Cohen's κ, bootstrap CIs, paired tests): [new]
- LLMOps (MLflow experiment tracking, Langfuse tracing, reproducible Dockerised pipelines): [new]
- Quantization trade-off analysis (GGUF Q4/Q5/Q8, RAM and VRAM budgeting): [new]

*Baseline Evidence & Calibration (Grilling Loop Cycles 1-3):*
- Rating status: self-ratings were recalibrated to an honest baseline (Python 7/10, Git/GitHub 8/10, Docker 3/10, Prompt Engineering 9/10, PyTorch 6/10, Scikit-Learn 6/10, SQL 6/10, Linux/Bash 5/10); accepted by CEO as self-assessment to be validated through deliverables.
- Calibration note: Docker (3/10) and Linux/Bash (5/10) are explicitly accounted for as practical growth areas alongside the LLMOps containerization goals; Prompt Engineering (9/10) remains an unverified self-assessment.
- Note: the Developmental Delta is defined primarily by the "[new]" skills above plus hands-on reproducible Docker workflows, so project scope remains grounded in realistic student capabilities.
- Diagnostic reference answers (to be defended orally by the student):
  1. **Ollama container setup (CPU local vs. NVIDIA GPU cloud):** locally on Windows 11 CPU-only hardware, run Ollama natively or in Docker without GPU flags; in NVIDIA GPU environments, install the NVIDIA driver and `nvidia-container-toolkit`, register the runtime (`nvidia-ctk runtime configure --runtime=docker`, restart Docker), then run `docker run -d --gpus all -v ollama:/root/.ollama -p 11434:11434 ollama/ollama` and verify via `nvidia-smi`, `ollama ps`, and `ollama run <model> --verbose`.
  2. **PyTorch AMP / gradient accumulation / checkpointing:** AMP uses `torch.autocast(device_type="cuda", dtype=torch.bfloat16 or torch.float16)`, plus `torch.amp.GradScaler("cuda")` for fp16 loss scaling. Gradient accumulation divides the loss by N and calls `optimizer.step()` / `zero_grad()` every N micro-batches. Training checkpoints save the model, optimizer, scheduler and scaler `state_dict`s together with the epoch/step and RNG states. Activation checkpointing (`torch.utils.checkpoint`) trades extra compute for lower memory use.
  3. **RAG metrics:** *Faithfulness* is the share of claims in the answer that are supported by the retrieved context (grounding / hallucination). *Answer relevance* measures how directly the answer addresses the question, regardless of correctness. *Context recall* is the share of the reference answer's information that is present in the retrieved context (retrieval completeness). *Context precision* is the rank-weighted share of retrieved chunks that are relevant.

#### 2. Target Technical Goals
*(Note for Students: If you do not know advanced AI architectures or frameworks yet, simply describe what you want the system to do functionally. Your AI CEO will analyze your goals and scaffold concrete options during the Grilling phase.)*

- **Project Target (This Semester):** What specific AI architecture, workflow, or framework do you need to master to execute this project?
  - *Response:* Beyond implementing a local RAG pipeline (structure-aware chunking, dense vs. hybrid BM25+dense retrieval with cross-encoder reranking, embedding models, Ollama inference of GGUF-quantized open-weight models), the Developmental Delta is (a) **evaluation science**: building a gold-labelled QA benchmark, IR metrics (Recall@k, MRR, nDCG), LLM-as-judge plus NLI-based claim verification calibrated against human labels (Cohen's κ), closed-book contamination control, bootstrap confidence intervals and paired significance tests, ablation design; and (b) **LLMOps**: MLflow experiment tracking, Langfuse tracing, fully reproducible Dockerised experiment runs with pinned model digests and seeds, and quantization/VRAM budgeting.
- **Diploma Target (Graduation Milestone):** What AI competencies must you prove for your final thesis?
  - *Response:* Ability to design, implement, and empirically evaluate an LLM-based system against explicit baselines (closed-book no-retrieval; naive fixed-size chunking + dense retrieval; larger/higher-precision model reference) using reproducible experiments, calibrated metrics, statistical testing, and literature-backed methodology. Agentic / self-correcting RAG (CRAG, Self-RAG) is deferred as a candidate thesis extension.
- **Career Target (3-5 Years):** What advanced engineering capabilities do you need for your target industry role?
  - *Response:* Building and deploying production-grade LLM applications: RAG optimization, model serving and quantization, containerized deployment (Docker), experiment tracking, tracing/monitoring and automated evaluation regression in CI (all exercised this semester), later extended with agentic workflows.

#### 3. Hardware & Compute Reality
- Primary Machine: Windows 11 Home Single Language Laptop - Lenovo IdeaPad Slim 3 15ABR8, AMD Ryzen 7 5825U (8 cores, 16 threads), 16 GB RAM (13.8 GB usable), integrated AMD Radeon Graphics (2 GB VRAM, no dedicated GPU)
- Available Accelerated Compute: No local dedicated GPU; Google Colab Free Tier T4 (16 GB VRAM) for cloud GPU batch runs when needed
- Compute Split Plan:
  - Laptop CPU (AMD Ryzen 7 5825U, 13.8 GB usable RAM): document ingestion, chunking, embedding, BM25/dense indexing, reranking, all **retrieval-only metrics** (Recall@k, MRR, nDCG need no LLM), NLI verification, and local quantized CPU inference / smoke tests with compact 3B-8B GGUF models in Ollama (e.g., Qwen2.5-3B, Llama-3.2-3B).
  - Google Colab Free Tier T4 (16 GB VRAM): accelerated sharded and resumable batch generation runs with results checkpointed to Drive/GitHub for larger model and quantization sweeps.
  - Generation budget: Study 1 ≈ 3 retrieval configs × 1 model × 300 Q ≈ 900 generations. Study 2 ≈ 7 model/quant conditions × 300 Q × 2 (RAG vs. closed-book) ≈ 4,200 generations, executed in sharded batches across local CPU and Colab Free T4.
  - Judging: NLI verifier (DeBERTa-v3 MNLI) on laptop CPU or Colab GPU; Gemini free-tier judge batched over several days within rate limits (public corpus only, so there is no data-protection issue).

---

### **Axis 2: Professional Domain & Research Interest**

#### 1. Target Scientific / Engineering Domain
- Broad Field: Computer Science / AI Technology (AI-Domain Exception claimed)
- Specific Sub-Domain: Empirical evaluation of fully local Retrieval-Augmented Generation (RAG) for question answering over educational documents; specifically, the interaction of model quantization/size with retrieval strategy on faithfulness and abstention under consumer laptop hardware constraints (AMD Ryzen 7 5825U, 16 GB RAM, integrated AMD Radeon Graphics with 2 GB VRAM).

#### 2. Domain Knowledge Baseline
- Formal Coursework or Practical Experience: University Computer Science coursework through semester 5 (standard curriculum: programming, algorithms & data structures, databases, operating systems, linear algebra, probability & statistics; exact course names to be confirmed by the student), practical project experience, and extensive self-study (online courses, documentation, personal projects). No formal background in information retrieval evaluation or experimental statistics yet (part of the Developmental Delta).

#### 3. Degree Completion Milestone
- Planned Bachelor's / Master's Thesis Area: Not yet decided. Tentative direction: applied LLM systems, namely empirical evaluation of RAG under resource constraints, with a possible extension to agentic / self-correcting RAG; this semester's project is intended to define the thesis topic.

#### 4. Career Target
- Target Professional Role: Not yet decided. Tentative direction: AI / LLM Engineer (Applied AI).

---

### **The Core Catalyst**

#### 1. The Vague Idea (1-2 Sentences)
> *What do you want to build, research, or explore this semester?*
- *Response:* Build a fully local RAG question-answering system over the openly licensed OpenStax textbook *Introduction to Python Programming* (CC BY 4.0, English) and release a human-verified QA benchmark (~300 questions with gold evidence spans, ~15% unanswerable) to measure, in two controlled studies, (1) how retrieval strategy (fixed vs. structure-aware chunking; dense vs. hybrid + reranking) affects retrieval quality and grounded answers, and (2) how quantization level (Q4/Q5/Q8) and model size (3B/8B, plus 14B Q4) affect faithfulness, correctness, and abstention under consumer laptop hardware constraints (16 GB RAM, 2 GB integrated VRAM, CPU inference with Colab T4 fallback), controlling for parametric memorisation with a closed-book baseline. "Local" is a design constraint (no external API calls in the inference path; containers run with `--network none`) and is not a privacy claim.

#### 2. The Alignment Hypothesis (1 Sentence)
> *How does building this specific project bridge your current technical baseline to your Degree Milestone and Career Target?*
- *Response:* Moving from general Python and Git skills with introductory Docker experience (3/10) to calibrated RAG evaluation (IR metrics, judge-human agreement, contamination control, significance testing) and LLMOps (quantization and memory budgeting, Dockerised workflows, experiment tracking, tracing, reproducibility) gives me the reproducible-experiment methodology my thesis requires and the serving and evaluation skills of an applied LLM Engineer, with a released benchmark and paper as evidence (target: Tier 3 proceedings, stretch Tier 2).

#### 3. Grilling Loop Audit Trail (Option Selections)
*Cycle 1:*
- I1 Baseline: Option B + C (calibration rubric + diagnostics; reference answers recorded above)
- I2 Developmental Delta: Option D = A (evaluation science) + B (LLMOps); C (agentic RAG) deferred to thesis
- I3 Novelty: Option D = B (quantization × retrieval study) + C (released benchmark); target Tier 3, stretch Tier 2
- I4 Data: Option A (open CC-BY corpus; LLM-drafted, human-verified QA)
- I5 Metrics: Option D (IR metrics + LLM judge calibrated on ~100 human-labelled answers + bootstrap CIs / paired tests)
- I6 Compute: Option A + C (Windows 11 Ryzen 7 5825U laptop dev and CPU runs; compact <=8B primary; Colab Free T4 fallback)
- I7 Privacy: Option A (design constraint only, no privacy claim)
- I8 Deliverables: Option A (AI-Domain Exception: single manuscript from 1(a); benchmark archived on Zenodo with DOI)

*Cycle 2-3:*
- C1 Baseline calibration: Option A/C hybrid - self-ratings recalibrated to honest levels (Python 7, Git/GitHub 8, Docker 3, Prompting 9, PyTorch/Scikit-Learn/SQL 6, Linux/Bash 5); reference diagnostic answers recorded; Developmental Delta defined by the "[new]" skills and practical Docker/LLMOps containerization
- C2 Hardware Reality: Real primary machine confirmed as Windows 11 Lenovo IdeaPad Slim 3 15ABR8 (AMD Ryzen 7 5825U, 16 GB RAM / 13.8 GB usable, integrated AMD Radeon Graphics 2 GB VRAM, no dedicated GPU), with Google Colab Free T4 fallback for GPU batch runs
- C3 Corpus: Option A (OpenStax *Introduction to Python Programming*, CC BY 4.0, English; English embedders such as `bge-base-en-v1.5` / `nomic-embed-text`)
- N4 Contamination: Option D (closed-book no-retrieval condition + ~15% unanswerable questions to measure parametric leakage and abstention)
- N5 Experimental design: Option A (Study 1: retrieval ablation at fixed 8B Q4_K_M; Study 2: {3B, 8B} × {Q4_K_M, Q5_K_M, Q8_0} + 14B Q4_K_M at the best Study 1 retrieval config)
- N6 Judge reliability: Option B + C (Gemini free-tier judge + DeBERTa-v3 MNLI claim verifier, both calibrated against ~100 human-labelled answers via Cohen's κ)
- N7 Reproducibility: Option A + B (temperature 0, fixed seed, pinned model digests, all runs logged in MLflow; 3 seeds at T>0 for the headline finding)

---

> **Grilling Loop Notice for Students:** Submitting this profile initiates Round 1 of the **Grilling Loop Protocol**. The AI CEO will not accept your baseline at face value or conclude in a single turn. Be prepared to defend your ratings, evaluate trade-offs among scaffolded options, and refine your project over 2 to 4 interrogation cycles until all developmental gaps are resolved.
