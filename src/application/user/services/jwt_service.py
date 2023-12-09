from datetime import datetime, timedelta

from jose import JWTError, jwt

from src.application.user.entities import value_objects as vo
from src.application.user.exceptions.user import AuthError
from src.application.user.protocols import JwtService


class JwtServiceImp(JwtService):
    # TODO: secret and expire from env
    # TODO: db token storage
    def encode(self, username: vo.UserName) -> str:
        to_encode = {"sub": username}
        expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode["exp"] = expire  # type: ignore FIX: type error
        return jwt.encode(to_encode, "secret", algorithm="HS256")

    def decode(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            return payload
        except JWTError:
            raise AuthError("Invalid token")
