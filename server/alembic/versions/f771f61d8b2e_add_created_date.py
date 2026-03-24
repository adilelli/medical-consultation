"""add created_date

Revision ID: f771f61d8b2e
Revises: a3674c479d95
Create Date: 2026-03-24 15:50:22.851983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f771f61d8b2e'
down_revision: Union[str, Sequence[str], None] = 'a3674c479d95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
