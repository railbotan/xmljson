from itertools import groupby
from urllib.request import urlopen
import json 


def get_date(rev):
    return rev.get('timestamp').split('T')[0]

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'

data = json.loads(urlopen(url).read().decode('utf8'))
revs = data['query']['pages']['192203']['revisions']

for _, group_items in groupby(revs, key=get_date):
    print(sum(1 for _ in group_items))
