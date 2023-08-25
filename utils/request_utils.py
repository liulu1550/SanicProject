import httpx
from user_agents import parse


async def get_real_ip(request):
    """
    获取请求的真实IP
    :param request:
    :return:
    """
    x_forwarded_for = request.headers.get('X-Forwarded-For')

    if x_forwarded_for:
        real_ip = x_forwarded_for.split(',')[0]
    else:
        real_ip = request.ip
    return real_ip


async def get_param(request, param_name):
    """
    获取POST请求参数
    :param request:
    :param param_name:
    :return:
    """
    if param_name in request.form:
        return request.form[param_name]
    elif param_name in request.json:
        return request.json[param_name]
    else:
        return None


async def get_browser_name(request):
    """
    获取浏览器名
    :param request:
    :return:
    """
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    return user_agent.browser.family


async def get_os(request):
    """
    获取操作系统
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    return user_agent.os.family


async def get_request_location(request):
    """
    获取请求IP地理位置信息
    :param request:
    :return:
    """
    ip = await get_real_ip(request)
    url = f"http://whois.pconline.com.cn/ip.jsp?ip={ip}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.text.replace("\n","")
    except:
        return ""
