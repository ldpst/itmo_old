from parser import parse_json
from parser.converter import convert_to_xml
json = open("in.json", 'r')
xml = open("out.xml", 'w')
xml.write(convert_to_xml(parse_json(json.read())))