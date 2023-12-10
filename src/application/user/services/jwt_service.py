from datetime import datetime, timedelta

from jose import JWTError, jwt

from src.application.user.exceptions.user import AuthError
from src.application.user.protocols import JwtService
from src.main.config import WebConfig


class JwtServiceImp(JwtService):
    # TODO: db token storage

    def __init__(self, config: WebConfig) -> None:
        self.config = config

    def encode(self, username: str) -> str:
        to_encode = {"sub": username}
        expire = datetime.utcnow() + timedelta(minutes=self.config.jwt_expire_time)
        to_encode["exp"] = expire  # type: ignore
        return jwt.encode(
            to_encode, self.config.jwt_secret, algorithm=self.config.jwt_algorithm
        )

    def decode(self, token: str) -> dict:
        try:
            payload = jwt.decode(
                token, self.config.jwt_secret, algorithms=[self.config.jwt_algorithm]
            )
            return payload
        except JWTError:
            raise AuthError("Invalid token")
