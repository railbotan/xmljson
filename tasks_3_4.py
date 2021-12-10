import datetime
from itertools import groupby
from json import loads
from operator import itemgetter
from urllib.request import urlopen

def get_date(jsonObj):
    return datetime.date.fromisoformat(jsonObj['timestamp'][0:jsonObj['timestamp'].find('T')])


def get_sorted_reviews(revisions):
    result = {}
    for key, items in groupby(revisions, key=get_date):
        result[key] = sum(1 for _ in items)
    return result


def task3():

    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    data = loads(urlopen(url).read().decode('utf8'))
    revisions = data['query']['pages']['183903']['revisions']

    for key, value in sorted(get_sorted_reviews(revisions).items(), key=itemgetter(1), reverse=True):
        print(key, value)


def task4():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,%20%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
    data = loads(urlopen(url).read().decode('utf8'))
    revisions = data['query']['pages']['192203']['revisions']
    key, val = sorted(get_sorted_reviews(revisions).items(), key=itemgetter(1), reverse=True)[0]
    print(key, val)
