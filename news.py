import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_news(ch: ET.Element):
    news = []
    for i in ch.findall('item'):
        news.append({
            'pubDate': i.find('pubDate').text,
            'title': i.find('title').text
        })
    return news


def get_first_branch():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def save_json(ch):
    json_file = json.dumps(get_news(ch), ensure_ascii=False).encode('utf8')
    with open("news.json", 'wb') as f:
        f.write(json_file)


channel = get_first_branch()
save_json(channel)
