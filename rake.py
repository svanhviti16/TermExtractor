from rake_nltk import Metric, Rake
from string import punctuation
import numpy as np
import re

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

with open("output/bunadarlog_lemmatized_clean.txt") as corp_file:
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


print(r.extract_keywords_from_text(token_string))

rake_terms = r.get_ranked_phrases()[:250]

for term in rake_terms:
    print(term)

