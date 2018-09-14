#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'qiuyongheng'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# 首页
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

# 初始化
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # 创建server
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()