from typing import Protocol

from src.application.user.entities import value_objects as vo


class JwtService(Protocol):
    def encode(self, username: vo.UserName) -> str:
        raise NotImplementedError

    def decode(self, token: str) -> dict:
        raise NotImplementedError
