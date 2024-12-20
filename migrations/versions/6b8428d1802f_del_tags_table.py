"""del tags table

Revision ID: 6b8428d1802f
Revises: d990bfe07026
Create Date: 2024-11-17 16:21:05.639583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6b8428d1802f'
down_revision: Union[str, None] = 'd990bfe07026'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booktag')
    op.drop_table('tags')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('uid', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('uid', name='tags_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('booktag',
    sa.Column('book_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('tag_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.uid'], name='booktag_book_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.uid'], name='booktag_tag_id_fkey'),
    sa.PrimaryKeyConstraint('book_id', 'tag_id', name='booktag_pkey')
    )
    # ### end Alembic commands ###
