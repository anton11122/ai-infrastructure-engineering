# AI Foundations — Common Pitfalls

Mistakes newcomers (even senior DevOps engineers) make when entering AI infra.

## Conceptual
- **Conflating training and inference.** They are different workloads with different hardware, scaling, and cost profiles. Never size or schedule them the same way.
- **Assuming "AI" means "GPU".** Plenty of classical ML runs best on CPUs. Reaching for a GPU by reflex wastes scarce, expensive capacity.
- **Believing models are deterministic.** LLMs sample; the same prompt can yield different outputs. This breaks naive testing and rollback assumptions.
- **Thinking a 200 response means it works.** Models degrade silently; latency/availability monitoring alone misses quality regressions.

## Engineering
- **Loading the model inside the request handler** → catastrophic latency and memory churn. Load once at startup.
- **Downloading weights at container runtime** → slow, flaky cold starts and a hidden external dependency. Bake or cache them.
- **No `readyz`** → traffic routed to pods whose model isn't loaded yet.
- **Unbounded input** → memory blowups and a DoS vector. Always cap input size.

## Sizing & cost
- **Forgetting KV cache + activations** when estimating VRAM. Weights are only part of the memory story.
- **Running GPUs at low utilization** and not noticing — the #1 silent money-burner.
- **Skipping the cost model** because "we don't know the numbers yet." Assumptions beat no estimate.

## Security
- **Loading pickled models from the internet** → remote code execution. Use `safetensors`.
- **Treating model output as safe/clean** → downstream injection and data-leak risks.

## Process
- **Not writing down the "why"** (no ADRs) → the team re-litigates the same decisions and can't reason about migrations later.
- **Big-bang migrations** (e.g. API → self-host overnight) instead of staging behind an abstraction.
