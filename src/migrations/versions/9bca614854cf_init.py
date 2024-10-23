"""init

Revision ID: 9bca614854cf
Revises:
Create Date: 2024-10-23 15:54:11.014855

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "9bca614854cf"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=50), nullable=True),
        sa.Column("first_name", sa.String(length=50), nullable=True),
        sa.Column("last_name", sa.String(length=50), nullable=True),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column(
            "registered_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index("idx_user_email", "user", ["email"], unique=False)
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column(
            "create_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False
        ),
        sa.Column(
            "due_date", sa.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False
        ),
        sa.Column("status", sa.Enum("NEW", "IN_PROGRESS", "DONE", "OVERDUE", name="status"), nullable=False),
        sa.Column("priority", sa.Enum("LOW", "MEDIUM", "HIGH", "CRITICAL", name="priority"), nullable=False),
        sa.Column("assignee_id", sa.Integer(), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("tags", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["assignee_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_index("idx_task_title", "tasks", ["title"], unique=False)


def downgrade() -> None:
    op.drop_index("idx_task_title", table_name="tasks")
    op.drop_table("tasks")
    op.drop_index("idx_user_email", table_name="user")
    op.drop_table("user")
