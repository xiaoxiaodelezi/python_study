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

