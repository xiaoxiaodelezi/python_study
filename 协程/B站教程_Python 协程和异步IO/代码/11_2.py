# 协程停止
# 协程有嵌套时
import asyncio, time


async def do_work(x):
    print('waiting', x)
    await asyncio.sleep(x)
    return 'done in {}s'.format(x)


async def main():
    coroutine1 = do_work(1)
    coroutine2 = do_work(2)
    coroutine3 = do_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print(task.result())


t1 = time.time()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
try:
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    #暂时有问题，报错
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print(time.time() - t1)
