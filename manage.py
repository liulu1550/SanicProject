# coding: utf-8

import os

from sanic import Sanic

from applications import create_app

app: Sanic = create_app(os.environ.get("ENV", "DEV"))  # 开发环境:DEV  生产环境: PRO


"""
数据库迁移更新命令

aerich init -t settings.base.TORTOISE      # 执行aerich初始化
aerich init-db                             # aerich初始化数据库
aerich migrate                             # 重新生成迁移文件
aerich upgrade                             # 重新执行迁移，写入数据库
aerich downgrade                           # 回到上一个版本
aerich history                             # 查看历史迁移记录
aerich heads                               # 查看形成当前版本的迁移记录文件
"""

if __name__ == '__main__':
    app.run(workers=1, port=8000, auto_reload=True)
