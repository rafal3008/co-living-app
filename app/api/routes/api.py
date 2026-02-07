from fastapi import APIRouter
from app.api.routes import users, expenses

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(expenses.router, prefix="/users", tags=["expenses"])