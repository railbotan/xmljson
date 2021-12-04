import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
channel = root[0]

news = []
for i in channel.findall('item'):
    areas = {}
    for area in i:
        areas[area.tag] = area.text
    news.append(areas)

news_json = json.dumps(news, ensure_ascii=False, indent=1).encode('utf8')
with open('news_task_2.json', 'wb') as item:
    item.write(news_json)
