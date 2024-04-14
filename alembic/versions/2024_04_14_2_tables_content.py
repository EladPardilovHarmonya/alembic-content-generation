"""2_tables_content

Revision ID: 3d09ba29d8cd
Revises: 8fed2ea3e748
Create Date: 2024-04-14 13:33:18.031417

"""
import sqlalchemy as sa

from alembic import op
from db_models import orm_helpers


# revision identifiers, used by Alembic.
revision = "3d09ba29d8cd"
down_revision = "8fed2ea3e748"
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
                    "version": "v1",
                    "hostname": "localhost",
                    "port": 8080,
                    "status": "on",
                }
            ],
        )
    )
    op.execute(
        orm_helpers.generate_insert_query(
            "configurations",
            [
                {
                    "service": "local_service2",
                    "version": "v1",
                    "hostname": "localhost",
                    "port": 8081,
                    "status": "off",
                }
            ],
        )
    )
    op.execute(
        orm_helpers.generate_insert_query(
            "configurations",
            [
                {
                    "service": "local_service2",
                    "version": "v2",
                    "hostname": "localhost",
                    "port": 8081,
                    "status": "on",
                }
            ],
        )
    )
    op.execute(
        orm_helpers.generate_insert_query(
            "configurations",
            [
                {
                    "service": "remote_service1",
                    "version": "v1",
                    "hostname": "remotehost",
                    "port": 8080,
                    "status": "on",
                }
            ],
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
            "configurations", {"service": "local_service1", "version": "v1"}
        )
    )
    op.execute(
        orm_helpers.generate_delete_query(
            "configurations", {"service": "local_service2", "version": "v1"}
        )
    )
    op.execute(
        orm_helpers.generate_delete_query(
            "configurations", {"service": "local_service2", "version": "v2"}
        )
    )
    op.execute(
        orm_helpers.generate_delete_query(
            "configurations", {"service": "remote_service1", "version": "v1"}
        )
    )
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
