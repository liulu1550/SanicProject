# coding: utf-8

from __future__ import annotations

from .base import BaseSettings, CONFIG_INFO


class Settings(BaseSettings):
    """配置类"""

    SECRET_KEY: str = "*5}nAn#4GyQVO'*qq_2AAOC\\fXsvi9;m0.-Q|#jAcS"

    # 跨域相关
    ENABLE_CORS: bool = False
    CORS_SUPPORTS_CREDENTIALS: bool = False

    REDIS: str = f"redis://" \
                 f":{CONFIG_INFO['redis']['password']}" \
                 f"@{CONFIG_INFO['redis']['host']}" \
                 f":{CONFIG_INFO['redis']['port']}" \
                 f"/{CONFIG_INFO['redis']['database']}" \
                 f"?max_connections=10"


