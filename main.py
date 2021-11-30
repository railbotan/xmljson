import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_pub_date_title(channel: ET.Element):
    news = []
    for item in channel.findall("item"):
        pub_date = item.find("pubDate").text
        title = item.find("title").text
        news.append({"pubDate": pub_date, "title": title})

    return news


def save_news(news: []):
    news_json = json.dumps(news, ensure_ascii=False).encode('utf8')
    with open("news.json", 'wb') as f:
        f.write(news_json)


def save_pub_date_title():
    channel = get_channel()
    news = get_pub_date_title(channel)
    save_news(news)


save_pub_date_title()
