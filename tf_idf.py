from string import punctuation
from collections import defaultdict
from operator import itemgetter
import re, os, math

# tf-idf = Term Frequency, Inverse Document Frequency

# Icelandic stopwords
with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    stopwords_is = []
    for line in stopwords_file:
        stopwords_is.append(line.strip())

# Creating list of punctuation
punct_list = list(punctuation)
# adding Icelandic quotation marks and other punctuation
punct_list.extend(("„", "“", "…", "«", "–"))

# Returns a list where stopwords, punctuation and digits have been removed
def exclude_stoptokens(corpus_file):
    temp_list = []
    for line in corpus_file:
        if line.strip():
            if line not in stopwords_is and line not in punct_list and not re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", line):
                temp_list.append(line)
    return(temp_list)


# set of all words (lemmas) after extracting stopwords
vocabulary = set()

# we want to store each word's idf in a dictionary
word_idf = defaultdict(lambda: 0)

# all the (relevant) words in the document we're looking at
working_words = []

# Fetching the document to be worked on
with open("output/lemmatized_clean.txt") as corp_file:
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            if len(line.split()) is 3:
                # only working with lemmas here
                working_words.append(line.split()[2])

working_words = exclude_stoptokens(working_words)

# Fetching the gold corpus from a local directory and counting the tokens and documents
file_paths = os.listdir("corpus/GOLD_split/")

# +1 is the document we're looking at, it is added to the corpus
document_count = len(file_paths) + 1

documents_list = []
for path in file_paths:
    total_words = []
    # file path with ~ 200 files from the Gold standard
    with open("corpus/GOLD_split/" + path) as g_file:
        lines = g_file.readlines()
        for line in lines:
            if line.strip():
                # omitting lines with no lemmas
                if len(line.split()) is 3:
                    lemma = line.split()[2]
                if lemma not in stopwords_is and lemma not in punct_list and not re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", lemma):
                    # adding the lemmas to a list, omitting stopwords and other unwanted tokens
                    total_words.append(lemma)
    # registering whether a word appears in the document
    for word in total_words:
        word_idf[word] += 1
    # adding a list of all lemmas in a document into a list
    documents_list.append(total_words)

    vocabulary.update(total_words)

# adding the list of working words to the documents list
documents_list.append(working_words)

# we also want the working_words into the vocabulary
vocabulary.update(working_words)

# and calculate the idf for each word
for word in working_words:
    word_idf[word] += 1

# now getting the vocabulary size
vocabulary = list(vocabulary)
vocabulary_size = len(vocabulary)
print("VOCABULARY SIZE: " + str(vocabulary_size))

# Calculate idf for all words in the vocabulary
for word in vocabulary:
    word_idf[word] = math.log(document_count / float(1 + word_idf[word]))
    #print(word)

# tf = term frequency
# word frequency in the document divided by the document length
def word_tf(word, document):
    print("Word frequency in a document: " + str(float(document.count(word))))
    return float(document.count(word)) / len(document)
 
def tf_idf(word, document):
    if word not in vocabulary:
        return .0
    print("IDF " + str(word_idf[word]))
    return word_tf(word, document) * word_idf[word]

# testing tf idf function
print("Bændasamtök: " + str(tf_idf("Bændasamtök", working_words)))
print("Bóndi: " + str(tf_idf("bóndi", working_words)))
print("Skjaldbaka: " + str(tf_idf("skjaldbaka", working_words)))
print("Búvara: " + str(tf_idf("búvara", working_words)))
print("Sauðfjárrækt: " + str(tf_idf("sauðfjárrækt", working_words)))
print("og: " + str(tf_idf("og", working_words)))

working_set = set()
working_set.update(working_words)

tf_idf_results = []
for word in working_set:
    tf_idf_results.append((word, tf_idf(word, working_words)))

tf_idf_results.sort(key=itemgetter(1), reverse=True)
new_list = [ seq[0] for seq in tf_idf_results[:150] ]

for term in new_list:
    print(term)