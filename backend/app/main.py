from fastapi import FastAPI
from .db import engine

app = FastAPI(title="Pertube API")

@app.get("/")
def root():
    try:
        with engine.connect() as conn:
            return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
