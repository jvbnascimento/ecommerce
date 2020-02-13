"""users table

Revision ID: f2f7da5a312c
Revises: 0b7e7ac5892f
Create Date: 2020-02-12 10:51:26.823476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f7da5a312c'
down_revision = '0b7e7ac5892f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('nome', sa.String(length=64), nullable=True))
    op.add_column('usuario', sa.Column('senha_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_usuario_nome'), 'usuario', ['nome'], unique=False)
    op.drop_index('ix_usuario_username', table_name='usuario')
    op.drop_column('usuario', 'username')
    op.drop_column('usuario', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.add_column('usuario', sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.create_index('ix_usuario_username', 'usuario', ['username'], unique=True)
    op.drop_index(op.f('ix_usuario_nome'), table_name='usuario')
    op.drop_column('usuario', 'senha_hash')
    op.drop_column('usuario', 'nome')
    # ### end Alembic commands ###