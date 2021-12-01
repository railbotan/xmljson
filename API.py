from itertools import groupby
from urllib.request import urlopen
from json import loads
import datetime

# Александр Градский url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500
# &titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,
# _%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87' id
# = '183903'

# Жан-Поль Бельмондо
id = '192203'
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '

data = loads(urlopen(url).read().decode('utf8'))
rev = data['query']['pages'][id]['revisions']


def convert_date(r):
    return datetime.datetime.strptime(r['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


for key, group_items in groupby(rev, key=convert_date):
    print(key, sum(1 for i in group_items))

# наибольшее кол-во поправок у Жан-Поля Бельмондо было сделано 2021-09-06 (58 правок) - дата смерти
