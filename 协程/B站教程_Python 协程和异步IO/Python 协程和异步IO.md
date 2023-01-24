# Python 协程和异步IO

B站地址：[Python 协程和异步IO_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1vE411F7Z9/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=eef98f9e120e9dac4c55f6547f221385)



## 1. 协程简介



## 2.yield的使用

有yield的函数会成为生成器函数

把yield看作是return

res=yield 4

先用next方法激活（不能给尚未激活的生成器函数发值），函数会运行到第一个yield处停留（只完成了yield右侧部分，左侧赋值等待下个send或者next方法）

如果使用next（.__next__)方法继续调用，res为None，函数运行到下一个yield右侧，或者程序结束返回stopiteration错误

如果使用send方法继续调用，res为send的参数，函数运行到下个yield右侧，或者程序结束返回stopiteration错误



## 3.yield实现生产者和消费者

使用send函数可以向协程函数发送数据

在生产者和消费者这个案例中，消费者是一个生成器函数，生产者是一个参数为生成器函数的函数。将逻辑中的后手设定为生成器函数，先手设定为带生成器函数参数的函数





## 4. 同步和异步的区别

同步：遇到阻塞，会一直等待，直到事务结束才会执行下一个

异步：遇到阻塞，直接执行第二个事务，不会等待，通过状态、通知、回调函数来处理结果

异步模块：asyncio

async修饰def定义函数，表示这个函数可以异步。调用不会立即执行，而是返回一个协程对象，一个coroutine

asyncio.sleep，异步中的等待

asyncio.get_event_loop

event_loop.run_until_complete(coroutine）



## 5.定义协程和异步

event_loop事件循环

coroutine 协程



## 6. 创建task任务

task 任务，对协程进一步封装

future 代表将来执行或没有执行的任务的结果，和task没有太多区别

task是future的子类

async/await python3.5关键字 async定义一个协程，await用于挂起阻塞的异步调用接口



## 7.绑定回调函数

给task绑定回调

task.add_done_callback(callback)来绑定

callback回调函数是一个带有参数future的函数

future.result()获取coroutine的return内容

方法1是通过给task绑定回调函数来展示task的return内容

方法2是task状态是finished时通过task.result来获取return内容



## 8.阻塞和await

await可以针对耗时操作进行挂起，函数让出控制权，挂起，直到再次轮到被唤醒



## 9.asyncio实现并发

并发和并行的区别

制作task列表：tasks列表包含多个task，每个task通过asyncio.ensure_future(coroutine)来创建

将列表传入：loop.run_until_complete(aysnoci.wait(list))

完成后遍历tasks列表获取单个task的返回值



## 10.协程的嵌套

```python
#内层协程
async def interior():
    pass

#外层协程
async def exterior():
    coroutine1=interior()
    coroutine2=interior()
    coroutine3=interior()
    
    将内层协程包装成外层的tasks
    tasks =[
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]
    
    #使用await来阻塞asyncio.wait(tasks)
    #不然外层协程会不等内层协程运行结束而直接终止，这样内层协程就没有返回结果
    #dones和pendings返回的两个时tasks的运行结果
	dones,pendings=await asyncio.wait(tasks)
    #通过对dones的循环来获取返回值
    for task in dones:
        print(task.result())

loop=asyncio.get_event_loop()
#创建后将外侧协程注册进循环
loop.run_until_complete(main())
    
```



获取嵌套的返回对象的方法

方法1和2都是在外层协程中获取返回结果

方法1：使用await asyncio.wait(tasks)返回dones和pendings两个值，遍历dones，使用done.result()来获取

方法2：使用await asyncio.gather(*tasks)返回result的集合，直接遍历获取值

方法3：将await asyncio.gather(*tasks)返回值作为外层协程的return值，然后在loop.run_until_complete(外层协程)中获取结果，循环结果取值

方法4：将await asyncio.wait(tasks)返回值作为外层协程的return值，然后在loop.run_until_complete(外层协程)中获取dones和pendings，循环dones，通过done.result()取值

方法5：通过在外层协程中使用asyncio.as_completed(tasks)来获取结果

```python
#await 必须加在task前，而不是asyncio.as_completed前
#await是必须的，不然main会提早结束
for task in asyncio.as_completed(tasks):
    result = await task
    print(result)
```

