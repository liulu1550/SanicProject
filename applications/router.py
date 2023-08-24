# coding: utf-8

from __future__ import annotations

from sanic import Blueprint

from .auth.router import router as user_router
from .apps.router import ROUTER_TUPLE as apps_router

BLUE_TUPLE: tuple[Blueprint, ...] = (
                                        user_router,
                                    ) + apps_router
