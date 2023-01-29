import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print('执行函数内部代码')

    tasks = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2'),
    ]

    print('main 结束')

    #等待任务列表完成，返回元组
    done, pending = await asyncio.wait(tasks, timeout=None)

    print(done)


asyncio.run(main())