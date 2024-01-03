import re
from dataclasses import dataclass

from src.domain.common.entities.value_objects.value_object import ValueObject
from src.domain.common.exceptions import DomainException


@dataclass(eq=False)
class WrongEmailValue(ValueError, DomainException):
    email: str
    text: str

    @property
    def title(self) -> str:
        return self.text


@dataclass(frozen=True)
class Email(ValueObject, str):
    value: str

    def __post_init__(self):
        v = self.value

        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if not re.fullmatch(regex, v):
            raise WrongEmailValue(v, "Email must be valid")
