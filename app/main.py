import os
import platform
import socket
from fastapi import FastAPI

app = FastAPI(title="Kubernetes DevOps Project API")

APP_NAME = os.getenv("APP_NAME", "Kubernetes DevOps Project")
APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.get("/")
def root():
    return {
        "application": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "version": APP_VERSION,
    }


@app.get("/metrics")
def metrics():
    return {
        "app_up": 1,
        "app_version": APP_VERSION,
        "environment": APP_ENV,
    }
