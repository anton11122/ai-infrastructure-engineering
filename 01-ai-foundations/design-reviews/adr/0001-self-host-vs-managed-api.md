# ADR-0001: Self-Host vs Managed API for the Initial Workload

- **Status:** Accepted
- **Date:** 2026-01-01
- **Deciders:** AI Platform Engineer (you), Eng lead
- **Difficulty context:** `A`

## Context
A team wants to ship an internal feature backed by an LLM. Traffic is low and uncertain at launch (early adoption). Data is internal but **not** highly regulated. The team has no existing GPU platform. We must choose between calling a managed API and self-hosting a model.

## Decision Drivers
- Time-to-first-value: weeks matter; this is an experiment.
- Volume: low and unpredictable initially.
- Data sensitivity: moderate (internal, non-regulated).
- Team capability: no GPU/serving platform yet (that's what this handbook builds).
- Cost: minimize upfront and avoid paying for idle GPUs.

## Options Considered
### Option A — Managed API (e.g. hosted LLM API / Bedrock)
- **Pros:** live in hours; zero infra to operate; scales elastically; no idle GPU cost at low volume.
- **Cons:** per-token cost can grow with success; data leaves our boundary (acceptable here); vendor rate limits; less control over latency.

### Option B — Self-host on GPUs (vLLM on K8s)
- **Pros:** full control + privacy; cheaper at *high steady* volume; any open model.
- **Cons:** weeks of platform work we don't yet have; risk of low GPU utilization at low volume = wasted spend; operational burden.

### Option C — Hybrid behind a gateway
- **Pros:** best long-term; route by cost/sensitivity.
- **Cons:** premature — we don't have the gateway or self-hosting yet.

## Decision
**Choose Option A (Managed API) for launch**, behind a thin internal abstraction (our own small gateway shim) so the backend can be swapped later without changing callers. Re-evaluate when steady-state volume crosses the cost-crossover point or when data-sensitivity requirements tighten.

## Consequences
- **Positive:** fastest path to value; no GPU ops now; elastic.
- **Negative / debt:** per-token cost exposure at scale; external data flow (documented + approved); we depend on vendor limits.
- **Follow-ups:** define the volume/cost threshold that triggers a self-host evaluation; build the abstraction layer now so migration is cheap (this becomes the AI gateway in Module 31).

## Validation
Track monthly token spend vs a modeled self-host cost. Revisit this ADR when API spend exceeds ~60% of modeled self-host TCO for 2 consecutive months, or on any change to data-residency requirements.
