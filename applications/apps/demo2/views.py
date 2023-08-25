from sanic import Request, HTTPResponse

from core.response import json_success_response
from utils.request_utils import get_request_location, get_real_ip, get_browser_name, get_os


async def demo2_view(request: Request) -> HTTPResponse:
    """
    测试视图
    :param request:
    :return:
    """

    return json_success_response()


async def get_location(request):
    data1 = await get_request_location(request)
    data2 = await get_real_ip(request)
    data3 = await get_browser_name(request)
    data4 = await get_os(request)
    print(type(data1))
    data = {
        "data1":data1,
        "data2":data2,
        "data3":data3,
        "data4":data4,
    }
    return json_success_response(data)
