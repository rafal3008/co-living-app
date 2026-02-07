from datetime import datetime
from sqlalchemy import String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100))
    amount: Mapped[float] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    family_id: Mapped[int] = mapped_column(ForeignKey("families.id"))

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="expenses")
    family: Mapped["Family"] = relationship("Family", back_populates="expenses")