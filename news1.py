from json import dump
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = ET.fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8'))
result = []
for i in data.findall('channel/item'):
    result.append( { 'pubDate': i.find('pubDate').text, 'title': i.find('title').text } )
with open("news.json", "w", encoding = 'UTF-8') as file:
    dump(result, file, indent = 1, ensure_ascii = False)