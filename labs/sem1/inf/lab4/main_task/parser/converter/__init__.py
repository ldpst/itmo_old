def convert_to_xml(d: dict, tag="root"):
    xml = ""
    for key, value in d.items():
        if isinstance(value, dict):
            xml += convert_to_xml(value, tag=key)
        elif isinstance(value, list):
            xml += f"<{key}>"
            for i in value:
                xml += "".join(convert_to_xml({key + "_element": i}, tag=""))
            xml += f"</{key}>"
        else:
            xml += f"<{key}>" + str(value) + f"</{key}>"
    if tag == "":
        return xml
    else:
        return '<?xml version="1.0" encoding="UTF-8" ?>' + f"<{tag}>" + xml + f"</{tag}>"
