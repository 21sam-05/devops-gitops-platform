from fastapi.testclient import TestClient
from services.notification_service.app.main import app

client=TestClient(app)

def test_health():
    response=client.get("/health")

    assert response.status_code==200
    data=response.json()

    assert data["status"]=="healthy"
    assert data["service"]=="notification-service"

def test_send_notification():
    payload={
        "message":"Test notification",
        "recipient":"sam"
    }

    response=client.post("/notify",json=payload)

    assert response.status_code==200

    data=response.json()

    assert data["status"]=="sent"
    assert data["recipient"]=="sam"
    assert data["message"]=="Test notification"