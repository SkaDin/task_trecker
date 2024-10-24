from src.app.tasks.schemas import TaskCreate
from src.utils.SQLAlchemyRepository.repository import IRepository


class TaskService:
    def __init__(self, repository: IRepository):
        self.repository: IRepository = repository

    async def add_task(self, task: TaskCreate, author_id: int):
        task_dict = task.model_dump()
        return await self.repository.add_one(task_dict, author_id)

    async def get_all_tasks(self):
        return await self.repository.get_all()

    async def get_one_task(self, task_id: int):
        return await self.repository.get_one(task_id)

    async def get_task_filter_by(self, title: str):
        return await self.repository.get_by_title(title)
