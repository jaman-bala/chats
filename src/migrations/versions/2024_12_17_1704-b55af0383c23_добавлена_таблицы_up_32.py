"""Добавлена таблицы UP:32

Revision ID: b55af0383c23
Revises: f9f1c91400dc
Create Date: 2024-12-17 17:04:38.462144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b55af0383c23'
down_revision: Union[str, None] = 'f9f1c91400dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('messages', sa.Column('files', postgresql.ARRAY(sa.String()), nullable=True))
    op.drop_column('messages', 'file')


def downgrade() -> None:
    op.add_column('messages', sa.Column('file', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.drop_column('messages', 'files')

