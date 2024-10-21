from fastapi import APIRouter

from src.app.tasks.repository import TaskRepository
from src.app.tasks.schemas import TaskCreate, TaskCreateResponse

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


# @router.get("/")
# async def get_tasks():
#     return {"message": "OK"}


@router.post("/create", response_model=TaskCreateResponse)
async def create_task(task: TaskCreate) -> TaskCreateResponse:
    task_dict = task.model_dump()
    task_id = await TaskRepository().add_one(task_dict)
    return {"task_id": task_id}
