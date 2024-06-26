"""1_tables_creation

Revision ID: 8fed2ea3e748
Revises: 
Create Date: 2024-04-14 13:32:54.134511

"""
import sqlalchemy as sa

from alembic import op
from db_models import orm_helpers


# revision identifiers, used by Alembic.
revision = "8fed2ea3e748"
down_revision = None
branch_labels = None
depends_on = None

# pylint: disable=no-member


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "configurations",
        sa.Column("service", sa.String(length=100), nullable=False),
        sa.Column("version", sa.String(length=100), nullable=False),
        sa.Column("hostname", sa.String(length=1000), nullable=True),
        sa.Column("port", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(length=100), nullable=True),
        sa.Column("updated_at", sa.DateTime(), server_default="now()", nullable=True),
        sa.PrimaryKeyConstraint("service", "version"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("configurations")
    # ### end Alembic commands ###
