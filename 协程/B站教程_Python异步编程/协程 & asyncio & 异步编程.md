#	协程 & asyncio & 异步编程

B站课程：Python异步编程---协程 & asyncio & 异步

[01 课程介绍_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1hR4y1Y7Y1?p=1&vd_source=eef98f9e120e9dac4c55f6547f221385)



##	1.协程

协程不是计算机提供。程序员人为创造。

协程（Coroutine），也可以被称为微线程，是一种用户态的上下文切换技术。简而言之，其实就是通过一个线程实现代码相互切换执行，例如：

```python
def func1():
    print(1)

def func2():
    print(2)

func1()
func2()
```

实现协程的几种方法

- greenlet，早期模块
- yield关键字
- asyncio装饰器（3.4）
- async、await关键字（3.5）【推荐】



###	1.1 greenlet实现协程

```python
from greenlet import greenlet


def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch()
    print(4)


gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch()
'''
1
3
2
4
'''
```



###	1.2 yield 关键字

```python
def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)
'''
1
3
4
2
'''
```



###	1.3 asyncio

python3.4之后版本

```python
import asyncio


@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
'''
1
3
2
4
'''
```

遇到IO阻塞可以自动切换



###	1.4 async、await 关键字

python3.5之后版本

```python
import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
'''
1
3
2
4
'''
```



##	2. 协程的意义

在一个线程中如果遇到IO等待时间，线程不会等待，利用空闲时间的时候再去干点其他事情。

案例：下载图片（网络IO）

- 普通方式（同步）

  ```python
  import requests
  
  
  def download_image(url):
      print('start')
      response = requests.get(url)
      file_name = url.rsplit('-')[-1]
      with open(file_name, mode='wb') as file_object:
          file_object.write(response.content)
      print('close')
  
  
  if __name__ == '__main__':
      url_list = []
      for item in url_list:
          download_image(item)
  ```

- 协程方式（异步）

  ```python
  import aiohttp, asyncio
  
  
  async def fetch(session, url):
      print('发送请求', url)
      async with session.get(url, verify_ssl=False) as response:
          content = await response.content.read()
          file_name = url.rsplit('-')[-1]
          with open(file_name, mode='wb') as file_object:
              file_object.write(content)
  
  
  async def main():
      async with aiohttp.ClientSession() as session:
          url_list = []
          tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
          await asyncio.wait(tasks)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```



##	3.异步编程

###	3.1 事件循环

理解成一个死循环，去检测并测试执行某些代码

```python
# 伪代码

任务列表=[任务1，任务2，任务3]

while True:
    可执行的任务列表，已完成的任务列表=去任务列表中检查所有的任务，将"可执行"和"已完成"的任务返回
    
    for 就绪任务 in 已准备就绪的任务列表:
    	执行已就绪的任务
        
    for 已完成的任务 in 已完成的任务列表:
        在任务列表中移除已完成的任务
        
    如果任务列表中的任务都已完成，终止循环
    	
```

```python
import asyncio

#去生成或获取一个事件循环
loop = asyncio.get_event_loop()
#将任务放到任务列表中
loop.run_until_complete(任务)
```



###	3.2 快速上手

协程函数是指定义函数时使用async def 函数名的方式。

协程对象是指执行协程函数()得到的对象。

```python
async def func():
    pass

result =  func()
```

注意：执行协程函数创建的对象，函数内部的代码不会执行

如果想要执行协程函数内部代码，必须要将协程对象交给事件循环来处理

```python
import asyncio

async def func():
    print('Come on')

result =  func()

#python3.7以前
loop = asyncio.get_event_loop()
loop.run_until_complete(result) #等同于loop.run_until_complete(func())

#python3.7
asyncio.run(result)
```



###	3.3 await 关键字

await+可等待的对象（协程对象，Future对象和Task对象等类似IO等待的对象）

示例1：

```python
import asyncio


async def func():
    print('come')
    response = await asyncio.sleep(2)
    print('结束', response)


asyncio.run(func())
```

示例2：

```python
import asyncio


async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'


async def func():
    print('执行函数内部代码')
	
    #遇到IO操作挂起当前协程，等IO操作完成后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程任务
    response = await others()

    print('IO请求结束，结果为：', response)


asyncio.run(func())
```

示例3：

```python
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
```

await就是等待对象的值得到结果后再继续往下走



### 3.4 Task对象

task是被用来并发地排定协程时间

当协程被通过诸如函数asyncio.create_task()来包装成一个Task，协程自动会被排定运行时间

本质上Task是帮住我们在事件循环中添加多个任务

包装协程成为Task对象的还有loop.create_task()或者ensure_future()函数。不建议手动实例化task对象

python3.7以前使用ensure_future



示例1：

```python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print('执行函数内部代码')

    #create以后立即加入事件循环中
    #被调用时运行，不在created位置卡住，而在await位置卡住
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    print('main 结束')
    #结果会出现再main结束这段文字之后
    #线程只在await位置卡住并等待切换
    ret1 = await task1

    ret2 = await task2

    print(ret1, ret2)


asyncio.run(main())
```



示例2：

```python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print('执行函数内部代码')

    #将任务添加到任务列表，name参数指定任务名称
    tasks = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2'),
    ]

    print('main 结束')

    #等待任务列表完成，返回元组
    #done表示所有完成任务的集合，pending表示尚未完成的
    #timeout参数表示等待时间
    done, pending = await asyncio.wait(tasks, timeout=None)

    
    print(done)


asyncio.run(main())
```



示例3：

```python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


tasks_list = [
    func(),
    func(),
]

asyncio.run(asyncio.wait(tasks_list))
```

tasks_list当出现在协程函数外时，不能使用create_task，因为这个时候循环还没有创建，会报错

只能以协程函数列表的形式直接传给asyncio.wait，会自动包装成一个任务列表



### 3.5 Future对象

Future是一个特殊的底层可等待对象，用来代表一个同步运行的最终结果

Future是Task的基类，Task内部await结果的处理基于Future对象来的

示例1：

```python
import asyncio


async def main():
    #获取当前事件循环
    loop = asyncio.get_running_loop()

    #创建一个任务（future对象），这个任务什么都不干
    fut = loop.create_future()

    #等待任务的最终结果（future对象），没有结果会一直等下去
    await fut


asyncio.run(main())
```

