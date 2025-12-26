from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="AI Resume Analyzer")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Resume Analyzer API is running"}

