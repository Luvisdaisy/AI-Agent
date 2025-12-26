from fastapi import FastAPI

app = FastAPI(title="AI Agent Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}