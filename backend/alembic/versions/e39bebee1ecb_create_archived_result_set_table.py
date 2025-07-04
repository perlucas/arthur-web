"""create archived_result_set table

Revision ID: e39bebee1ecb
Revises: 170d26c1f32c
Create Date: 2025-07-04 13:53:57.994547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e39bebee1ecb'
down_revision: Union[str, Sequence[str], None] = '170d26c1f32c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'archived_result_set',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('job_search_id', sa.Integer(), nullable=False),
        sa.Column('download_url', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Index('ix_archived_result_set_job_search_id_created_at', 'job_search_id', 'created_at')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('archived_result_set')