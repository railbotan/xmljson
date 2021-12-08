import xml.etree.ElementTree as ET
from json import dump
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

res = [{i.tag: i.text for i in item
        } for item in root.findall('channel/item')]

with open("news_2.json", "w", encoding = 'UTF-8') as f:
    dump(res, f, indent = 1, ensure_ascii = False)