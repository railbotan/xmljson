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

def get_all_data(channel):
    news = []
    for i in channel.findall('item'):
        data = {}
        for t in i:
            data[t.tag] = t.text
        news.append(data)
    return news

def save_news(news, filename):
    news_json = json.dumps(news, ensure_ascii=False, indent=1).encode('utf8')
    with open(filename, 'wb') as f:
        f.write(news_json)


save_news(get_news(get_channel()), "news.json")
save_news(get_all_data(get_channel()), "all_news.json")