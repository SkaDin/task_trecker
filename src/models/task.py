from datetime import datetime

from sqlalchemy import TIMESTAMP, Enum, ForeignKey, Index, Integer, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base
from src.core.enum import Priority, Status


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256), unique=True)
    description: Mapped[str] = mapped_column(Text())
    create_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=text("TIMEZONE('utc', now())")
    )
    due_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text("TIMEZONE('utc', now())"))
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.NEW)
    priority: Mapped[Priority] = mapped_column(Enum(Priority), default=Priority.MEDIUM)

    assignee_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    assignee: Mapped["User"] = relationship("User", back_populates="assigned_task", foreign_keys=[assignee_id])  # noqa

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    author: Mapped["User"] = relationship("User", back_populates="created_tasks", foreign_keys=[author_id])  # noqa

    tags: Mapped[str] = mapped_column(String(255), nullable=True)

    __table_args__ = (Index("idx_task_title", title),)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status}, priority={self.priority})>"
