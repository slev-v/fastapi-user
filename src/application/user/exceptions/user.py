from dataclasses import dataclass

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class UserIdNotExist(ApplicationException):
    user_id: int

    @property
    def title(self) -> str:
        return f"User with id {self.user_id} not found"


@dataclass(eq=False)
class UsernameNotExist(ApplicationException):
    username: str

    @property
    def title(self) -> str:
        return f"User with username {self.username} not found"


@dataclass(eq=False)
class UsernameAlreadyExist(ApplicationException):
    username: str

    @property
    def title(self) -> str:
        return f"User with username {self.username} already exist"


@dataclass(eq=False)
class EmailAlreadyExist(ApplicationException):
    email: str

    @property
    def title(self) -> str:
        return f"User with email {self.email} already exist"


@dataclass(eq=False)
class InvalidSessionId(ApplicationException):
    @property
    def title(self) -> str:
        return "Invalid session id"


@dataclass(eq=False)
class InvalidPassword(ApplicationException):
    @property
    def title(self) -> str:
        return "Invalid password"
