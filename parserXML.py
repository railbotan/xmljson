import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_XML():
    return ET.fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8'))


def get_data_title(content):
    return [{'pubDate': i.find('pubDate').text, 'title': i.find('title').text} for i in content.findall('channel/item')]


def get_tags_item(content):
    json_data = []
    for item in content.findall('channel/item'):
        json_data.append({i.tag: i.text for i in item})
    return json_data


if __name__ == '__main__':
    data = get_XML()
    xml_to_json = json.dumps(get_data_title(data), ensure_ascii=False, indent=1).encode('utf8')
    news_json = json.dumps(get_tags_item(data), ensure_ascii=False, indent=1).encode('utf8')

    with open('news.json', 'wb') as file:
        file.write(xml_to_json)

    with open('all_news.json', 'wb') as file:
        file.write(news_json)

