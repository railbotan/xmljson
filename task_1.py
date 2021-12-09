import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen("https://lenta.ru/rss").read().decode("utf8")
root = ET.fromstring(data)

dataToJson = [
    {"pubDate": item.find("pubDate").text, "title": item.find("title").text} for item in root.iter("item")
]

with open("news.json", "w", encoding="utf8") as f:
    json.dump(dataToJson, f, ensure_ascii=False, indent=4)
