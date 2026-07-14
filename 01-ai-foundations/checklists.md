# AI Foundations — Checklists

## Module readiness (before starting)
- [ ] Comfortable on Linux, Docker, Kubernetes, Terraform, AWS, CI/CD (assumed prerequisites).
- [ ] Python 3.11+ available; can create virtual envs.
- [ ] (Optional) access to a GPU (local or cloud) for the dramatic version of Lab 01.1.

## Concept mastery (before advancing to Module 02)
- [ ] Can place any system in the AI/ML/DL/GenAI/LLM hierarchy with justification.
- [ ] Can explain training vs inference as distinct workloads.
- [ ] Can name the platform-owned lifecycle stages.
- [ ] Can explain from first principles why GPUs beat CPUs for DL.
- [ ] Can estimate model VRAM (~2 bytes/param) and compute (~2 FLOP/param/token).
- [ ] Can draw the 7-layer modern AI stack from memory.

## Minimal inference service (production-shaped)
- [ ] Model loaded once at startup (not per request).
- [ ] `/healthz` (liveness) and `/readyz` (model-loaded) endpoints.
- [ ] Input validation + size limits.
- [ ] Prometheus `/metrics`: request rate, errors, latency histogram, in-flight.
- [ ] Structured logs.
- [ ] Weights baked/cached (no runtime download).
- [ ] Typed response schema (no raw model output).
- [ ] Load-tested; p50/p95/p99 + RPS recorded; bottleneck understood.

## Security & provenance
- [ ] Model format is `safetensors` (no untrusted pickles).
- [ ] Model source, version, checksum, and license recorded.
- [ ] Input treated as untrusted; output treated as potentially sensitive.

## Cost
- [ ] A first-order cost model exists (per-token or per-GPU-hour) with stated assumptions.
- [ ] Hardware right-sized (GPU only where justified).
- [ ] Utilization is observable.

## Decision hygiene
- [ ] ADRs written for self-host-vs-API and CPU-vs-GPU choices.
- [ ] An abstraction sits between callers and the model backend.
