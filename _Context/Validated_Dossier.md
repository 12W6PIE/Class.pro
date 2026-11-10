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


---

## Candidate Bounded Domains (Class 1 Output)

> **Selection Guidance:** Each candidate below forces mastery of your four `[new]` Developmental Delta pillars (IR/RAG Evaluation Science, Psychometric Judge Calibration & Non-Parametric Statistics, Contamination-Controlled Experimental Design, and Reproducible LLMOps under a $12\text{ GB}$ VRAM ceiling) and operates under the **AI-Domain Exception** (Set `1a` + `1b` as the primary scholarly output, supported by a Zenodo-archived benchmark with a permanent DataCite DOI).

### Candidate 1 (Primary Recommended): Quantization $\times$ Retrieval Interaction on Faithfulness and Abstention in Educational RAG
- **Bounded Domain:**
  - *In-Scope:* OpenStax *Introduction to Python Programming* (`CC BY 4.0`, English); a human-verified 300-item QA benchmark ($255$ answerable with span-level gold evidence, $45$ unanswerable abstention probes); Study 1 retrieval ablation (naive fixed-size chunking + dense retrieval vs. Markdown/AST structure-aware chunking + dense retrieval vs. structure-aware chunking + hybrid BM25/dense + cross-encoder reranking) on a fixed `8B Q4_K_M` generator; Study 2 quantization/scale matrix (`{3B, 8B} × {Q4_K_M, Q5_K_M, Q8_0} + 14B Q4_K_M`) paired with a closed-book no-retrieval baseline on an RTX 4070 (`12 GB VRAM`).
  - *Out-of-Scope:* Multimodal diagram/image OCR, fine-tuning / LoRA weight training, multi-turn conversational memory, models exceeding $12\text{ GB}$ VRAM (`14B Q8_0`), and live student classroom trials.
- **Core Hypothesis & Expected Scientific Delta:**
  - *Hypothesis:* Aggressive weight quantization (`Q4_K_M` vs. `Q8_0`) degrades **unanswerable abstention F1** and **claim-level faithfulness** under noisy top-$k$ retrieval significantly more than it degrades standard answer correctness on answerable queries, and structure-aware hybrid retrieval with cross-encoder reranking partially compensates for sub-8B quantization loss.
  - *Scientific Delta:* Quantifies the joint sensitivity surface of quantization bit-width and retrieval precision after subtracting pre-training parametric memorization ($\Delta \text{Correctness} = \text{Score}_{\text{RAG}} - \text{Score}_{\text{ClosedBook}}$), validated via dual NLI (`DeBERTa-v3-MNLI`) + human-calibrated LLM judging ($\kappa \ge 0.70$) and paired bootstrap confidence intervals.
- **Target Publication Tier:** **Tier 3** (International Conference Proceedings, e.g., OCETA Connect 2027 / IEEE educational & applied AI tracks), with **Tier 2 (JCR Q3/Q4)** stretch potential.
- **Career Trajectory Alignment:** Directly builds a portfolio-grade local RAG benchmarking harness, quantization/VRAM profiler, and reproducible `MLflow`/`Langfuse` pipeline sought in Applied AI / LLM Engineer interviews.

### Candidate 2: Code- and Formula-Aware Structural Chunking vs. Naive Token Splitting for CS Textbook QA
- **Bounded Domain:**
  - *In-Scope:* Benchmarking syntax- and section-aware chunking strategies (preserving complete Python functions, trace tables, and worked code examples in OpenStax *Introduction to Python Programming*) against sliding-window token chunking ($256, 512, 1024$ tokens) across dense (`bge-base-en-v1.5`, `nomic-embed-text`) and sparse (`BM25`) retrievers, evaluated on code-tracing vs. conceptual questions using fixed `3B` and `8B` `Q4_K_M` generators.
  - *Out-of-Scope:* Execution-guided code synthesis (sandboxed compiler feedback loops), multi-repository software engineering agents, and non-CS humanities textbooks.
