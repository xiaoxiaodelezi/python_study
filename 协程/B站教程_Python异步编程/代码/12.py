import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print('执行函数内部代码')

    #create以后立即加入事件循环中
    #被调用时运行，不在created位置卡住，而在await位置卡住
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    print('main 结束')
    #结果会出现再main结束这段文字之后
    #线程只在await位置卡住并等待切换
    ret1 = await task1

    ret2 = await task2

    print(ret1, ret2)


asyncio.run(main())