from sqlalchemy import Enum, ForeignKey, Index, Integer, String, Table, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, create_at, due_date, int_pk
from src.core.enum import Priority, Status

task_dependencies = Table(
    "task_dependencies",
    Base.metadata,
    mapped_column("task_id", ForeignKey("task.id"), primary_key=True),
    mapped_column("dependency_id", ForeignKey("task.id"), primary_key=True),
)


class Task(Base):
    __tablename__ = "task"
    id: Mapped[int_pk]
    title: Mapped[String] = mapped_column(String(256))
    description: Mapped[Text] = mapped_column(Text())
    create_at: Mapped[create_at]
    due_date: Mapped[due_date]
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.NEW)
    priority: Mapped[Priority] = mapped_column(Enum(Priority), default=Priority.MEDIUM)

    assignee_id: Mapped[Integer] = mapped_column(ForeignKey("user.id"), nullable=True)
    assignee: Mapped["User"] = relationship("User", back_populates="tasks")

    author_id: Mapped[Integer] = mapped_column(ForeignKey("user.id"), nullable=False)
    author: Mapped["User"] = relationship("User", back_populates="assigned_task")

    tags: Mapped[String] = mapped_column(String(255), nullable=True)

    dependencies: Mapped[list["Task"]] = relationship(
        "Task",
        secondary=task_dependencies.c.task.id,
        primaryjoin=id == task_dependencies.c.task.id,
        secondaryjoin=id == task_dependencies.c.dependency_id,
        backref="dependents",
        lazy="selectin",
    )
    __table_args__ = (Index("idx_task_title", title), Index("idx_"))

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status}, priority={self.priority}>"
