# coding: utf-8

from __future__ import annotations

import os

from libs.config import Config

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR, 'logs')

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

# 配置信息
CONFIG_INFO = Config(os.path.join(BASE_DIR, '.env')).format()



TORTOISE: dict = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": CONFIG_INFO["db"]["host"],
                "port": CONFIG_INFO["db"]["port"],
                "user": CONFIG_INFO["db"]["user"],
                "password": CONFIG_INFO["db"]["password"],
                "database": CONFIG_INFO["db"]["database"],
                "maxsize": 5,
                # 注意：启动时直接创建5个session
                "minsize": 5,
                # 回收时间，每次获取session时判断，如果超时，全部重新创建
                "pool_recycle": 60 * 60 * 2,
                # 设置事务隔离级别为RC
                "init_command": "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED",
            }
        }
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "applications.models"],  # aerich.models是必填，后面的models填自己创建的models路径
            "default_connection": "default",
        }
    },
    "use_tz": False,
    # set session time_zone
    "timezone": "Asia/Shanghai",
}


class BaseSettings:
    """配置基类"""

    DEBUG: bool = True

    # 随机秘钥
    SECRET_KEY: str

    # 关闭可提高性能
    ACCESS_LOG: bool = True

    # 跨域相关
    ENABLE_CORS: bool = False
    CORS_SUPPORTS_CREDENTIALS: bool = False

    # 日志配置
    BASE_LOGGING: dict = {
        'version': 1,
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['console', 'info_file', 'error_file'],
                'propagate': False
            },
            'sanic': {
                'level': 'INFO',
                'handlers': ['console', 'info_file', 'error_file'],
                'propagate': False
            },
        },
        'formatters': {
            'default': {
                'format': '[%(asctime)s.%(msecs).3d] - [%(levelname)s] - [%(name)s:%(lineno)d] - [%(message)s]',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'info_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'info.log'),
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'INFO',
                'formatter': 'default',
            },
            'error_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'error.log'),
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'ERROR',
                'formatter': 'default',
            },
        },
    }

    # tortoise
    TORTOISE: dict = TORTOISE

    # redis
    REDIS: str


