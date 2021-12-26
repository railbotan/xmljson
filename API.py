from urllib.request import urlopen
from json import loads
from itertools import groupby
id_belmondo = '192203'
url_belmondo = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data_belmondo = loads(urlopen(url_belmondo).read().decode('utf8'))
edited= groupby([i['timestamp'][:10] for i in data_belmondo['query']['pages'][id_belmondo]['revisions']])
for date, edit in edited:
    print(date, len(list(edit)))

#06.09.2021 больше всего правок из за смерти Бельмондо. Метрика не надежная т.к из - за любых хайповых новостей будут появлятся
#новые правки