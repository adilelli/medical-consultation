"""...

Revision ID: b0d5cfd81776
Revises: 70f64bb15d0b
Create Date: 2026-03-24 15:56:01.015960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0d5cfd81776'
down_revision: Union[str, Sequence[str], None] = '70f64bb15d0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
