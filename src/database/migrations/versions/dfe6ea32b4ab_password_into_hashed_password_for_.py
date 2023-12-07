"""password into hashed_password for mapping

Revision ID: dfe6ea32b4ab
Revises: cdbd8fc4989a
Create Date: 2023-12-07 18:38:37.993442

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "dfe6ea32b4ab"
down_revision: Union[str, None] = "cdbd8fc4989a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users", "password", new_column_name="hashed_password")


def downgrade() -> None:
    op.alter_column("users", "hashed_password", new_column_name="password")
