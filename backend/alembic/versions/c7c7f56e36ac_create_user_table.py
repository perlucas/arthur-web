"""create user table

Revision ID: c7c7f56e36ac
Revises: 
Create Date: 2025-07-04 10:53:57.994547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7c7f56e36ac'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True, index=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('setting_send_email_notifications', sa.Boolean(), nullable=False, server_default=sa.text('1')),
        sa.Column('setting_language', sa.Enum('es', 'en', name='language'), nullable=False, server_default='en'),
        sa.Column('plan_type', sa.Enum('demo', 'premium', 'custom', name='plantype'), nullable=False),
        sa.Column('plan_expires_on', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
