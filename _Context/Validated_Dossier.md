# Validated Research Dossier (`Validated_Dossier.md`)

> **Governance Status:** FORMALLY LOCKED (Grilling Loop Converged after 3 Cycles)  
> **Student Identity:** Felix Login ID `12` | Bachelor's Degree in Computer Science (3rd Year, 5th Semester)  
> **Supervisor / Orchestrator:** Course CEO Agent (`01_ideation_ceo`)  
> **Lock Timestamp:** 2026-11-10

---

## 1. Validated Dual-Axis Baseline

### Axis 1: AI Technology & Engineering Stack
- **Self-Reported Core & Additional Stack (Retained as Unverified Self-Assessment — Documented Baseline Risk `R1`):**
  - Python: `[9/10]` | Git / GitHub: `[9/10]` | Docker: `[9/10]` | Prompt Engineering & LLM Utilization: `[9/10]`
  - PyTorch: `[9/10]` | Scikit-Learn: `[9/10]` | SQL: `[9/10]` | Linux / Bash: `[9/10]`
- **Methodological Mitigation for `R1`:** Because uniform `9/10` ratings lack external repository links at intake, the project's **Developmental Delta** is anchored strictly on newly introduced competencies (`[new]`) that the student has not previously practiced.
- **Verified Oral/Diagnostic Reference Anchor:**
  1. *Docker GPU Passthrough:* Configured via `nvidia-container-toolkit` (`nvidia-ctk runtime configure --runtime=docker`), executed with `--gpus all`, and verified deterministically via `nvidia-smi` process tables, `ollama ps` (`100% GPU` offload), CUDA layer allocation logs, and `ollama run --verbose` token evaluation throughput ($\approx 10\times$ CPU baseline).
  2. *PyTorch Training Mechanics:* Mixed precision via `torch.autocast("cuda", dtype=torch.float16/bfloat16)` paired with `torch.amp.GradScaler("cuda")`, gradient accumulation dividing micro-batch loss by $N$ prior to `.backward()`, full stateful checkpointing (`model`, `optimizer`, `scheduler`, `scaler`, RNG states), and activation checkpointing (`torch.utils.checkpoint`).
  3. *RAG Evaluation Triplet:* Strict separation between **Faithfulness** (fraction of generated claims entailed by retrieved context), **Answer Relevance** (semantic alignment of answer to query intent regardless of factual grounding), **Context Recall** (coverage of ground-truth claims within top-$k$ retrieved chunks), and **Context Precision** (rank-weighted signal-to-noise ratio of retrieved chunks).

### Hardware & Compute Reality (Validated)
- **Primary Development Machine:** Linux Laptop (EndeavourOS), AMD Ryzen 7 5825U, 16 GB system RAM ($\approx 14\text{ GB}$ usable), integrated Radeon graphics (CPU-only inference).
- **Accelerated Lab Compute:** University Lab Nvidia RTX 4070 (`12 GB VRAM`), accessible during scheduled laboratory hours ($\approx 3\text{ hours/week}$, no remote SSH access $\Rightarrow \approx 20\text{ GPU-hours}$ total across Weeks 4–10).
- **Elastic Fallback Compute:** Google Colab Free Tier (Nvidia T4 `16 GB VRAM`) using checkpointed, resumable batch shards.
- **Operational Workload Split:**
  - *Laptop (CPU):* Corpus ingestion, structure-aware chunking, embedding generation, BM25 + dense vector indexing, cross-encoder reranking, all retrieval-only evaluation metrics ($\text{Recall@}k$, $\text{MRR}$, $\text{nDCG@}k$), NLI claim verification (`DeBERTa-v3-large/base-MNLI`), and pipeline smoke tests with $\le 3\text{B}$ quantized models.
  - *Lab RTX 4070 (12 GB VRAM):* Batch LLM generation in network-isolated Docker + Ollama containers (`--network none`). Peak VRAM strictly bounded below $12\text{ GB}$ (`8B Q8_0` $\approx 8.5\text{ GB}$ or `14B Q4_K_M` $\approx 9.0\text{ GB}$ + $4\text{k}$ KV cache). Total generation volume across the two-study design is $\approx 5,100$ completions ($\approx 1.3\text{M}$ output tokens $\Rightarrow \mathbf{8\text{--}12\text{ GPU-hours}}$), fitting safely inside the $20\text{ GPU-hour}$ lab budget.

