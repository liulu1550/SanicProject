import random
import re
import secrets


def generate_random_string(length=64):
    """
    :param length: 生成字符串的位数
    :return:
    """
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_string = ''.join(secrets.choice(charset) for _ in range(length))
    return random_string


def is_valid_mobile(phonenum):
    """
    验证是否手机号
    :param phonenum:
    :return:
    """
    pattern = re.compile(r'^((13[0-9])|(14([0-1]|[4-9]))|(15([0-3]|[5-9]))|(16(2|[5-7]))|(17[1-9])|(18[0-9])|(19[0|1|3])|(19[5-9]))\d{8}$')
    match = pattern.match(phonenum)
    return bool(match)


async def generate_code():
    """
    生成四位数字的验证码
    """
    seeds = "1234567890"
    random_str = []
    for i in range(6):
        random_str.append(random.choice(seeds))

    return "".join(random_str)