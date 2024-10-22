from datetime import date

from pydantic import BaseModel, Field

from src.core.enum import Priority, Status


class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: date
    status: Status
    priority: Priority
    assignee_id: int = Field(..., ge=1)
    author_id: int = Field(..., ge=1)
    tags: str

    class Config:
        from_attributes = True


class TaskCreateResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True


class TaskResponse(TaskCreate):
    class Config:
        from_attributes = True
