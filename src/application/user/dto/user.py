from dataclasses import dataclass
from typing import List

from src.application.common.dto import DTO, Pagination


@dataclass
class UserResponseDTO(DTO):
    user_id: int
    username: str
    email: str


@dataclass
class UserRequestDTO(DTO):
    username: str
    email: str
    password: str


@dataclass
class UserLoginRequestDTO(DTO):
    user_id: int
    password: str


@dataclass
class SessionResponseDTO(DTO):
    session_id: str


@dataclass
class UsersRequestDTO(DTO):
    pagination: Pagination


@dataclass
class UsersResponseDTO(DTO):
    users: List[UserResponseDTO]
