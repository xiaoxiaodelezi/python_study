# [`asyncio`](https://docs.python.org/zh-cn/3/library/asyncio.html#module-asyncio) --- 异步 I/O

asyncio 是用来编写 **并发** 代码的库，使用 **async/await** 语法。

asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

asyncio 往往是构建 IO 密集型和高层级 **结构化** 网络代码的最佳选择。

asyncio 提供一组 **高层级** API 用于:

- 并发地 [运行 Python 协程](https://docs.python.org/zh-cn/3/library/asyncio-task.html#coroutine) 并对其执行过程实现完全控制;
- 执行 [网络 IO 和 IPC](https://docs.python.org/zh-cn/3/library/asyncio-stream.html#asyncio-streams);
- 控制 [子进程](https://docs.python.org/zh-cn/3/library/asyncio-subprocess.html#asyncio-subprocess);
- 通过 [队列](https://docs.python.org/zh-cn/3/library/asyncio-queue.html#asyncio-queues) 实现分布式任务;
- [同步](https://docs.python.org/zh-cn/3/library/asyncio-sync.html#asyncio-sync) 并发代码;

此外，还有一些 **低层级** API 以支持 *库和框架的开发者* 实现:

- 创建和管理 [事件循环](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio-event-loop)，以提供异步 API 用于 [`网络化`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.loop.create_server), 运行 [`子进程`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec)，处理 [`OS 信号`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler) 等等;
- 使用 [transports](https://docs.python.org/zh-cn/3/library/asyncio-protocol.html#asyncio-transports-protocols) 实现高效率协议;
- 通过 async/await 语法 [桥接](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio-futures) 基于回调的库和代码。

你可以在REPL中尝试一个asyncio并发环境：

```
$ python -m asyncio
asyncio REPL ...
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
'hello'
```

[Availability](https://docs.python.org/zh-cn/3/library/intro.html#availability): not Emscripten, not WASI.

可用性：不是编译器，不是WASI



参考

高层级 API

- [Runners](https://docs.python.org/zh-cn/3/library/asyncio-runner.html)
- [协程与任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html)
- [流](https://docs.python.org/zh-cn/3/library/asyncio-stream.html)
- [同步原语](https://docs.python.org/zh-cn/3/library/asyncio-sync.html)
- [子进程集](https://docs.python.org/zh-cn/3/library/asyncio-subprocess.html)
- [队列集](https://docs.python.org/zh-cn/3/library/asyncio-queue.html)
- [异常](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html)

低层级 API

- [事件循环](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html)
- [Futures](https://docs.python.org/zh-cn/3/library/asyncio-future.html)
- [传输和协议](https://docs.python.org/zh-cn/3/library/asyncio-protocol.html)
- [策略](https://docs.python.org/zh-cn/3/library/asyncio-policy.html)
- [平台支持](https://docs.python.org/zh-cn/3/library/asyncio-platforms.html)
- [Extending](https://docs.python.org/zh-cn/3/library/asyncio-extending.html)

指南与教程

- [高层级 API 索引](https://docs.python.org/zh-cn/3/library/asyncio-api-index.html)
- [低层级 API 索引](https://docs.python.org/zh-cn/3/library/asyncio-llapi-index.html)
- [用 asyncio 开发](https://docs.python.org/zh-cn/3/library/asyncio-dev.html)

备注：asyncio 的源代码可以在 [Lib/asyncio/](https://github.com/python/cpython/tree/3.11/Lib/asyncio/) 中找到。



# 协程与任务

本节将简述用于协程与任务的高层级 API。

- [协程](https://docs.python.org/zh-cn/3/library/asyncio-task.html#coroutines)
- [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#awaitables)
- [创建任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html#creating-tasks)
- [Task Cancellation](https://docs.python.org/zh-cn/3/library/asyncio-task.html#task-cancellation)
- [Task Groups](https://docs.python.org/zh-cn/3/library/asyncio-task.html#task-groups)
- [休眠](https://docs.python.org/zh-cn/3/library/asyncio-task.html#sleeping)
- [并发运行任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html#running-tasks-concurrently)
- [屏蔽取消操作](https://docs.python.org/zh-cn/3/library/asyncio-task.html#shielding-from-cancellation)
- [超时](https://docs.python.org/zh-cn/3/library/asyncio-task.html#timeouts)
- [简单等待](https://docs.python.org/zh-cn/3/library/asyncio-task.html#waiting-primitives)
- [在线程中运行](https://docs.python.org/zh-cn/3/library/asyncio-task.html#running-in-threads)
- [跨线程调度](https://docs.python.org/zh-cn/3/library/asyncio-task.html#scheduling-from-other-threads)
- [内省](https://docs.python.org/zh-cn/3/library/asyncio-task.html#introspection)
- [Task 对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#task-object)





## [协程](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id2)

**Source code:** [Lib/asyncio/coroutines.py](https://github.com/python/cpython/tree/3.11/Lib/asyncio/coroutines.py)

------

通过 async/await 语法来声明 [协程](https://docs.python.org/zh-cn/3/glossary.html#term-coroutine) 是编写 asyncio 应用的推荐方式。 例如，以下代码段会打印 "hello"，等待 1 秒，再打印 "world":

```
>>> import asyncio

>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')

>>> asyncio.run(main())
hello
world
```

注意：简单地调用一个协程并不会使其被调度执行

```
>>> main()
<coroutine object main at 0x1053bb7c8>
```

为了确实运行协程，asyncio提供了下面的机制：

- [`asyncio.run()`](https://docs.python.org/zh-cn/3/library/asyncio-runner.html#asyncio.run) 函数用来运行最高层级的入口点 "main()" 函数 (参见上面的示例。)

- 等待一个协程。以下代码段会在等待 1 秒后打印 "hello"，然后 *再次* 等待 2 秒后打印 "world":

  ```python
  import asyncio
  import time
  
  async def say_after(delay, what):
      await asyncio.sleep(delay)
      print(what)
  
  async def main():
      print(f"started at {time.strftime('%X')}")
  
      #一个协程函数中有2个await后直接加协程函数的情况，不会并行
      #整个函数的完成时间是3秒
      await say_after(1, 'hello')
      await say_after(2, 'world')
  
      print(f"finished at {time.strftime('%X')}")
  
  asyncio.run(main())
  ```

  预期的输出:

  ```
  started at 17:13:52
  hello
  world
  finished at 17:13:55
  ```

- [`asyncio.create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task) 函数用来并发运行作为 asyncio [`任务`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 的多个协程。

  让我们修改以上示例，*并发* 运行两个 `say_after` 协程:

  ```python
  async def main():
  
  	#将协程函数包装成task以后，在await后面调用，可以并行
  	#整个程序完成时间是2秒
      task1 = asyncio.create_task(
          say_after(1, 'hello'))
  
      task2 = asyncio.create_task(
          say_after(2, 'world'))
  
      print(f"started at {time.strftime('%X')}")
  
      # await等待两个task全部完成（预计2秒）
      await task1
      await task2
  
      print(f"finished at {time.strftime('%X')}")
  ```

  注意，预期的输出显示代码段的运行时间比之前快了 1 秒:

  ```
  started at 17:14:32
  hello
  world
  finished at 17:14:34
  ```

-  [`asyncio.TaskGroup`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.TaskGroup) 类通过一种更现代化的可选方式来 [`create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task)。使用API后，上个例子变为下面的样子：

  ```python
  async def main():
  	#使用taskgroup创建一个asyncio的组类实例
      async with asyncio.TaskGroup() as tg:
      	#调用实例的create_task方法来向组内添加任务
          task1 = tg.create_task(
              say_after(1, 'hello'))
  
          task2 = tg.create_task(
              say_after(2, 'world'))
  
          print(f"started at {time.strftime('%X')}")
  
      # wait被隐式包含在上下文管理器中的退出中.
  
      print(f"finished at {time.strftime('%X')}")
  ```

  运行时间和输出和上个版本一致.

  *3.11 新版功能:* [`asyncio.TaskGroup`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.TaskGroup).

## [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id3)

如果一个对象可以在 [`await`](https://docs.python.org/zh-cn/3/reference/expressions.html#await) 语句中使用，那么它就是 **可等待** 对象。许多 asyncio API 都被设计为接受可等待对象。

*可等待* 对象有三种主要类型: **协程**, **任务** 和 **Future**.

协程

Python 协程属于 *可等待* 对象，因此可以在其他协程中被等待:

```
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```

重要

 

在本文档中 "协程" 可用来表示两个紧密关联的概念:

- *协程函数*: 定义形式为 [`async def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-def) 的函数;
- *协程对象*: 调用 *协程函数* 所返回的对象。

任务

*任务* 被用来“并行的”调度协程

当一个协程通过 [`asyncio.create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task) 等函数被封装为一个 *任务*，该协程会被自动调度执行:

```python
import asyncio

async def nested():
    return 42

async def main():
    # 通过main()调用来排定nested()的不久后并发运行时间
    task = asyncio.create_task(nested())

    #通过"task"可以被用来取消"nested()"，或者可以简单的使用await task来等待它直到完成
    await task

asyncio.run(main())
```

Futures

[`Future`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future) 是一种特殊的 **低层级** 可等待对象，表示一个异步操作的 **最终结果**。

当一个 Future 对象 *被等待*，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。

通常情况下 **没有必要** 在应用层级的代码中创建 Future 对象。

Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:

```
async def main():
	#等待一个future对象完成
    await function_that_returns_a_future_object()

    # 一个future对象和另一个协程函数并列收集在一起也是可以的:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

一个很好的返回对象的低层级函数的示例是 [`loop.run_in_executor()`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)。



## [创建任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id4)

**Source code:** [Lib/asyncio/tasks.py](https://github.com/python/cpython/tree/3.11/Lib/asyncio/tasks.py)

------

- asyncio.**create_task**(*coro*, *, *name=None*, *context=None*)

  将 *coro* [协程](https://docs.python.org/zh-cn/3/library/asyncio-task.html#coroutine) 封装为一个 [`Task`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 并调度其执行。

  返回 Task 对象。*name* 不为 `None`，它将使用 [`Task.set_name()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.set_name) 来设为任务的名称。

  context这个可选关键字允许指定一个定制的[`contextvars.Context`](https://docs.python.org/zh-cn/3/library/contextvars.html#contextvars.Context) 来让协程在其中运行。如果不提供，回复制当前上下文并创建。

  该任务会在 [`get_running_loop()`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.get_running_loop) 返回的循环中执行，如果当前线程没有在运行的循环则会引发 [`RuntimeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#RuntimeError)。

  备注 ：[`asyncio.TaskGroup.create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.TaskGroup.create_task) 是一个新的允许等待一组相关任务的方便的可选方法。

  重要：保存对于这组数结果的引用，避免任务在运行过程中消失。事件循环对于任务是弱引用，一个任务如果没有被其他地方引用，也许会被GC随时回收，这甚至可能发生在任务完成前。为了保证那些注册后就不观察的任务存在，将它们收集在一个容器中：

  ```python
  background_tasks = set()
  
  for i in range(10):
      task = asyncio.create_task(some_coro(param=i))
  
      # 将这个任务加到一个set中，这样task会成为强引用
      background_tasks.add(task)
  
  
      #为了避免在任务结束后还持有引用导致无法回收，在每个任务结束后移出set
      task.add_done_callback(background_tasks.discard)
  ```

  *3.7 新版功能.*

  在 3.8 版更改：添加了 *name* 形参。 

  在 3.11 版更改：增加了context参数.

  

  

## [Task Cancellation](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id5)

  任务可以被简单和安全地取消。任务被取消时，[`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 会在下次任务调用时产生。

  推荐使用try/finally模块来增强清理逻辑地编程。这样 [`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 可以被显式捕获这样就可以在清理程序完成以后更加好地拓展。绝大部分代码都可以安全地忽略 [`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError)。

  那些开启结构并发地aysncio内容，比如[`asyncio.TaskGroup`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.TaskGroup) 和 [`asyncio.timeout()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.timeout)被设计成使用自己的取消方式。如果协程自己解析了 [`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError)，可能会导致程序运行的不确定。同样，用户代码不应该调用 [`uncancel`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel).

  

## [Task Groups](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id6)

  Task groups combine a task creation API with a convenient and reliable way to wait for all tasks in the group to finish.

  任务组提供一个便捷可靠的API方法来等任务组中的所有任务完成

  - *class* asyncio.**TaskGroup**

    一个[asynchronous context manager](https://docs.python.org/zh-cn/3/reference/datamodel.html#async-context-managers) （异步上下文管理器）控制着整个任务组。任务可以被通过 [`create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task)添加进组。所有任务在上下文管理器退出后都会await。

    *3.11 新版功能.*

    ***create_task**(*coro,*, *name=None*, *context=None*)在这个任务组中增加一个任务。参数签名和 [`asyncio.create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task)一致。

  示例:

  ```python
  async def main():
      #async with 只能存在在要给协程函数中
      async with asyncio.TaskGroup() as tg:
          task1 = tg.create_task(some_coro(...))
          task2 = tg.create_task(another_coro(...))
      print("Both tasks have completed now.")
  ```

   `async with` 会等待所有组中的任务完成。在等待过程中，新的任务可以被加入（比如，通过传递tg到其中一个协程中，在那个协程中调用 `tg.create_task()` ）。一旦最后的任务完成了，  `async with` 模块会退出，就不能有新的任务加入了。

  当属于任务组中的任何任务第一次出现[`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError)时，组中剩余的所有任务都会取消，也不能添加更多的任务。此时，如果 `async with`语句依旧运行中（也就是 [`__aexit__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aexit__) 还没有被调用)直接包含这个任务的 `async with` 语句也会被取消。作为结果的 [`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 错误会打断一个await，不过不会上浮到包含它的 `async with` 语句中。

  Once all tasks have finished, if any tasks have failed with an exception other than 

  当所有任务完成，如果一个任务由于非[`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError)导致了运行失败，这些错误会结合在 [`ExceptionGroup`](https://docs.python.org/zh-cn/3/library/exceptions.html#ExceptionGroup) 或者 [`BaseExceptionGroup`](https://docs.python.org/zh-cn/3/library/exceptions.html#BaseExceptionGroup) (推荐阅读这两个类的文档) 被提出。

  这两个错误会被特殊对待：如果任务由于 [`KeyboardInterrupt`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyboardInterrupt) 或者 [`SystemExit`](https://docs.python.org/zh-cn/3/library/exceptions.html#SystemExit)，任务组依旧会取消剩下的任务然后等待它们，不过最初的 [`KeyboardInterrupt`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyboardInterrupt) 或者 [`SystemExit`](https://docs.python.org/zh-cn/3/library/exceptions.html#SystemExit) 会被再次提出，而不是 [`ExceptionGroup`](https://docs.python.org/zh-cn/3/library/exceptions.html#ExceptionGroup) 或者 [`BaseExceptionGroup`](https://docs.python.org/zh-cn/3/library/exceptions.html#BaseExceptionGroup)。

  如果 `async with` 语句的主题由于一个错误（ [`__aexit__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aexit__)被一个错误set调用）退出，这等同于任务组中的一个任务失败：剩余的任务会被取消，然后等待，一个非取消错误会被包装进一个错误组然后提出。 错误会被传入 [`__aexit__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aexit__), 除非它是[`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError), 也会被包含在错误组中。 和前文提及的一样，相同的特殊操作也适用于 [`KeyboardInterrupt`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyboardInterrupt) 和 [`SystemExit`](https://docs.python.org/zh-cn/3/library/exceptions.html#SystemExit) 。

  

## [休眠](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id7)

*coroutine* asyncio.**sleep**(*delay*, *result=None*)

​	阻塞 *delay* 指定的秒数。

​	如果指定了 *result*，则当协程完成时将其返回给调用者。

​	`sleep()` 总是会挂起当前任务，以允许其他任务运行。

​	将 delay 设为 0 将提供一个经优化的路径以允许其他任务运行。 这可供长期间运行的函数使用以避免在函数调	用的全过程中阻塞事件循环。

​	以下协程示例运行 5 秒，每秒显示一次当前日期:

    import asyncio
    import datetime
    
    async def display_date():
        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0
        while True:
            print(datetime.datetime.now())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)
    
    asyncio.run(display_date())


​	*在 3.10 版更改:* 移除了 *loop* 形参。



## [并发运行任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id8)

*awaitable* asyncio.**gather**(**aws*, *return_exceptions=False*)

​	*并发* 运行 *aws* 序列中的 [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables)。

​	如果 *aws* 中的某个可等待对象为协程，它将自动被作为一个任务调度。

​	如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 *aws* 中可等待	对象的顺序一致。

​	如果 *return_exceptions* 为 `False` (默认)，所引发的首个异常会立即传播给等待 `gather()` 的任务。*aws* 序列中	的其他可等待对象 **不会被取消** 并将继续运行。

​	如果 *return_exceptions* 为 `True`，异常会和成功的结果一样处理，并聚合至结果列表。

​	如果 `gather()` *被取消*，所有被提交 (尚未完成) 的可等待对象也会 *被取消*。

​	如果 *aws* 序列中的任一 Task 或 Future 对象 *被取消*，它将被当作引发了 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 一样处理 -- 在此情	况下 `gather()` 调用 **不会** 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也	被取消。

​	备注：一个更加新的创建和运行并发任务和等待其完成的方法时使用 [`asyncio.TaskGroup`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.TaskGroup)。

​	示例:

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]
```

备注：如果 *return_exceptions* 为 False，则在 gather() 被标记为已完成后取消它将不会取消任何已提交的可等待对象。 例如，在将一个异常传播给调用者之后，gather 可被标记为已完成，因此，在从 gather 捕获一个（由可等待对象所引发的）异常之后调用 `gather.cancel()` 将不会取消任何其他可等待对象。



## [屏蔽取消操作](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id9)

*awaitable* asyncio.**shield**(*aw*)

​	保护一个 [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables) 防止其被 [`取消`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel)。

​	如果 *aw* 是一个协程，它将自动被作为任务调度。

​	以下语句:

```python
task = asyncio.create_task(something())
res = await shield(task)
```

​	相当于:

```python
res = await something()
```

​	*不同之处* 在于如果包含它的协程被取消，在 `something()` 中运行的任务不会被取消。从 `something()` 的角	度看来，取消操作并没有发生。然而其调用者已被取消，因此 "await" 表达式仍然会引发 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError)。

​	如果通过其他方式取消 `something()` (例如在其内部操作) 则 `shield()` 也会取消。

​	如果希望完全忽略取消操作 (不推荐) 则 `shield()` 函数需要配合一个 try/except 代码段，如下所示:

```python
task = asyncio.create_task(something())
try:
    res = await shield(task)
except CancelledError:
    res = None
```

重要：对于传给这个函数的引用要额外保存，避免task在执行过程消失。事件循环只能保留对task的弱引用。task如果没有被其他地方引用，可能会随时被GC回收，甚至发生在task完成前。

*在 3.10 版更改:* 移除了 *loop* 形参。

*3.10 版后已移除:* 如果 *aw* 不是 Future 类对象并且没有正在运行的事件循环则会发出弃用警告。



## [超时](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id10)

*coroutine* asyncio.**timeout**(*delay*)

​	一个 [asynchronous context manager](https://docs.python.org/zh-cn/3/reference/datamodel.html#async-context-managers) （异步上下文管理器）可以被使用来限制在某些任务的等待时间。

​	delay参数可以是None或浮点/整数代表的秒数。如果delay是None，没有时间限制；这个在上下文管理器创建时没有明确的delay时间时很有用。

​	其他情况，上下文管理器可以通过使用 [`Timeout.reschedule()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Timeout.reschedule)在创建后重新规划时间。

示例:

```python
async def main():
    async with asyncio.timeout(10):
        await long_running_task()
```

如果长时间任务超过了10秒还未完成，上下文管理器会将现有任务关闭，然后再内部处理 [`asyncio.CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 结果，将其转为一个[`asyncio.TimeoutError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.TimeoutError) ，这样就能处理错误。

示例 [`asyncio.TimeoutError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.TimeoutError):

```python
async def main():
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
```

通过 [`asyncio.timeout()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.timeout) 产生的上下文管理器可以被重新规划到一个不同的截至时间和检查中。

*class* asyncio.**Timeout**

​	一个 [asynchronous context manager](https://docs.python.org/zh-cn/3/reference/datamodel.html#async-context-managers) 用来限定其内部的任务的消耗时间。

​	*3.11 新版功能.*

​	**when**() → [float](https://docs.python.org/zh-cn/3/library/functions.html#float) | [None](https://docs.python.org/zh-cn/3/library/constants.html#None)

​		返回现在的截至时间，或者在现在截至时间没有设置的时候返回None

​		截至时间是浮点数，和通过 [`loop.time()`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.loop.time) 返回的时间一致

​	**reschedule**(*when: [float](https://docs.python.org/zh-cn/3/library/functions.html#float) | [None](https://docs.python.org/zh-cn/3/library/constants.html#None)*)

​		改变触发超时的时间

​		如果when的参数是None，任何现在的截至时间会被取消，上下文管理器将会无限制等待。

​		如果when是一个浮点数，会被设置成新的截至时间。

​		如果when已经在过去，超时会在下一个事件循环迭代时触发。

​	**expired**() → [bool](https://docs.python.org/zh-cn/3/library/functions.html#bool)

​		返回上下文管理器是否已经超过了截至日期（过期）。

示例：

```python
async def main():
    try:
        # We do not know the timeout when starting, so we pass ``None``.
        async with asyncio.timeout(None) as cm:
            # We know the timeout now, so we reschedule it.
            new_deadline = get_running_loop().time() + 10
            cm.reschedule(new_deadline)

            await long_running_task()
    except TimeoutError:
        pass

    if cm.expired:
        print("Looks like we haven't finished on time.")
```

超时上下文管理器可以被安全嵌套

*3.11 新版功能.*

*coroutine* asyncio.**timeout_at**(*when*)

​	和 [`asyncio.timeout()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.timeout)类似，除了when是一个停止等待的绝对时间或者None。

示例:

```python
async def main():
    loop = get_running_loop()
    deadline = loop.time() + 20
    try:
        async with asyncio.timeout_at(deadline):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
```

*3.11 新版功能.*

*coroutine* asyncio.**wait_for**(*aw*, *timeout*)

​	等待 *aw* [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables) 完成，指定 timeout 秒数后超时。

​	如果 *aw* 是一个协程，它将自动被作为任务调度。

​	*timeout* 可以为 `None`，也可以为 float 或 int 型数值表示的等待秒数。如果 *timeout* 为 `None`，则等待直到完	成。

​	如果超时发生，将会取消task，抛出 [`TimeoutError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TimeoutError)。

​	要避免任务 [`取消`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel)，可以加上 [`shield()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.shield)。

​	此函数将等待直到 Future 确实被取消，所以总等待时间可能超过 *timeout*。 如果在取消期间发生了异常，异常	将会被传播。

​	如果等待被取消，则 *aw* 指定的对象也会被取消。

​    *在 3.10 版更改:* 移除了 *loop* 形参。

示例：

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
```

*在 3.7 版更改:* 当aw由于超时被取消， `wait_for` 会等待aw取消。前个版本是会直接立刻抛出 [`TimeoutError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TimeoutError) 。

*在 3.10 版更改:* 移除了 *loop* 形参。



## [简单等待](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id11)

- *coroutine* asyncio.**wait**(*aws*, ***, *timeout=None*, *return_when=ALL_COMPLETED*)

  在aws可迭代并发和区块中运行 [`Future`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future) 和 [`Task`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 实例，直到*return_when*.*aws* 返回特定的状态可迭代对象必须不为空。返回两个 Task/Future 集合: `(done, pending)`。用法：

```python
done, pending = await asyncio.wait(aws)
```

如指定 *timeout* (float 或 int 类型) 则它将被用于控制返回之前等待的最长秒数。

注意这个函数不会抛出 [`TimeoutError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TimeoutError)。因为超时没有完成的Futures 或者 Tasks 时只是返回设定的second值。

*return_when* 指定此函数应在何时返回。它必须为以下常数之一:

| 常量              | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| `FIRST_COMPLETED` | 函数将在任意可等待对象结束或取消时返回。                     |
| `FIRST_EXCEPTION` | 函数将在任意可等待对象因引发异常而结束时返回。当没有引发任何异常时它就相当于 `ALL_COMPLETED`。 |
| `ALL_COMPLETED`   | 函数将在所有可等待对象结束或取消时返回。                     |

与 [`wait_for()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.wait_for) 不同，`wait()` 在超时发生时不会取消可等待对象。

*在 3.10 版更改:* 移除了 *loop* 形参。

*在 3.11 版更改:* Passing coroutine objects to `wait()` directly is forbidden.

asyncio.**as_completed**(*aws*, ***, *timeout=None*)

​	并发地运行 *aws* 可迭代对象中的 [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables)。 返回一个协程的迭代器。 所返回的每个协程可被等待以从剩余	的可等待对象的可迭代对象中获得最早的下一个结果。Raises [`TimeoutError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TimeoutError) if the timeout occurs before all 	Futures are done.*在 3.10 版更改:* 移除了 *loop* 形参。示例:

```python
for coro in as_completed(aws):
    earliest_result = await coro
    # ...
```

*在 3.10 版更改:* 移除了 *loop* 形参。

*3.10 版后已移除:* 如果 *aws* 可迭代对象中的可等待对象不全为 Future 类对象并且没有正在运行的事件循环则会发出弃用警告。



## [在线程中运行](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id12)

*coroutine* asyncio.**to_thread**(*func*, */*, **args*, ***kwargs*)

在不同的线程中异步地运行函数 *func*。向此函数提供的任何 *args 和 **kwargs 会被直接传给 *func*。 并且，当前 [`contextvars.Context`](https://docs.python.org/zh-cn/3/library/contextvars.html#contextvars.Context) 会被传播，允许在不同的线程中访问来自事件循环的上下文变量。返回一个可被等待以获取 *func* 的最终结果的协程。这个协程函数会优先被适用于执行如果在主线程中会阻塞事件循环的绑定IO的函数/方法。

比如：

```python
def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54
```

直接在任何协程中调用 `blocking_io()` 会在其运行中阻塞事件循环，会增加运行时间1秒。如果使用 `asyncio.to_thread()`，我们可以在不阻塞事件循环的情况下将其运行在要给单独胡的线程中。

备注：

由于 [GIL](https://docs.python.org/zh-cn/3/glossary.html#term-GIL),，`asyncio.to_thread()` 通常只能被用来使得绑定IO的函数不会被阻塞。但是，对于一些扩展模型（释放了GIL或者不具有GIL限制的其他Python编译器）， `asyncio.to_thread()` 也可以用来绑定CPU的函数。

*3.9 新版功能.*



## [跨线程调度](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id13)

asyncio.**run_coroutine_threadsafe**(*coro*, *loop*)

向指定事件循环提交一个协程。（线程安全）返回一个 [`concurrent.futures.Future`](https://docs.python.org/zh-cn/3/library/concurrent.futures.html#concurrent.futures.Future) 以等待来自其他 OS 线程的结果。此函数应该从另一个 OS 线程中调用，而非事件循环运行所在线程。示例:

```python
# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
```

如果在协程内产生了异常，将会通知返回的 Future 对象。它也可被用来取消事件循环中的任务:

```python
try:
    result = future.result(timeout)
except TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')
```

参见 [concurrency and multithreading](https://docs.python.org/zh-cn/3/library/asyncio-dev.html#asyncio-multithreading) 部分的文档。

不同与其他 asyncio 函数，此函数要求显式地传入 *loop* 参数。

*3.5.1 新版功能.*



## [内省](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id14)

asyncio.**current_task**(*loop=None*)

返回当前运行的 [`Task`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 实例，如果没有正在运行的任务则返回 `None`。如果 *loop* 为 `None` 则会使用 [`get_running_loop()`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.get_running_loop) 获取当前事件循环。*3.7 新版功能.*

asyncio.**all_tasks**(*loop=None*)

返回事件循环所运行的未完成的 [`Task`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 对象的集合。如果 *loop* 为 `None`，则会使用 [`get_running_loop()`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.get_running_loop) 获取当前事件循环。*3.7 新版功能.*



## [Task 对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#id15)

*class* asyncio.**Task**(*coro*, ***, *loop=None*, *name=None*)

一个与 [`Future 类似`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future) 的对象，可运行 Python [协程](https://docs.python.org/zh-cn/3/library/asyncio-task.html#coroutine)。非线程安全。

Task 对象被用来在事件循环中运行协程。如果一个协程在等待一个 Future 对象，Task 对象会挂起该协程的执行并等待该 Future 对象完成。当该 Future 对象 *完成*，被打包的协程将恢复执行。

事件循环使用协同日程调度: 一个事件循环每次运行一个 Task 对象。而一个 Task 对象会等待一个 Future 对象完成，该事件循环会运行其他 Task、回调或执行 IO 操作。

使用高层级的 [`asyncio.create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task) 函数来创建 Task 对象，也可用低层级的 [`loop.create_task()`](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html#asyncio.loop.create_task) 或 [`ensure_future()`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.ensure_future) 函数。不建议手动实例化 Task 对象。

要取消一个正在运行的 Task 对象可使用 [`cancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel) 方法。调用此方法将使该 Task 对象抛出一个 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 异常给打包的协程。如果取消期间一个协程正在等待一个 Future 对象，该 Future 对象也将被取消。

[`cancelled()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancelled) 可被用来检测 Task 对象是否被取消。如果打包的协程没有抑制 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 异常并且确实被取消，该方法将返回 `True`。

[`asyncio.Task`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 从 [`Future`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future) 继承了其除 [`Future.set_result()`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future.set_result) 和 [`Future.set_exception()`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future.set_exception) 以外的所有 API。

Task 对象支持 [`contextvars`](https://docs.python.org/zh-cn/3/library/contextvars.html#module-contextvars) 模块。当一个 Task 对象被创建，它将复制当前上下文，然后在复制的上下文中运行其协程。

*在 3.7 版更改:* 加入对 [`contextvars`](https://docs.python.org/zh-cn/3/library/contextvars.html#module-contextvars) 模块的支持。

*在 3.8 版更改:* 添加了 *name* 形参。

*3.10 版后已移除:* 如果未指定 *loop* 并且没有正在运行的事件循环则会发出弃用警告。



**done**()

如果 Task 对象 *已完成* 则返回 `True`。

当 Task 所封包的协程返回一个值、引发一个异常或 Task 本身被取消时，则会被认为 *已完成*。

**result**()

返回 Task 的结果。如果 Task 对象 *已完成*，其封包的协程的结果会被返回 (或者当协程引发异常时，该异常会被重新引发。)如果 Task 对象 *被取消*，此方法会引发一个 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 异常。如果 Task 对象的结果还不可用，此方法会引发一个 [`InvalidStateError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.InvalidStateError) 异常。

**exception**()

返回 Task 对象的异常。如果所封包的协程引发了一个异常，该异常将被返回。如果所封包的协程正常返回则该方法将返回 `None`。如果 Task 对象 *被取消*，此方法会引发一个 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 异常。如果 Task 对象尚未 *完成*，此方法将引发一个 [`InvalidStateError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.InvalidStateError) 异常。

**add_done_callback**(*callback*, ***, *context=None*)

添加一个回调，将在 Task 对象 *完成* 时被运行。此方法应该仅在低层级的基于回调的代码中使用。要了解更多细节请查看 [`Future.add_done_callback()`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future.add_done_callback) 的文档。

**remove_done_callback**(*callback*)

从回调列表中移除 *callback* 。此方法应该仅在低层级的基于回调的代码中使用。要了解更多细节请查看 [`Future.remove_done_callback()`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future.remove_done_callback) 的文档。

**get_stack**(***, *limit=None*)

返回此 Task 对象的栈框架列表。如果所封包的协程未完成，这将返回其挂起所在的栈。如果协程已成功完成或被取消，这将返回一个空列表。如果协程被一个异常终止，这将返回回溯框架列表。框架总是从按从旧到新排序。每个被挂起的协程只返回一个栈框架。可选的 *limit* 参数指定返回框架的数量上限；默认返回所有框架。返回列表的顺序要看是返回一个栈还是一个回溯：栈返回最新的框架，回溯返回最旧的框架。(这与 traceback 模块的行为保持一致。)

**print_stack**(***, *limit=None*, *file=None*)

打印此 Task 对象的栈或回溯。此方法产生的输出类似于 traceback 模块通过 [`get_stack()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.get_stack) 所获取的框架。*limit* 参数会直接传递给 [`get_stack()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.get_stack)。*file* 参数是输出所写入的 I/O 流；默认情况下输出会写入 [`sys.stderr`](https://docs.python.org/zh-cn/3/library/sys.html#sys.stderr)。

**get_coro**()

返回由 [`Task`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task) 包装的协程对象。*3.8 新版功能.*

**get_name**()

返回 Task 的名称。如果没有一个 Task 名称被显式地赋值，默认的 asyncio Task 实现会在实例化期间生成一个默认名称。*3.8 新版功能.*

**set_name**(*value*)

设置 Task 的名称。*value* 参数可以为任意对象，它随后会被转换为字符串。在默认的 Task 实现中，名称将在任务对象的 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 输出中可见。*3.8 新版功能.*

**cancel**(*msg=None*)

请求取消 Task 对象。这将安排在下一轮事件循环中抛出一个 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 异常给被封包的协程。协程在之后有机会进行清理甚至使用 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) ... ... `except CancelledError` ... [`finally`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#finally) 代码块抑制异常来拒绝请求。不同于 [`Future.cancel()`](https://docs.python.org/zh-cn/3/library/asyncio-future.html#asyncio.Future.cancel)，[`Task.cancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel) 不保证 Task 会被取消，虽然抑制完全取消并不常见，也很不鼓励这样做。*在 3.9 版更改:* 增加了 *msg* 形参。*在 3.11 版更改:* The `msg` parameter is propagated from cancelled task to its awaiter.以下示例演示了协程是如何侦听取消请求的:

```python
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
```

**cancelled**()

如果 Task 对象 *被取消* 则返回 `True`。当使用 [`cancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel) 发出取消请求时 Task 会被 *取消*，其封包的协程将传播被抛入的 [`CancelledError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.CancelledError) 异常。

**uncancel**()

Decrement the count of cancellation requests to this Task.Returns the remaining number of cancellation requests.

减少对于取消这个任务的申请的计数。返回现在存在的取消申请的数量。需要注意，一旦取消任务的执行完成，再次调用 [`uncancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel) 没有任何效果。

*3.11 新版功能.*

This method is used by asyncio's internals and isn't expected to be used by end-user code.这个方法主要针对asyncio的内部使用，没有计划被终端客户的代码使用。特别是，如果任务被成功取消，它允许并发结构的元素，比如  [Task Groups](https://docs.python.org/zh-cn/3/library/asyncio-task.html#taskgroups) 和 [`asyncio.timeout()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.timeout) 继续执行，将取消和各自的结构分开。比如：

```python
async def make_request_with_timeout():
    try:
        async with asyncio.timeout(1):
            # Structured block affected by the timeout:
            await make_request()
            await make_another_request()
    except TimeoutError:
        log("There was a timeout")
    # Outer code not affected by the timeout:
    await unrelated_code()
```

当模块 `make_request()` 和d `make_another_request()` 有可能由于超时而被取消的时候， `unrelated_code()` 应该会继续执行，即使超时。这是类似通过[`uncancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel). [`TaskGroup`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.TaskGroup) 上下文管理器使用 [`uncancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel) 。



**cancelling**()

返回暂停中的对于任务的取消请求。也就是调用  [`cancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel) 的结果减去调用 [`uncancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel) 结果的数量。

需要注意的是，如果这个数字比0大，但是任务还在可能在执行， [`cancelled()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancelled) 还是会返回False，这是由于调用 [`uncancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel)会使得这个数字降低，导致任务无法在取消申请变为0的时候还是取消任务。

这个方法主要在asyncio内部代码中使用，不建议用在终端用户代码中，更多细节查看 [`uncancel()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.uncancel) 。

*3.11 新版功能.*
