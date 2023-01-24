# 协程停止
# 协程没有嵌套时
import asyncio, time


async def do_work(x):
    print('waiting', x)
    await asyncio.sleep(x)
    return 'done in {}s'.format(x)


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
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(tasks)
    #和视频不同，直接循环调用task取消
    for task in tasks:
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print(time.time() - t1)
