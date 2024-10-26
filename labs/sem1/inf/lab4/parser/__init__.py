from functools import reduce


def parse_json(json: str):
    xml = ""
    # print(json)
    print(__parse_value(json.strip()))


def __parse_keyvalue(string: str):
    parsed_string = __parse_string(string)
    if parsed_string is None:
        return None
    parsed_colon = __parse_colon(parsed_string[1])
    if parsed_colon is None:
        return None
    parsed_value = __parse_value(parsed_colon[1])
    if parsed_value is None:
        return None
    return (parsed_string[0], parsed_value[0]), parsed_value[1].strip()


def __parse_value(string: str):
    res = reduce(
        lambda f, g: f if f(string) else g,
        [
            __parse_number,
            __parse_string,
            __parse_array,
            __parse_object,
        ],
    )(string)
    if res is None:
        return None
    else:
        return res[0], res[1].strip()


def __parse_comma(string: str):
    if not string.startswith(','):
        return None
    return ",", string[1:].strip()


def __parse_comma_values(string: str):
    res = []
    while True:
        parsed_value = __parse_value(string)
        if parsed_value is None:
            break
        res.append(parsed_value[0])
        string = parsed_value[1]

        parsed_comma = __parse_comma(string)
        if parsed_comma is None:
            break
        string = parsed_comma[1]
    return res, string.strip()


def __parse_array(string: str):
    if not string.startswith('['):
        return None
    parse_comma_values = __parse_comma_values(string[1:].strip())
    if parse_comma_values is None:
        res, string = [], string[1:]
    else:
        res, string = parse_comma_values
    if not string.startswith(']'):
        return None
    return res, string[1:].strip()


def __parse_string(string: str):
    if not string.startswith("\""):
        return None
    second_quote = string.find("\"", 1)
    if second_quote == -1:
        return None
    return string[1:second_quote], string[second_quote + 1:]


def __parse_colon(string: str):
    if not string.startswith(":"):
        return None
    else:
        return ":", string[2:].strip()


def __parse_comma_keyvalues(string: str):
    res = {}
    while True:
        parsed_keyvalue = __parse_keyvalue(string)
        if parsed_keyvalue is None:
            break
        key, val = parsed_keyvalue[0]
        res[key] = val
        string = parsed_keyvalue[1]

        parsed_comma = __parse_comma(string)
        if parsed_comma is None:
            break
        string = parsed_comma[1].strip()
    return res, string.strip()


def __parse_object(string: str):
    if not string.startswith("{"):
        return None
    arr, string = __parse_comma_keyvalues(string[1:].strip())
    if not string.startswith("}"):
        return None
    return arr, string[1:].strip()


def __parse_number(string: str):
    num = ""
    for i in string:
        if i in "0123456789.Ee-+":
            num += i
        else:
            break
    if num.isnumeric():
        return int(num), string[len(num):].strip()
    else:
        try:
            return float(num), string[len(num):].strip()
        except ValueError:
            return None
