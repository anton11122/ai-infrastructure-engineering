# Lab 01.2 — containerize the inference service (reuses your Docker skills).
FROM python:3.11-slim

WORKDIR /app

# System deps kept minimal; torch CPU wheel needs no CUDA here.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the model at build time so containers don't fetch it at runtime
# (a real cold-start concern — see the lab's Production Discussion).
ENV HF_HOME=/app/.hf
RUN python -c "from transformers import pipeline; \
    pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

COPY app.py .

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/healthz').status==200 else 1)"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
