# Project State & Multi-Turn Persistence Record (`state.md`)

> **Checkpoint Phase:** End of Phase 1 (Classes 1 & 2 - Ideation, Grilling Loop Convergence, SOTA Alignment, and 1-Page Project Brief)  
> **Active Operational Mode for Next Session:** `STATE 2: Active Execution Mode` (Unlocking Class 3 / Phase 2 Literature Synthesis `02_literature_coo`)  
> **Student Identity:** Felix Login ID `12` | Bachelor of Science in Computer Science (3rd Year, 5th Semester)  
> **Last Updated:** 2026-11-23

---

## 1. Student Dual-Axis Baseline & Developmental Delta

- **Validated Technical Baseline (Axis 1):**
  - Python `[7/10]`, Git/GitHub `[8/10]`, Docker `[3/10]`, Prompt Engineering & LLM Utilization `[9/10]`, PyTorch `[6/10]`, Scikit-Learn `[6/10]`, SQL `[6/10]`, Linux/Bash `[5/10]` (recalibrated honest baseline; Docker `3/10` and Linux/Bash `5/10` are practical growth areas alongside LLMOps, while Prompt Engineering `9/10` remains an unverified self-assessment risk `R1`).
  - Hardware Reality: Windows 11 Home Single Language Laptop - Lenovo IdeaPad Slim 3 15ABR8, AMD Ryzen 7 5825U (8 cores, 16 threads), 16 GB RAM (13.8 GB usable), integrated AMD Radeon Graphics (2 GB VRAM, no dedicated GPU) + Google Colab Free Tier T4 (`16 GB VRAM`) checkpointed fallback for cloud GPU batch runs.
- **Validated Domain Baseline (Axis 2):**
  - Broad Field: Computer Science / AI Technology (**AI-Domain Exception** applied).
  - Sub-Domain: Empirical evaluation of local, resource-constrained Retrieval-Augmented Generation (RAG) over openly licensed CS educational textbooks.
- **Mandatory Developmental Delta (`[new]` Competencies to Bridge):**
  1. *IR & RAG Evaluation Science:* Span-level $\text{Recall@}k$, $\text{MRR@}k$, $\text{nDCG@}k$; claim-level NLI entailment (`DeBERTa-v3-MNLI`) and rubric judging for Faithfulness, Correctness, and Abstention F1.
  2. *Psychometric Calibration & Non-Parametric Statistics:* Human annotation on a 100-item stratified sample with **Cohen's $\kappa \ge 0.70$**; paired bootstrap 95% confidence intervals ($10,000$ resamples) and Wilcoxon signed-rank / McNemar's tests with Holm-Bonferroni correction.
  3. *Contamination-Controlled Benchmarking:* Closed-book (no-retrieval) baseline across all model/quantization conditions to isolate net RAG gain ($\Delta \text{Correctness} = \text{Score}_{\text{RAG}} - \text{Score}_{\text{ClosedBook}}$) alongside $15\%$ ($45/300$) unanswerable abstention probes.
  4. *Reproducible LLMOps & Memory Budgeting:* Network-isolated Docker execution (`--network none`), pinned Ollama SHA-256 digests, `temperature = 0.0` + 3-seed sensitivity sweep, tracked in `MLflow` and `Langfuse` and archived to Zenodo with a DataCite DOI.

---

## 2. Approved Working Title, Bounded Domain & Core Hypothesis

- **Approved Primary Working Title:** *Quantization Versus Retrieval Precision: Evaluating Faithfulness and Abstention in Local Retrieval-Augmented Generation Over Computer Science Textbooks Under Consumer Hardware Constraints*
- **Bounded Domain:**
  - *Corpus:* OpenStax *Introduction to Python Programming* (`CC BY 4.0`, English).
  - *Benchmark Artifact:* 300 human-verified QA pairs (255 answerable with gold evidence spans across conceptual, syntax, and code-tracing categories; 45 unanswerable abstention probes).
  - *Study 1 (Retrieval Ablation):* Fixed `8B Q4_K_M` generator across 3 retrieval pipelines (fixed-window dense vs. AST/Markdown structure-aware dense vs. structure-aware hybrid BM25+dense with `ms-marco-MiniLM-L-6-v2` cross-encoder reranking) $\Rightarrow 900$ generations.
  - *Study 2 (Quantization $\times$ Scale Matrix):* Optimal Study 1 retriever evaluated across `{3B, 8B} × {Q4_K_M, Q5_K_M, Q8_0} + 14B Q4_K_M` (7 conditions $\times 300$ queries $\times 2$ [RAG vs. Closed-Book] $= 4,200$ generations), executed in sharded batches across local CPU and Google Colab Free T4 (`14B Q8_0` excluded due to consumer memory limits).
