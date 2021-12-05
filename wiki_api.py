from urllib.request import urlopen
from json import loads
from itertools import groupby


def get_revisions_by_date(url):
    data = loads(urlopen(url).read().decode('utf8'))
    page_id = list(data['query']['pages'].keys())[0]
    revisions = data['query']['pages'][page_id]['revisions']
    return [{d: len(list(r))} for d, r in groupby([rev['timestamp'][0:10] for rev in revisions])]

url_gradski = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
url_belmondo = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'

print("Александр Градский:")
for i in get_revisions_by_date(url_gradski):
    print(list(i.keys())[0], list(i.values())[0])

print("Жан-Поль Бельмондо:")
for i in get_revisions_by_date(url_belmondo):
    print(list(i.keys())[0], list(i.values())[0])

