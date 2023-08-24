import secrets


def generate_random_string(length=64):
    """
    :param length: 生成字符串的位数
    :return:
    """
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_string = ''.join(secrets.choice(charset) for _ in range(length))
    return random_string
