"""create notification table

Revision ID: 1547c0afe49c
Revises: e39bebee1ecb
Create Date: 2025-07-04 11:40:04.443720

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1547c0afe49c'
down_revision: Union[str, Sequence[str], None] = 'e39bebee1ecb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'notification',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), nullable=False, index=True),
        sa.Column('is_read', sa.Boolean(), nullable=False),
        sa.Column('type', sa.String(length=255), nullable=False),
        sa.Column('metadata', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('notification')
