from urllib.request import urlopen
from json import loads
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
id = '192203'

groupby_data = groupby([i['timestamp'][:10] for i in data['query']['pages'][id]['revisions']])
for d, edit in groupby_data:
    print(d, len(list(edit)))

#Наибольшее число правок приходится на 06.09.2021
#Такой метрикой лучше не пользоваться, т.к. большое количество правок может быть связано и с другим важным событием в жизни человека.