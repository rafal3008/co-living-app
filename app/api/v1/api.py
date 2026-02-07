from fastapi import APIRouter
from app.api.v1.routes import expenses, users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(expenses.router, prefix="/users", tags=["expenses"])