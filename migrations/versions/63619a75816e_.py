"""empty message

Revision ID: 63619a75816e
Revises: dab0ada097df
Create Date: 2017-09-01 00:25:22.142438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63619a75816e'
down_revision = 'dab0ada097df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament', sa.Column('judge', sa.Integer(), nullable=True))
    op.add_column('tournament', sa.Column('organizer', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tournament', 'user', ['judge'], ['id'])
    op.create_foreign_key(None, 'tournament', 'user', ['organizer'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tournament', type_='foreignkey')
    op.drop_constraint(None, 'tournament', type_='foreignkey')
    op.drop_column('tournament', 'organizer')
    op.drop_column('tournament', 'judge')
    # ### end Alembic commands ###
