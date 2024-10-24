from src.models import Task
from src.utils.SQLAlchemyRepository.repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = Task
