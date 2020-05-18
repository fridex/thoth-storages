"""Added kebechet installation table

Revision ID: 340d6e381d75
Revises: a7442899ef28
Create Date: 2020-05-18 18:28:55.710850+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '340d6e381d75'
down_revision = 'a7442899ef28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kebechet_github_installations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('slug', sa.Text(), nullable=False),
    sa.Column('repo_name', sa.Text(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.Column('installation_id', sa.Text(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kebechet_github_installations')
    # ### end Alembic commands ###
