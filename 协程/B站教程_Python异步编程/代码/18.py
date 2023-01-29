import time
import asyncio
import concurrent.futures


def func1():
    time.sleep(2)
    return 'SB'


async def main():
    loop = asyncio.get_running_loop()

    #1.run in the default loop's executor（默认threadpoolexecutor）
    #第一步：内部会先调用Threadpoolexecutor的submit方法去线程池中申请一个线程去执行func1函数
    #返回一个concurrent.futures.Futures对象
    #第二步：调用asyncio.wrap_future方法将concurrent.futures.Future对象
    #包装为asyncio.Future对象
    #因为concurrent.futures.Future对象不支持await语法，所以需要包装
    fut = loop.run_in_executor(None, func1)
    #包装后的fut可以使用await
    result = await fut
    print('default thread poo1', result)

    # 2.run in custom thread pool"
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print('custom thread pool', result)

    # 3.run in a custom process pool
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print('custom process pool', result)


asyncio.run(main)