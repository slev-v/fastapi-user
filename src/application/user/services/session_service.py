import uuid

from src.application.user.exceptions import InvalidSessionId
from src.application.user.protocols import SessionService
from src.infrastructure.redis.repositories import RedisRepository
from src.main.config import WebConfig


class SessionServiceImp(SessionService):
    def __init__(
        self,
        config: WebConfig,
        redis_repo: RedisRepository,
    ) -> None:
        self.config = config
        self.redis_repo = redis_repo

    async def create_session(self, user_id: int) -> str:
        session_id = str(uuid.uuid4())
        while await self.redis_repo.exists(session_id):
            session_id = str(uuid.uuid4())

        ex_seconds = self.config.session_expire_time * 60
        await self.redis_repo.set_with_ex(session_id, user_id, ex_seconds)
        return session_id

    async def delete_session(self, session_id: str) -> None:
        await self.redis_repo.delete(session_id)

    async def get(self, session_id: str) -> int:
        user_id = await self.redis_repo.get(session_id)
        if not user_id:
            raise InvalidSessionId
        return int(user_id)
