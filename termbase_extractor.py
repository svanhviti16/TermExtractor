# Retrieves Icelandic terms from .tbx files from Íðorðabankinn
# and saves them to corresponding files
# Accepts a directory path as a single argument
# -------------------------

import xml.etree.ElementTree as ET
import re, os, sys

try:
    # getting path
    dir_path=sys.argv[1]
except:
    print('Please provide a directory path')

files = os.listdir(dir_path)
file_list = [] 

for f in files:
    
    file_path =  os.path.join(dir_path, f)
    file_path_str = os.path.basename(file_path)

    file_prefix = file_path_str.replace(".tbx", "")
    if file_path.endswith('.tbx'):
        print(file_path)
        tree = ET.parse(file_path)
        root = tree.getroot()

        # need to first select the language tag to get Icelandic terms
        langset_elems = root.findall(".//*langSet")

        output = open("termbase/" + file_prefix + ".txt", 'a')

        for element in langset_elems:
            # finding all terms with the "is" attribute
            if element.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == "is":
                terms = element.findall("./*term")
                for t in terms:
                    output.write(t.text + "\n")