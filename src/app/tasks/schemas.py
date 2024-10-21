from datetime import datetime, timezone

from pydantic import BaseModel

from src.core.enum import Status, Priority


class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: datetime
    status: Status
    priority: Priority
    assignee_id: int
    author_id: int
    tags: str

    class Config:
        from_attributes = True


class TaskCreateResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True
