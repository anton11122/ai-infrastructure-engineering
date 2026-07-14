# Module 01 · Assessments

Complete these to prove mastery before advancing to Module 02. Scoring guidance is in the [assessment framework](../../00-roadmap/assessment-framework.md). **Gate:** pass the Practical Exam **and** the System-Design Interview.

Answer key for the quiz + final is in [`answers.md`](./answers.md) (no peeking until you've attempted them).

---

## 1. Self-Assessment Quiz
`B→I` — 12 questions. Aim for ≥ 10/12.

1. Place each in the AI/ML/DL/GenAI/LLM hierarchy: a hand-coded chess engine; a gradient-boosted fraud model; Stable Diffusion; Llama-3.
2. In one sentence each, contrast **training** and **inference** as *workloads*.
3. Which lifecycle stages does an AI *platform* engineer primarily own?
4. Why are GPUs faster than CPUs for neural-net math? Answer from first principles.
5. Estimate the FP16 VRAM needed for a 13B-parameter model. Show the rule you used.
6. Estimate the compute (FLOPs) to generate one token from a 7B model. Show the rule.
7. Name three reasons a model can return HTTP 200 while being "broken".
8. Give two signals from a product's UX that imply a RAG architecture.
9. When is a **managed API** the right call over self-hosting? Give three conditions.
10. What is the single scarcest resource on a GPU, and why does it cap model size?
11. Why is `safetensors` preferred over pickled model files?
12. What does "GPU utilization" have to do with cost, and why is low utilization the #1 way to waste money?

## 2. Practical Exam  `I`
- **Task:** From scratch, deploy the Lab 01.2 inference service, load-test it at 3 concurrency levels, and produce a one-page report with a latency/throughput table and an explanation of where and why it saturates.
- **Environment:** your machine (CPU is fine) + `hey`/`ab`.
- **Time box:** 90 minutes.
- **Pass bar:** service runs with `/healthz` + `/metrics`; report shows p50/p95/p99 and RPS at each level; explanation correctly identifies the CPU/single-process bottleneck and names the fix (batching/replicas).

## 3. Architecture Interview  `A`
- **Prompt:** "Design a minimal but production-shaped serving setup for one internal model. Walk me from request to response, and tell me your first three scaling bottlenecks."
- **Expected topics:** replicas + LB, health/readiness gating, metrics (RED), model artifact source + rollback, where batching/gateway/autoscaling enter later.
- **Rubric:** correctness, trade-offs, scale, operability (framework).

## 4. Troubleshooting Interview  `I→A`
- **Setup:** the Lab 01.2 service is deployed but "the first request after every restart takes 8 seconds, then it's fast."
- **Injected fault (hidden):** the model is loaded lazily on first request instead of at startup; container also downloads the model at runtime.
- **Success:** candidate identifies cold-start/lazy-load + runtime download, and proposes startup warming + baking the model into the image (or a cache volume) + `readyz` gating.

## 5. Code Review  `A`
Review the snippet in [`code-review.md`](./code-review.md) and list the issues with impact + fix.

## 6. Scenario Interview  `A`
- **Prompt:** "Leadership loved the API-backed prototype; traffic is now 50× and finance is alarmed at the per-token bill. Data is still non-regulated. What do you do, and how do you decide?"
- **Success:** references the cost-crossover, proposes evaluating self-hosting behind the existing abstraction, quantifies the decision, and stages a migration (hybrid + gateway) rather than a big-bang rewrite.

## 7. System Design Interview  `S`
- **Prompt:** "You're the first platform hire. Sketch a 6-month plan to evolve a single API-backed feature into a small internal AI platform serving several teams. What do you build first and why?"
- **Deliverable:** a short design doc + a Mermaid diagram + a prioritized roadmap tied to the knowledge graph (gateway → self-host → observability → multi-tenancy). Defend sequencing on risk/value.

## 8. Production Incident  `I→A`
- **Alert:** "p95 latency on the tagging service tripled at 09:00; error rate normal; CPU pinned at 100%."
- **Target MTTR:** 30 min.
- **Injected fault (reveal at debrief):** a batch job started sending 20× normal volume to the CPU-bound classifier; no autoscaling, single replica.
- **Deliverable:** mitigation (scale replicas / rate-limit the batch source / move to async) + a postmortem (impact, timeline, root cause, action items incl. capacity + autoscaling).

## 9. Module Final Exam
`B→S` — combines:
- **Practical (40%):** the Practical Exam above.
- **Design (40%):** the System Design Interview above.
- **Short answer (20%):** answer these 5:
  1. Draw the 7-layer modern AI stack and place vLLM, a vector DB, and an AI gateway.
  2. Explain why training and inference clusters are sized differently.
  3. Given a 70B model in FP16, does it fit on one 80GB GPU? Show the math and state the implication.
  4. Give three things that make a model a *supply-chain* risk.
  5. Describe the hybrid (gateway + routing) pattern and why enterprises converge on it.

**Pass bar:** ≥ 70% weighted, with neither Practical nor Design below 60%.
