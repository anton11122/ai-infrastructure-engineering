"""Lab 02.1 — Demonstrate the three performance rules of AI Python.

1. Vectorize instead of looping (NumPy).
2. Match device/dtype (fp16 on GPU uses Tensor Cores).
3. Avoid per-step CPU<->GPU copies (bulk transfer once).

Prints a comparison table with measured speedups so you trust the rules
because you measured them, not because a book said so.
"""
from __future__ import annotations

import argparse
import time

import numpy as np
import torch


def timeit(fn, iters: int) -> float:
    """Return average milliseconds per call over `iters`, after a warm-up."""
    for _ in range(3):  # warm-up (caches, lazy init)
        fn()
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return (time.perf_counter() - start) / iters * 1000.0


def compare_vectorize(n: int, iters: int) -> tuple[float, float]:
    a = np.random.rand(n).astype(np.float32)

    def loop():
        total = 0.0
        for v in a:  # the interpreter tax, per element
            total += v * 2.0
        return total

    def vectorized():
        return float((a * 2.0).sum())

    return timeit(loop, max(1, iters // 20)), timeit(vectorized, iters)


def compare_item_copies(n: int, iters: int) -> tuple[float, float]:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    t = torch.arange(n, dtype=torch.float32, device=device)

    def per_step():  # BAD: forces a device->host copy every element
        total = 0.0
        for i in range(0, n, max(1, n // 1000)):
            total += t[i].item()
        return total

    def bulk():  # GOOD: reduce on device, one copy at the end
        return float(t.sum().item())

    return timeit(per_step, max(1, iters // 20)), timeit(bulk, iters)


def compare_dtype(iters: int) -> tuple[float, float] | None:
    if not torch.cuda.is_available():
        return None  # fp16 matmul is CPU-unsupported/slow; only meaningful on GPU
    a32 = torch.randn(2048, 2048, device="cuda", dtype=torch.float32)
    a16 = a32.half()

    def mm32():
        return a32 @ a32

    def mm16():
        return a16 @ a16

    return timeit(mm32, iters), timeit(mm16, iters)


def row(name: str, slow_ms: float, fast_ms: float) -> str:
    speedup = slow_ms / fast_ms if fast_ms else float("inf")
    return f"{name:34} {slow_ms:8.2f} {fast_ms:8.2f} {speedup:8.1f}x"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1_000_000)
    parser.add_argument("--iters", type=int, default=50)
    args = parser.parse_args()

    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"\n{'comparison':34} {'slow_ms':>8} {'fast_ms':>8} {'speedup':>8}")
    print("-" * 62)

    slow, fast = compare_vectorize(args.n, args.iters)
    print(row("vectorize (loop vs numpy)", slow, fast))

    slow, fast = compare_item_copies(args.n, args.iters)
    print(row("per-step .item() vs bulk copy", slow, fast))

    dtype_res = compare_dtype(args.iters)
    if dtype_res:
        slow, fast = dtype_res
        print(row("fp32 vs fp16 matmul (cuda)", slow, fast))
    else:
        print("fp32 vs fp16 matmul: skipped (no CUDA)")


if __name__ == "__main__":
    main()
