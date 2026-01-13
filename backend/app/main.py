from fastapi import FastAPI
from .db import engine
from .routers import interests

app = FastAPI(title="Pertube API")

app.include_router(interests.router)

@app.get("/")
def root():
    return {"status": "ok"}
