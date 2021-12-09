import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen("https://lenta.ru/rss").read().decode("utf8")
root = ET.fromstring(data)

dataToJson = [
    {i.tag: i.text for i in item} for item in root.iter("item") 
]

with open("full_news.json", "w", encoding="utf8") as f:
    json.dump(dataToJson, f, ensure_ascii=False, indent=4)

