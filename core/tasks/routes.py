from fastapi import APIRouter

router = APIRouter(tags=["tasks"])

@router.get("/tasks")
async def read_users():
    return []


