import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_news(channel):
    news = []
    for i in channel.findall('item'):
        news.append({'pubDate': i.find('pubDate').text,'title': i.find('title').text})
    return news


def save_news(news):
    news_json = json.dumps(news, ensure_ascii=False).encode('utf8')
    with open("news.json", 'wb') as f:
        f.write(news_json)


save_news(get_news(get_channel()))