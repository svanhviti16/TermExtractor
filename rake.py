from rake_nltk import Metric, Rake
import numpy as np

# To use it with a specific language supported by nltk.
#r = Rake(language="icelandic")

with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    stopwords_is = []
    for line in stopwords_file:
        stopwords_is.append(line)


# If you want to provide your own set of stop words and punctuations to
r = Rake(
    stopwords = stopwords_is,
    punctuations=[";", ",", ".", ":", "?", "„", "“", "\'", "/"]
)


# If you want to control the metric for ranking. Paper uses d(w)/f(w) as the
# metric. You can use this API with the following metrics:
# 1. d(w)/f(w) (Default metric) Ratio of degree of word to its frequency.
# 2. d(w) Degree of word only.
# 3. f(w) Frequency of word only.

q = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
r = Rake(ranking_metric=Metric.WORD_DEGREE)
r = Rake(ranking_metric=Metric.WORD_FREQUENCY)


# If you want to control the max or min words in a phrase, for it to be
# considered for ranking you can initialize a Rake instance as below:

r = Rake(min_length=1, max_length=3)

# TODO: nota lemmaðan texta
with open("corpus/law_corpus/lagaskrar/bunadarlog_lemmatized.txt") as corp_file:
    corpus_list = []
    tokens_string = ""
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            corpus_list.append((tuple(line.strip().split())))

tokens_list = []
for line in corpus_list:
    tokens_string += (line[1] + " ")
    tokens_list.append(line[0])
#print(tokens_string)
r.extract_keywords_from_text(tokens_string)
print(r.get_ranked_phrases())
#print(r._get_phrase_list_from_words(tokens_list))