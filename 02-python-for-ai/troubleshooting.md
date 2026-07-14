# Python for AI — Troubleshooting

Symptom → likely root cause → fix.

| Symptom | Likely root cause | Fix |
|---------|-------------------|-----|
| All concurrent requests slow at once, one core pinned | Sync/CPU-bound work blocking the event loop in an `async def` | Offload compute to `run_in_executor`/worker/batch loop |
| Throughput doesn't improve with batching | Requests not overlapping (low concurrency) or `max_delay_ms` too small | Raise concurrency; tune the batch delay/size |
| `RuntimeError: Expected all tensors on the same device` | Input on CPU, model on GPU (or vice versa) | `x = x.to(model_device)` once at the edge |
| `RuntimeError: expected scalar type Half but found Float` | dtype mismatch | Cast input to model dtype: `x.to(dtype=torch.float16)` |
| `torch.cuda.is_available()` is False on a GPU box | CPU-only torch wheel or driver/CUDA mismatch | Install matching cuXX torch; verify `nvidia-smi` + driver |
| Pods OOMKilled under load spike | Unbounded request queue / no load shedding | Bound the queue; return 503 when full; add autoscaling |
| Very slow NumPy/torch section | Python loop over elements | Vectorize the operation |
| Latency spikes from logging/metrics | `.item()`/`.cpu()` per step forcing sync copies | Reduce on device; copy once |
| Docker rebuilds deps every code change | `COPY src` before dependency install | Copy lockfiles + install first, then source |
| `uv sync --frozen` fails in CI | Lockfile stale vs `pyproject.toml` | `uv lock` and commit |
| Container `ModuleNotFoundError` | venv not on PATH / wrong `PYTHONPATH` | Set `ENV PATH=/app/.venv/bin:$PATH` |
| Non-reproducible results across machines | Unpinned deps / unset seeds / different torch build | Lock deps; pin torch; set seeds where determinism matters |

## General method
1. **Reproduce under controlled load** (fixed concurrency) to separate latency vs throughput issues.
2. **Check `/readyz` + `/metrics`** (inflight, batch-size histogram) to localize the stall.
3. **Profile** the hot path (`torch.profiler`, `cProfile`) rather than guessing.
4. **Isolate the layer:** environment (deps/CUDA), web (async/queue), or compute (model/device/dtype)?
5. **Bisect config** (`MAX_BATCH`, `MAX_DELAY_MS`, workers) and re-measure each change.
