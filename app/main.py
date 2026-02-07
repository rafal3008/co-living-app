from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
app = FastAPI(
    title = settings.PROJECT_NAME,
    version = settings.PROJECT_VERSION,
)

app.include_router(api_router, prefix=settings.API_V1_STR)
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    #TODO add wellness check for other stuff along the way (like db etc.)
    return {
        "Project Name": settings.PROJECT_NAME,
        "status": "ok"}