### Axis 2: Professional Domain & Research Interest
- **Broad Field:** Computer Science / AI Technology (**AI-Domain Exception** invoked under Course Rubric Section 4).
- **Specific Sub-Domain:** Empirical evaluation of resource-constrained, fully local Retrieval-Augmented Generation (RAG) over openly licensed educational textbooks, focusing on the interaction between model quantization/scale and retrieval architecture on grounded faithfulness and abstention.
- **Domain Knowledge Baseline:** 5 semesters of undergraduate CS coursework (algorithms, data structures, databases, operating systems, probability & statistics); zero prior formal training in Information Retrieval (IR) evaluation theory, psychometric/annotation reliability, or non-parametric statistical benchmarking.

---

## 2. Trajectory Alignment

- **Semester Project Target:** Construct a reproducible, Docker-sandboxed local RAG evaluation harness and a human-verified 300-item educational QA benchmark (with $15\%$ unanswerable queries) over an open CC-BY textbook; execute a controlled two-study ablation across retrieval strategies and GGUF quantization tiers within a hard $12\text{ GB}$ VRAM envelope.
- **Diploma Target (Bachelor's Thesis Milestone):** Establish a publication-grade empirical baseline and evaluation methodology (closed-book memorization controls, calibrated automated judges, paired bootstrap significance testing) that can be directly extended into a final Bachelor's thesis on self-correcting / agentic local RAG architectures (e.g., CRAG, Self-RAG).
- **Career Target (3–5 Year Applied AI / LLM Engineer):** Demonstrate production-grade competencies required by global AI engineering teams: quantized model serving under hardware constraints, retrieval optimization, automated evaluation harnesses, experiment tracking (`MLflow`), execution tracing (`Langfuse`), and deterministic containerization.

---

## 3. Calibrated Developmental Delta (Mandatory Semester Growth)

To satisfy the **Continuous Progress Rule**, the student must bridge four concrete competency gaps (`[new]`) during this 14-week semester:

1. **Information Retrieval & RAG Evaluation Science:**
   - Implement rank-aware IR metrics ($\text{Recall@}k$, $\text{MRR@}k$, $\text{nDCG@}k$) from scratch / verified libraries against span-level gold evidence.
   - Design a two-tier generation verification protocol combining an external LLM judge (Gemini Free Tier on public CC-BY data) and a local NLI entailment model (`DeBERTa-v3-MNLI`) to measure claim-level **Faithfulness**, **Answer Correctness**, and **Abstention Accuracy** (F1 on unanswerable queries).
2. **Psychometric Judge Calibration & Non-Parametric Statistics:**
   - Manually annotate a stratified 100-sample calibration subset and compute inter-annotator / human-judge agreement via **Cohen's $\kappa$** (requiring $\kappa \ge 0.70$ before trusting automated judge scores).
   - Apply **paired bootstrap resampling** ($10,000$ iterations, $95\%$ confidence intervals) and **Wilcoxon signed-rank / McNemar's tests** with Holm-Bonferroni multiple-comparison correction.
3. **Contamination-Controlled Experimental Design:**
   - Isolate pre-training parametric memorization of open textbooks by running a **closed-book (no-retrieval) baseline** alongside every RAG model condition and measuring **RAG Net Gain** ($\Delta \text{Correctness} = \text{Score}_{\text{RAG}} - \text{Score}_{\text{ClosedBook}}$) as well as counterfactual / unanswerable abstention rates.
4. **Reproducible LLMOps & Hardware-Bounded Quantization Budgeting:**
   - Enforce deterministic execution (`temperature = 0.0`, fixed RNG seeds, pinned Ollama SHA-256 model digests, plus 3-seed variance checks at $T = 0.3$ for headline findings).
   - Track all runs, hyperparameters, VRAM profiles, and latency distributions (`TTFT`, `tok/s`) in **MLflow** and **Langfuse**, packaged inside network-isolated Docker containers (`--network none` during local inference) and archived to **Zenodo** with a permanent DataCite DOI.

---

## 4. Grilling Loop Audit Trail (3 Cycles to Convergence)

| Cycle | Open Gaps | Status | Key Interrogations & Resolved Bottlenecks |
| :---: | :---: | :---: | :--- |
| **Cycle 1** | 8 (`I1`–`I8`) | `ITERATING` | Exposed uniform `9/10` baseline (`I1`), missing Developmental Delta (`I2`), empirical triviality of naive chunking comparisons (`I3`), undefined corpus/licensing (`I4`), unoperationalized hallucination metrics (`I5`), unbudgeted laptop/lab compute (`I6`), unsupported privacy claims (`I7`), and Track 1/2 ambiguity (`I8`). |
| **Cycle 2** | 7 (`C1`–`C3`, `N4`–`N7`) | `ITERATING` | Locked in options for `I2, I3, I5, I7, I8`. Exposed four deeper methodological threats: pre-training contamination on public textbooks (`N4`), infeasible full-factorial VRAM grid where `14B Q8` exceeds $12\text{ GB}$ (`N5`), local small-judge self-bias (`N6`), and Ollama sampling nondeterminism (`N7`). |
| **Cycle 3** | 0 | `CONVERGED` | Confirmed lab schedule ($\approx 3\text{ h/week}$ class access, no SSH $\Rightarrow$ two-study split requiring $8\text{--}12\text{ GPU-hours}$); retained `9/10` as documented risk `R1` while binding the Developmental Delta to `[new]` competencies; adopted OpenStax CC-BY corpus, closed-book contamination control, dual NLI + human-calibrated judge, and pinned MLflow/Docker reproducibility. |

### Summary of All 12 Resolved Issues
- **`I1 / C1` (Baseline Calibration):** Retained `9/10` ratings as unverified self-assessment (`R1`), recorded full technical diagnostic anchors, and decoupled the Developmental Delta onto four unpracticed `[new]` competency pillars.
- **`I2` (Developmental Delta):** Selected **Option D (Evaluation Science + LLMOps)**; deferred multi-step agentic RAG to the Bachelor's thesis.
- **`I3` (Novelty & Publication Tier):** Selected **Option D (Quantization $\times$ Retrieval interaction study + 300-item Zenodo benchmark)** targeting **Tier 3 (International Conference Proceedings)** with **Tier 2 (JCR Q3/Q4)** stretch potential.
- **`I4 / C3` (Corpus & Licensing):** Selected **Option A** — OpenStax *Introduction to Python Programming* (`CC BY 4.0`, English), permitting unrestricted redistribution of derived chunks and the 300-item QA benchmark on Zenodo.
- **`I5` (Metrics):** Selected **Option D** — $\text{Recall@}k, \text{MRR}, \text{nDCG}$ for retrieval; claim-level faithfulness and abstention F1 with paired bootstrap CIs.
- **`I6 / C2` (Compute Feasibility):** Selected **Option B** ($\approx 3\text{ h/week}$ lab RTX 4070, no SSH) paired with a CPU-laptop / GPU-lab split that keeps total GPU generation to $8\text{--}12\text{ hours}$.
- **`I7` (Privacy Framing):** Selected **Option A** — reframed "local execution" strictly as a deterministic systems constraint (`--network none`, zero paid APIs in inference) rather than a cryptographic/privacy contribution.
- **`I8` (Deliverable Bifurcation):** Selected **Option A (AI-Domain Exception)** — primary focus on Set 1 (`1a` AI Tech Utilization Report + `1b` AI Tech Manuscript), supported by the Zenodo-archived benchmark dataset (`2a`).
- **`N4` (Parametric Contamination):** Selected **Option D** — closed-book (no-retrieval) baseline across all models plus $15\%$ unanswerable queries ($45/300$) to quantify parametric leakage and hallucinated fabrication.
- **`N5` (Experimental Design):** Selected **Option A (Two-Study Sequential Design)** — Study 1 ablates chunking/retrieval on a fixed `8B Q4_K_M` backbone ($3 \times 300 = 900$ runs); Study 2 evaluates `{3B, 8B} × {Q4_K_M, Q5_K_M, Q8_0} + 14B Q4_K_M` ($7 \times 300 \times 2 = 4,200$ runs) using the optimal retriever from Study 1.
- **`N6` (Judge Reliability):** Selected **Option B + C** — cross-checked NLI entailment verifier (`DeBERTa-v3-MNLI`) + Gemini Free Tier rubric judge, validated against $100$ human-annotated responses via Cohen's $\kappa$.
- **`N7` (Reproducibility):** Selected **Option A + B** — `temperature = 0`, fixed seeds, SHA-256 model digests, MLflow logging, plus a 3-seed sensitivity check at $T = 0.3$ on the top configuration.
