import json
import requests

url = r'https://lenta.ru/rss'

if __name__ == "__main__":
    main()

def xml_loading(url: str) -> ET.Element:
    element_request = requests.get(url)
    return ET.fromstring(element_request.text)[0]

def json_xml_selectors(root: ET.Element, child_selector: str, selectors: list[str]) -> list[dict[str | None, str | None]]:
    return [{s: child.find(s).text for s in selectors} for child in root.findall(child_selector)]

def json_xml(root: ET.Element, child_selector: str):
    return [{tag.tag: tag.text for tag in child} for child in root.findall(child_selector)]

def save_json_file(data: dict | list, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main() -> None:
    element = xml_loading(url)
    name_child = "item"
    lim_data = json_xml_selectors(element, name_child, ["pubDate", "title"])
    save_json_file(lim_data, "news.json")
    data = json_xml(element, name_child)
    save_json_file(data, "news_2.json")
