from typing import Any

from aioredis import Redis
from sanic import request, Request


async def get_value(request: Request, key: str) -> Any:
    """
    过去redis中的值
    :param request:
    :param key:
    :return:
    """

    redis_client: Redis = request.ctx.redis_client
    value = await redis_client.get(key)
    if value:
        value = value.decode()
    return value


async def set_value(request: Request, key: str, value: Any, exp: int) -> Any:
    """
    设置值
    :param request:
    :param key: 键
    :param value: 值
    :param exp: 过期时间
    :return:
    """

    redis_client: Redis = request.ctx.redis_client
    await redis_client.set(key, value, exp)

