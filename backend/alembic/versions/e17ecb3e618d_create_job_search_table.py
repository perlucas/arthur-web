"""create job search table

Revision ID: e17ecb3e618d
Revises: c7c7f56e36ac
Create Date: 2025-07-04 11:53:57.994547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e17ecb3e618d'
down_revision: Union[str, Sequence[str], None] = 'c7c7f56e36ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'job_search',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), nullable=False, index=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.Column('search_parameters', sa.JSON(), nullable=False),
        sa.Column('setting_send_email_notifications', sa.Boolean(), nullable=False, server_default=sa.text('1')),
        sa.Column('updated_at', sa.DateTime(), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('job_search')