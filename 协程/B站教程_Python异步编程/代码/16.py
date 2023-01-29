import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')


async def main():
    loop = asyncio.get_running_loop()

    #创建一个任务（future对象），没有绑定任何行为，这个任务永远不会结束
    fut = loop.create_future()
    
    #将fut这个future作为参数传给set_after，返回一个绑定行为的future
    #并将这个future对象传给create_task，创建task
    await loop.create_task(set_after(fut))

    #等待fut获取结果
    data = await fut
    print(data)


asyncio.run(main())