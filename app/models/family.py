from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


#Relations tab

user_family_table = Table(
    "user_family",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("family_id", ForeignKey("families.id"), primary_key=True),
)


class Family(Base):
    __tablename__ = "families"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))

    # Relationships

    users: Mapped[list["User"]] = relationship(
        "User",
        secondary= "user_family",
        back_populates="families"
    )

    expenses: Mapped[list["Expense"]] = relationship(
        "Expense",
        back_populates="family",
        cascade="all, delete-orphan" #delete
    )