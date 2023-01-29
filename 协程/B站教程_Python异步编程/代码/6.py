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