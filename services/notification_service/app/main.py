from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="Notification Service")

class Notification(BaseModel):
    message:str
    recipient: str

@app.get("/health")
def health():
    return{
        "status":"healthy",
        "service":"notification-service"
    }

@app.post("/notify")
def send_notification(notification:Notification):
    return{
        "status":"sent",
        "recipient":notification.recipient,
        "message":notification.message
    }