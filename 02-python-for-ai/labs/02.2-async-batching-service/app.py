"""Lab 02.2 — Async FastAPI service with hand-rolled dynamic batching.

Demonstrates the core serving pattern: async handlers enqueue (request, future)
pairs; a single background loop drains the queue into batches (up to MAX_BATCH
items, waiting at most MAX_DELAY_MS), runs ONE forward pass, and resolves the
futures. The "model" is a fixed matmul so behavior is deterministic and runs on
any hardware.

Env vars:
  BATCH_ENABLED (default 1)  -> set 0 to serve per-request (for comparison)
  MAX_BATCH      (default 32)
  MAX_DELAY_MS   (default 5)
  MAX_QUEUE      (default 1000)
"""
from __future__ import annotations

import asyncio
import os
import time
from contextlib import asynccontextmanager

import torch
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from pydantic import BaseModel, Field

BATCH_ENABLED = os.getenv("BATCH_ENABLED", "1") == "1"
MAX_BATCH = int(os.getenv("MAX_BATCH", "32"))
MAX_DELAY_MS = float(os.getenv("MAX_DELAY_MS", "5"))
MAX_QUEUE = int(os.getenv("MAX_QUEUE", "1000"))
DIM = 128

REQUESTS = Counter("inference_requests_total", "Total requests")
REJECTED = Counter("inference_rejected_total", "Requests rejected (queue full)")
INFLIGHT = Gauge("inference_inflight", "In-flight requests")
BATCH_SIZE = Histogram(
    "inference_batch_size", "Observed batch sizes",
    buckets=(1, 2, 4, 8, 16, 32, 64),
)
LATENCY = Histogram("inference_latency_seconds", "End-to-end latency (s)")

state: dict = {}


def embed(batch: torch.Tensor) -> torch.Tensor:
    """A stand-in 'model': a fixed linear projection. One call = one batch."""
    return torch.tanh(batch @ state["W"])


def text_to_tensor(text: str) -> torch.Tensor:
    """Deterministic pseudo-encoding of text into a DIM-vector input."""
    h = abs(hash(text)) % (2**31)
    g = torch.Generator().manual_seed(h)
    return torch.randn(DIM, generator=g)


async def batch_loop() -> None:
    """Drain the queue into batches and run one forward pass per batch."""
    queue: asyncio.Queue = state["queue"]
    while True:
        req = await queue.get()  # block until at least one request
        batch_items = [req]
        deadline = time.perf_counter() + MAX_DELAY_MS / 1000.0
        # Accumulate more items until batch full or delay window elapses.
        while len(batch_items) < MAX_BATCH:
            timeout = deadline - time.perf_counter()
            if timeout <= 0:
                break
            try:
                batch_items.append(await asyncio.wait_for(queue.get(), timeout))
            except asyncio.TimeoutError:
                break

        BATCH_SIZE.observe(len(batch_items))
        inputs = torch.stack([item[0] for item in batch_items])
        # Model compute is offloaded off the event loop via a thread.
        outputs = await asyncio.to_thread(embed, inputs)
        for (_, fut), vec in zip(batch_items, outputs):
            if not fut.done():
                fut.set_result(vec)


@asynccontextmanager
async def lifespan(app: FastAPI):
    torch.manual_seed(0)
    state["W"] = torch.randn(DIM, DIM)
    state["queue"] = asyncio.Queue(maxsize=MAX_QUEUE)
    state["ready"] = True
    task = asyncio.create_task(batch_loop()) if BATCH_ENABLED else None
    yield
    state["ready"] = False
    if task:
        task.cancel()


app = FastAPI(title="Async Batching Service", version="0.1.0", lifespan=lifespan)


class EmbedRequest(BaseModel):
    text: str = Field(min_length=1, max_length=8192)


@app.get("/readyz")
def readyz() -> dict:
    return {"ready": bool(state.get("ready"))}


@app.get("/metrics")
def metrics() -> PlainTextResponse:
    return PlainTextResponse(generate_latest())


@app.post("/embed")
async def embed_endpoint(req: EmbedRequest) -> dict:
    REQUESTS.inc()
    INFLIGHT.inc()
    start = time.perf_counter()
    try:
        x = text_to_tensor(req.text)
        if BATCH_ENABLED:
            fut: asyncio.Future = asyncio.get_running_loop().create_future()
            try:
                state["queue"].put_nowait((x, fut))
            except asyncio.QueueFull:
                REJECTED.inc()
                raise HTTPException(status_code=503, detail="overloaded")
            vec = await fut
            batch = 0  # actual batch size is in the metrics histogram
        else:
            # Per-request path: run a batch of size 1 inline (for comparison).
            vec = await asyncio.to_thread(embed, x.unsqueeze(0))
            vec = vec.squeeze(0)
            BATCH_SIZE.observe(1)
            batch = 1
        LATENCY.observe(time.perf_counter() - start)
        return {"dim": int(vec.shape[0]), "batch_size": batch,
                "norm": round(float(vec.norm()), 4)}
    finally:
        INFLIGHT.dec()
