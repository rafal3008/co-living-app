from pydantic import BaseModel, ConfigDict


class FamilyBase(BaseModel):
    name: str


class FamilyCreate(FamilyBase):
    pass


class FamilyRead(FamilyBase):
    id: int

    model_config = ConfigDict(from_attributes=True)