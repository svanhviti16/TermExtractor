import sys
from collections import defaultdict


rakepath = sys.argv[1]
nppath = sys.argv[2]
tfidfpath = sys.argv[3]

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



for key, value in sorted(combined.items(), key=lambda kv: kv[1], reverse=True):
    print(key.strip())
