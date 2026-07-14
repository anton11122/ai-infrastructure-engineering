# ADR-0002: Dynamic Batching vs Per-Request Serving

- **Status:** Accepted
- **Date:** 2026-01-01
- **Deciders:** AI Platform Engineer (you)
- **Difficulty context:** `A`

## Context
Our inference service faces concurrent traffic against an expensive model (GPU-bound). We must decide whether to serve each request independently or batch concurrent requests into single forward passes. This choice sets our throughput-per-dollar and our tail latency.

## Decision Drivers
- Throughput per GPU (cost efficiency).
- Tail latency SLO (p95/p99).
- Implementation + operational complexity.
- Traffic shape (interactive vs bulk; bursty vs steady).

## Options Considered
### Option A — Per-request serving
- **Pros:** simplest; lowest latency at very low load; no batch coordination.
- **Cons:** terrible GPU utilization under concurrency; low throughput; high $/request; doesn't scale.

### Option B — Static dynamic batching (build here)
- **Pros:** large throughput gain under concurrency; tunable latency↔throughput dial; moderate complexity.
- **Cons:** adds a few ms latency; a straggler input can slow a batch; waits for whole batch to finish.

### Option C — Continuous batching (vLLM-class, Module 24)
- **Pros:** best throughput for token-generating LLMs; frees slots per token step.
- **Cons:** significant complexity; provided by a dedicated engine, not hand-rolled.

## Decision
**Adopt dynamic batching (Option B) as the default** for concurrent GPU inference, exposing `max_batch_size` and `max_delay_ms` as configuration tuned per workload (small delay for interactive, larger for bulk). For **token-generating LLMs at scale, defer to a purpose-built engine with continuous batching (Option C, Module 24)** rather than hand-rolling. Use **per-request (Option A) only** for trivial CPU models or extremely low, latency-critical traffic.

## Consequences
- **Positive:** major cost/throughput win; clear tuning knobs; smooth path to vLLM later.
- **Negative / debt:** batch coordination code to maintain; straggler + timeout handling required; must bound the queue to avoid OOM.
- **Follow-ups:** add length bucketing + per-request timeouts; plan migration of LLM workloads to vLLM (Module 24).

## Validation
Measure throughput and p95 with batching on vs off at representative concurrency. Batching must deliver a meaningful throughput gain (target ≥ 3× at 50 concurrent) without breaching the latency SLO. Re-evaluate per workload; move to continuous batching when serving generative LLMs.
