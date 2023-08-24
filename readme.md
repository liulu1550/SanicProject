# Sanic 项目通用模板

[![pyversions](https://img.shields.io/badge/python%20-3.9%2B-blue.svg)]()
[![sanicversions](https://img.shields.io/badge/sanic-23.6.0-brightgreen.svg)]()
[![ver](https://img.shields.io/badge/release-v0.1-red.svg)]()
[![MIT](https://img.shields.io/badge/license-MIT-ff69b4.svg)]()

## 环境：
- Python >= 3.9
- sanic == 23.6.0
- aiomysql==0.2.0
- aioredis==2.0.1
- tortoise-orm == 0.20.0


```
.SanicProject
├── applications                       
│   ├── __init__.py                            # app模块
│   ├── models.py                              # 模型
│   ├── router.py                              # 总路由
│   ├── auth                                   # 用户模块
│   │   ├── __init__.py
│   │   ├── router.py           
│   │   └── views.py          
│   └── apps                                   # app子模块
│       ├── __init__.py
│       ├── router.py           
│       └── demo1                               
│           ├── __init__.py
│           ├── router.py
│           └── views.py
│       └── demo2
│           ├── __init__.py
│           ├── router.py
│           └── views.py
├── settings                  # 配置
│   ├── __init__.py           # 获取配置方法
│   ├── base.py               # 配置基类
│   ├── development.py        # 开发环境配置
│   └── production.py         # 生产环境配置
├── core
│   ├── error_code.py         # 错误码
│   ├── exception_handlers    # 异常处理器
│   │   ├── base.py           # 异常处理基类
│   │   ├── error_code.py     # 错误码异常处理
│   │   ├── __init__.py
│   │   └── unknown.py        # 未知异常处理
│   ├── __init__.py
│   ├── listeners             # 监听
│   │   ├── __init__.py
│   │   ├── base.py           # 监听基类
│   │   └── redis.py          # redis监听
│   ├── middlewares           # 中间件
│   │   ├── __init__.py
│   │   ├── base.py           # 中间件基类
│   │   ├── redis.py          # redis中间件
│   │   └── timer.py          # 计时中间件
│   └── response.py           # 响应函数
├── utils                      # 工具集
├── libs                      # 公共库
│   ├── config.py             # 配置文件处理方法
│   ├── error_code            # 错误码处理
│   │   ├── __init__.py
│   │   ├── enum.py           # 错误码枚举
│   │   └── exception.py      # 错误码异常
│   ├── __init__.py
│   ├── logger.py             # logger
│   └── secret_key.py         # 生成secret_key方法
├── logs                      # 日志文件存储路径
├── manage.py                 # 启动文件
├── .env                  # 配置文件模板
└── requirements.txt
```