import asyncio


class Reader(object):

    def __init__(self):
        self.count = 0

    #需要加async
    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    #需要加async
    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    #async for必须在async的函数中使用
    async for item in obj:
        print(item)


asyncio.run(func())