from dataclasses import dataclass
from abc import ABC


class DTO(ABC):
    pass


@dataclass
class Pagination(DTO):
    limit: int
    offset: int
