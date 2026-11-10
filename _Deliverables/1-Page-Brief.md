# Course Completion Project Brief: 1-Page Research Charter

- **Course:** AI Engineering
- **Supervisor:** PhD Academic Lead
- **Date:** November 2026
- **Student Felix ID:** 12
- **Degree Milestone:** Bachelor of Science Thesis (Computer Science, 5th Semester)

---

## 1. Working Titles
1. **Primary:** Quantization Versus Retrieval Precision: Evaluating Faithfulness and Abstention in Local Retrieval-Augmented Generation Over Computer Science Textbooks Under a 12 GB VRAM Constraint
2. **Alternative A:** Resource-Constrained Educational RAG: How GGUF Weight Quantization and Hybrid Structural Retrieval Interact to Govern Hallucination and Abstention on Consumer GPUs
3. **Alternative B:** Beyond Parametric Memorization: Contamination-Controlled Benchmarking of Quantized Open-Weight LLMs and Hybrid Retrieval Over Openly Licensed Programming Curricula

## 2. Project Idea & Motivation
Deploying Retrieval-Augmented Generation (RAG) assistants for university programming courses on consumer hardware (12 GB VRAM) requires aggressive weight quantization (4-bit to 8-bit GGUF) and compact open-weight models (3B–14B parameters). While general RAG chunking is well studied, two critical methodological flaws undermine existing local educational evaluations: (1) failure to control for pre-training parametric memorization of public textbooks, and (2) uncalibrated evaluation of how low-bit quantization interacts with retrieval noise to degrade claim-level faithfulness and unanswerable query abstention. This project constructs a reproducible, network-isolated (`--network none`) local RAG evaluation harness and releases a human-verified 300-item QA benchmark (255 answerable with gold evidence spans, 45 unanswerable abstention probes) over the CC BY 4.0 OpenStax textbook *Introduction to Python Programming* to quantify the joint sensitivity of quantization bit-width and hybrid structural retrieval.

## 3. Bounded Domain & Scientific Delta (SOTA Alignment)
- **Target Domain Scope:** *In-Scope:* OpenStax Python textbook (CC BY 4.0); 300-item verified QA benchmark; Study 1 retrieval ablation (fixed-size dense vs. AST/Markdown structure-aware dense vs. structure-aware hybrid BM25+dense with cross-encoder reranking) on an 8B Q4_K_M backbone; Study 2 quantization matrix ({3B, 8B} $\times$ {Q4_K_M, Q5_K_M, Q8_0} + 14B Q4_K_M) vs. closed-book no-retrieval baseline on an RTX 4070 (12 GB VRAM, 8–12 GPU-hours total). *Out-of-Scope:* Weight fine-tuning, multimodal OCR, $>12\text{ GB}$ VRAM models (14B Q8_0), and live classroom trials.
- **Scientific Baseline (SOTA):** Grounded against foundational RAG and IR benchmarks in WoS/Scopus/OpenAlex: Lewis et al. (2020), BEIR (Thakur et al., 2021), SQuAD 2.0 abstention (Rajpurkar et al., 2018), RAGAS (Es et al., 2024), ARES (Saad-Falcon et al., 2024), and post-training quantization literature (Frantar et al., 2023; Dettmers et al., 2023).
- **Expected Scientific Delta:** Isolates net retrieval gain ($\Delta \text{Correctness} = \text{Score}_{\text{RAG}} - \text{Score}_{\text{ClosedBook}}$) and demonstrates whether hybrid reranked retrieval compensates for 4-bit quantization loss on claim-level faithfulness and abstention F1, verified via NLI entailment (`DeBERTa-v3-MNLI`), human-calibrated LLM judging (Cohen's $\kappa \ge 0.70$), and paired bootstrap 95% confidence intervals.

## 4. Developmental Delta (Continuous Progress Rule)
- **Current Student Baseline:** Strong self-reported software baseline in Python, Git, Docker, Linux/Bash, SQL, Scikit-Learn, and PyTorch (9/10 self-assessment retained as documented baseline risk `R1`), but zero prior formal training in IR evaluation metrics, psychometric judge calibration, contamination controls, or LLMOps observability.
- **Specific Skill/Architecture Gaps to Bridge:** Master four new engineering pillars: (1) rank-aware IR metrics ($\text{Recall@}k, \text{MRR}, \text{nDCG}$) and claim-level NLI verification; (2) human annotation reliability (Cohen's $\kappa$ on 100 items) and paired bootstrap / Wilcoxon hypothesis testing with Holm-Bonferroni correction; (3) closed-book contamination control and abstention F1 benchmarking; and (4) reproducible LLMOps (`MLflow` experiment tracking, `Langfuse` tracing, pinned Ollama SHA-256 digests, and VRAM/latency profiling).

## 5. Tooling Architecture & Automated Pipelines
- **Agent Governance:** Google Antigravity IDE (`01_ideation_ceo`) + NotebookLM MCP for WoS/Scopus/OpenAlex synthesis and Zotero Better BibTeX citation management.
- **Compute & Sandboxing:** Split execution across Linux laptop CPU (ingestion, embeddings, reranking, IR metrics, NLI verification) and University Lab Nvidia RTX 4070 12 GB VRAM (network-isolated Docker + Ollama batch generation, 8–12 GPU-hours across Weeks 4–10, with Google Colab Free T4 shard fallback), tracked in `MLflow` and `Langfuse`.
- **Artifact Archiving:** GitHub repository (`12W6PIE/Class.pro`) releases bridged to Zenodo (CERN Data Centre) minting a permanent DataCite DOI for the 300-item CC-BY QA benchmark, evaluation code, and raw generation logs.

## 6. Course Deliverables Mapping
- **Track 1(a) AI Tech Utilization Report:** Comprehensive engineering manual detailing Docker `--network none` GPU sandboxing, GGUF VRAM budgeting, `MLflow`/`Langfuse` telemetry, NLI + LLM judge calibration, and Antigravity/MCP workflow orchestration.
- **Track 1(b) AI Tech Draft Manuscript:** Primary scientific manuscript reporting the two-study empirical evaluation of quantization $\times$ retrieval interactions on faithfulness, net RAG gain over closed-book memory, and unanswerable abstention.
- **Track 2(a) Domain Deliverables Report:** Dataset documentation, schema specification, and Zenodo DataCite DOI release notes for the 300-item OpenStax Python QA benchmark and reproducible evaluation harness.
- **Track 2(b) Domain Draft Manuscript:** Unified with Track 1(b) under the AI-Domain Exception Rule, incorporating educational CS error-taxonomy analysis (syntax vs. conceptual vs. code-tracing queries).
- **AI Domain Exception Applied:** YES — because the core research domain is AI Technology (resource-constrained RAG evaluation and quantization methodology), Track 1(a) and Track 1(b) fulfill the primary course mandate, supported by the Zenodo-archived benchmark artifact in Track 2(a).

## 7. Statement of Publishing Level Assessment
**Assessment:** Target **Tier 3 (International Conference Proceedings, e.g., OCETA Connect 2027 or IEEE/ACM applied AI & CS education venues)**, with stretch potential for **Tier 2 (JCR Q3/Q4 indexed journal)** if the quantization $\times$ abstention interaction yields statistically significant cross-family findings ($\kappa \ge 0.70$, Holm-Bonferroni $p < 0.05$) and a reusable public benchmark. If empirical effect sizes between quantization tiers prove statistically indistinguishable on the 300-item sample, the rigorous negative/null methodology and Zenodo-archived dataset are guaranteed routing to **Tier 4 (Internal Semi-Scientific Course Publishing Service Database)**.
