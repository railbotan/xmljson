import xml.etree.ElementTree as ET
from json import dump
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

res = [
    {
        c.tag: c.text for c in item
    }
    for item in root.findall('channel/item')]

with open("detailed_news.json", "w", encoding='UTF-8') as out:
    dump(res, out, indent=1, ensure_ascii=False)
