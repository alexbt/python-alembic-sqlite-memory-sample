"""initial

Revision ID: 6e56fd14ef29
Revises: 
Create Date: 2021-03-30 07:19:54.445748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e56fd14ef29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'some_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('some_column', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('some_table')
