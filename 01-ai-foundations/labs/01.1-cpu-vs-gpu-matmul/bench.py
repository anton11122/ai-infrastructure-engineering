"""Lab 01.1 — Benchmark matrix multiply (inference vs training) on CPU vs GPU.

Neural-network compute is dominated by matrix multiplication. This script
measures the two canonical workloads:

  * forward-only  (A @ B)                -> the shape of INFERENCE
  * forward+backward (with autograd)      -> the shape of a TRAINING step

It runs on CPU always, and on CUDA GPU if available, printing latency and
achieved GFLOP/s so you can *feel* the differences discussed in Module 01.
"""
from __future__ import annotations

import argparse
import time

import torch


def time_matmul(device: str, n: int, iters: int, train: bool) -> tuple[float, float]:
    """Return (avg_ms, gflops) for an n x n matmul on `device`.

    A single matmul of two (n, n) matrices costs ~2 * n**3 FLOPs. A training
    step (forward + backward) does roughly 3x that work, which we account for
    when computing achieved GFLOP/s.
    """
    a = torch.randn(n, n, device=device, requires_grad=train)
    b = torch.randn(n, n, device=device, requires_grad=train)

    # Warm-up (kernel compilation / caching / lazy init are not part of timing).
    for _ in range(3):
        c = a @ b
        if train:
            c.sum().backward()
            a.grad = None
            b.grad = None
    if device == "cuda":
        torch.cuda.synchronize()

    start = time.perf_counter()
    for _ in range(iters):
        c = a @ b
        if train:
            c.sum().backward()
            a.grad = None
            b.grad = None
    if device == "cuda":
        torch.cuda.synchronize()
    elapsed = time.perf_counter() - start

    avg_s = elapsed / iters
    flops = 2.0 * (n ** 3) * (3.0 if train else 1.0)
    gflops = flops / avg_s / 1e9
    return avg_s * 1e3, gflops


def main() -> None:
    parser = argparse.ArgumentParser(description="CPU vs GPU matmul benchmark")
    parser.add_argument("--sizes", type=int, nargs="+", default=[512, 1024, 2048])
    parser.add_argument("--iters", type=int, default=20)
    args = parser.parse_args()

    devices = ["cpu"]
    if torch.cuda.is_available():
        devices.append("cuda")
        print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA not available — running CPU-only (this is fine for the lab).")

    print(f"\n{'device':6}  {'op':18} {'N':>5}  {'avg_ms':>8}  {'GFLOP/s':>9}")
    print("-" * 56)
    for device in devices:
        for n in args.sizes:
            for train, label in [(False, "forward"), (True, "forward+backward")]:
                try:
                    avg_ms, gflops = time_matmul(device, n, args.iters, train)
                    print(f"{device:6}  {label:18} {n:>5}  {avg_ms:>8.2f}  {gflops:>9.0f}")
                except RuntimeError as exc:  # e.g. CUDA OOM
                    print(f"{device:6}  {label:18} {n:>5}  ERROR: {exc}")


if __name__ == "__main__":
    main()
