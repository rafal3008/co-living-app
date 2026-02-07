from fastapi import FastAPI, Response, status
from app.api.v1.api import api_router
from app.core.config import settings
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager



engine = create_async_engine(settings.DATABASE_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    await engine.dispose()
    print("Shutting down...")

app = FastAPI(
    title = settings.PROJECT_NAME,
    version = settings.PROJECT_VERSION,
    lifespan = lifespan,
)
app.include_router(api_router, prefix=settings.API_V1_STR)
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check(response: Response):
    #TODO add wellness check for other stuff along the way (like db etc.)
    try:
        # Actually try to talk to the database
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected",
            "app": settings.PROJECT_NAME
            }

    except Exception as e:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {
            "status": "error",
            "database": "disconnected",
            "error": str(e)
        }








