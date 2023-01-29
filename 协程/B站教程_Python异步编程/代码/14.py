import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


tasks_list = [
    func(),
    func(),
]

asyncio.run(asyncio.wait(tasks_list))