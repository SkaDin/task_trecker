from typing import Any, Protocol

from sqlalchemy import Result, insert, select

from src.core.db import AsyncSessionLocal


class AbstractRepository(Protocol):
    async def get_one(self, task_id: int):
        ...

    async def add_one(self, data: dict) -> int:
        ...

    async def get_all(self) -> Result[tuple[Any]]:
        ...


class SQLAlchemyRepository(AbstractRepository):
    model = None

    # def __init__(self, session: AsyncSession):
    #     self.session = session

    async def add_one(self, data: dict) -> int:
        async with AsyncSessionLocal() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
        return res.scalar_one()

    async def get_one(self, task_id: int):
        async with AsyncSessionLocal() as session:
            stmt = select(self.model).where(self.model.id == task_id)
            res = await session.execute(stmt)
        return res.scalar_one()

    async def get_all(self) -> Result[tuple[Any]]:
        async with AsyncSessionLocal() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
        return res.scalars().all()
