from dataclasses import dataclass, field

from src.domain.common.entities import Entity
from src.domain.user.entities import value_objects as vo


@dataclass
class User(Entity):
    email: vo.Email
    username: vo.UserName
    hashed_password: vo.HashedPassword
