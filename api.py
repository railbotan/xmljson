import datetime
from itertools import groupby
from urllib.request import urlopen
from json import loads


def get_date(revision):
    return datetime.datetime.strptime(revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


# Александр Градский

# id = 183903
# url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'

# Жан Бельмондо

id = 192203
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'

data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages'][str(id)]['revisions']

for key, group_items in groupby(revisions, key=get_date):
    print(key, sum(1 for i in group_items))
