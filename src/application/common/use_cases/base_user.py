from fastapi import Depends

from src.database.repositories.user import UserRepo
from src.di.stub import provide_user_repo_stub


class BaseUseCase:
    def __init__(self, user_repo: UserRepo = Depends(provide_user_repo_stub)):
        self.user_repo = user_repo
