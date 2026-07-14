# Code Review Exercise  `A`

Review this async inference endpoint. Find every issue with **impact** and **fix**. Attempt before reading the model answer.

```python
import torch
from fastapi import FastAPI

app = FastAPI()
model = torch.load("model.pkl")          # (a)

@app.post("/predict")
async def predict(text: str):            # (b)
    x = encode(text)                      # returns a CPU fp32 tensor
    for i in range(len(x)):               # (c)
        x[i] = x[i] / 255.0
    y = model(x)                          # (d) sync compute in async handler
    return {"logits": y.tolist(), "top": float(y.max().item())}   # (e)
```

---

## Model answer (planted issues)

| # | Issue | Impact | Fix |
|---|-------|--------|-----|
| a | **`torch.load` on a pickle** | Arbitrary code execution on load (supply-chain RCE) | Use `safetensors`; verify checksum/provenance |
| a2 | **Model loaded at import, no error handling / readiness** | Import-time failure crashes worker; no `/readyz` | Load in lifespan; expose `/readyz` gating traffic |
| b | **No input validation / size limit** | Unbounded input → memory/DoS | Pydantic model with `max_length` |
| c | **Python loop over tensor elements** | 50–200× slower than vectorized; blocks the loop longer | `x = x / 255.0` (vectorized) |
| d | **Synchronous model compute inside `async def`** | Blocks the event loop → all concurrent requests stall | Offload via `run_in_executor`/worker/batch loop |
| d2 | **No device/dtype handling** | CPU tensor into a possibly-GPU model → error or slow copies | Move+cast once: `x.to(device, dtype)` |
| d3 | **No `inference_mode`** | Builds grad graph → wasted memory/time | Wrap compute in `torch.inference_mode()` |
| d4 | **No batching under concurrency** | Poor GPU utilization, low throughput | Add dynamic batching (batch loop) |
| e | **`.item()`/`.tolist()` chatter + raw output leak** | Extra device→host copies; unstable/oversharing response contract | Minimize copies; define a typed response schema |
| f | **No metrics/logging/timeouts** | No observability; stuck requests hang forever | Add RED metrics, structured logs, per-request timeout |

**Strong candidates also note:** unpinned deps (reproducibility), no graceful shutdown of any background tasks, and no backpressure/queue bound.
