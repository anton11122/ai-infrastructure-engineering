# AI Foundations — Troubleshooting

Symptom → likely root cause → fix. Foundational issues you'll hit in the labs and beyond.

| Symptom | Likely root cause | Fix |
|---------|-------------------|-----|
| First request after restart is very slow, then fast | Model loaded lazily on first request | Load at startup (lifespan); gate with `readyz` |
| Container start is slow / flaky | Weights downloaded at runtime | Bake weights into image or mount a cache volume |
| `torch.cuda.is_available()` is `False` on a GPU box | CPU-only torch wheel, or driver/CUDA mismatch | Install CUDA-matching torch; verify `nvidia-smi` |
| `CUDA out of memory` | Model + activations + KV cache exceed VRAM | Smaller model, quantize, reduce batch/context, or shard (Module 28) |
| High p95/p99 under load, CPU pinned | Single-process, CPU-bound, no batching | Add replicas / workers; move to a serving engine (Module 24) |
| Throughput plateaus as concurrency rises | Serialized model calls, no batching | Batch requests; scale replicas |
| Model returns 200 but answers got worse | Data/embedding drift or a bad model/prompt version | Add quality evals to monitoring (Modules 17, 29); roll back the version |
| Non-reproducible outputs across runs | Sampling / unpinned model or revision | Pin model + revision; set decoding params; expect some non-determinism |
| `OSError: can't load model` | No network / registry blocked | Pre-download; set `HF_HOME` cache; use an internal mirror |
| Loading a `.bin`/pickle triggers weird behavior | Executable pickle format | Use `safetensors`; never load untrusted pickles |

## General method
1. **Reproduce with a single request** to get a clean baseline before load testing.
2. **Check `readyz`/`healthz`** — distinguish "not started" from "slow".
3. **Watch resources:** `nvidia-smi -l 1` for GPU, `top`/metrics for CPU/mem.
4. **Isolate:** is it the model (inference time), the server (concurrency), or the environment (driver/deps)?
5. **Consult `/metrics`** for in-flight count and latency histogram to localize the bottleneck.
