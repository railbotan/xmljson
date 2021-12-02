import xml.etree.ElementTree as ET
import json
from urllib.request import urlopen


def get_data():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    return ET.fromstring(data)


def get_pubdate_title(content):
    return [
        [{'pubDate': i.find('pubDate').text, 'title': i.find('title').text} for i in content.findall('channel/item')]]


def get_news(content: ET.Element):
    data = []
    for element in content.findall('channel/item'):
        data.append({i.tag: i.text for i in element})
    return data


if __name__ == "__main__":
    data = get_data()
    pubdate_title_json = json.dumps(get_pubdate_title(data), ensure_ascii=False, indent=1).encode('utf-8')
    news_json = json.dumps(get_news(data), ensure_ascii=False, indent=1).encode('utf-8')

    with open('news.json', 'wb') as file:
        file.write(pubdate_title_json)

    with open('all_news.json', 'wb') as file:
        file.write(news_json)
