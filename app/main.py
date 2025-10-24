from fastapi import FastAPI
from .api.routes import router as api_router

app = FastAPI(title="Course API", version="0.1.0")

@app.get("/", tags=["root"])
def read_root():
    return {"status": "ok", "service": "course-api", "version": "0.1.0"}

app.include_router(api_router, prefix="/api")
