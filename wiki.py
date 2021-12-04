import requests
from itertools import groupby
from datetime import datetime as dt

URL_GAB = (r"https://ru.wikipedia.org/w/api.php?action=query&format=json&"
           r"prop=revisions&rvlimit=500&titles=Градский,_Александр_Борисович")

URL_BJP = (r"https://ru.wikipedia.org/w/api.php?action=query&"
           r"format=json&prop=revisions&rvlimit=500&titles=Бельмондо,_Жан-Поль")

PEOPLE = ({"id": "183903", "url": URL_GAB}, {"id": "192203", "url": URL_BJP})


def main() -> None:
    for person in PEOPLE:
        data = requests.get(person["url"]).json()
        revisions = data["query"]["pages"][person["id"]]["revisions"]

        groups = groupby(revisions, key=lambda rev: dt.strptime(rev["timestamp"], "%Y-%m-%dT%H:%M:%SZ").date())

        for key, group in groups:
            print(key, len([i for i in group]))

        print()


# Количество правок, для отобранный людей, в день смерти действительно максимально,
# однако данная метрика не является достоверной, т.к правки могут вноситься и по другим поводам.
if __name__ == "__main__":
    main()
