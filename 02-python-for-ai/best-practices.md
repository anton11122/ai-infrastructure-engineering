# Python for AI — Best Practices

## Performance
- **Vectorize everything hot.** No Python loops over tensor/array elements. Express operations on whole arrays.
- **Batch at the compute boundary.** One forward pass over N inputs beats N passes.
- **Match device + dtype once, early.** Convert inputs to the model's device/dtype at the edge, not per element.
- **Use `torch.inference_mode()`** for all inference paths.
- **Keep data resident on the GPU;** transfer in bulk at boundaries; avoid `.item()`/`.cpu()` in loops.
- **Profile before optimizing.** `cProfile`/`torch.profiler`/`memory_profiler` — fix the top line, then re-measure.

## Async & concurrency
- **Never run model compute inline in an `async def` handler.** Offload to a worker/executor/batch loop.
- **Use processes for CPU-bound parallelism** (GIL); async for I/O-bound glue.
- **Separate the web layer from the model worker** so they scale independently.
- **Bound your queues** and shed load with 503 rather than OOM.
- **Add per-request timeouts + cancellation;** shut down background tasks gracefully.

## Packaging & reproducibility
- **Declare + lock deps** (`pyproject.toml` + committed `uv.lock`); pin `torch` to a CUDA build.
- **Immutable images;** no runtime `pip install`.
- **Multi-stage Docker, lockfile-first layer ordering** for cache efficiency.
- **Treat the driver→CUDA→torch chain as pinned infrastructure.**

## Safety
- **`safetensors`, never untrusted `pickle`/`torch.load`.**
- **Validate + size-limit all input.** Define typed response schemas; don't leak raw model output.
- **Strip notebook outputs + secrets before commit.** Notebooks are for exploration; production is packaged code.

## Interfaces
- Every service exposes `/healthz`, `/readyz`, `/metrics` with RED + batch-size + inflight signals.
