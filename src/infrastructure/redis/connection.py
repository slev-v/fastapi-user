import redis.asyncio as redis

from src.main.config import WebConfig


def create_redis_pool(config: WebConfig):
    return redis.ConnectionPool.from_url(config.redis_uri)


def new_redis_connection(redis_pool):
    return redis.Redis(connection_pool=redis_pool)
