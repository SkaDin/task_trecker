from src.app.tasks.repository import TaskRepository
from src.app.tasks.services import TaskService


def task_service():
    return TaskService(TaskRepository())
