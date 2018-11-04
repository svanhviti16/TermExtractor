import sys

# accepts a .txt file in the Gullstaðall format and returns 
# a simple alphabetically sorted termlist from the lemmas



if len(sys.argv) < 2 or not sys.argv[1].endswith(".txt"):
    print("Usage: python3 prepare_brat <filename.txt>")
    exit(1)

dir_path = sys.argv[1]

termset = set()
with open(dir_path, "r") as termfile:
    for line in termfile:
        if line.strip():
            line = line.split()
            termset.add(line[1].strip())

termset = sorted(termset)

for term in termset:
    print(term)