import os
import sys
import xml.etree.ElementTree as ET

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from converters.xml_to_json import xml_to_json

input_data = "<?xml version='1.0' encoding='UTF-8'?><root><thousand>True</thousand><shells>paragraph</shells><poet>farther</poet><shine><line>-1265860017</line><yes>chosen</yes><everywhere>1336309099</everywhere><secret>-1166799671.8364677</secret><relationship><leather>swung</leather><effect>distance</effect><doubt>war</doubt><spin>planning</spin><plant>85188892.10432577</plant><in>solid</in></relationship><among>1736220330.222403</among></shine><pale>-1230047760.1221113</pale><pond>1990243112</pond></root>"
expected_data = '{"root": {"thousand": "True", "shells": "paragraph", "poet": "farther", "shine": {"line": -1265860017, "yes": "chosen", "everywhere": 1336309099, "secret": -1166799671.8364677, "relationship": {"leather": "swung", "effect": "distance", "doubt": "war", "spin": "planning", "plant": 85188892.10432577, "in": "solid"}, "among": 1736220330.222403}, "pale": -1230047760.1221113, "pond": 1990243112}}'
output_data = xml_to_json(input_data)

if (expected_data == output_data):
   print("Xml to Json test passed")
else:
   print("Xml to Json test failed")