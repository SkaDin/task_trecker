from sqlalchemy import Enum, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, create_at, due_date
from src.core.enum import Priority, Status


class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())
    create_at: Mapped[create_at]
    due_date: Mapped[due_date]
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.NEW)
    priority: Mapped[Priority] = mapped_column(Enum(Priority), default=Priority.MEDIUM)

    assignee_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    assignee: Mapped["User"] = relationship("User", back_populates="assigned_task", foreign_keys=[assignee_id])

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    author: Mapped["User"] = relationship("User", back_populates="created_tasks", foreign_keys=[author_id])

    tags: Mapped[str] = mapped_column(String(255), nullable=True)

    __table_args__ = (Index("idx_task_title", title),)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status}, priority={self.priority})>"
