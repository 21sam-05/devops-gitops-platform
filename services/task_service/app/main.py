import os

import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task Service")

#loook for an environment variable called notification_service_url, if it doesn't exist,use the default value
NOTIFICATION_SERVICE_URL = os.getenv(
    "NOTIFICATION_SERVICE_URL",
    "http://notification-service:8001"
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "task-service"
    }


@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Learn Docker", "completed": True},
        {"id": 2, "title": "Learn Kubernetes", "completed": False},
        {"id": 3, "title": "Build GitOps pipeline", "completed": False},
    ]


@app.post("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    notification = {
        "message": f"Task {task_id} has been completed!",
        "recipient": "sam"
    }

    try:
        response = httpx.post(
            f"{NOTIFICATION_SERVICE_URL}/notify",
            json=notification,
            timeout=5.0
        )

        response.raise_for_status()

    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Notification service unavailable: {exc}"
        )

    return {
        "task_id": task_id,
        "status": "completed",
        "notification": response.json()
    }