"""Lab 02.3 — tests prove the module is importable and deterministic."""
from fastapi.testclient import TestClient

from service.app import app, score

client = TestClient(app)


def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_score_is_deterministic():
    values = [float(i) for i in range(16)]
    a = score(values)
    b = score(values)
    assert a == b  # fixed weights -> deterministic


def test_score_endpoint_validates_length():
    r = client.post("/score", json={"values": [1.0, 2.0]})  # too short
    assert r.status_code == 422


def test_score_endpoint_ok():
    r = client.post("/score", json={"values": [float(i) for i in range(16)]})
    assert r.status_code == 200
    assert "score" in r.json()
