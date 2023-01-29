import asyncio


async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'


async def func():
    print('执行函数内部代码')

    response1 = await others()
    print('IO请求结束，结果为：', response1)

    #一个协程函数中可以有多个await，但只能依次执行
    response2 = await others()
    print('IO请求结束，结果为：', response2)


asyncio.run(func())