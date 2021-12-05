import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

def get_news(channel):
    news = []
    for c in channel.findall('item'):
        news.append({'pubDate': c.find('pubDate').text, 'title': c.find('title').text})
    return news

def create_json_file(channel):
    json_file = json.dumps(get_news(channel), ensure_ascii=False, indent=4).encode('utf8')
    with open("news.json", 'wb') as f:
        f.write(json_file)

def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    create_json_file(root[0])

if __name__ == "__main__":
    main()