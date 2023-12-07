from dataclasses import dataclass

from src.application.common.entities.entity import Entity
from src.application.user.entities import value_objects as vo


@dataclass
class User(Entity):
    email: vo.Email
    username: vo.UserName
    hashed_password: vo.HashedPassword
