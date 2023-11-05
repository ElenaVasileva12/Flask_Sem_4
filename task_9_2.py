# � Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
# файле, название которого соответствует названию изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
# image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и
# асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через
# аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.

import sys
import argparse
import asyncio
import aiohttp
import requests
import time

urls = ['https://images.wallpaperscraft.ru/image/single/chelovek_kub_vsadnik_1087361_1280x720.jpg',
        'https://kipmu.ru/wp-content/uploads/rdglbslv.jpg',
        'http://pic.rutubelist.ru/video/ff/e4/ffe4195d355e6b059dd7c336592a7036.jpg',
        'https://i.ytimg.com/vi/CDUf1dEN9p4/maxresdefault.jpg',
        'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-10.jpg'
        ]


# парсер
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("url_parser", nargs='*', help="Пути(в ковычках) к картинке через пробел", type=str,
                        default=urls)
    return parser


async def get_url(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as responce:
            filename = url.split('/')[-1]
            with open(f'Home_work_async/{filename}', 'wb') as f:
                txt = await responce.read()
                f.write(txt)
                print(f"Downloaded {url} in {time.time() - ts:.2f} seconds")


async def main():
    tasks = []
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.url_parser:
        urls = namespace.url_parser
        # print(namespace.url_parser)
        for url in urls:
            tasks.append(get_url(url, ))
    await asyncio.gather(*tasks)

ts = time.time()
if __name__ == '__main__':
    asyncio.run(main())
    tf = time.time()
    print(f'Время выполнения {tf - ts}')

#  python task_9_2.py 'https://images.wallpaperscraft.ru/i# mage/single/chelovek_kub_vsadnik_1087361_1280x720.jpg' 'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-10.jpg'
