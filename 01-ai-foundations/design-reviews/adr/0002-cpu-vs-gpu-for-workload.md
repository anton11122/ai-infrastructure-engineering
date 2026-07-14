# ADR-0002: CPU vs GPU for a Given Inference Workload

- **Status:** Accepted
- **Date:** 2026-01-01
- **Deciders:** AI Platform Engineer (you)
- **Difficulty context:** `A`

## Context
We are deploying two very different models: (1) a small text classifier (~66M params, DistilBERT-class) used for internal tagging, and (2) a 7B-parameter LLM for a chat feature. We must decide hardware for each. GPUs are scarce and expensive; CPUs are plentiful.

## Decision Drivers
- Latency SLO per workload.
- Model size vs available memory.
- Throughput required.
- Cost per request.
- GPU scarcity — don't waste GPUs on work CPUs can do.

## Options Considered
### Workload 1 — small classifier
- **Option A: CPU.** ~40–80 ms/request on CPU; cheap, abundant, no driver complexity. Meets SLO comfortably at expected volume.
- **Option B: GPU.** Faster per-request but wastes a scarce GPU on a tiny model; poor utilization; higher cost.

### Workload 2 — 7B LLM
- **Option A: CPU.** Technically possible but latency is unacceptable (seconds/token) and throughput tiny.
- **Option B: GPU.** ~14GB in FP16 fits on a single mid-range GPU (e.g. L4/A10); acceptable latency; required for interactive chat.

## Decision
- **Workload 1 (classifier): CPU.** It meets the SLO, keeps scarce GPUs free, and is cheapest. Reserve GPUs for work that needs them.
- **Workload 2 (7B LLM): single GPU** with a serving engine (vLLM, Module 24) for batching/throughput. Quantize (Module 06) if we need to fit a larger model or raise throughput.

## Consequences
- **Positive:** GPU spend concentrated where it delivers value; classifier is trivially scalable/cheap on CPU.
- **Negative / debt:** two different deployment shapes to operate; the LLM introduces GPU node pools, drivers, and autoscaling concerns (Modules 20, 21).
- **Follow-ups:** define GPU node pool + autoscaling policy for Workload 2; set a rule of thumb — *default to CPU; require justification (size or latency) to consume a GPU.*

## Validation
Measure: classifier p95 on CPU stays under SLO at peak; LLM GPU utilization stays healthy (not idle, not saturated). If classifier volume grows 100×, re-evaluate batching or GPU. If LLM utilization is chronically low, consolidate onto shared GPUs (MIG/time-slicing, Module 20).
