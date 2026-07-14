# Python for AI — Common Pitfalls

## Performance
- **Python loops over array elements.** The #1 slowdown. Vectorize.
- **`.item()`/`.cpu()` inside loops.** Forces per-step device→host sync; batch the reduction and copy once.
- **Forgetting `inference_mode()`.** Wastes memory building a grad graph you never use.
- **Serving one request at a time** on a GPU → abysmal utilization and cost.

## Async
- **Blocking the event loop** with sync/CPU/GPU work in an `async def` → *all* concurrent requests freeze. The classic beginner-to-senior trap.
- **Using threads for CPU-bound work** and expecting parallelism (GIL says no).
- **Unbounded queues** → memory blowup under spikes → OOMKilled.
- **No per-request timeout** → a stuck model holds futures forever.

## Tensors
- **Device mismatch** (CPU input into GPU model) → runtime error or silent slow copies.
- **Dtype mismatch** (fp32 vs fp16) → errors or precision loss.
- **Ignoring batch/seq dimensions** when estimating memory → surprise OOM.

## Packaging
- **Unpinned deps / no lockfile** → irreproducible builds, "works on my GPU".
- **`COPY src` before installing deps** in Docker → dependency layer rebuilds every code change.
- **Single-stage images with build tools** → bloated, slow, larger attack surface.
- **Runtime `pip install`** → non-deterministic, slow, flaky container starts.

## Safety / process
- **`torch.load` on downloaded pickles** → remote code execution.
- **Secrets in notebook output cells** committed to git.
- **Shipping notebooks to production** instead of packaged, tested modules.
