# Задание XML/JSON
Я выполнил первые два задания связанные с RSS Lenta.ru в файле [a relative link](newsparser)
##№1
Код для создания файла [a relative link](news.json):
```data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
filtered_data = []
for item in root.iter('item'):
    filtered_data.append({'pubDate': item.find('pubDate').text, 'title': item.find('title').text})
with open('news.json', 'w') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)
```
Файл полученный выполнением программы выглядит так:
![news](https://github.com/speedUpDev/PyCharm_task/blob/main/screenshots/profiler_filter.png)
##№2
Код для создания файла [a relative link](full_news.json):
```news_data = []
for item in root.iter('item'):
    news = {}
    for child in item:
        news[child.tag] = child.text
    news_data.append(news)
with open('full_news.json', 'w', encoding='utf-8') as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)
```
![full_news](https://github.com/speedUpDev/PyCharm_task/blob/main/screenshots/profiler_filter.png)
