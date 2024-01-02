from dataclasses import dataclass

from src.domain.common.entities.entity import Entity
from src.domain.user.entities import value_objects as vo


@dataclass
class User(Entity):
    email: vo.Email
    username: vo.UserName
    hashed_password: vo.HashedPassword
