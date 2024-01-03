from dataclasses import dataclass

from src.domain.common.entities.value_objects.value_object import ValueObject
from src.domain.common.exceptions import DomainException


@dataclass(eq=False)
class WrongPasswordValue(ValueError, DomainException):
    text: str

    @property
    def title(self) -> str:
        return self.text


@dataclass(frozen=True)
class RawPassword(ValueObject):
    value: str

    def __post_init__(self):
        v = self.value

        if len(v) < 8:
            raise WrongPasswordValue("Password must be at least 8 characters long")

        if len(v) > 32:
            raise WrongPasswordValue("Password must be at most 32 characters long")

        if not any(char.isdigit() for char in v):
            raise WrongPasswordValue("Password must contain at least one digit")

        if not any(char.isupper() for char in v):
            raise WrongPasswordValue(
                "Password must contain at least one uppercase letter"
            )

        if not any(char.islower() for char in v):
            raise WrongPasswordValue(
                "Password must contain at least one lowercase letter"
            )

        if not any(char in "!@#$%^&*()_+" for char in v):
            raise WrongPasswordValue(
                "Password must contain at least one special character"
            )
