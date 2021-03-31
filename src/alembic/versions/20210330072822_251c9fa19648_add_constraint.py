"""add username constraint on user

Revision ID: 251c9fa19648
Revises: 6e56fd14ef29
Create Date: 2021-03-30 07:28:22.626963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '251c9fa19648'
down_revision = '6e56fd14ef29'
branch_labels = None
depends_on = None


def upgrade():
    table = sa.Table(
        'some_table',
        sa.MetaData(),
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('some_column', sa.String(), nullable=False)
    )

    with op.batch_alter_table('some_table', copy_from=table) as batch_op:
        batch_op.create_check_constraint(
            'ck_some_table_some_column_len',
            'length(some_column) <= 10')

def downgrade():
    table = sa.Table(
        'some_table',
        sa.MetaData(),
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('some_column', sa.String(), nullable=False),
        sa.CheckConstraint('length(some_column) <= 10',
                           name='ck_some_table_some_column_len'),
    )

    with op.batch_alter_table('some_table', copy_from=table) as batch_op:
        batch_op.drop_constraint('ck_some_table_some_column_len')
