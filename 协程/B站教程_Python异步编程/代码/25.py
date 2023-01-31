import asyncio
import aiomysql


async def execute():
    conn = await aiomysql.connect(
        host='111',
        port=3306,
        user='aaa',
        password='123',
        db='mysql',
    )

    cur = await conn.cursor()

    await cur.execute('SELECT HOST,User FROM user')

    result = await cur.fetchall()
    print(result)

    await cur.close()
    conn.close()


asyncio.run(execute())