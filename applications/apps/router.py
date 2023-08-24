from __future__ import annotations

from sanic import Blueprint

from .demo1.router import router as demo1_router
from .demo2.router import router as demo2_router


ROUTER_GROUP = Blueprint.group(demo1_router, demo2_router, url_prefix="/api")

