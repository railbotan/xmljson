import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from collections import OrderedDict


def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_news(channel):
    for item in channel.findall('item'):
        fields = {field.tag: field.text for field in item}
        yield OrderedDict(sorted(fields.items()))


news = list(get_news(get_channel()))
with open("news_full.json", 'w', encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=4)
