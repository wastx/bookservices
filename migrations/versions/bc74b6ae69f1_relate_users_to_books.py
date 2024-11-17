"""relate users to books

Revision ID: bc74b6ae69f1
Revises: dc21fadb3085
Create Date: 2024-11-03 01:01:41.029583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'bc74b6ae69f1'
down_revision: Union[str, None] = 'dc21fadb3085'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('user_uid', sa.Uuid(), nullable=True))
    op.create_foreign_key(None, 'books', 'users', ['user_uid'], ['uid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'user_uid')
    # ### end Alembic commands ###