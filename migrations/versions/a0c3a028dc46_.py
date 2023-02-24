"""empty message

Revision ID: a0c3a028dc46
Revises: fc7e6d6a79a4
Create Date: 2023-02-22 20:39:19.079950

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a0c3a028dc46'
down_revision = 'fc7e6d6a79a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('upper_cap', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('lower_cap', sa.String(length=150), nullable=True))
        batch_op.alter_column('file_name',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('mimetype',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.drop_column('data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', postgresql.BYTEA(), autoincrement=False, nullable=False))
        batch_op.alter_column('mimetype',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('file_name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.drop_column('lower_cap')
        batch_op.drop_column('upper_cap')
        batch_op.drop_column('title')

    # ### end Alembic commands ###
