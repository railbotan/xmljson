import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
channel = root[0]


def getAllNews():
    allNews = []
    for i in channel.findall('item'):
        allNews.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})
    return allNews

def getFinalFile():
    final_file = json.dumps(getAllNews(), ensure_ascii=False).encode('utf8')
    with open('news.json', 'wb') as file:
        file.write(final_file)


getFinalFile()

def getNewsForTaskTwo():
    allNewsTwo = []
    for item in channel.findall('item'):
        fields = {}
        for field in item:
            fields[field.tag] = field.text
        allNewsTwo.append(fields)
    return allNewsTwo

def getFinalFile2():
    final_file = json.dumps(getNewsForTaskTwo(), ensure_ascii=False).encode('utf8')
    with open('news2.json', 'wb') as file:
        file.write(final_file)

getFinalFile2()