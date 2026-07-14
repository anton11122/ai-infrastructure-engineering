# Module 01 · Answer Key & Model Answers

> Attempt everything before reading. These are model answers, not the only correct ones.

## Quiz
1. **Hierarchy:** chess engine = AI only (rules, no learning); fraud GBM = AI+ML (not DL); Stable Diffusion = AI+ML+DL+GenAI (not an LLM); Llama-3 = all five (LLM).
2. **Training** = build the model: forward+backward passes over huge data, stateful, checkpointed, throughput-bound. **Inference** = use the model: forward pass only, per-request, latency-sensitive, mostly stateless.
3. **Platform-owned stages:** model registry, deployment/serving, monitoring/observability (and enabling training infra + retraining automation). The "outer loop".
4. **GPUs:** neural-net math is massively parallel matrix multiplication; GPUs have thousands of simple cores doing the same op on different data (SIMT), matching that pattern; CPUs have few latency-optimized cores.
5. **13B FP16:** ~2 bytes/param × 13e9 ≈ **26 GB** (weights only; add activations + KV cache in practice).
6. **7B compute/token:** ~2 FLOP/param/token × 7e9 ≈ **14 GFLOP/token**.
7. **Silent breakage:** data/embedding drift; a bad prompt/model version deployed; upstream retrieval returning stale/empty context — all return 200 with worse content.
8. **RAG signals:** shows citations/sources; answers reflect *your* private/up-to-date documents rather than only training data.
9. **Managed API right when:** low/uncertain volume; no GPU/platform expertise yet; non-sensitive data; need speed-to-market. (Any three.)
10. **VRAM** is scarcest; weights + activations + KV cache must all fit in GPU memory, so model size is capped by it (drives quantization + distributed inference).
11. **safetensors:** pickled models can execute arbitrary code on load (deserialization RCE); safetensors is a pure data format — a supply-chain safety win.
12. **Utilization ↔ cost:** GPUs bill by the hour regardless of use; idle GPUs cost the same as busy ones, so low utilization = paying for nothing = the top waste vector.

## Final — short answers
1. **7-layer stack:** Hardware → Orchestration platform (K8s/Ray) → Data & retrieval → Serving engines → AI gateway → Orchestration (agents) → Applications. vLLM = serving engine; vector DB = data & retrieval; AI gateway = gateway layer.
2. **Cluster sizing:** training is throughput-bound, long-running, tolerant of latency, uses big batches + interconnect for gradient sync → optimize for aggregate FLOPs/bandwidth. Inference is latency-sensitive, bursty, per-request → optimize for low latency + high utilization via batching + autoscaling.
3. **70B FP16 on 80GB:** ~2 × 70e9 = **140 GB** > 80 GB → **does not fit**; implication: quantize (e.g. FP8/INT4) and/or split across GPUs with tensor/pipeline parallelism (Module 28).
4. **Supply-chain risks:** executable model formats (pickle RCE); unverified provenance/checksums of downloaded weights; compromised or poisoned upstream datasets/base models; dependency chain of the serving stack.
5. **Hybrid pattern:** an AI gateway fronts multiple backends (small self-hosted, large self-hosted, premium API) and routes by cost/latency/sensitivity, centralizing auth, rate limiting, cost tracking, and observability. Enterprises converge on it because it optimizes cost + control while preserving flexibility and a single control point.
