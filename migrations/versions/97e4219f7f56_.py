"""empty message

Revision ID: 97e4219f7f56
Revises: 689bc38313a4
Create Date: 2017-09-01 14:52:33.772245

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97e4219f7f56'
down_revision = '689bc38313a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('captain', sa.Column('tournament_id', sa.Integer(), nullable=True))
    op.drop_constraint('captain_ibfk_2', 'captain', type_='foreignkey')
    op.create_foreign_key(None, 'captain', 'tournament', ['tournament_id'], ['id'])
    op.drop_column('captain', 'tournament')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('captain', sa.Column('tournament', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'captain', type_='foreignkey')
    op.create_foreign_key('captain_ibfk_2', 'captain', 'tournament', ['tournament'], ['id'])
    op.drop_column('captain', 'tournament_id')
    # ### end Alembic commands ###