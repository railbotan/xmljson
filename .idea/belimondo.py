from itertools import groupby
from json import loads
from urllib.request import urlopen

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))

data_belimondo = groupby([i['timestamp'][:10] for i in data['query']['pages']['192203']['revisions']])
[print(d, len(list(e))) for d, e in data_belimondo]

#Резкий скачок правок совпал с датой смерти Бельмондо.
#Такой метод поиска не будет давать 100% правильные результаты, так как скачок количества правок могут вызывать любые события связанные с человеком.