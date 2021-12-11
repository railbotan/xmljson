from urllib.request import urlopen
from itertools import groupby
from json import loads
import numpy as np

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))

revision_dates = groupby(i['timestamp'][:10] for i in data['query']['pages']['192203']['revisions'])

#num_revision = []
for date, revisions in revision_dates:
    print(date, len(list(revisions)))
    # Резкий скачок с наибольшим числом правок совпала c датой смерти (2021-09-06)
	# Однако этот метод поиска не будет давать правильный результат, так как скачок количества правок может быть связан с любым другим событием

	# num_revision.append(int(len(list(revisions))))
	# max_num_revision = np.max(num_revision)
	# if (int(len(list(revisions))) == int(max_num_revision)):
	# 	print(date)