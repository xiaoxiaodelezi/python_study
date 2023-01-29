import asyncio


async def func():
    print('come')
    response = await asyncio.sleep(2)
    print('结束', response)


asyncio.run(func())