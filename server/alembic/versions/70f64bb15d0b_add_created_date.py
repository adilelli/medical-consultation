"""add created_date

Revision ID: 70f64bb15d0b
Revises: f771f61d8b2e
Create Date: 2026-03-24 15:52:39.631074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70f64bb15d0b'
down_revision: Union[str, Sequence[str], None] = 'f771f61d8b2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
