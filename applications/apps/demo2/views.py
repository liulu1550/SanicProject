from typing import Any

from aioredis import Redis
from sanic import Request, HTTPResponse

from core.response import response_ok
from utils import redis_utils
from utils.redis_utils import get_value, set_value


async def demo2_view(request: Request) -> HTTPResponse:
    """
    测试视图
    :param request:
    :return:
    """

    return response_ok()


async def get_redis_value(request):
    data = await get_value(request, "13")
    print(data)
    return response_ok()




async def set_redis_value(request):
    data = await set_value(request, "cheshi", 123, 20)
    return response_ok()