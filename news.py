import requests
import json

URL = r'https://lenta.ru/rss'


def load_xml(url: str) -> ET.Element:
    req = requests.get(url)
    return ET.fromstring(req.text)[0]


def convert_xml_to_json_by_selectors(root: ET.Element,
                                     child_selector: str,
                                     selectors: list[str]) -> list[dict[str | None, str | None]]:
    return [{s: child.find(s).text for s in selectors} for child in root.findall(child_selector)]


def convert_xml_to_json(root: ET.Element, child_selector: str):
    return [{tag.tag: tag.text for tag in child} for child in root.findall(child_selector)]


def save_dict_as_json_file(data: dict | list, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main() -> None:
    elem = load_xml(URL)
    child_name = "item"
    limited_data = convert_xml_to_json_by_selectors(elem, child_name, ["pubDate", "title"])
    save_dict_as_json_file(limited_data, "news.json")
    data = convert_xml_to_json(elem, child_name)
    save_dict_as_json_file(data, "all_news.json")


if __name__ == "__main__":
    main()
