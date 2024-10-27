from main_task.parser import parse_json
from main_task.parser.converter import convert_to_xml
from os import path

json = open(path.join(path.dirname(__file__), "../data/in.json"), 'r').read()
xml = open(path.join(path.dirname(__file__), "../data/out.xml"), 'w')
xml.write(convert_to_xml(parse_json(json)))
