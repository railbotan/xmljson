from urllib.request import urlopen
from json import loads
import itertools as it

def gradskiy():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80' \
          '%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,' \
          '_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8' \
          '%D1%87 '
    data = loads(urlopen(url).read().decode('utf8'))
    sorted_data = it.groupby(i['timestamp'][:10] for i in data['query']['pages']['183903']['revisions'])
    for date, edits in sorted_data:
        print(date, len(list(edits)))

    # Жан-Поль Бельмондо
def belmondo():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5' \
          '%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
    data = loads(urlopen(url).read().decode('utf8'))
    sorted_data = it.groupby(i['timestamp'][:10] for i in data['query']['pages']['192203']['revisions'])
    date, max_edits = '', 0
    for d, edits in sorted_data:
        edits_count = len(list(edits))
        if edits_count > max_edits:
            date, max_edits = d, edits_count
    print(date, max_edits)


if __name__ == "__main__":
    gradskiy()
    belmondo()
