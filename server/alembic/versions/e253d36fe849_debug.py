"""debug

Revision ID: e253d36fe849
Revises: 4653475dcad0
Create Date: 2026-03-24 16:11:17.912765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e253d36fe849'
down_revision: Union[str, Sequence[str], None] = '4653475dcad0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
