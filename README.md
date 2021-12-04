# Задание XML/JSON
Я выполнил первые два задания связанные с RSS Lenta.ru в файле: [newsparser.py](newsparser.py)

## №1

Код для создания файла [news.json](news.json):
```data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
filtered_data = []
for item in root.iter('item'):
    filtered_data.append({'pubDate': item.find('pubDate').text, 'title': item.find('title').text})
with open('news.json', 'w') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)
```
Файл полученный выполнением программы выглядит так:
![news](https://github.com/speedUpDev/xmljson/blob/main/source/screenshots/FirstTask.png)

## №2

Код для создания файла [full_news.json](full_news.json):
```news_data = []
for item in root.iter('item'):
    news = {}
    for child in item:
        news[child.tag] = child.text
    news_data.append(news)
with open('full_news.json', 'w', encoding='utf-8') as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)
```
Файл полученный выполнением программы выглядит так:

![full_news](https://github.com/speedUpDev/xmljson/blob/main/source/screenshots/SecondTask.png)

# API, ДЗ
Задание связанное с API Википедии я выполнил в файле: [wiki_api.py](wiki_api.py)

Код программы:
```from urllib.request import urlopen
from json import loads
from itertools import groupby


def grouper(item):
    return item['timestamp'][:10]


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages']['183903']['revisions']
for key, rev in groupby(revisions, key=grouper):
    count = 0
    for item in rev:
        count += 1
    print(key, count)
```

В результате выполнения программы я получил следующие результаты:

![full_news](https://github.com/speedUpDev/xmljson/blob/main/source/screenshots/ThirdTask.png)