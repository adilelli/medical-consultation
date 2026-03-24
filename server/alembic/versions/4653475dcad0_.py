"""...

Revision ID: 4653475dcad0
Revises: a26f7597d734
Create Date: 2026-03-24 16:03:20.728921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4653475dcad0'
down_revision: Union[str, Sequence[str], None] = 'a26f7597d734'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
