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
news_json = json.dumps(news, ensure_ascii=False).encode('utf8')
with open("news.json", 'wb') as f:
    f.write(news_json)





