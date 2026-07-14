# AI Foundations — Best Practices

Principles to carry into every later module. These are the "senior instincts" for AI infra.

## Mindset
- **Treat models and prompts as versioned, testable, rollback-able artifacts** — not config you tweak in prod.
- **Default to the simplest thing that meets the SLO.** Prefer CPU over GPU, managed over self-host, one replica over a cluster — until requirements force otherwise.
- **Measure before optimizing.** Always know your p50/p95/p99 latency, RPS/tokens-per-second, and utilization before touching anything.
- **Assume non-determinism.** Design tests, monitoring, and rollback for systems that don't return identical outputs.

## Engineering
- **Warm models at startup**, gate traffic with `readyz`, and bake/cache weights so cold start isn't a model download.
- **Right-size hardware.** Require justification (model size or latency SLO) before consuming a scarce GPU.
- **Instrument from day one:** RED metrics (Rate/Errors/Duration) + saturation, plus AI-specific signals (tokens, cost) as you add LLMs.
- **Put an abstraction between callers and the model backend** so you can swap managed↔self-hosted later without breaking consumers.

## Cost & scale
- **Utilization is the master cost lever.** Idle GPUs cost the same as busy ones.
- **Model the cost before you build.** Even a rough per-token or per-GPU-hour estimate prevents nasty surprises.
- **Know your first bottleneck** (usually GPU memory or single-process concurrency) and the module that fixes it.

## Security
- **Use `safetensors`; never load untrusted pickles.**
- **Treat all model input as untrusted** and all model output as potentially sensitive/leaky.
- **Track model provenance** (source, checksum, license) as a supply-chain artifact.

## Communication
- **Write ADRs for consequential choices** (self-host vs API, CPU vs GPU). Future-you and your team need the "why".
- **Diagram everything.** If you can't draw it, you don't understand it.
