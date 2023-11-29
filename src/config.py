import os
from dataclasses import dataclass

DB_INF_ENV = "DB_URI"
JWT_SECRET_ENV = "JWT_SECRET"


class ConfigParseError(ValueError):
    pass


@dataclass
class WebConfig:
    jwt_secret: str
    async_db_uri: str
    db_uri: str


def get_str_env(key) -> str:
    val = os.getenv(key)
    if not val:
        raise ConfigParseError(f"{key} is not set")
    return val


def load_web_config() -> WebConfig:
    jwt_secret = get_str_env(JWT_SECRET_ENV)
    async_db_uri = f"postgresql+asyncpg://{get_str_env(DB_INF_ENV)}"
    db_uri = f"postgresql://{get_str_env(DB_INF_ENV)}"
    return WebConfig(
        jwt_secret=jwt_secret,
        async_db_uri=async_db_uri,
        db_uri=db_uri,
    )
