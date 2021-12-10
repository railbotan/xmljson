import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news_arr = [{element.tag: element.text for element in item} for item in root.findall('channel/item')]


def create_json():
    with open("task-2_news.json", "w", encoding="UTF-8") as news_file:
        json.dump(news_arr, news_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    create_json()
