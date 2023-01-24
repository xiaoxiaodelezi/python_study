import time
import asyncio


def foo(x):
    print('starting')
    for i in range(2):
        print('cycling')
        time.sleep(x)
    print('finished')


t1 = time.time()
foo(3)
print(time.time() - t1)


#这里运行时间和上面没有区别
#异步包装的是async修饰的整体，而并非await的暂停
async def foo_(x):
    print('cycling')
    await asyncio.sleep(x)


loop = asyncio.get_event_loop()
t2 = time.time()
for i in range(2):
    loop.run_until_complete(foo_(3))
print(time.time() - t2)
