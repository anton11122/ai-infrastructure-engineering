# Module 02 · Answer Key & Model Answers

> Attempt everything before reading.

## Quiz
1. A Python loop executes bytecode through the interpreter per element while holding the GIL; a vectorized call makes one trip into optimized, GIL-releasing, SIMD/multi-threaded native code that processes the whole array. The per-element interpreter tax is what makes loops 50–200× slower.
2. **shape** (dimensions → determines element count/broadcast validity), **dtype** (bytes/element → memory + Tensor-Core eligibility), **device** (cpu/cuda → must match the compute, or you error/pay copy costs).
3. `64 × 1024 × 4096 = 268,435,456` elements × 2 bytes (fp16) ≈ **536 MB** for one tensor.
4. Running synchronous/CPU-or-GPU-bound work directly in the handler **blocks the event loop**, freezing *every* concurrent request. Offload to a worker/executor/batch loop.
5. `max_batch_size` ↑ → throughput + memory + latency ↑. `max_delay_ms` ↑ → fuller batches (throughput) but higher latency. Together they are the latency↔throughput dial.
6. The GIL serializes Python bytecode across threads, so CPU-bound threads don't run in parallel; separate **processes** each have their own interpreter/GIL and truly parallelize. (Native libs that release the GIL are the exception.)
7. So the event loop stays free to accept/await other requests, and so compute can be batched and scaled independently of the web layer; running inline serializes and blocks.
8. Hidden/out-of-order state (non-reproducible), no tests/packaging, secrets leaking into output cells (any two).
9. **NVIDIA driver → CUDA runtime → torch cuXX build → your code.** Mismatch → `cuda.is_available()==False` or cryptic kernel errors; can't use the GPU.
10. Each `.item()` forces a device→host synchronization + copy; doing it per-step serializes on transfers. Reduce on-device and copy once at the end.
11. `inference_mode()` disables autograd bookkeeping (no grad graph), reducing memory and speeding execution; correct for inference where you never call `.backward()`.
12. Reproducibility: exact resolved versions → identical builds/rollbacks. Security: pinning + hashes prevent dependency substitution/tampering and let you scan a known set for CVEs.

## Final — short answers
1. **Diagram:** clients → FastAPI async handler → bounded async queue → batch loop → **model worker (compute here, off the loop)** → model. The **event loop must never run model compute**; it only enqueues and awaits futures.
2. **Interactive chat:** small `max_delay_ms` (e.g. 2–5 ms), modest `max_batch` → protect p95. **Nightly bulk embedding:** large `max_batch` (e.g. 128+) and larger `max_delay_ms` (tens of ms) → maximize throughput/utilization; latency doesn't matter.
3. torch is compiled against a specific CUDA version; the NVIDIA driver must support that CUDA runtime. A common failure: CPU-only torch (or a cu-mismatch) → `torch.cuda.is_available()` is `False`, GPU unused.
4. Threads share one GIL so CPU-bound Python doesn't parallelize; processes each have their own interpreter and parallelize. Async handles many concurrent **I/O-bound** tasks on one thread by yielding while waiting — great for the web layer, not for CPU-bound compute.
5. Committed lockfile (full resolved tree, ideally hashed); torch pinned to an explicit CUDA build; immutable image built on a pinned base (record digest); no runtime `pip install`; deterministic model source + version + checksum.

## Practical exam — what "good" looks like
A table like:
```
c    mode        RPS     p50   p95
1    batched     190     5ms   9ms
1    per-req     195     5ms   8ms     # ~equal at c=1
10   batched     1400    6ms   14ms
10   per-req     640     14ms  28ms
50   batched     1850    24ms  41ms
50   per-req     520     92ms  160ms   # batching ~3.5x throughput
```
Plus a correct narrative: at c=1 they're equal (no batch to form); under concurrency batching amortizes the forward pass across requests; raising `max_delay_ms` fills batches (more throughput) at the cost of latency.
