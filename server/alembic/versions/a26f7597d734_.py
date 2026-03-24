"""...

Revision ID: a26f7597d734
Revises: b0d5cfd81776
Create Date: 2026-03-24 15:57:39.269503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a26f7597d734'
down_revision: Union[str, Sequence[str], None] = 'b0d5cfd81776'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
