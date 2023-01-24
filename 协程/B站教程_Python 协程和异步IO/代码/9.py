# asyncio实现并发
import asyncio, time


async def do_work(x):
    print('waiting', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


coroutine1 = do_work(1)
coroutine2 = do_work(2)
coroutine3 = do_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(task.result())

print(time.time() - t1)
