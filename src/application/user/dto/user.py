from dataclasses import dataclass
from typing import List


@dataclass
class UserResponseDTO:
    user_id: int
    username: str
    email: str


@dataclass
class UserRequestDTO:
    username: str
    email: str
    password: str


@dataclass
class UserLoginRequestDTO:
    user_id: int
    password: str


@dataclass
class SessionResponseDTO:
    session_id: str


@dataclass
class UsersResponseDTO:
    users: List[UserResponseDTO]
