from datetime import datetime
from typing import Annotated, AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column

from src.core.config import config

create_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

update_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.now())]

due_date = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now()"))]

int_pk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    pass


engine = create_async_engine(config.DB_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as async_session:
        yield async_session
