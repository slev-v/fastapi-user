from dataclasses import dataclass

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class UserIdNotExists(ApplicationException):
    user_id: int

    @property
    def title(self) -> str:
        return f"User with id {self.user_id} not found"


@dataclass(eq=False)
class UsernameNotExists(ApplicationException):
    username: str

    @property
    def title(self) -> str:
        return f"User with username {self.username} not found"


@dataclass(eq=False)
class UsernameAlreadyExists(ApplicationException):
    username: str

    @property
    def title(self) -> str:
        return f"User with username {self.username} already exist"


@dataclass(eq=False)
class EmailAlreadyExists(ApplicationException):
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
