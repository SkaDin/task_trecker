from datetime import datetime

from pydantic import BaseModel

from src.core.enum import Priority, Status


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: Status
    priority: Priority
    due_date: datetime
    author_id: int
    assignee_id: int

    class Config:
        from_attributes = True
