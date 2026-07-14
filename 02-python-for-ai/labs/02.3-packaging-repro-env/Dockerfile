# Lab 02.3 — multi-stage, lockfile-first, slim image.
# Layer ordering: copy lockfiles + install BEFORE copying source so dependency
# layers cache across code-only changes.

# ---- builder ----
FROM python:3.11-slim AS builder
RUN pip install --no-cache-dir uv
WORKDIR /app
# Only the dependency manifests here -> this layer is cached unless deps change.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# ---- runtime ----
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src"
# Source copied last: changing it does NOT invalidate the dependency layer.
COPY src/ ./src/

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/healthz').status==200 else 1)"

CMD ["uvicorn", "service.app:app", "--host", "0.0.0.0", "--port", "8000"]
