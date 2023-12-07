from src.application.common.exceptions import BaseException


class AuthError(BaseException):
    """Raised when a user cannot pass the authentication"""
