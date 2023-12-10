import os
from dataclasses import dataclass

DB_URI_ENV = "DB_URI"
JWT_SECRET_ENV = "JWT_SECRET"
JWT_EXPIRE_TIME_ENV = "JWT_EXPIRE_TIME"
JWT_ALGORITHM_ENV = "JWT_ALGORITHM"


class ConfigParseError(ValueError):
    pass


@dataclass
class WebConfig:
    jwt_secret: str
    jwt_expire_time: int
    jwt_algorithm: str
    async_db_uri: str
    db_uri: str


def get_str_env(key) -> str:
    val = os.getenv(key)
    if not val:
        raise ConfigParseError(f"{key} is not set")
    return val


def load_web_config() -> WebConfig:
    jwt_secret = get_str_env(JWT_SECRET_ENV)
    jwt_expire_time = int(get_str_env(JWT_EXPIRE_TIME_ENV))
    jwt_algorithm = get_str_env(JWT_ALGORITHM_ENV)
    async_db_uri = f"postgresql+asyncpg://{get_str_env(DB_URI_ENV)}"
    db_uri = f"postgresql://{get_str_env(DB_URI_ENV)}"
    return WebConfig(
        jwt_secret=jwt_secret,
        jwt_expire_time=jwt_expire_time,
        jwt_algorithm=jwt_algorithm,
        async_db_uri=async_db_uri,
        db_uri=db_uri,
    )
