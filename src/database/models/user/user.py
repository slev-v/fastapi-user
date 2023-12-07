import datetime

from sqlalchemy import sql
from sqlalchemy.orm import Mapped, mapped_column

from src.application.user import entities
from src.database.models.base import Base


class User(Base):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    email: Mapped[str] = mapped_column("email", nullable=False, unique=True)
    username: Mapped[str] = mapped_column("username", nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column("hashed_password", nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=sql.func.now()
    )


def user_mapping(mapper_registry):
    table = User.__table__
    mapper_registry.map_imperatively(entities.User, table)
