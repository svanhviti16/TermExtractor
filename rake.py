from rake_nltk import Metric, Rake
from string import punctuation
import numpy as np
import re, sys, os

try:
    file_path = sys.argv[1]
except IndexError:
    print("Usage: " + os.path.basename(__file__) + " <filename.txt>")
    sys.exit(1)

stopwords = []
    
with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    for line in stopwords_file:
        stopwords.append(line.strip())

# Creating list of punctuation
punct_list = list(punctuation)
# adding Icelandic quotation marks and other punctuation
punct_list.extend(("„", "“", "…", "«"))

r = Rake(
    stopwords = stopwords,
    punctuations = punct_list,
    min_length=1, 
    max_length=2
)

with open(file_path) as corp_file:
    corpus_list = []
    tokens_string = ""
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            corpus_list.append((list(line.strip().split())))


token_list = []
token_string = ""
for line in corpus_list:
    if len(line) is 3:
        token_string += (line[0] + " ")
        token_list.append(line[0])


r.extract_keywords_from_text(token_string)

rake_terms = r.get_ranked_phrases()

for term in rake_terms:
    print(term)

# getting rid of duplicates
new_set = set()
new_set.update(rake_terms)
for term in new_set:
    print(term)