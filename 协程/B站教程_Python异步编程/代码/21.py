import asyncio


class AsyncContextManager:

    def __init__(self):
        self.conn = conn

    async def do_something(self):
        return 666

    async def __aenter__(self):
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self):
        await asyncio.sleep(1)


obj = AsyncContextManager()


#async with必须嵌套在一个async函数中
async def func():
    async with obj as f:
        result = await f.do_somthing()
        print(result)


asyncio.run(func())