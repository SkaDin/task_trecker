from datetime import datetime, timezone

from pydantic import BaseModel, Field, PrivateAttr, field_validator

from src.core.enum import Priority, Status


class TaskCreate(BaseModel):
    title: str
    description: str
    _create_at: datetime = PrivateAttr(default_factory=lambda: datetime.now(timezone.utc))
    due_date: datetime
    status: Status
    priority: Priority
    assignee_id: int = Field(..., ge=1)
    tags: str

    class Config:
        from_attributes = True

    @field_validator("due_date")
    def check_due_date(cls, value):
        if value < datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future")
        return value


class TaskCreateResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True


class TaskResponse(TaskCreate):
    id: int
    create_at: datetime | str

    class Config:
        from_attributes = True

    @field_validator("create_at")
    def convert_create_at(cls, value: datetime):
        return value.replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
