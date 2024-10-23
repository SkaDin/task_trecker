from datetime import date, datetime

from pydantic import BaseModel, Field, PrivateAttr, field_validator

from src.core.enum import Priority, Status


class TaskCreate(BaseModel):
    title: str
    description: str
    _create_at: datetime = PrivateAttr(default_factory=datetime.now)
    due_date: date
    status: Status
    priority: Priority
    assignee_id: int = Field(..., ge=1)
    tags: str

    class Config:
        from_attributes = True

    @field_validator("due_date")
    def check_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date must be in the future")
        return value


class TaskCreateResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True


class TaskResponse(TaskCreate):
    id: int
    create_at: datetime

    class Config:
        from_attributes = True

    @field_validator("create_at")
    def convert_create_at(cls, value: datetime):
        return datetime.fromisoformat(value.strftime("%Y-%m-%d %H:%M:%S"))
