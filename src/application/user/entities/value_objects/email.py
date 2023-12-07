import re
from dataclasses import dataclass

from src.application.common.entities.value_objects.value_object import \
    ValueObject


@dataclass(frozen=True)
class Email(ValueObject, str):
    value: str

    def __post_init__(self):
        v = self.value

        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if not isinstance(v, str):
            raise TypeError("Email must be a string")

        if not re.fullmatch(regex, v):
            raise ValueError("Email must be valid")
