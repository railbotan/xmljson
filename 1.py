import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)


newsJson = [{'pubDate': i.find('pubDate').text, 'title': i.find('title').text}
            for i in root.iter('item')]

with open("news.json", "w", encoding='UTF-8') as file:
    json.dump(newsJson, file, ensure_ascii=False, indent=1)
