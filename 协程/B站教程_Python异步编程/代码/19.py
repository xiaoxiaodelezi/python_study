import asyncio
import requests


async def download_image(url):
    print('start', url)
    loop = asyncio.get_event_loop()
    #requests模块默认不支持异步操作，所以就使用线程池来配合实现
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('finished')
    file_name = url.rsplit('-')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = [
        1,
        2,
        3,
    ]

    tasks = [download_image(url) for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
