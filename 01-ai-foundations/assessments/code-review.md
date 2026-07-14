# Code Review Exercise  `A`

Review this inference service snippet. List every issue you can find with **impact** and **fix**. Planted issues are hidden below — attempt first.

```python
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

@app.post("/predict")
def predict(text: str):
    clf = pipeline("sentiment-analysis")   # (a)
    result = clf(text)                       # (b)
    return result

@app.get("/health")
def health():
    return "ok"                              # (c)

# no metrics, no readiness, no input limits, no error handling  # (d)
```

---

## Model answer (planted issues)

| # | Issue | Impact | Fix |
|---|-------|--------|-----|
| a | **Model loaded inside the request handler** | Every request re-loads (or re-downloads) the model → huge latency + memory churn | Load once at startup (lifespan/global); reuse across requests |
| a2 | **No pinned model name** | `pipeline("sentiment-analysis")` pulls a default that can change → non-reproducible | Pin an explicit model + revision |
| b | **No input validation / size limit** | Unbounded text → memory blowup, DoS vector | Use a Pydantic model with `max_length`; reject empty |
| b2 | **Untrusted input passed straight to model** | Foreshadows prompt-injection class (Module 30) | Validate/sanitize; document trust boundary |
| c | **Health check is trivial and always returns ok** | Returns "healthy" even if the model failed to load → bad traffic routing | Add `/readyz` that checks model is loaded; `/healthz` for liveness |
| d | **No metrics** | No visibility into latency/throughput/errors | Add Prometheus counters + latency histogram |
| d2 | **No error handling** | Model exceptions → 500s with stack traces leaked | try/except → clean error response + logging |
| d3 | **No concurrency/throughput consideration** | Single blocking model call, no batching | Note batching/replicas as the scaling path (Modules 19, 24) |
| e | **Returns raw model output** | Leaks internal structure; unstable contract | Define a typed response schema |

**Strong candidates also note:** no logging, no auth/rate limiting (gateway concern), model not baked into image (cold start), and no timeout on inference.
