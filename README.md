# Class.pro

This repository contains my research project for the AI Engineering course, created by Student Felix ID 12 in the 5th semester of the Bachelor of Science in Computer Science program.

## Overview
The project investigates how low-bit GGUF weight quantization and structure-aware hybrid retrieval affect the quality of local Retrieval-Augmented Generation assistants for computer science education under resource-constrained consumer hardware limits without a dedicated GPU. The study isolates true retrieval gain from closed-book parametric memorization and evaluates claim-level faithfulness alongside safe abstention on unanswerable queries.

## Research Scope
- **Dataset:** A human-verified benchmark of 300 question-answering items over the openly licensed OpenStax *Introduction to Python Programming* textbook, including 255 answerable questions with gold evidence spans and 45 unanswerable abstention probes.
- **Experiments:** A retrieval ablation comparing fixed-window dense search, structure-aware dense search, and hybrid BM25 with dense search and cross-encoder reranking, followed by a quantization study across compact open-weight models at Q4_K_M, Q5_K_M, and Q8_0 precision levels against closed-book baselines.
- **Evaluation and Reproducibility:** Claim-level natural language inference verification with DeBERTa-v3-MNLI, human-calibrated LLM judging, network-isolated Docker execution with Ollama, and full telemetry tracked via MLflow and Langfuse.

## Repository Structure
- `_Context/` - student profile, locked research dossier, and project state.
- `_Deliverables/` - 1-Page Project Brief, NotebookLM slide deck, infographic, mind map, and formal course outputs.
- `_Docs/` - course playbooks, student guides, and NotebookLM research prompts.
- `_X_Pros/` - external course repositories such as `Prime.pro`, ignored by Git.
- `backups/` - backup copies of modified project files and grilling loop records.