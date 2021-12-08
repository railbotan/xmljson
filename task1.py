import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

res = [{'pubDate': item.find('pubDate').text,
        'title': item.find('title').text}
       for item in root.findall('channel/item')]

with open("news.json", 'w', encoding='utf-8') as file:
    json.dump(res, file, ensure_ascii=False, indent=3)