- **Core Hypothesis & Expected Scientific Delta:**
  - *Hypothesis:* Standard fixed-window chunking bisects code blocks and trace explanations, causing a statistically significant drop in $\text{Recall@}k$ and downstream faithfulness on code-comprehension queries compared to AST/Markdown block-preserving chunking, even when total retrieved token budgets are held constant.
  - *Scientific Delta:* Provides controlled empirical curves stratified by query taxonomy (conceptual definition vs. syntax rules vs. code execution tracing) with span-level IR metrics and NLI-verified generation faithfulness.
- **Target Publication Tier:** **Tier 3** (International Conference Proceedings) or **Tier 4** (Course Publishing Repository fallback if structural gains prove domain-narrow).
- **Career Trajectory Alignment:** Masters production document ingestion, AST-aware preprocessing, and hybrid indexing—the highest-leverage failure mode in enterprise technical-documentation RAG systems.

### Candidate 3: Calibrating Small Local Evaluators vs. NLI Verifiers for Offline RAG Auditing
- **Bounded Domain:**
  - *In-Scope:* Meta-evaluation of automated RAG faithfulness and relevance judges runnable on a $12\text{ GB}$ RTX 4070 (`3B`–`14B` open-weight judges in Ollama, plus `DeBERTa-v3-large-MNLI` sentence-level entailment and a reference Gemini Free Tier rubric judge) against a double-annotated 150-item human gold standard drawn from the OpenStax Python RAG pipeline.
  - *Out-of-Scope:* Training custom reward models, commercial paid judge APIs (GPT-4o/Claude paid tiers), and non-English evaluation corpora.
- **Core Hypothesis & Expected Scientific Delta:**
  - *Hypothesis:* Uncalibrated $\le 8\text{B}$ local LLM judges exhibit severe family self-preference bias and low agreement with human annotators ($\kappa < 0.50$) on subtle extrinsic hallucinations, whereas a lightweight sentence-level NLI decomposition pipeline (`DeBERTa-v3-MNLI`) achieves higher human agreement ($\kappa \ge 0.70$) at less than $10\%$ of the GPU compute cost.
  - *Scientific Delta:* Delivers an empirically calibrated, zero-budget RAG evaluation protocol quantifying self-preference bias, positional bias, and quantization sensitivity of local LLM judges versus NLI entailment.
- **Target Publication Tier:** **Tier 2 / Tier 3** (JCR Q3/Q4 or international NLP/evaluation workshop proceedings).
- **Career Trajectory Alignment:** Directly targets evaluation engineering and automated CI/CD regression gating—a critical specialization for production LLM Engineers.

### Candidate 4: Parametric Memorization vs. Contextual Grounding via Counterfactual Perturbations in Local RAG
- **Bounded Domain:**
  - *In-Scope:* Constructing a paired factual vs. counterfactual textbook evaluation set (systematically mutating operator precedence rules, standard library defaults, and Complexity bounds in OpenStax Python passages) to measure whether quantized local LLMs (`3B`, `8B`, `14B` at `Q4_K_M`–`Q8_0`) obey retrieved context or revert to pre-training priors.
  - *Out-of-Scope:* Model weight editing (ROME/MEMIT), continual pre-training, and adversarial jailbreak security testing.
- **Core Hypothesis & Expected Scientific Delta:**
  - *Hypothesis:* On unmodified open textbooks, closed-book parametric memory accounts for $>50\%$ of apparent RAG accuracy; under counterfactual context perturbations, lower-bit quantization (`Q4_K_M`) increases **parametric override rate** (ignoring retrieved evidence in favor of pre-training priors) relative to `Q8_0`.
  - *Scientific Delta:* Separates true context-following capability from benchmark contamination in local quantized RAG using paired factual/counterfactual accuracy and abstention deltas.
- **Target Publication Tier:** **Tier 2 / Tier 3** (JCR Q3/Q4 or international conference proceedings).
- **Career Trajectory Alignment:** Equips the engineer to diagnose and mitigate stale-knowledge override when deploying RAG over rapidly changing internal APIs and proprietary company documentation.


---

## 6. Class 2 Output: Selected Idea, Working Titles & SOTA Query Payload (Prompt 4)

