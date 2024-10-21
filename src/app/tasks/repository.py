from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.tasks.irepository import AbstractRepository
from src.core.db import get_async_session
from src.models import Task


class TaskRepository(AbstractRepository):
    model = Task


class SQLAlchemyRepository(AbstractRepository):
    model = None
    session = Annotated[AsyncSession, Depends(get_async_session)]

    async def add_one(self):
        ...

    async def get_one(self):
        async with self.session() as session:
            stmt = select(Task)
            res = await session.execute(stmt)
        return res.scalars()

    async def update_one(self):
        ...

    async def delete_one(self):
        ...

    async def get_all(self):
        ...
