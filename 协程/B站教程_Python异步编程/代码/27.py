import asyncio, aioredis

import uvicorn

from fastapi import FastAPI

app = FastAPI()

REDIS_POOL = aioredis.ConnectionPool('redis.....',
                                     password='asdf',
                                     minsize=1,
                                     maxsize=10)


@app.get('/red')
async def red():
    print('request')
    await asyncio.sleep(3)
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    await redis.hmset_dict('car', key1=1, key2=2)

    result = await redis.hgetall('car', encoding='utf-8')

    REDIS_POOL.release(conn)

    return result


@app.get('/')
def index():
    return {'message': 'hello world'}


if __name__ == '__main__':
    uvicorn.run('luffy:app', host='127.0.0.1', port=5000, log_level='info')
