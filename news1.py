from xml.etree.ElementTree import fromstring
from json import dump
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = fromstring(data)

res = []
for i in root.findall('channel/item'):
    res.append({
        'pubDate': i.find('pubDate').text,
        'title': i.find('title').text
    })

with open("news.json", "w", encoding='UTF-8') as out:
    dump(res, out, indent=1, ensure_ascii=False)