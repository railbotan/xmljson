import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def save_news(news: [], filename):
    news_json = json.dumps(news, ensure_ascii=False).encode('utf8')
    with open(filename, 'wb') as f:
        f.write(news_json)


def get_pub_date_title(channel: ET.Element):
    news = []
    for item in channel.findall("item"):
        pub_date = item.find("pubDate").text
        title = item.find("title").text
        news.append({"pubDate": pub_date, "title": title})

    return news


def get_all_fields(channel: ET.Element):
    news = []
    for item in channel.findall('item'):
        fields = {}
        for field in item:
            fields[field.tag] = field.text
        news.append(fields)
    return news


def save_pub_date_title():
    channel = get_channel()
    news = get_pub_date_title(channel)
    save_news(news, "news.json")


def save_all_fields():
    channel = get_channel()
    news = get_all_fields(channel)
    save_news(news, "all_fields_news.json")


save_all_fields()
