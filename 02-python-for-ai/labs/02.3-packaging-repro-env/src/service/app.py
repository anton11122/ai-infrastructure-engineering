"""A minimal, importable, testable inference service.

Kept deliberately dependency-light (NumPy stand-in 'model') so the lab focuses
on packaging + reproducibility rather than model weight downloads.
"""
from __future__ import annotations

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

from . import __version__

app = FastAPI(title="repro-svc", version=__version__)

# Fixed "model" weights (deterministic) — a stand-in for a real model.
_RNG = np.random.default_rng(0)
_W = _RNG.standard_normal((16, 16)).astype(np.float32)


class ScoreRequest(BaseModel):
    values: list[float] = Field(min_length=16, max_length=16)


def score(values: list[float]) -> float:
    """Pure function so it is trivially unit-testable (see tests/)."""
    x = np.asarray(values, dtype=np.float32)
    return float(np.tanh(x @ _W).sum())


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "version": __version__}


@app.post("/score")
def score_endpoint(req: ScoreRequest) -> dict:
    return {"score": round(score(req.values), 6), "version": __version__}
