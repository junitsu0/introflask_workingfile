"""add post table

Revision ID: 31364fb5c8d4
Revises: 4f55102d5940
Create Date: 2022-08-21 13:04:35.537493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31364fb5c8d4'
down_revision = '4f55102d5940'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('body', sa.String(length=50), nullable=False),
    sa.Column('data_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
