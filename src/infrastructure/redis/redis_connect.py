from typing import AsyncGenerator

from redis.asyncio import ConnectionPool, Redis

from src.core.config import config


def init_redis_pool() -> ConnectionPool:
    return ConnectionPool.from_url(
        config.REDIS_URL,
        decode_responses=True,
    )


async def close_redis_pool(redis_pool: ConnectionPool) -> None:
    await redis_pool.disconnect()


async def get_redis_session() -> AsyncGenerator[Redis, None]:
    redis_pool = init_redis_pool()
    redis = Redis(connection_pool=redis_pool)
    try:
        yield redis
    finally:
        await redis.close()
