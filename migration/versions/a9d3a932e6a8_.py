"""empty message

Revision ID: a9d3a932e6a8
Revises: 
Create Date: 2022-05-30 13:33:46.722719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9d3a932e6a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    op.drop_table('interests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interests',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=105), autoincrement=False, nullable=False),
    sa.Column('interest_code', sa.VARCHAR(length=3), autoincrement=False, nullable=False),
    sa.Column('job_zone', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=733), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='mytable_pkey')
    )
    op.create_table('courses',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=102), autoincrement=False, nullable=False),
    sa.Column('is_paid', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('num_subscribers', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('avg_rating', sa.NUMERIC(precision=7, scale=5), autoincrement=False, nullable=False),
    sa.Column('avg_rating_recent', sa.NUMERIC(precision=7, scale=5), autoincrement=False, nullable=False),
    sa.Column('rating', sa.NUMERIC(precision=7, scale=5), autoincrement=False, nullable=False),
    sa.Column('num_reviews', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('num_published_lectures', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('field', sa.VARCHAR(length=22), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='courses_pkey')
    )
    # ### end Alembic commands ###
