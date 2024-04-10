"""Added Timestamp

Revision ID: 3e889d46a9d8
Revises: 53abdc28d705
Create Date: 2024-04-09 18:21:00.217904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e889d46a9d8'
down_revision: Union[str, None] = '53abdc28d705'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column(
        'created_at', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column(
        'updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###
