"""empty message

Revision ID: 717a78a53cc0
Revises: 
Create Date: 2018-12-16 11:30:27.298173

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '717a78a53cc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('menu_name', sa.String(length=50), nullable=False))
    op.drop_column('menu', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('name', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('menu', 'menu_name')
    # ### end Alembic commands ###
