"""actualizacions

Revision ID: a297f71ad806
Revises: 860bc5abc504
Create Date: 2024-10-04 11:08:50.842639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a297f71ad806'
down_revision = '860bc5abc504'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mantenimientos', schema=None) as batch_op:
        batch_op.alter_column('descripcion',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mantenimientos', schema=None) as batch_op:
        batch_op.alter_column('descripcion',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###
