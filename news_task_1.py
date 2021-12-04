import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
channel = root[0]

news = []
for i in channel.findall('item'):
    news.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})

news_json = json.dumps(news, ensure_ascii=False, indent=1).encode('utf8')
with open('news.json', 'wb') as item:
    item.write(news_json)
