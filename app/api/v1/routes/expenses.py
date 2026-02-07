from fastapi import APIRouter

router = APIRouter()

@router.get("/expenses")
def get_expenses():
    return [{"id": 1, "amount": 10.0, "description": "expenses"}]