### Selected Project Idea
- **Selected Candidate:** **Candidate 1** — *Quantization $\times$ Retrieval Interaction on Faithfulness and Abstention in Educational RAG* (integrating structural code-preserving chunking from Candidate 2 and NLI + human-calibrated evaluation from Candidate 3).

### Preliminary Academic Working Titles
1. **Primary Working Title:** *Quantization Versus Retrieval Precision: Evaluating Faithfulness and Abstention in Local Retrieval-Augmented Generation Over Computer Science Textbooks Under a 12 GB VRAM Constraint*
2. **Alternative A (Systems & Efficiency Focus):** *Resource-Constrained Educational RAG: How GGUF Weight Quantization and Hybrid Structural Retrieval Interact to Govern Hallucination and Abstention on Consumer GPUs*
3. **Alternative B (Evaluation & Contamination Focus):** *Beyond Parametric Memorization: Contamination-Controlled Benchmarking of Quantized Open-Weight LLMs and Hybrid Retrieval Over Openly Licensed Programming Curricula*
4. **Alternative C (Applied AI Engineering Focus):** *Can Reranked Hybrid Retrieval Compensate for 4-Bit Quantization Loss? An Empirical Study of Grounded Question Answering on a 300-Item Python Textbook Benchmark*

### Structured TOON SOTA Query Handoff Payload (`application/toon`)
```toon
sota_verification_payload:
  orchestrator: "Google Antigravity IDE (01_ideation_ceo)"
  downstream_consumer: "02_literature_coo & NotebookLM MCP"
  student_felix_id: "12"
  selected_candidate: "Candidate 1 - Quantization x Retrieval Interaction in Local Educational RAG"
  target_databases[3]: "Web of Science (WoS)", "Scopus", "OpenAlex"
  publication_window: "2020-2026"
  language: "English"
  search_queries[4]:
    - query_id: "Q1_RAG_Quantization_Faithfulness"
      focus: "Interaction of LLM weight quantization and model scale with RAG grounded faithfulness and hallucination"
      boolean_string: "(\"Retrieval-Augmented Generation\" OR \"retrieval augmented generation\" OR \"RAG\") AND (\"quantization\" OR \"GGUF\" OR \"GPTQ\" OR \"AWQ\" OR \"4-bit\" OR \"low-bit\" OR \"small language model\" OR \"SLM\") AND (\"faithfulness\" OR \"hallucination\" OR \"grounding\" OR \"factuality\" OR \"abstention\")"
    - query_id: "Q2_Hybrid_Structural_Chunking_Education"
      focus: "Structure-aware / code-aware chunking and hybrid BM25 + dense + cross-encoder reranking over textbooks"
      boolean_string: "(\"Retrieval-Augmented Generation\" OR \"passage retrieval\" OR \"question answering\") AND (\"chunking\" OR \"document segmentation\" OR \"hybrid retrieval\" OR \"BM25\" OR \"reranking\" OR \"cross-encoder\") AND (\"textbook\" OR \"educational\" OR \"computer science education\" OR \"programming course\")"
    - query_id: "Q3_RAG_Evaluation_NLI_Judge_Calibration"
      focus: "RAG evaluation frameworks, LLM-as-a-judge biases, NLI claim verification, and human inter-annotator calibration"
      boolean_string: "(\"RAGAS\" OR \"ARES\" OR \"RAG evaluation\" OR \"LLM-as-a-judge\") AND (\"natural language inference\" OR \"NLI\" OR \"entailment\" OR \"Cohen's kappa\" OR \"human calibration\" OR \"self-preference bias\")"
    - query_id: "Q4_Parametric_Contamination_Unanswerable_Abstention"
      focus: "Separating pre-training parametric memory from contextual grounding and unanswerable query abstention in QA"
      boolean_string: "(\"Retrieval-Augmented Generation\" OR \"open-book question answering\" OR \"in-context learning\") AND (\"parametric knowledge\" OR \"memorization\" OR \"data contamination\" OR \"closed-book\") AND (\"unanswerable\" OR \"abstention\" OR \"selective prediction\" OR \"counterfactual\")"
  benchmark_seed_references[6]:
    - "Lewis et al. (2020) - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS)"
    - "Thakur et al. (2021) - BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models (NeurIPS Datasets & Benchmarks)"
    - "Es et al. (2024) - RAGAS: Automated Evaluation of Retrieval Augmented Generation (EACL)"
    - "Saad-Falcon et al. (2024) - ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems (NAACL)"
    - "Dettmers et al. / Frantar et al. (2023) - Post-training quantization (GPTQ / NF4 / k-quants) accuracy-memory trade-offs"
    - "Rajpurkar et al. (2018) - SQuAD 2.0: Know What You Don't Know: Unanswerable Questions for SQuAD (ACL)"
```

