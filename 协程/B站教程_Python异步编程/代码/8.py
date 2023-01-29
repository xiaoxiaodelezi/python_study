import asyncio


async def func():
    print('Come on')


result = func()

#python3.7以前
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result) #等同于loop.run_until_complete(func())

#python3.7
asyncio.run(result)