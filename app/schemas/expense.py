from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ExpenseBase(BaseModel):
    title: str
    amount: float = Field(gt=0, description="Amount must be positive")

class ExpenseCreate(ExpenseBase):
    family_id: int 

class ExpenseRead(ExpenseBase):
    id: int
    user_id: int
    family_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)