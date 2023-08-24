# coding: utf-8

from __future__ import annotations

from .base import BaseSettings, CONFIG_INFO


class Settings(BaseSettings):
    """配置类"""

    DEBUG: bool = False

    SECRET_KEY: str = 'wdATN(TPpSB-269m0Ayd9[H+^:/TZW;qkIJD8a:-K{'

    ACCESS_LOG: bool = False

    # 跨域相关
    ENABLE_CORS: bool = True
    CORS_SUPPORTS_CREDENTIALS: bool = True

    REDIS: str = f"redis://" \
                 f":{CONFIG_INFO['redis']['password']}" \
                 f"@{CONFIG_INFO['redis']['host']}" \
                 f":{CONFIG_INFO['redis']['port']}" \
                 f"/{CONFIG_INFO['redis']['database']}" \
                 f"?max_connections=50"
