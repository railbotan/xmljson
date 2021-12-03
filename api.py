from urllib.request import urlopen
from json import loads
import itertools
from datetime import datetime

url1 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
key1 = '183903'
url2 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
key2 = '192203'
url = url2
key = key2
data = loads(urlopen(url).read().decode('utf8'))
corrections = data['query']['pages'][key]['revisions']


def transform_date(date):
    return datetime.strptime(date['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


for key, count in itertools.groupby(corrections, key=transform_date):
    sum_count = sum(1 for i in count)
    print(key, sum_count)
