# 协程的嵌套
# 在外层通过await asyncio.await(内层嵌套的协程)来使得程序等待内层协程完成

# 获取返回结果的第三种方式：
# await asyncio.gather(*tasks)作为main的返回值直接返回到调用异步的run_until_complete的结果
# 遍历results获取结果

import asyncio, time


async def do_work(x):
    print('waiting:', x)
    await asyncio.sleep(x)
    return 'Done after{}s'.format(x)


async def main():
    coroutine1 = do_work(1)
    coroutine2 = do_work(2)
    coroutine3 = do_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    return await asyncio.gather(*tasks)


t1 = time.time()

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())
for result in results:
    print(result)

print(time.time() - t1)
