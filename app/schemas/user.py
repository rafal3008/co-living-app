from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    is_superuser: bool

    model_config = ConfigDict(from_attributes=True)