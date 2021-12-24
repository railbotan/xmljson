import xml.etree.ElementTree as ET
from urllib.request import urlopen
from json import dump

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
ans = []

for item in root.findall('channel/item'):
    ans.append({element.tag: element.text for element in item})

with open("news_2.json", "w", encoding='utf-8') as file:
    dump(ans, file, ensure_ascii=False)

