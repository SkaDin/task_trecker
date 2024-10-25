from typing import Annotated

from fastapi import Depends, HTTPException

from src.app.tasks.dependencies import task_service
from src.app.tasks.schemas import TaskCreate
from src.app.tasks.services import TaskService


async def check_duplicate_title(
    data: TaskCreate,
    task_services: Annotated[TaskService, Depends(task_service)],
) -> None:
    if await task_services.get_task_filter_by(data.title):
        raise HTTPException(status_code=409, detail=f"Task this title <{data.title}> already exists")
