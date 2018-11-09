# coding: utf-8

import sys

# For lemmatizing termlists, used once for testing purposes

termlist_file = sys.argv[1]
lemma_file = sys.argv[2]

terms = []
lemmas = []

with open(termlist_file) as termlist:
    for line in termlist:
        line = line.split()
        terms.append(line)
    

with open(lemma_file) as lemmalist:
    for lemma in lemmalist:
        if lemma.strip():
            lemmas.append(lemma.split()[1])
    
combined = []
print(len(terms), len(lemmas))
for idx, term in enumerate(terms):
    term[0] = lemmas[idx]
    combined.append(term)

for term in combined:
    print(" ".join(term))
