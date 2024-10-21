from typing import Protocol

from sqlalchemy import insert
from src.core.db import AsyncSessionLocal


class AbstractRepository(Protocol):

    async def get_one(self):
        ...

    async def add_one(self, data: dict) -> int:
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


