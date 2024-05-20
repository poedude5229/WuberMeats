"""empty message

Revision ID: 3abc717a7f7b
Revises:
Create Date: 2024-05-19 18:51:36.079023

"""
from alembic import op
import sqlalchemy as sa
from dotenv import load_dotenv
import os
# revision identifiers, used by Alembic.
SCHEMA = os.getenv("SCHEMA")

revision = '3abc717a7f7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(f'{SCHEMA}.user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('firstname', sa.String(length=25), nullable=False),
    sa.Column('lastname', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(length=25), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table(f'{SCHEMA}.restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('cuisine', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('hours_of_operation', sa.String(length=255), nullable=False),
    sa.Column('delivery_radius', sa.Integer(), nullable=True),
    sa.Column('cover_image', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], [f'{SCHEMA}.user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(f'{SCHEMA}.menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=55), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=55), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], [f'{SCHEMA}.restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(f'{SCHEMA}.review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(length=255), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], [f'{SCHEMA}.restaurant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [f'{SCHEMA}.user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(f'{SCHEMA}.carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['menu_item_id'], [f'{SCHEMA}.menu.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [f'{SCHEMA}.user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table(f'{SCHEMA}.carts')
    op.drop_table(f'{SCHEMA}.review')
    op.drop_table(f'{SCHEMA}.menu')
    op.drop_table(f'{SCHEMA}.restaurant')
    op.drop_table(f'{SCHEMA}.user')
    # ### end Alembic commands ###
