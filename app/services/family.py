from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.family import Family
from app.schemas.family import FamilyCreate
from app.models.user import User


async def create_family(db: AsyncSession, family: FamilyCreate, current_user: User) -> Family:
    db_family = Family(name=family.name)
    db.add(db_family)
    await db.commit()
    await db.refresh(db_family)

    return db_family




async def get_family_by_id(db: AsyncSession, family_id: int) -> Family | None:
    result = await db.execute(select(Family).where(Family.id == family_id))
    return result.scalar_one_or_none()


async def get_all_families(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Family).offset(skip).limit(limit))
    return result.scalars().all()