from itertools import groupby
from json import loads
from urllib.request import urlopen

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))

data_belmondo = groupby([i['timestamp'][:10] for i in data['query']['pages']['192203']['revisions']])
[print(d, len(list(e))) for d, e in data_belmondo]

#Резкий скачок правок произошёл 6.09.2021, в день смерти Бельмондо

#Самое большое количество правок сопало с датой смерти, но такой метод поиска не будет давать правильные результаты на 100%,
#так как это может не совпасть(могут произойти любые события, связанные с человеком), и дата будет определена неверно