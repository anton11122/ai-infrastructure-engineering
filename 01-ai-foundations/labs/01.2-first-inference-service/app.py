"""Lab 01.2 — A minimal, production-shaped inference microservice.

Wraps a small pretrained sentiment classifier in FastAPI with health checks
and Prometheus metrics. This is the smallest realistic version of an inference
service and intentionally omits batching, GPUs, auth, and quality evals so you
can see exactly what later modules add.
"""
from __future__ import annotations

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from pydantic import BaseModel
from transformers import pipeline

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# --- Metrics (mirrors the observability instincts you already have) ---------
REQUESTS = Counter("inference_requests_total", "Total prediction requests", ["label"])
INFLIGHT = Gauge("inference_inflight", "In-flight prediction requests")
LATENCY = Histogram(
    "inference_latency_seconds",
    "Prediction latency in seconds",
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5),
)

_model = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Warm the model at startup so the first user request isn't a cold download.
    _model["clf"] = pipeline("sentiment-analysis", model=MODEL_NAME)
    yield
    _model.clear()


app = FastAPI(title="First Inference Service", version="0.1.0", lifespan=lifespan)


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    label: str
    score: float
    latency_ms: float
    model: str


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "model_loaded": "clf" in _model}


@app.get("/metrics")
def metrics() -> PlainTextResponse:
    return PlainTextResponse(generate_latest())


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest) -> PredictResponse:
    INFLIGHT.inc()
    start = time.perf_counter()
    try:
        with LATENCY.time():
            result = _model["clf"](req.text)[0]
        latency_ms = (time.perf_counter() - start) * 1000
        REQUESTS.labels(label=result["label"]).inc()
        return PredictResponse(
            label=result["label"],
            score=round(float(result["score"]), 4),
            latency_ms=round(latency_ms, 1),
            model=MODEL_NAME,
        )
    finally:
        INFLIGHT.dec()
