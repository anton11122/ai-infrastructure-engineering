# Python for AI — References

Curated, categorized. Verify versions as the ecosystem moves fast.

## Official docs (primary sources)
- **PyTorch docs** — tensors, `inference_mode`, `torch.profiler`, CUDA semantics. The canonical reference.
- **NumPy docs** — broadcasting rules, vectorization, dtypes.
- **FastAPI docs** — async, dependencies, lifespan, testing.
- **uv docs (Astral)** — projects, locking, `uv sync --frozen`.
- **Uvicorn docs** — workers, deployment settings.

## Books
- **"Fluent Python"** — Luciano Ramalho. Deep Python (async, data model, performance). The reference for writing idiomatic, fast Python.
- **"High Performance Python"** — Gorelick & Ozsvald. Profiling, vectorization, and where Python is slow — directly relevant to this module.
- **"Designing Machine Learning Systems"** — Chip Huyen (relevant chapters on serving/infra).

## Videos / talks
- **"Async/await in Python"** talks (e.g. by core devs / EuroPython) — mental model for the event loop.
- **PyTorch performance tuning guide** (official) — inference_mode, AMP, data movement.
- **Anyscale / Ray talks on batched serving** — real-world batching motivation (bridges to Modules 22, 24).

## Blogs / explainers
- **Real Python** — practical async, packaging, testing tutorials.
- **PyTorch blog** — performance and serving posts.
- **Astral blog** — uv design and reproducibility rationale.

## GitHub repositories
- `pytorch/pytorch` — the framework.
- `tiangolo/fastapi` — async web framework used throughout.
- `astral-sh/uv` — env/dependency tool (the handbook default).
- `vllm-project/vllm` — see how continuous batching/KV cache extend the batching you built here (Module 24 preview).
- `huggingface/safetensors` — the safe model format.

## Standards / references
- **PEP 8 / PEP 484 (type hints) / PEP 517–518 (build system)** — the Python packaging + style baseline.
- **OWASP Top 10 for LLM Apps** — supply-chain + input-handling context (deep-dive Module 30).

## Benchmarks / tools (awareness)
- **`cProfile`, `torch.profiler`, `memory_profiler`, `py-spy`** — the profiling toolkit (Lab 02.1).
- **`hey`, `wrk`, `locust`** — HTTP load generators for the serving labs.

## How to use these
For this module: read PyTorch's tensor + inference_mode docs, skim "High Performance Python" ch. on profiling/vectorization, and the FastAPI async + uv locking docs. Everything else is bookmark-and-return.
