from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Kubernetes DevOps Project is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "v1"}
