import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
channelElement = root[0]

newsTitleDate = []
for i in channelElement.findall('item'):
    elements = {}
    for element in i:
        elements[element.tag] = element.text
    newsTitleDate.append(elements)

newsJson = json.dumps(newsTitleDate, ensure_ascii=False, indent=2).encode('utf8')
with open('news2.json', 'wb') as n:
    n.write(newsJson)
