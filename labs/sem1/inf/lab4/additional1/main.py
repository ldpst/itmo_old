from json import loads
from os import path
from dicttoxml import dicttoxml

def convert_to_xml(string: str):
    json_data = loads(string)
    xml = dicttoxml(json_data).decode()
    return xml

if __name__ == "__main__":
    json = open(path.join(path.dirname(__file__), "../in.json"), 'r').read()
    open(path.join(path.dirname(__file__), "../out-add1.xml"), 'w').write(convert_to_xml(json))
