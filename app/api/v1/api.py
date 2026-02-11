from fastapi import APIRouter
from app.api.v1.routes import (
    expenses, users, login, families)

api_router = APIRouter()

api_router.include_router(login.router, tags=["Login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
api_router.include_router(families.router, prefix="/families", tags=["Families"])