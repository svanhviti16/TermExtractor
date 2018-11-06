import sys, os
from collections import defaultdict

# Given three termlists this script combines them into one, sorting by the order
# of how often each term appears in the files, such that if it appears in all 
# three files it scores the highest.

try:
    rakepath = sys.argv[1]
    nppath = sys.argv[2]
    tfidfpath = sys.argv[3]
except IndexError:
    print("Usage: " + os.path.basename(__file__) + " <rake_terms.txt> <pos_terms.txt> <tf_idf_terms.txt>")
    sys.exit(1)

rake_list = []
np_list = []
tfidf_list = []

with open(rakepath) as rake:
    for line in rake:
        rake_list.append(line)

with open(nppath) as np:
    for line in np:
        np_list.append(line)

with open(tfidfpath) as tfidf:
    for line in tfidf:
        tfidf_list.append(line)

combined = defaultdict(lambda: 0)

for term in rake_list:
    combined[term] += 1

for term in np_list:
    combined[term] += 1

for term in tfidf_list:
    combined[term] += 1

# sorting in descending order
for key, value in sorted(combined.items(), key=lambda kv: kv[1], reverse=True):
    print(key.strip())
