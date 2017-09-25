"""empty message

Revision ID: 8590e9460f6c
Revises: c7f173f1484d
Create Date: 2017-09-22 14:43:33.401322

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8590e9460f6c'
down_revision = 'c7f173f1484d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('judge_tournament')
    op.drop_constraint('tournament_ibfk_2', 'tournament', type_='foreignkey')
    op.drop_column('tournament', 'judge_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament', sa.Column('judge_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('tournament_ibfk_2', 'tournament', 'judge', ['judge_id'], ['id'])
    op.create_table('judge_tournament',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('judge_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('tournament_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['judge_id'], ['judge.id'], name='judge_tournament_ibfk_1'),
    sa.ForeignKeyConstraint(['tournament_id'], ['tournament.id'], name='judge_tournament_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###