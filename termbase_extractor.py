import xml.etree.ElementTree as ET

termfile = open("termbase/uppl.tbx")

tree = ET.parse(termfile)
root = tree.getroot()

langset_elems = root.findall(".//*langSet")

output = open("termbase/output.txt", 'a')

for element in langset_elems:
    if element.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == "is":
        terms = element.findall("./*term")
        for t in terms:
            output.write(t.text + "\n")