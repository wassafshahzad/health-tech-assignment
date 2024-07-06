"""Added date time field

Revision ID: e2a58abc7970
Revises: 60315e42ffb6
Create Date: 2024-07-06 14:09:01.856689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2a58abc7970'
down_revision = '60315e42ffb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('interaction', sa.Column('created_datetime', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('interaction', 'created_datetime')
    # ### end Alembic commands ###kk