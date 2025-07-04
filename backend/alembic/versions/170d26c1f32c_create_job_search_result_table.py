"""create job search result table

Revision ID: 170d26c1f32c
Revises: e17ecb3e618d
Create Date: 2025-07-04 12:53:57.994547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '170d26c1f32c'
down_revision: Union[str, Sequence[str], None] = 'e17ecb3e618d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'job_search_result',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('job_search_id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(length=255), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('platform', sa.String(length=255), nullable=False),
        sa.Column('published_at', sa.DateTime(), nullable=False),
        sa.Column('processed_at', sa.DateTime(), nullable=False),
        sa.Index('ix_job_search_result_job_search_id_published_at', 'job_search_id', 'published_at')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('job_search_result')