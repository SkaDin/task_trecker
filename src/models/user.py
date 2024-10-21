from sqlalchemy import Boolean, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, create_at


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    registered_at: Mapped[create_at]

    created_tasks: Mapped[list["Task"]] = relationship(  # noqa
        "Task", back_populates="author", foreign_keys="[Task.author_id]"
    )
    assigned_task: Mapped[list["Task"]] = relationship(  # noqa
        "Task", back_populates="assignee", foreign_keys="[Task.assignee_id]"
    )

    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean(), default=False)  # TODO: DROP COLUMN
    is_verified: Mapped[bool] = mapped_column(Boolean(), default=False)  # TODO: DROP COLUMN

    __table_args__ = (Index("idx_user_email", email),)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}>"
