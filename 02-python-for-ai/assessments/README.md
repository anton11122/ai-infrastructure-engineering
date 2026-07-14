# Module 02 · Assessments

Prove mastery before advancing to Module 03. Scoring in the [assessment framework](../../00-roadmap/assessment-framework.md). **Gate:** pass the Practical Exam **and** the System-Design Interview.

Answer key: [`answers.md`](./answers.md). Code-review exercise: [`code-review.md`](./code-review.md).

---

## 1. Self-Assessment Quiz
`B→I` — 12 questions. Aim ≥ 10/12.

1. Why is a Python `for` loop over array elements so much slower than a vectorized call? Reference the GIL and the native layer.
2. Name the three defining properties of a tensor and why each affects cost.
3. Compute the fp16 memory of a `(64, 1024, 4096)` activation tensor.
4. What is the cardinal sin in an `async def` inference handler, and what does it cause?
5. In dynamic batching, what do `max_batch_size` and `max_delay_ms` trade off?
6. Why use *processes* (not threads) for CPU-bound parallelism in Python?
7. Why should model compute run in a worker rather than inline in the async handler?
8. Give two reasons notebooks are unsafe for production.
9. What four layers must align in the GPU stack, and what happens on mismatch?
10. Why copy tensors to the GPU in bulk instead of per-step `.item()`?
11. What does `torch.inference_mode()` buy you and why?
12. Why is a committed lockfile a *security* and *reproducibility* control?

## 2. Practical Exam  `I→A`
- **Task:** Deploy Lab 02.2's service, then produce a report proving batching improves throughput: run load at c=1, 10, 50 with batching ON and OFF; tabulate RPS + p50/p95; explain the crossover and the effect of `max_delay_ms`.
- **Environment:** local, `hey`/`ab`.
- **Time box:** 90 minutes.
- **Pass bar:** service healthy with `/metrics`; report shows batching ≥ 3× throughput at c=50; correct explanation of the latency↔throughput dial and why per-request loses under concurrency.

## 3. Architecture Interview  `A`
- **Prompt:** "Design a Python inference service for a GPU model under concurrent load. Walk me from request to response and justify where compute runs."
- **Expected topics:** async web layer, bounded queue/backpressure, batch loop + dial, model worker separation, RED + batch-size metrics, graceful shutdown, first scaling bottleneck.

## 4. Troubleshooting Interview  `A`
- **Setup:** "Under load, *all* requests to our async service get slow simultaneously, even ones that should be instant. CPU shows one core pinned."
- **Injected fault (hidden):** a synchronous, CPU-bound model call runs directly inside the `async def` handler, blocking the event loop.
- **Success:** identifies event-loop blocking; fixes via `run_in_executor`/worker/batch loop; explains the GIL/async interaction.

## 5. Code Review  `A`
Review the snippet in [`code-review.md`](./code-review.md); list issues with impact + fix.

## 6. Scenario Interview  `A`
- **Prompt:** "A data scientist's notebook 'works' and product wants it live this week. It uses `pickle` model files, hardcoded paths, and unpinned deps. How do you productionize it safely and fast?"
- **Success:** promotion plan (extract pure functions, tests, pydantic, config via env), `safetensors` migration, lockfile + slim image, and a staged rollout — while communicating the risks of shortcutting.

## 7. System Design Interview  `S`
- **Prompt:** "Design a shared Python inference platform component that several teams can deploy their small models onto, with good utilization and reproducibility. What are the contracts and the scaling model?"
- **Deliverable:** design doc + Mermaid diagram + a prioritized roadmap tying to the async/batching/packaging patterns; define the service contract (health/ready/metrics, batching config), and how web vs model scale independently.

## 8. Production Incident  `A`
- **Alert:** "Inference service pods OOMKilled repeatedly during a traffic spike; latency was fine right before."
- **Target MTTR:** 30 min.
- **Injected fault (reveal at debrief):** unbounded in-memory request queue + no load shedding; the spike queued faster than the model drained → memory blowup.
- **Deliverable:** mitigation (bound the queue, shed with 503, add per-request timeout, scale replicas) + a postmortem with action items (backpressure, autoscaling signal, capacity).

## 9. Module Final Exam
`B→S`:
- **Practical (40%):** the batching report above.
- **Design (40%):** the System Design Interview above.
- **Short answer (20%):**
  1. Draw the async-front / batch-at-compute-boundary architecture and label where the event loop must never block.
  2. Given interactive chat vs nightly bulk embedding, choose `max_batch`/`max_delay_ms` for each and justify.
  3. Explain the driver→CUDA→torch chain and one failure it causes.
  4. Explain why processes beat threads for CPU-bound Python and where async fits.
  5. List the reproducibility controls that make an ML image deployable identically everywhere.

**Pass bar:** ≥ 70% weighted, neither Practical nor Design below 60%.
