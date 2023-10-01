import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import lxml
import urllib3

fake = UserAgent()  # Фейковый юзер агент


def getnews():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'User-Agent': 'fake.random'
    }

    url = 'https://kaktus.media/?lable=8'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')  # Получаем информайию с сайта делая запрос
    articl = soup.find_all('div', class_='Tag--article')
    news_dict = {}
    for articls in articl:
        articl_title = articls.find("a", class_="ArticleItem--name").text.strip()
        articl_url = articls.find("a", class_='ArticleItem--name').get('href').strip()

        # print(f"{articl_title}|{articl_url}")
        news_dict[articl_title] = {  # Сохраняем запрос ввиде словаря
            'Ссылки': articl_url
        }
    with open('news_dict.json', "w") as file:  # Создаем json файл и записываем в него данные
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def main():  # Запускаем файл
    getnews()


if __name__ == '__main__':
    main()
