# 协程的嵌套
# 在外层通过await asyncio.await(内层嵌套的协程)来使得程序等待内层协程完成

# 获取返回结果的第五种方式：
# 通过在外层协程中使用asyncio.as_completed(tasks)来获取结果

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

    #await 必须加在task前，而不是asyncio.as_completed前
    #await是必须的，不然main会提早结束
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)
 

t1 = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print(time.time() - t1)
