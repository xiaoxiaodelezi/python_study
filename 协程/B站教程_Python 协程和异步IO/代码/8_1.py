#await 演示

import asyncio, time


async def foo(x):
    print('waiting', x)
    await asyncio.sleep(x)
    return 'done after {}s'.format(x)


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(foo(3))
loop.run_until_complete(task)
print(task.result())