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
news_json = json.dumps(news, ensure_ascii=False).encode('utf8')
with open("news_full.json", 'wb') as f:
    f.write(news_json)
