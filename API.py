from urllib.request import urlopen
from json import loads
from itertools import groupby
import datetime

def transform_date(rev):
    return datetime.datetime.strptime(rev['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()

def main():
    # Александр Градский
    # url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    # id = '183903'

    # Жан-Поль Бельмондо
    id = '192203'
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '

    data = loads(urlopen(url).read().decode('utf8'))
    total_rev = data['query']['pages'][id]['revisions']
    for date, items in groupby(total_rev, key=transform_date):
        print(date, sum(1 for i in items))

if __name__ == "__main__":
    main()

#Жан-Поль Бельмондо умер 06.09.2021. В этот день было зарегестрировано 58 правок его страницы в Википедии (наибольшее количество).