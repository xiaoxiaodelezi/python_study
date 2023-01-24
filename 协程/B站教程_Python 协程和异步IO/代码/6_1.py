#定义异步中的协程函数
#将协程函数包装成task任务然后传入
#创建task方法1：使用loop.create_task方法

import asyncio, time


async def foo(x):
    print('start')
    await asyncio.sleep(x)
    print('finished')


loop = asyncio.get_event_loop()
task = loop.create_task(foo(3))
print(task)
loop.run_until_complete(task)
print(task)
