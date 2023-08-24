# coding: utf-8

"""用户蓝图"""

from sanic import Blueprint

from .views import user_list


router: Blueprint = Blueprint('user', url_prefix='auth')


router.add_route(user_list, "/list", ('GET',))  # 用户列表
