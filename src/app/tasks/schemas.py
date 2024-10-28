from datetime import datetime, timezone

from pydantic import BaseModel, Field, PrivateAttr

from src.core.enum import Priority, Status


class TaskCreate(BaseModel):
    title: str = Field(..., max_length=10)
    description: str
    _create_at: datetime = PrivateAttr(default_factory=lambda: datetime.now(timezone.utc))
    due_date: datetime
    status: Status
    priority: Priority
    assignee_id: int = Field(..., ge=1)
    tags: str

    class Config:
        from_attributes = True

    def json_encoder(self):
        return {
            "title": self.title,
            "description": self.description,
            "_create_at": self._create_at.isoformat(),
            "due_date": self.due_date.isoformat(),
            "status": self.status,
            "priority": self.priority,
            "assignee_id": self.assignee_id,
            "tags": self.tags,
        }


class TaskCreateResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True


class TaskResponse(TaskCreate):
    id: int
    create_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }
