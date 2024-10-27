from json import loads
from os import path
from dicttoxml import dicttoxml


def convert_to_xml(json_data):
    xml = dicttoxml(json_data).decode()
    return xml


def parse_json(string: str):
    json_data = loads(string)
    return json_data


if __name__ == "__main__":
    json = open(path.join(path.dirname(__file__), "../data/in.json"), 'r').read()
    open(path.join(path.dirname(__file__), "../data/out-add1.xml"), 'w').write(convert_to_xml(json))
