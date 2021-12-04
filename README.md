# Задание XML/JSON
Я выполнил первые два задания связанные с RSS Lenta.ru в файле [a relative link](newsparser)

##№1
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

##№2
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
![full_news](https://github.com/speedUpDev/xmljson/blob/main/source/screenshots/SecondTask.png)
