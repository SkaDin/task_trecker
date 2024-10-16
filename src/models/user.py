from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, create_at


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    registered_at: Mapped[create_at]

    created_tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="author", foreign_keys="Task.author_id"
    )  # type ignore

    assigned_task: Mapped[list["Task"]] = relationship(
        "Task", back_populates="assignee", foreign_keys="Task.assignee_id"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}>"
