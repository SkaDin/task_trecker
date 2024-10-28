from typing import Annotated

from fastapi import APIRouter, Depends

from src.app.tasks.dependencies import task_service
from src.app.tasks.schemas import TaskCreate, TaskCreateResponse, TaskResponse
from src.app.tasks.services import TaskService
from src.app.tasks.validators import check_duplicate_title
from src.auth.manager import current_user
from src.core.config import config
from src.infrastructure.kafka.depends_kafka import kafka_producer_dependency
from src.infrastructure.kafka.kafka_produser import KafkaProducer
from src.models import User

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get(
    "/",
    response_model=list[TaskResponse],
    dependencies=[Depends(current_user)],
)
async def get_all_tasks(
    task_services: Annotated[TaskService, Depends(task_service)],
):
    return await task_services.get_all_tasks()


@router.post(
    "/create",
    dependencies=[Depends(current_user)],
)
async def create_task(
    task: TaskCreate,
    task_services: Annotated[TaskService, Depends(task_service)],
    kafka_producer: Annotated[KafkaProducer, Depends(kafka_producer_dependency)],
    user: User = Depends(current_user),
) -> TaskCreateResponse:
    await check_duplicate_title(task, task_services)
    task_id = await task_services.add_task(task, user.id)
    await kafka_producer.send_message(config.CLIENT_ID, task.json_encoder(), key=bytes(user.id))
    return TaskCreateResponse(id=task_id)


@router.get("/{task_id}", response_model=TaskResponse)
async def get_one_task(
    task_id: int,
    task_services: Annotated[TaskService, Depends(task_service)],
) -> TaskResponse:
    result = await task_services.get_one_task(task_id)
    return result
