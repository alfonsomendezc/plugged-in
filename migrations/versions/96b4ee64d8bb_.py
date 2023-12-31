"""empty message

Revision ID: 96b4ee64d8bb
Revises: 303797a2312f
Create Date: 2022-07-07 21:02:20.106610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96b4ee64d8bb'
down_revision = '303797a2312f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('profile_platform_key', 'profile', type_='unique')
    op.drop_column('profile', 'platform')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('platform', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.create_unique_constraint('profile_platform_key', 'profile', ['platform'])
    # ### end Alembic commands ###
