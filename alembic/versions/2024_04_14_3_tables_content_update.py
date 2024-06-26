"""3_tables_content_update

Revision ID: 6303e1a985df
Revises: 3d09ba29d8cd
Create Date: 2024-04-14 13:34:16.139663

"""
import sqlalchemy as sa

from alembic import op
from db_models import orm_helpers


# revision identifiers, used by Alembic.
revision = "6303e1a985df"
down_revision = "3d09ba29d8cd"
branch_labels = None
depends_on = None

# pylint: disable=no-member


def upgrade() -> None:
    # upgrade content changes
    # added rows from configurations
    op.execute(
        orm_helpers.generate_insert_query(
            "configurations",
            [
                {
                    "service": "local_service1",
                    "version": "v2",
                    "hostname": "localhost",
                    "port": 8080,
                    "status": "on",
                }
            ],
        )
    )
    # updated rows from configurations
    op.execute(
        orm_helpers.generate_update_query(
            "configurations",
            {"service": "local_service1", "version": "v1"},
            {"hostname": "localhost", "port": 8080, "status": "off"},
        )
    )
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # downgrade content changes
    # revert added rows from configurations
    op.execute(
        orm_helpers.generate_delete_query(
            "configurations", {"service": "local_service1", "version": "v2"}
        )
    )
    # revert updated rows from configurations
    op.execute(
        orm_helpers.generate_update_query(
            "configurations",
            {"service": "local_service1", "version": "v1"},
            {"hostname": "localhost", "port": 8080, "status": "on"},
        )
    )
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
