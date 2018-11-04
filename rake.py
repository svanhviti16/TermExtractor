from rake_nltk import Metric, Rake
from string import punctuation
import numpy as np
import re

with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    stopwords = []
    for line in stopwords_file:
        stopwords.append(line.strip())

# Creating list of punctuation
punct_list = list(punctuation)
# adding Icelandic quotation marks and other punctuation
punct_list.extend(("„", "“", "…", "«"))


#re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", line)

# If you want to provide your own set of stop words and punctuations to
r = Rake(
    stopwords = stopwords,
    punctuations = punct_list
)


# If you want to control the metric for ranking. Paper uses d(w)/f(w) as the
# metric. You can use this API with the following metrics:
# 1. d(w)/f(w) (Default metric) Ratio of degree of word to its frequency.
# 2. d(w) Degree of word only.
# 3. f(w) Frequency of word only.

r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
r = Rake(ranking_metric=Metric.WORD_DEGREE)
r = Rake(ranking_metric=Metric.WORD_FREQUENCY)


# If you want to control the max or min words in a phrase, for it to be
# considered for ranking you can initialize a Rake instance as below:

r = Rake(min_length=1, max_length=3)

# TODO: nota lemmaðan texta
with open("output/lemmatized_clean.txt") as corp_file:
    corpus_list = []
    tokens_string = ""
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            corpus_list.append((list(line.strip().split())))


lemma_list = []
lemma_string = ""
for line in corpus_list:
    if len(line) is 3:
        lemma_string += (line[2] + " ")
        lemma_list.append(line[2])


r.extract_keywords_from_text(lemma_string)
print(r.get_ranked_phrases()[:150])

