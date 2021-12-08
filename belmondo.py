from urllib.request import urlopen
from json import loads
from itertools import groupby


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
edits_data = groupby([edit['timestamp'][:10] for edit in data['query']['pages']['192203']['revisions']])


def find_max_edits(data_about_edits):
    date = ''
    max_edits = 0
    for d, edits in data_about_edits:
        count_edits = len(list(edits))
        if max_edits < count_edits:
            max_edits = count_edits
            date = d
    print(date, max_edits)


find_max_edits(edits_data)
"""
Дата смерти определилась правильно, но данной метрикой, пользоваться нельзя 
т.к. в жизни может произойти множество событий, которые повлекут правки
(новая неожданная информация о человеке, раскрытие тайни и т.д.)
"""