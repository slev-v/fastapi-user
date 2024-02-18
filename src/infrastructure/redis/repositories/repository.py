import redis.asyncio as redis


class RedisRepository:
    def __init__(self, connection: redis.Redis) -> None:
        self.connection = connection

    async def get(self, key: str) -> str:
        return await self.connection.get(key)

    async def set_with_ex(self, key: str, value: int, ex: int) -> None:
        await self.connection.set(key, value, ex=ex)

    async def delete(self, key: str) -> None:
        await self.connection.delete(key)

    async def exists(self, key: str) -> bool:
        return await self.connection.exists(key)
