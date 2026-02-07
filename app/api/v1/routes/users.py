from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from app.schemas.user import UserCreate, UserRead
from app.services import user as user_service
from app.api.db_helper import get_db
router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(
        user_in: UserCreate,
        db: AsyncSession = Depends(get_db)
) -> Any:
    user = await user_service.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = await user_service.create_user(db, user=user_in)
    return user