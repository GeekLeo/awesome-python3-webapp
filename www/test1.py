#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm, asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.destory_pool()


async def find(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    rs = await User.findAll()
    print('查找测试： %s' % rs)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop), find(loop)]))
loop.close()
