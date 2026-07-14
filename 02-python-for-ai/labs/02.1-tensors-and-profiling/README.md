# Lab 02.1 · Tensors & Profiling  `I`

## Objective
Prove — with a profiler, not faith — the three performance rules of AI Python: vectorize instead of looping, match device/dtype, and avoid CPU↔GPU chatter. You'll produce a before/after speedup report.

## Architecture
```mermaid
graph LR
    S[profile_me.py] --> L[loop vs vectorized]
    S --> D[fp32 vs fp16, cpu vs cuda]
    S --> C[per-step .item() vs bulk copy]
    L --> P[cProfile / timing report]
    D --> P
    C --> P
```

## Prerequisites
- **Tools:** Python 3.11+, `uv` (or pip). Deps in [`requirements.txt`](./requirements.txt).
- **Infra:** CPU is enough; a GPU makes the dtype/device sections vivid (optional).
- **Prior labs:** none (Module 01 recommended).
- **Estimated cost:** free (local).
- **Estimated time:** 30–45 min.

## Implementation
```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# Run the demonstrations
python profile_me.py --n 2000000

# Profile the slow vs fast paths with cProfile
python -m cProfile -s cumtime profile_me.py --n 500000 | head -n 25
```
`profile_me.py` runs three head-to-head comparisons and prints timings + speedups:
1. **loop_sum** vs **vectorized_sum** (NumPy).
2. **fp32** vs **fp16** matmul, on CPU and (if available) CUDA.
3. **per-step `.item()`** copies vs **bulk** transfer.

## Validation
```bash
python profile_me.py --n 1000000
# Expect a table with 'speedup' > 20x for vectorized vs loop.
```

## Expected Output
```
comparison                         slow_ms   fast_ms   speedup
vectorize (loop vs numpy)          420.11      3.90     107.7x
per-step .item() vs bulk copy       88.40      2.10      42.1x
fp32 vs fp16 matmul (cuda)           5.10      1.80       2.8x   # only if GPU present
```

## Failure Scenarios
| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `speedup` near 1x for vectorize | `--n` too small; overhead dominates | Increase `--n` (e.g. 2_000_000) |
| fp16 rows missing | No CUDA (fp16 on CPU is often unsupported/slow) | Expected on CPU; run on a GPU box to see it |
| `RuntimeError: "addmm" not implemented for 'Half'` on CPU | fp16 matmul on CPU | Guarded in code to GPU-only; upgrade torch if you edited it |
| High variance between runs | Background load / no warm-up | Code warms up; close other apps; increase iters |

## Debugging Guide
1. Confirm the venv + `python -c "import torch,numpy"`.
2. `python -c "import torch; print(torch.cuda.is_available())"` to know which sections will run.
3. Read the `cProfile` `cumtime` column — the top rows are where real time goes.
4. If numbers look off, raise `--n` and `--iters` so timing dominates measurement noise.

## Cleanup
```bash
deactivate && rm -rf .venv
```

## Production Discussion
Every speedup here is a cost saving in production: fewer GPU-seconds per request = lower $/request and higher achievable RPS. The `.item()`-in-a-loop anti-pattern is a *real* recurring bug in ML services (often hidden in logging/metrics code). Profiling discipline — measure, then optimize the top line — is exactly how you'll tune serving engines in Modules 24–28.
