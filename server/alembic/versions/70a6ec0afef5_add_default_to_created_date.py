"""add default to created_date

Revision ID: 70a6ec0afef5
Revises: db1a6678949a
Create Date: 2026-03-25 14:41:30.139633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70a6ec0afef5'
down_revision: Union[str, Sequence[str], None] = 'db1a6678949a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('users', 'created_date', server_default=sa.func.now())


def downgrade() -> None:
    """Downgrade schema."""
    pass
