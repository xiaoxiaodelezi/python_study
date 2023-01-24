#定义异步中的协程函数
#直接通过async定义协程函数并作为参数传入
import asyncio, time


async def foo(x):
    print('starting')
    await asyncio.sleep(x)
    print('finished')


loop = asyncio.get_event_loop()
loop.run_until_complete(foo(3))