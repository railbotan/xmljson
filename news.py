import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def save_dictlist_to_json(path, list_of_dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(list_of_dict, f, ensure_ascii=False, indent=2)


data = urlopen('https://lenta.ru/rss').read().decode('utf8')
items = ET.fromstring(data)[0].findall('item')
save_dictlist_to_json('news.json', [{'pubDate': i.find('pubDate').text, 'title': i.find('title').text} for i in items])
save_dictlist_to_json('news_all.json', [{elm.tag: elm.text for elm in i} for i in items])
