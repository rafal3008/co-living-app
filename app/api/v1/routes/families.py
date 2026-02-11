from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.db_helper import get_db, get_current_user
from app.schemas.family import FamilyCreate, FamilyRead
from app.models.user import User
from app.services import family

router = APIRouter()

@router.get("/", response_model=List[FamilyRead])
async def read_families(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
) -> Any:
    return await family.get_all_families(db, skip=skip, limit=limit)

@router.post("/", response_model=FamilyRead)
async def create_family(
    family_in: FamilyCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:

    return await family.create_family(db, family=family_in, current_user=current_user)