from parser import parse_json
from parser.converter import convert_to_csv
from os import path

json = open(path.join(path.dirname(__file__), "../data/in.json"), 'r').read()
csv = open(path.join(path.dirname(__file__), "../data/out-add5.csv"), 'w')
csv.write(convert_to_csv(parse_json(json)))
