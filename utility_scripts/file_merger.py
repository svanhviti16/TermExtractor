# coding: utf-8

# A script to join all .txt files in a folder of .txt files into a single file.
# Accepts a directory path as a single argument
# -------------------------

import os, sys
try:
    # getting path
    dir_path=sys.argv[1]
except:
    print('Please provide a directory path')

files = os.listdir(dir_path)
file_list = [] 

output = open("../corpus/output.txt", 'a')

for f in files:
    file_path = os.path.join(dir_path, f)
    if file_path.endswith('.txt'):
        with open(file_path) as file:	
            for line in file:
                line_stripped = line.strip()
                output.write(line_stripped + '\n')
    else:
        print("Not a .txt file, skipped.")

output.close()

