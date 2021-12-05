import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

#Старая версия get_news
# def get_news(channel):
#     news = []
#     for c in channel.findall('item'):
#         news.append({'pubDate': c.find('pubDate').text, 'title': c.find('title').text})
#     return news

def get_news(channel):
    news = []
    for c in channel.findall('item'):
        item_dict = {}
        for i in c:
            item_dict[i.tag] = i.text
        news.append(item_dict)
    return news

def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(get_news(root[0]), f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()