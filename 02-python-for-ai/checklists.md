# Python for AI — Checklists

## Module readiness
- [ ] Completed Module 01.
- [ ] Python 3.11+, `uv` installed, Docker available.
- [ ] `hey` or `ab` for load testing.

## Concept mastery (before Module 03)
- [ ] Can explain why vectorized beats looped (GIL + native layer).
- [ ] Can compute tensor memory from shape × dtype-bytes.
- [ ] Can explain and avoid event-loop blocking.
- [ ] Can describe dynamic batching + the latency↔throughput dial.
- [ ] Can choose async vs processes vs model worker for a given workload.
- [ ] Can produce a reproducible, locked, slim-container service.

## Inference service (production-shaped)
- [ ] Model loaded at startup; `/readyz` gates traffic.
- [ ] Input validated + size-limited; typed response schema.
- [ ] Compute offloaded off the event loop (worker/batch loop).
- [ ] Dynamic batching with tunable size/delay; batch-size metric exposed.
- [ ] Bounded queue + 503 load shedding; per-request timeout + cancellation.
- [ ] RED metrics + inflight gauge; structured logs.
- [ ] Device/dtype matched once; `inference_mode()` used.

## Performance
- [ ] Hot paths vectorized; no `.item()` in loops.
- [ ] Profiled; top bottleneck identified + addressed; re-measured.
- [ ] Batching throughput win demonstrated with numbers.

## Reproducibility & packaging
- [ ] `pyproject.toml` + committed lockfile; torch pinned to CUDA build.
- [ ] Multi-stage image; lockfile-first layer ordering; slim base.
- [ ] No runtime `pip install`; image digest recorded.

## Safety
- [ ] `safetensors` only; no untrusted pickle/`torch.load`.
- [ ] No secrets in notebooks/output cells; outputs stripped.
- [ ] Dependencies scannable for CVEs.
