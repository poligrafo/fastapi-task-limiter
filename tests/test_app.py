from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_test_endpoint():
    response = client.get("/test")
    assert response.status_code == 200
    data = response.json()
    assert "elapsed" in data
    assert data["elapsed"] >= 3
