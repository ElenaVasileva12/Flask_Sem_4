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
import multiprocessing
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


def get_url(url):
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(f'Home_work_multi/{filename}', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    te=0
    proces = []
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.url_parser:
        urls = namespace.url_parser
        # print(namespace.url_parser)

        for url in urls:
            ts = time.time()
            t = multiprocessing.Process(target=get_url, args=(url,))
            proces.append(t)
            t.start()
            tf = time.time()
            te += (tf - ts)
            print(f'Прошло {tf - ts}')

    for i in proces:
        i.join()
    print(f'Всего времени прошло {te}')

#  python task_9_1.py 'https://images.wallpaperscraft.ru/i# mage/single/chelovek_kub_vsadnik_1087361_1280x720.jpg' 'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-10.jpg'
