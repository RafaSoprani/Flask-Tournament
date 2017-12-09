"""empty message

Revision ID: d5965da89905
Revises: 
Create Date: 2017-12-09 18:26:27.417108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5965da89905'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pair', sa.Column('tournament_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pair', 'tournament', ['tournament_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pair', type_='foreignkey')
    op.drop_column('pair', 'tournament_id')
    # ### end Alembic commands ###
