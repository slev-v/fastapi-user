from typing import Dict, List
import uuid

from src.application.user.exceptions import InvalidSessionId


class SessionServiceMock:
    def __init__(self):
        self.storage: Dict[str, List] = {}

    async def create_session(self, user_id: int) -> str:
        session_id = str(uuid.uuid4())
        while session_id in self.storage:
            session_id = str(uuid.uuid4())

        ex_seconds = 30 * 60
        self.storage[session_id] = [user_id, ex_seconds]
        return session_id

    async def delete_session(self, session_id: str) -> None:
        del self.storage[session_id]

    async def get(self, session_id: str) -> int:
        user_id = self.storage[session_id][0]
        if not user_id:
            raise InvalidSessionId
        return int(user_id)
