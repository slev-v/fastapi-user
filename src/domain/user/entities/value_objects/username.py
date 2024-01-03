from dataclasses import dataclass

from src.domain.common.entities.value_objects.value_object import ValueObject
from src.domain.common.exceptions import DomainException


@dataclass(eq=False)
class WrongUsernameValue(ValueError, DomainException):
    username: str
    text: str

    @property
    def title(self) -> str:
        return self.text


class TooShortUsername(WrongUsernameValue):
    pass


class TooLongUsername(WrongUsernameValue):
    pass


class InvalidUsername(WrongUsernameValue):
    pass


@dataclass(frozen=True)
class UserName(ValueObject, str):
    value: str

    def __post_init__(self):
        v = self.value

        if len(v) < 3:
            raise TooShortUsername(v, "Username must be at least 3 characters long")

        if len(v) > 32:
            raise TooLongUsername(v, "Username must be at most 32 characters long")

        if " " in v:
            raise InvalidUsername(v, "Username must not contain spaces")

        if v[0].isnumeric():
            raise InvalidUsername(v, "Username must not start with a digit")

        if v.isnumeric():
            raise InvalidUsername(v, "Username must not be numeric")

    def __composite_values__(self):
        return (self.value,)
