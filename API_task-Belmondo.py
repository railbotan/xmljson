from urllib.request import urlopen
from json import loads
from itertools import groupby


def make_prediction(_data):
    death_day, death_day_edits = '', 0

    for date, edits in _data:
        cnt = len(list(edits))
        if cnt > death_day_edits:
            death_day, death_day_edits = date, cnt

    print(death_day, death_day_edits)


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '

data = loads(urlopen(url).read().decode('utf8'))
grouped_data = groupby([i['timestamp'][:10] for i in data['query']['pages']['192203']['revisions']])
make_prediction(grouped_data)
