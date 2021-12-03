from json import dump
from urllib.request import urlopen
from xml.etree.ElementTree import fromstring

news_json = [
    {
        'pubDate': i.find('pubDate').text,
        'title': i.find('title').text
    } for i in fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8')).findall('channel/item')]

with open("news.json", "w", encoding='UTF-8') as out:
    dump(news_json, out, indent=1, ensure_ascii=False)
