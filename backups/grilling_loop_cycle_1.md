# Grilling Loop Cycle 1 - Interrogation & Defense Record

```toon
grilling_loop_status:
  cycle_number: 1
  open_gaps_count: 8
  status: "ITERATING"
  convergence_achieved: false
```

CEO, here is my defense and gap resolution for Grilling Loop Cycle 1:

---

## Challenge 1 (I1) - Technical Baseline Calibration
- **CEO Critique:** Initial uniform 9/10 self-ratings across core and auxiliary tools lack external verification and risk hiding practical engineering gaps.
- **Scaffolded Options:** Option A (keep ratings with mandatory code audit), Option B (apply explicit calibration rubrics), Option C (add diagnostic reference answers to defend orally), Option D (recalibrate baseline honestly).
- **Student Defense:** I adopt **Option B + C with honest recalibration**: Python `7/10`, Git/GitHub `8/10`, Docker `3/10`, Prompt Engineering `9/10`, PyTorch `6/10`, Scikit-Learn `6/10`, SQL `6/10`, and Linux/Bash `5/10`. Diagnostic reference answers for Ollama container setup, PyTorch AMP/checkpointing, and RAG metrics are documented in `_Context/STUDENT-PROFILE.md`, and Docker containerization is explicitly included in my semester growth plan.

## Challenge 2 (I2) - Developmental Delta Scope
- **CEO Critique:** Building a basic local RAG demo does not establish a clear Developmental Delta beyond existing Python/LLM familiarity.
- **Scaffolded Options:** Option A (IR & RAG evaluation science), Option B (reproducible LLMOps & containerization), Option C (multi-step agentic CRAG/Self-RAG), Option D (combine A + B and defer C to thesis).
- **Student Defense:** I adopt **Option D (A + B)**. My semester Developmental Delta focuses on four `[new]` pillars: rank-aware IR metrics and claim-level NLI verification, human-calibrated LLM judging and non-parametric statistics, closed-book contamination control, and reproducible LLMOps with Docker, MLflow, and Langfuse. Agentic RAG is deferred as a candidate Bachelor's thesis extension.

## Challenge 3 (I3) - Scientific Novelty & Publication Target
- **CEO Critique:** Naive chunking comparison alone exhibits empirical triviality and lacks publication-grade novelty.
- **Scaffolded Options:** Option A (simple retrieval tuning), Option B (quantization x retrieval interaction study), Option C (release a verified domain QA benchmark), Option D (combine B + C).
- **Student Defense:** I adopt **Option D (B + C)**. The project combines a two-study empirical evaluation of GGUF quantization versus hybrid structural retrieval with a human-verified 300-item Python textbook QA benchmark archived on Zenodo with a DataCite DOI, targeting Tier 3 international conference proceedings with Tier 2 stretch potential and Tier 4 fallback.

## Challenge 4 (I4) - Corpus Selection & Licensing
- **CEO Critique:** The target textbook corpus and redistribution license for benchmark artifacts must be explicitly defined.
- **Scaffolded Options:** Option A (openly licensed CC BY 4.0 OpenStax textbook), Option B (internal university lecture notes), Option C (scraped web tutorials), Option D (custom synthetic corpus).
- **Student Defense:** I adopt **Option A**. Using the English CC BY 4.0 OpenStax textbook *Introduction to Python Programming* allows unrestricted legal redistribution of derived chunks and the 300-item QA benchmark on Zenodo.

## Challenge 5 (I5) - Operationalizing Faithfulness & Hallucination Metrics
- **CEO Critique:** Subjective or uncalibrated hallucination checks are not methodologically valid.
- **Scaffolded Options:** Option A (manual inspection only), Option B (single uncalibrated LLM judge), Option C (IR metrics only), Option D (IR metrics + NLI claim verification + LLM judge calibrated on 100 human-labelled items with bootstrap CIs).
- **Student Defense:** I adopt **Option D**. Retrieval is measured with Recall@k, MRR, and nDCG; generation is evaluated with claim-level NLI (`DeBERTa-v3-MNLI`) and a rubric LLM judge calibrated against 100 human-annotated items (Cohen's kappa >= 0.70), reported with paired bootstrap 95% confidence intervals and Holm-Bonferroni corrected tests.

## Challenge 6 (I6) - Hardware & Compute Reality
- **CEO Critique:** Running large unbudgeted model sweeps locally without a dedicated GPU is computationally infeasible.
- **Scaffolded Options:** Option A (CPU-only laptop execution for lightweight stages), Option B (paid cloud GPU rental), Option C (zero-budget hybrid split using local laptop CPU + Google Colab Free T4 sharded batches), Option D (API-only inference).
- **Student Defense:** I adopt **Option A + C**. My real primary machine is a Windows 11 Lenovo IdeaPad Slim 3 15ABR8 laptop (AMD Ryzen 7 5825U, 8 cores / 16 threads, 16 GB RAM with 13.8 GB usable, integrated AMD Radeon Graphics with 2 GB VRAM, no dedicated GPU). Ingestion, indexing, reranking, IR metrics, NLI verification, and compact 3B-8B CPU smoke tests run locally on the laptop, while larger batch generation runs execute in resumable checkpointed shards on Google Colab Free Tier T4 (16 GB VRAM).

## Challenge 7 (I7) - Local Execution vs. Privacy Framing
- **CEO Critique:** Claiming privacy contributions over a public open textbook is logically inconsistent.
- **Scaffolded Options:** Option A (reframe local execution strictly as a deterministic systems constraint with `--network none`), Option B (switch to private medical/legal data), Option C (remove local requirement).
- **Student Defense:** I adopt **Option A**. Local execution is framed strictly as a reproducible systems constraint (no external API calls in the inference path, Docker containers executed with `--network none`) rather than a privacy claim.

## Challenge 8 (I8) - Course Deliverable Track Alignment
- **CEO Critique:** Ambiguity between Track 1 (AI Technology) and Track 2 (Application Domain) deliverables must be resolved.
- **Scaffolded Options:** Option A (invoke the AI-Domain Exception Rule for unified primary manuscript + Zenodo benchmark artifact), Option B (write two separate manuscripts).
- **Student Defense:** I adopt **Option A**. Because the core domain is AI Technology (resource-constrained RAG evaluation and quantization methodology), the AI-Domain Exception applies: Track 1(a) AI Tech Utilization Report and Track 1(b) primary manuscript are supported by the Track 2(a) Zenodo-archived benchmark release.

---

Re-evaluate my project baseline against the Context Triad. If critical flaws or developmental gaps remain, issue the next interrogation cycle with scaffolded options. If all issues and gaps are resolved, confirm loop convergence with `convergence_achieved: true`.