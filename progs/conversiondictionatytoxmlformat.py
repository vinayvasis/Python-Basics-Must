from dicttoxml import dicttoxml
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# xml = dicttoxml.dicttoxml(some_dict)

xml = dicttoxml(thisdict)
print(xml)






# Code to save xml as file from string
xml = "<myxmldata/>"
xml_data='''<?xml version="1.0"?>
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>'''

from xml.etree import ElementTree as ET
tree = ET.XML(xml_data)
c = ET.tostring(tree)
with open("study/LambdaFunctions/filename1.xml", "wb") as f:
    f.write(c)

