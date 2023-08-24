# coding: utf-8

from __future__ import annotations

from sanic import Request, HTTPResponse
from tortoise.queryset import QuerySet

from applications.models import User
from core.error_code import ECEnum
from core.response import response_ok, response_fail
from libs.error_code.exception import ECException
from libs.logger import LoggerProxy

logger: LoggerProxy = LoggerProxy(__name__)


async def user_list(request: Request) -> HTTPResponse:
    """用户列表"""
    page: int = 1
    per_page: int = 5
    queryset: QuerySet = User.filter().order_by("-ctime", "-id"). \
        offset((page - 1) * per_page).limit(per_page)
    result: list = await queryset
    data = [{k: v for k, v in vars(obj).items() if not k.startswith("_")} for obj in result]
    # raise ECException(ECEnum.TestError)
    # return response_fail(enum=ECEnum.TestError)

    return response_ok(data=data)