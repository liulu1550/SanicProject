# coding: utf-8

from __future__ import annotations

from sanic import Blueprint

from .auth.router import router as user_router
from .apps.router import ROUTER_GROUP as APP_ROUTER_GROUP

ROUTER_GROUP = Blueprint.group(user_router, APP_ROUTER_GROUP)