- **Core Hypothesis:** Low-bit GGUF weight quantization (`Q4_K_M` vs. `Q8_0`) disproportionately degrades claim-level faithfulness under noisy retrieval and unanswerable query abstention F1 compared to standard answerable correctness, while structure-aware hybrid retrieval with cross-encoder reranking partially offsets 4-bit quantization loss under consumer hardware constraints.

---

## 3. Target Deliverables Mapping & Publishing Level Assessment

- **Track 1(a) AI Tech Utilization Report:** Primary engineering manual covering `--network none` Docker GPU sandboxing, GGUF VRAM profiling, `MLflow`/`Langfuse` observability, NLI + LLM judge calibration, and Antigravity/MCP orchestration.
- **Track 1(b) AI Tech Draft Manuscript:** Primary scientific manuscript presenting the two-study quantization $\times$ retrieval evaluation and contamination-controlled findings.
- **Track 2(a) Domain Deliverables Report:** Formal dataset documentation and Zenodo DataCite DOI release for the 300-item OpenStax Python QA benchmark and evaluation suite.
- **Track 2(b) Domain Draft Manuscript:** Unified with Track 1(b) under the **AI-Domain Exception Rule**, incorporating CS query-type error analysis.
- **Publishing Level Assessment:** Primary target is **Tier 3 (International Conference Proceedings, e.g., OCETA Connect 2027 / IEEE & ACM applied AI tracks)** with stretch potential to **Tier 2 (JCR Q3/Q4)** if cross-family interaction effects are statistically significant ($\kappa \ge 0.70$, Holm-Bonferroni $p < 0.05$). Guaranteed fallback routing to **Tier 4 (Internal Semi-Scientific Course Publishing Service Database)** if quantization differences yield null effect sizes.

---

## 4. Phase 1 Gate Status & SOTA Search Queries (TOON)

- **Phase 1 Gate (`skill_gate_phase1`):** `[SKILL_PASS]` verified on `_Deliverables/1-Page-Brief.tex` (all 7 sections complete, 0 placeholders).

```toon
phase1_exit_handoff:
  phase1_gate_status: "SKILL_PASS"
  validated_deliverable: "_Deliverables/1-Page-Brief.tex"
  dossier_path: "_Context/Validated_Dossier.md"
  sota_queries[4]:
    - id: "Q1_RAG_Quantization_Faithfulness"
      query: "(\"Retrieval-Augmented Generation\" OR \"retrieval augmented generation\" OR \"RAG\") AND (\"quantization\" OR \"GGUF\" OR \"GPTQ\" OR \"AWQ\" OR \"4-bit\" OR \"low-bit\" OR \"small language model\" OR \"SLM\") AND (\"faithfulness\" OR \"hallucination\" OR \"grounding\" OR \"factuality\" OR \"abstention\")"
    - id: "Q2_Hybrid_Structural_Chunking_Education"
      query: "(\"Retrieval-Augmented Generation\" OR \"passage retrieval\" OR \"question answering\") AND (\"chunking\" OR \"document segmentation\" OR \"hybrid retrieval\" OR \"BM25\" OR \"reranking\" OR \"cross-encoder\") AND (\"textbook\" OR \"educational\" OR \"computer science education\" OR \"programming course\")"
    - id: "Q3_RAG_Evaluation_NLI_Judge_Calibration"
      query: "(\"RAGAS\" OR \"ARES\" OR \"RAG evaluation\" OR \"LLM-as-a-judge\") AND (\"natural language inference\" OR \"NLI\" OR \"entailment\" OR \"Cohen's kappa\" OR \"human calibration\" OR \"self-preference bias\")"
    - id: "Q4_Parametric_Contamination_Unanswerable_Abstention"
      query: "(\"Retrieval-Augmented Generation\" OR \"open-book question answering\" OR \"in-context learning\") AND (\"parametric knowledge\" OR \"memorization\" OR \"data contamination\" OR \"closed-book\") AND (\"unanswerable\" OR \"abstention\" OR \"selective prediction\" OR \"counterfactual\")"
  next_actions_class_3[4]:
    - "1. Execute Q1-Q4 in Web of Science, Scopus, and OpenAlex; export 25-40 core peer-reviewed papers into Zotero (Better BibTeX -> _Deliverables/references.bib)"
    - "2. Ingest the selected PDFs into NotebookLM / 02_literature_coo to generate the comparative SOTA matrix in _Deliverables/Lit_Synthesis.md"
    - "3. Download the CC BY 4.0 OpenStax Introduction to Python Programming source text and lock the document ingestion schema"
    - "4. Draft the annotation guidelines and stratified sampling plan for the 300-item QA benchmark (255 answerable + 45 unanswerable)"
```

