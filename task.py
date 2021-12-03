import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]

def get_news(channel):
    news = []
    for item in channel.findall('item'):
        news.append({
            'pubDate': item.find('pubDate').text,
            'title': item.find('title').text
        })
    return news

def get_all_news(channel):
    all_news = []
    for item in channel.findall('item'):
        tags = {}
        for tag in item:
            tags[tag.tag] = tag.text
        all_news.append(tags)
    return all_news

def save_to_json(news, filename):
    json_file = json.dumps(news, ensure_ascii=False, indent=4 ).encode('utf8')
    with open(filename, 'wb') as f:
        f.write(json_file)

save_to_json(get_all_news(get_channel()), 'all_news.json')
save_to_json(get_news(get_channel()), 'news.json')
