from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_async_session
from src.models import Task

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("/")
async def get_task(session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = select(Task)
    res = await session.execute(stmt)
    print(stmt)
    print(res)
