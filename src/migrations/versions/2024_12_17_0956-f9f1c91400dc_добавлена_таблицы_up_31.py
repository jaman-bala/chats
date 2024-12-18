"""Добавлена таблицы UP:31

Revision ID: f9f1c91400dc
Revises: 00f36a7e97f8
Create Date: 2024-12-17 09:56:58.177870

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "f9f1c91400dc"
down_revision: Union[str, None] = "00f36a7e97f8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("roles", postgresql.ARRAY(sa.String()), nullable=False)
    )


def downgrade() -> None:
    op.drop_column("users", "roles")
