from urllib.request import urlopen
from json import loads
from itertools import groupby


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
edits_data = groupby([edit['timestamp'][:10] for edit in data['query']['pages']['183903']['revisions']])

for date, edits in edits_data:
    print(date, len(list(edits)))

#Всплеск правок произошел 2021-11-28 их количество 153
#В этот день умер Градский



