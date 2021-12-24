import xml.etree.ElementTree as ET
from urllib.request import urlopen
from json import dump

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
ans = []

for i in root.findall('channel/item'):
    ans.append({'pubDate': i.find('pubDate').text,
                'title': i.find('title').text})

with open("news.json", "w", encoding='utf-8') as file:
    dump(ans, file, ensure_ascii=False)

