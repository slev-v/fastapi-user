from dataclasses import dataclass

from src.domain.common.exceptions import AppException


class ApplicationException(AppException):
    """Base Application Exception"""

    @property
    def title(self) -> str:
        return "An application error occurred"


class UnexpectedError(ApplicationException):
    pass


@dataclass(eq=False)
class MappingError(ApplicationException):
    _text: str

    @property
    def title(self) -> str:
        return self._text


@dataclass(eq=False)
class WrongPaginationValue(ApplicationException):
    _text: str

    @property
    def title(self) -> str:
        return self._text
