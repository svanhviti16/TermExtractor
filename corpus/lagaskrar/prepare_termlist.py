import sys

# Utility script to prepare a .txt file creating 
# a simple alphabetically sorted termlist from the lemmas



if len(sys.argv) < 2 or not sys.argv[1].endswith(".txt"):
    print("Usage: python3 prepare_termlist <filename.txt>")
    exit(1)

dir_path = sys.argv[1]

termset = set()
with open(dir_path, "r") as termfile:
    for line in termfile:
        if line.strip():
            termset.add(line.strip())

termset = sorted(termset)

for term in termset:
    print(term)