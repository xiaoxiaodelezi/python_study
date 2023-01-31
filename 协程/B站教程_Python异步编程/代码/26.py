import asyncio
import aiomysql


async def execute(host, password):
    conn = await aiomysql.connect(
        host=host,
        port=3306,
        user='aaa',
        password=password,
        db='mysql',
    )

    cur = await conn.cursor()

    await cur.execute('SELECT HOST,User FROM user')

    result = await cur.fetchall()
    print(result)

    await cur.close()
    conn.close()


tasks_list = [
    execute('1', '1'),
    execute('2', '2'),
]

asyncio.run(asyncio.wait(tasks_list))