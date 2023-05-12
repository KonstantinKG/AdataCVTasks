import xml.etree.ElementTree as ET

def traverse_json(data, parent):
    if isinstance(data, dict):
        for key, value in data.items():
            elem = ET.SubElement(parent, key)
            traverse_json(value, elem)
    elif isinstance(data, list):
        for value in data:
            traverse_json(value, parent)
    else:
        parent.text = str(data)

def json_to_xml(data):
    root = ET.Element('root')
    traverse_json(data, root)
    converted_data = root[0]

    declaration ="<?xml version='1.0' encoding='UTF-8'?>"
    xml_body = ET.tostring(converted_data, encoding='unicode')
    result = declaration + xml_body
    return result

