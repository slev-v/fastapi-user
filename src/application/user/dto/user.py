from dataclasses import dataclass
from typing import List


@dataclass
class UserResponseDTO:
    id: int
    username: str
    email: str


@dataclass
class UserRequestDTO:
    username: str
    email: str
    password: str


@dataclass
class UserLoginRequestDTO:
    username: str
    password: str


@dataclass
class TokenResponseDTO:
    access_token: str
    token_type: str


@dataclass
class UsersResponseDTO:
    users: List[UserResponseDTO]
