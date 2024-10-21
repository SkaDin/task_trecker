from fastapi import APIRouter
from fastapi.params import Depends

from src.app.tasks.schemas import TaskResponse
from src.auth.manager import current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get(
    "/",
    dependencies=[Depends(current_user)],
)
async def get_task() -> list[TaskResponse]:
    return []
