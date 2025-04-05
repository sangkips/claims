"""initial migrations

Revision ID: 4712a9e1a658
Revises: 
Create Date: 2025-04-05 16:02:09.074576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4712a9e1a658'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claims')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('claims',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('policy_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('claimant_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('claim_amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('fraud_flag', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='claims_pkey')
    )
    # ### end Alembic commands ###
