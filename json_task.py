import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_element():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    return ET.fromstring(data)[0]


def get_news(element):
    news = []
    for item in element.findall("item"):
        news.append({"pubDate": item.find("pubDate").text, "title": item.find("title").text})
    return news


def get_all_news(element):
    news = []
    for item in element.findall('item'):
        field_dictionary = {}
        for field in item:
            field_dictionary[field.tag] = field.text
        news.append(field_dictionary)
    return news


def save_to_json_file(news, name):
    json_file = json.dumps(news, ensure_ascii=False,  sort_keys=True, indent=4).encode('utf8')
    with open(name, 'wb') as f:
        f.write(json_file)


def main():
    element = get_element()
    news = get_news(element)
    save_to_json_file(news, "news.json")
    all_news = get_all_news(element)
    save_to_json_file(all_news, "all_news.json")


if __name__ == "__main__":
    main()
