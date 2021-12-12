import xml.etree.ElementTree as ET
from urllib.request import urlopen
from json import dump

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news = []

for i in root.findall('channel/item'):
    news.append({'pubDate': i.find('pubDate').text,
                'title': i.find('title').text})

with open('news.json', 'w', encoding='utf-8') as file:
    dump(news, file, indent=1, ensure_ascii=False)
