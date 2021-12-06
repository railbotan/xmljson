import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_news(channel):
    for item in channel.findall("item"):
        pub_date = item.find("pubDate").text
        title = item.find("title").text
        yield {"pubDate": pub_date, "title": title}


news = list(get_news(get_channel()))
with open("news.json", 'w', encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=4)





