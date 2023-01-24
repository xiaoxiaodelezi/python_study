#获取异步中协程的返回值
#方法1：使用回调函数

import asyncio


async def foo(x):
    print('start')
    await asyncio.sleep(x)
    return 'Done for {}s'.format(x)


loop = asyncio.get_event_loop()
task = loop.create_task(foo(3))


def callback(future):
    print(future.result())


task.add_done_callback(callback)

loop.run_until_complete(task)
