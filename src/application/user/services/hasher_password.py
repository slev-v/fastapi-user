from passlib.context import CryptContext

from src.application.user.protocols import HasherPassword


class HasherPasswordImp(HasherPassword):
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self._pwd_context.hash(password)
