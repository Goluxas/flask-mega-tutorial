"""new fields in user model

Revision ID: 98ccc7c221fc
Revises: 5a508f385b29
Create Date: 2019-07-14 17:03:47.053162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98ccc7c221fc'
down_revision = '5a508f385b29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###