import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#编写asyncio的代码与hi前代码一致

#内部的事件循环会自动变为uvloop

asyncio.run()