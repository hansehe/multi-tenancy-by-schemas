"""baseline

Revision ID: 34a0a0231e4a
Revises:
Create Date: 2022-08-18 15:35:17.002763

"""
import sqlalchemy as sa
import sqlalchemy_utils as sau
from alembic import op

# revision identifiers, used by Alembic.
revision = '34a0a0231e4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('TestTable',
                    sa.Column('id', sau.types.uuid.UUIDType(), nullable=False),
                    sa.Column('stuff', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))


def downgrade():
    op.drop_table('TestTable')