---

## 7. Class 2 Output: Zero-Budget Tooling, Sandboxing & Archiving Blueprint (Prompt 5)

```toon
tooling_and_execution_blueprint:
  project_id: "PIE-W6-12-LOCAL-RAG"
  governance_mode: "Agent-First & Deterministic-First (Google Antigravity IDE)"
  compute_allocation:
    local_laptop:
      hardware: "AMD Ryzen 7 5825U, 16GB RAM (~14GB usable), iGPU only, EndeavourOS Linux"
      assigned_workloads[5]:
        - "OpenStax CC-BY corpus ingestion and Markdown/AST structure-aware chunking"
        - "CPU embedding generation (bge-base-en-v1.5, nomic-embed-text) and FAISS/BM25 index construction"
        - "Cross-encoder reranking (ms-marco-MiniLM-L-6-v2) and full IR metric calculation (Recall@k, MRR@k, nDCG@k)"
        - "Sentence-level NLI claim verification via DeBERTa-v3-base/large-MNLI and bootstrap statistical tests"
        - "Pipeline smoke testing using Qwen2.5-3B-Instruct Q4_K_M on CPU"
    university_lab_gpu:
      hardware: "Nvidia RTX 4070 (12GB VRAM), scheduled lab sessions (~3h/week, ~20 GPU-hours total across Weeks 4-10)"
      assigned_workloads[2]:
        - "Study 1 generation: 3 retrieval strategies x 300 queries = 900 runs on pinned 8B Q4_K_M backbone (~1.5 GPU-hours)"
        - "Study 2 generation: 7 model/quantization conditions ({3B, 8B} x {Q4_K_M, Q5_K_M, Q8_0} + 14B Q4_K_M) x 300 queries x 2 (RAG vs Closed-Book) = 4,200 runs (~6.5-10 GPU-hours)"
      vram_ceiling_enforcement: "Hard cap <= 11.2 GB VRAM (4k context window, 14B Q8_0 strictly excluded)"
    cloud_fallback:
      provider: "Google Colab Free Tier (Nvidia T4 16GB VRAM)"
      resilience_protocol: "JSONL/Parquet append-only shard checkpointing every 25 queries to survive session preemption"
  docker_sandboxing_spec:
    base_images[2]: "ollama/ollama:latest (pinned SHA256 digest)", "python:3.11-slim (pinned SHA256 digest)"
    gpu_passthrough: "nvidia-container-toolkit with --gpus all"
    network_isolation: "Inference containers executed with --network none to guarantee zero external API leakage during RAG/closed-book generation"
    reproducibility_controls[4]:
      - "temperature = 0.0 and top_p = 1.0 for primary deterministic runs"
      - "Fixed seed = 42 across Python, NumPy, PyTorch, and Ollama options"
      - "3-seed sensitivity sweep (seeds 42, 1337, 2026 at temperature = 0.3) on top-performing configuration"
      - "Full telemetry logged to local MLflow tracking server and self-hosted Langfuse trace store"
  archiving_and_typesetting_pipeline:
    version_control: "GitHub repository (git@github.com:12W6PIE/Class.pro.git) managed via .agents/skills/skill_git_sync"
    dataset_and_code_doi: "GitHub Release v1.0.0 bridged to Zenodo (CERN Data Centre, <50GB limit) minting a permanent DataCite DOI for the 300-item OpenStax Python QA benchmark and evaluation harness"
    bibliography_management: "Zotero with Better BibTeX auto-exporting to _Deliverables/references.bib"
    manuscript_typesetting: "LaTeX (Overleaf / local TeX Live) starting from _Deliverables/1-Page-Brief.tex"
```
