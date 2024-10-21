from src.app.SQLAlchemyRepository.repository import SQLAlchemyRepository
from src.models import Task


class TaskRepository(SQLAlchemyRepository):
    model = Task
