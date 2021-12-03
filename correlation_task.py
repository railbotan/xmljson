from itertools import groupby
from json import loads
from urllib.request import urlopen


def print_max_revisions(gr):
    date, max_r_count = '', 0
    for d, r in gr:
        r_count = len(list(r))
        if r_count > max_r_count:
            date, max_r_count = d, r_count
    print(date, max_r_count)


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
data = loads(urlopen(url).read().decode('utf8'))

grouped_data = groupby([i['timestamp'][:10] for i in data['query']['pages']['192203']['revisions']])
print_max_revisions(grouped_data)
