#!/bin/bash

basename=$(basename $1)
x=${basename%.txt}
filepath=${x##*/}

mkdir output/$filepath
mkdir output/$filepath/prepared
mkdir output/$filepath/termlists

# Preparing the input file using IceNLP to tag and lemmatize
./prepare.sh $1

# Executing the three different approaches for term extraction
# 1. RAKE algorithm
python3 rake.py output/$filepath/prepared/lemmatized_clean.txt > output/$filepath/termlists/rake_terms.txt

# 2. PoS pattern matching 
python3 PoS_matching.py output/$filepath/prepared/lemmatized_clean.txt > output/$filepath/termlists/PoS_terms.txt

# 3. tf*idf algorithm 
python3 tf_idf.py output/$filepath/prepared/lemmatized_clean.txt > output/$filepath/termlists/tf_idf_terms.txt

# Finally combining the termlists into one
python3 utility_scripts/combine_termlists.py output/$filepath/termlists/rake_terms.txt output/$filepath/termlists/PoS_terms.txt output/$filepath/termlists/tf_idf_terms.txt > output/$filepath/termlists/combined_terms.txt
