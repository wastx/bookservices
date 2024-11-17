from redis import asyncio as aioredis
from src.config import Config

redis_token_blocklist = aioredis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)

JTI_EXPIRY = 3600


async def add_jti(jti: str) -> None:
    await redis_token_blocklist.set(name=jti, value="", ex=JTI_EXPIRY)


async def token_in_blocklist(jti: str) -> bool:
    jti = await redis_token_blocklist.get(jti)
    return jti is not None











