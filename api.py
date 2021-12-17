import datetime
from itertools import groupby
from urllib.request import urlopen
import json


def get_day(revision):
    timestamp = revision['timestamp']
    return datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').date()



def get_revisions(id, url):
    data = json.loads(urlopen(url).read().decode('utf-8'))
    revisions = data['query']['pages'][str(id)]['revisions']
    for key, group_items in groupby(revisions, key=get_day):
        print(key, sum(1 for i in group_items))


pade_id_grad = 183903
url_grad = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
# get_revisions(pade_id_grad, url_grad)

page_id_bel = 192203
url_bel = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
get_revisions(page_id_bel, url_bel)