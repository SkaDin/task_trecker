from fastapi_users.authentication import AuthenticationBackend, BearerTransport, RedisStrategy

from src.core.config import config
from src.infrastructure.redis.redis_connect import get_redis_session

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


async def get_redis_strategy() -> RedisStrategy:
    async for redis in get_redis_session():
        return RedisStrategy(redis, lifetime_seconds=config.TTL_REDIS, key_prefix=config.SECRET_KEY)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)
