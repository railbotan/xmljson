import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
channelElement = root[0]

newsTitleDate = []
for i in channelElement.findall('item'):
    newsTitleDate.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})

newsJson = json.dumps(newsTitleDate, ensure_ascii=False, indent=2).encode('utf8')
with open('news.json', 'wb') as n:
    n.write(newsJson)
