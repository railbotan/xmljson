import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_channel():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_date_title(channel):
    news_list = []
    for element in channel.findall("item"):
        date = element.find("pubDate").text
        title = element.find("title").text
        news_list.append({"pubDate": date, "title": title})

    return news_list


def write_json(news_list):
    json_file = json.dumps(news_list, ensure_ascii=False).encode('utf8')
    with open("news.json", 'wb') as f:
        f.write(json_file)


news = get_date_title(get_channel())
write_json(news)