import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def load_data():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root

def task1(xml_root):
    with open("result1.json", 'w', encoding='utf-8') as file:
        result = []
        for item in xml_root.iter('item'):
            pubDate = item.find('pubDate').text
            title = item.find('title').text
            result.append({
                'pubDate': pubDate,
                'title': title
            })
        json.dump(result, file, ensure_ascii=False)


def task2(xml_root: ET.Element):
    with open("result2.json", 'w', encoding='utf-8') as file:
        result = []
        for item in xml_root.iter('item'):
            temp = {}
            for element in item.iter():
                if element.tag != 'item':
                    temp[element.tag] = element.text

            result.append(temp)

        json.dump(result, file, ensure_ascii=False)