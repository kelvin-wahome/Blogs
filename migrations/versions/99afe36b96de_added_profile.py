"""Added profile

Revision ID: 99afe36b96de
Revises: c79f7dcb23ad
Create Date: 2019-02-18 14:35:48.956860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99afe36b96de'
down_revision = 'c79f7dcb23ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
