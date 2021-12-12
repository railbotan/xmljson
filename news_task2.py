import xml.etree.ElementTree as ET
from urllib.request import urlopen
from json import dump

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news = []

for item in root.findall('channel/item'):
    news.append({i.tag: i.text for i in item})

with open('all_news.json', 'w', encoding='utf-8') as file:
    dump(news, file, indent=1, ensure_ascii=False)
