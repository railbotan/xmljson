from urllib.request import urlopen
from json import loads
import datetime
from itertools import groupby


def convert_date(revision):
    return datetime.datetime.strptime(revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


def get_statistic(revisions):
    res = {}
    for key, group_items in groupby(revisions, key=convert_date):
        res[key] = sum(1 for i in group_items)
    return sorted(res.items(), key=lambda item: item[1], reverse=True)[0:5]


if __name__ == "__main__":
    url1 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    url2 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'

    statistic_one = get_statistic(loads(urlopen(url1).read())['query']['pages']["183903"]['revisions'])
    statistic_two = get_statistic(loads(urlopen(url2).read())['query']['pages']["192203"]['revisions'])

    print("Александр Градский")
    [print("{} {}".format(key, value)) for key, value in statistic_one]
    print("Жан-Поль Бельмондо")
    [print("{} {}".format(key, value)) for key, value in statistic_two]
