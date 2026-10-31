from fastapi.testclient import TestClient
from examples.api.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_demo_run():
    response = client.post("/run-demo", json={"goal": "Research API design"})
    assert response.status_code == 200
    assert response.json()["simulated"] is True
    assert response.json()["steps_used"] == 1

def test_empty_goal_rejected():
    assert client.post("/run-demo", json={"goal": ""}).status_code == 422
