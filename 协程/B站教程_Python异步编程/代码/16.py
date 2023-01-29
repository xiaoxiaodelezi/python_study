import asyncio


async def set_after(fut):
    print('cc')
    await asyncio.sleep(2)
    fut.set_result('666')


async def main():
    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    await loop.create_task(set_after(fut))
    print('aa')
    data = await fut
    print('vv')
    print(data)


asyncio.run(main())