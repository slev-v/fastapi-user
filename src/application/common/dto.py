from dataclasses import dataclass
from abc import ABC

from src.application.common.exceptions import WrongPaginationValue


class DTO(ABC):
    pass


@dataclass
class Pagination(DTO):
    limit: int
    offset: int

    def __post_init__(self):
        if self.limit < 0:
            raise WrongPaginationValue("limit must be greater than 0")
        if self.limit > 1000:
            raise WrongPaginationValue("limit must be less than 1000")
        if self.offset < 0:
            raise WrongPaginationValue("offset must be greater than 0")
