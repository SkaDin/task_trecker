import redis.asyncio as aioredis

from src.core.config import config

redis = aioredis.from_url(config.REDIS_URL)
