from sanic import Request, HTTPResponse

from core.response import response_ok


async def demo1_view(request: Request) -> HTTPResponse:
    """
    测试视图
    :param request:
    :return:
    """
    return response_ok()
