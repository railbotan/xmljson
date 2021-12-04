import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

# №1
data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
filtered_data = []
for item in root.iter('item'):
    filtered_data.append({'pubDate': item.find('pubDate').text, 'title': item.find('title').text})
with open('news.json', 'w') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

# №2 Создаем новости со всеми тегами
news_data = []
for item in root.iter('item'):
    news = {}
    for child in item:
        news[child.tag] = child.text
    news_data.append(news)
with open('full_news.json', 'w', encoding='utf-8') as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)