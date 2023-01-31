import asyncio
import aioredis


async def execute(address, password):
    print('start:', address)
    redis = await aioredis.create_redis(address, password)

    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()

    await redis.wait_closed()

    print('finished', address)


task_list = [
    execute(redis1, ps1),
    execute(redis2, ps2),
]

asyncio.run(asyncio.wait(task_lists))