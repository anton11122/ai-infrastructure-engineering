# AI Foundations — References

Curated, categorized starting points. Prefer primary sources. Verify versions/links as the ecosystem moves fast.

## Research papers (foundational context)
- **"Attention Is All You Need"** (Vaswani et al., 2017) — the transformer paper. You'll read it properly in Module 05; skim now for context.
- **"Deep Learning"** (LeCun, Bengio, Hinton, 2015, *Nature*) — a concise overview of why deep learning works.
- **"Scaling Laws for Neural Language Models"** (Kaplan et al., 2020) — why more compute/data/params → better models; motivates GPU demand.

## Books
- **"Designing Machine Learning Systems"** — Chip Huyen. The best bridge from software/infra thinking to ML systems. Highly recommended for this whole track.
- **"Machine Learning Engineering"** — Andriy Burkov. Practical lifecycle view.
- **"The Hundred-Page Machine Learning Book"** — Burkov. Fast conceptual grounding for Modules 03–04.

## Videos / courses
- **3Blue1Brown — "Neural Networks" series** (YouTube). Best visual intuition for what a neural net *is*.
- **Andrej Karpathy — "Intro to Large Language Models"** (YouTube, ~1hr). The single best "what is an LLM" talk for engineers.
- **Karpathy — "Let's build GPT from scratch"** — deeper; revisit during Module 05.

## Blogs / explainers
- **Hugging Face blog & docs** — practical, engineer-oriented, current.
- **Jay Alammar — "The Illustrated Transformer"** — visual transformer intuition (Module 05 companion).
- **Chip Huyen's blog** — ML systems design and MLOps essays.

## GitHub repositories (orientation)
- `huggingface/transformers` — the library you touched in Lab 01.2.
- `pytorch/pytorch` — the framework under most of this track.
- `vllm-project/vllm` — the serving engine you'll master in Module 24 (browse the README now).

## Industry standards / references
- **OWASP Top 10 for LLM Applications** — the security backbone for Module 30; skim now.
- **NIST AI Risk Management Framework (AI RMF)** — governance vocabulary for Module 30/32.

## Benchmarks (awareness)
- **MLPerf Inference** — industry-standard inference benchmarks; you'll interpret these in serving modules.
- **Hugging Face Open LLM Leaderboard** — how open models are compared (quality, not infra).

## How to use these
Don't read everything now. For Module 01, watch Karpathy's "Intro to LLMs", the 3Blue1Brown NN series, and skim Chip Huyen's book intro. Bookmark the rest — each later module points back here.
