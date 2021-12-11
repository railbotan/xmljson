import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)


newsJson = [{n.tag: n.text for n in i}
            for i in root.iter('item')]

with open("news_all.json", "w", encoding='UTF-8') as file:
    json.dump(newsJson, file, ensure_ascii=False, indent=1)
