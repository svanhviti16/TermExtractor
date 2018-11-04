import sys

try:
    test_path = sys.argv[1]
except:
    print('Please provide a file path')

fileset = set()


with open(test_path) as test_file:
    for term in test_file:
        fileset.add(term)


for term in fileset:
    print(term.strip())