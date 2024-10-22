"""unique title

Revision ID: 310613ac2915
Revises: 0d975fed47b4
Create Date: 2024-10-22 12:58:59.745096

"""
from typing import Sequence, Union

from alembic import op

revision: str = "310613ac2915"
down_revision: Union[str, None] = "0d975fed47b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(None, "tasks", ["title"])


def downgrade() -> None:
    op.drop_constraint(None, "tasks", type_="unique")
