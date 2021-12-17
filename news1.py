import json
import xml.etree.ElementTree as Et
from urllib.request import urlopen



data = urlopen('https://lenta.ru/rss').read().decode("utf-8")
root = Et.fromstring(data)
channel = root[0]
allNews = []

def get_news():
    for i in channel.findall("item"):
        allNews.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})
    return allNews


result = json.dumps(get_news(), ensure_ascii=False).encode('utf-8')
with open('news.json', 'wb') as f:
    f.write(result)

# rework for task2

allNews2 = []
def get_news_new():
    for i in channel.findall("item"):
        fields = {}
        for field in i:
            fields[field.tag] = field.text
        allNews2.append(fields)
    return allNews2


result = json.dumps(get_news_new(), ensure_ascii=False).encode('utf-8')
with open('news2.json', 'wb') as f:
    f.write(result)



