import xml.etree.ElementTree as ET
import json


def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    return json.dumps({root.tag: xml_to_dict(root)})


def xml_to_dict(root):
    result = {}
    for child in root:
        if len(child) == 0:
            result[child.tag] = parseType(child.text)
        else:
            result[child.tag] = xml_to_dict(child)
    return result

def parseType(value):
    if try_parse_type(int, value):
        return int(value)
    elif try_parse_type(float, value):
        return float(value)
    elif try_parse_type(bool, value):
        return bool(value)
    else:
        return value
    
def try_parse_type(t, val):
    try:
        return t(val)
    except ValueError:
        return None