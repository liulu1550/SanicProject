# coding: utf-8

from libs.error_code.enum import BaseECEnum, ECData


class ECEnum(BaseECEnum):
    """错误码枚举类"""
    ServerError = ECData("500", "服务异常，请稍后重试")

    TestError = ECData("TEST", "测试错误")

    RequestError = ECData("4000", "请求错误")

    OperationError = ECData("4001", "操作错误")

    ParamsError = ECData("4002", "参数错误")

    NotFoundError = ECData("40004", "未找到相应数据")

    LimitError = ECData("40029", "已锁定")


