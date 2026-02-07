from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from app.models.user import User
from app.models.family import Family
from app.models.expenses import Expense