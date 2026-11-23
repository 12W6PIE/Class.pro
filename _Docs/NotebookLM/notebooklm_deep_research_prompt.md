# NotebookLM Deep Research Prompts

Paste the compact primary prompt into NotebookLM: **Discover / Search Web -> Deep Research**.

## Primary Deep Research Prompt (Compact)

```text
Find peer-reviewed papers (2020-2026, arXiv, ACL, EMNLP, NeurIPS, SIGIR, IEEE, ACM) for an empirical study on local resource-constrained RAG over Python programming textbooks. Focus on four areas:
1. Weight quantization (GGUF, GPTQ, AWQ, 4-bit vs 8-bit) in 3B-14B open-weight LLMs and its impact on RAG faithfulness, hallucinations, and abstention.
2. Structure-aware and code-aware chunking, hybrid BM25 + dense retrieval, and cross-encoder reranking for technical or educational QA.
3. RAG evaluation frameworks (RAGAS, ARES), claim-level NLI entailment verification (DeBERTa-MNLI), LLM-as-a-judge self-preference bias, and human calibration via Cohen's kappa.
4. Closed-book parametric memorization, data contamination on open textbooks, and unanswerable query abstention benchmarks (SQuAD 2.0 style).
Prioritize empirical benchmarks, reproducible evaluation protocols, and open-access full papers.
```

## Optional Follow-Up Deep Research Prompt (Gap-Filling)

Use this after importing the first batch of sources if statistical testing or educational CS benchmarks are underrepresented:

```text
Identify gaps in the current sources and find peer-reviewed studies (2021-2026) specifically covering:
1. Statistical significance testing for RAG and IR benchmarks using paired bootstrap confidence intervals, Wilcoxon signed-rank, McNemar tests, and Holm-Bonferroni correction.
2. Contamination-controlled evaluation comparing open-book RAG against closed-book parametric baselines on computer science or programming education datasets.
3. Failure taxonomies for code-tracing, syntax, and conceptual QA in educational LLM assistants.
```