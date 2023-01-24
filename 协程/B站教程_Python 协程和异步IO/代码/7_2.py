#获取异步中协程的返回值
#方法2：在task完成后直接使用task.result()来调用协程中的返回

import asyncio


async def foo(x):
    print('start')
    await asyncio.sleep(x)
    return 'Done for {}s'.format(x)


loop = asyncio.get_event_loop()
task = loop.create_task(foo(3))

loop.run_until_complete(task)
print(task.result())
