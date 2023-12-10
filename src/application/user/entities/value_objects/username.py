from dataclasses import dataclass

from src.application.common.entities.value_objects.value_object import ValueObject


@dataclass(frozen=True)
class UserName(ValueObject, str):
    value: str

    def __post_init__(self):
        v = self.value

        if not isinstance(v, str):
            raise TypeError("Username must be a string")

        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters long")

        if len(v) > 32:
            raise ValueError("Username must be at most 32 characters long")

        if " " in v:
            raise ValueError("Username must not contain spaces")

        if v[0].isnumeric():
            raise ValueError("Username must not start with a digit")

        if v.isnumeric():
            raise ValueError("Username must not be numeric")

    def __composite_values__(self):
        return (self.value,)
