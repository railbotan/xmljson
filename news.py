import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def save_to_json(path, attributes):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(attributes, file, ensure_ascii=False, indent=3)

if __name__ == "__main__":
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)[0].findall('item')
    save_to_json('news.json', [{'pubDate': i.find('pubDate').text, 'title': i.find('title').text} for i in root])
    save_to_json('news_xml.json', [{element.tag: element.text for element in i} for i in root])
