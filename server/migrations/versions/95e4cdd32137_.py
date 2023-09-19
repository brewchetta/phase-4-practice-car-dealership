"""empty message

Revision ID: 95e4cdd32137
Revises: 
Create Date: 2023-09-19 11:04:49.857458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e4cdd32137'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dealerships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('date_sold', sa.Date(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('dealership_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dealership_id'], ['dealerships.id'], name=op.f('fk_cars_dealership_id_dealerships')),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_cars_owner_id_owners')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    op.drop_table('owners')
    op.drop_table('dealerships')
    # ### end Alembic commands ###