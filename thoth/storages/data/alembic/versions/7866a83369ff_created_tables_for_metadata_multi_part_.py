"""Created tables for metadata multi part keys

Revision ID: 7866a83369ff
Revises: dd19dd789f6d
Create Date: 2019-11-05 14:25:01.902734+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7866a83369ff'
down_revision = 'dd19dd789f6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('python_package_metadata_classifier',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classifier', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('python_package_metadata_distutils',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('distutils', sa.String(length=256), nullable=True),
    sa.Column('distutils_type', postgresql.ENUM('REQUIRED', 'PROVIDED', 'OBSOLETE', name='distutils_type'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('python_package_metadata_platform',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('platform', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('python_package_metadata_project_url',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('project_url', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('python_package_metadata_provides_extra',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('optional_feature', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('python_package_metadata_requires_external',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dependency', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('python_package_metadata_supported_platform',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('supported_platform', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('has_metadata_classifier',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_classifier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_classifier_id'], ['python_package_metadata_classifier.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_classifier_id')
    )
    op.create_table('has_metadata_distutils',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_distutils_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_distutils_id'], ['python_package_metadata_distutils.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_distutils_id')
    )
    op.create_table('has_metadata_platform',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_platform_id'], ['python_package_metadata_platform.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_platform_id')
    )
    op.create_table('has_metadata_project_url',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_project_url_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_project_url_id'], ['python_package_metadata_project_url.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_project_url_id')
    )
    op.create_table('has_metadata_provides_extra',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_provides_extra_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_provides_extra_id'], ['python_package_metadata_provides_extra.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_provides_extra_id')
    )
    op.create_table('has_metadata_requires_external',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_requires_external_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_requires_external_id'], ['python_package_metadata_requires_external.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_requires_external_id')
    )
    op.create_table('has_metadata_supported_platform',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('python_package_metadata_id', sa.Integer(), nullable=False),
    sa.Column('python_package_metadata_supported_platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['python_package_metadata_id'], ['python_package_metadata.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['python_package_metadata_supported_platform_id'], ['python_package_metadata_supported_platform.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'python_package_metadata_id', 'python_package_metadata_supported_platform_id')
    )
    op.add_column('python_package_metadata', sa.Column('description', sa.String(length=256), nullable=True))
    op.drop_column('python_package_metadata', 'classifier')
    op.drop_column('python_package_metadata', 'requires_dist')
    op.drop_column('python_package_metadata', 'provides_extra')
    op.drop_column('python_package_metadata', 'project_url')
    op.drop_column('python_package_metadata', 'platform')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('python_package_metadata', sa.Column('platform', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('python_package_metadata', sa.Column('project_url', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('python_package_metadata', sa.Column('provides_extra', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('python_package_metadata', sa.Column('requires_dist', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('python_package_metadata', sa.Column('classifier', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.drop_column('python_package_metadata', 'description')
    op.drop_table('has_metadata_supported_platform')
    op.drop_table('has_metadata_requires_external')
    op.drop_table('has_metadata_provides_extra')
    op.drop_table('has_metadata_project_url')
    op.drop_table('has_metadata_platform')
    op.drop_table('has_metadata_distutils')
    op.drop_table('has_metadata_classifier')
    op.drop_table('python_package_metadata_supported_platform')
    op.drop_table('python_package_metadata_requires_external')
    op.drop_table('python_package_metadata_provides_extra')
    op.drop_table('python_package_metadata_project_url')
    op.drop_table('python_package_metadata_platform')
    op.drop_table('python_package_metadata_distutils')
    op.drop_table('python_package_metadata_classifier')
    # ### end Alembic commands ###
