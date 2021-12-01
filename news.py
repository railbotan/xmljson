import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_first_branch():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_news(ch: ET.Element):
    news = []
    for i in ch.findall('item'):
        news.append({
            'pubDate': i.find('pubDate').text,
            'title': i.find('title').text
        })
    return news


def get_full_news(ch: ET.Element):
    full_news = []
    for i in ch.findall('item'):
        fields_dict = {}
        for f in i:
            fields_dict[f.tag] = f.text
        full_news.append(fields_dict)
    return full_news


def save_json(file_name, news):
    json_file = json.dumps(news, ensure_ascii=False).encode('utf8')
    with open(file_name, 'wb') as f:
        f.write(json_file)


channel = get_first_branch()
# save_json("news.json", get_news(channel))
save_json("full_news.json", get_full_news(channel))
