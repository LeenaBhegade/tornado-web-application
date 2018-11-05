"""create word table

Revision ID: 8ce64cdc03a4
Revises: 
Create Date: 2018-10-28 19:14:33.712522

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8ce64cdc03a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'words',
        sa.Column('word_hash', sa.String(100), primary_key=True),
        sa.Column('word', sa.LargeBinary, nullable=False),
        sa.Column('count', sa.Integer, nullable=False)
    )

def downgrade():
    op.drop_table('words')
