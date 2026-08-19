from fastapi.testclient import TestClient

from services.task_service.app.main import app



client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "task-service"


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3
    assert data[0]["title"] == "Learn Docker"