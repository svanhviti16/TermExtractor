from string import punctuation
from collections import defaultdict
import re, os, math

# Term Frequency, Inverse Document Frequency:
    # tf = count(word, document) / len(document) – term frequency
    # idf = log( len(collection) / count(document_containing_term, collection) – inverse document frequency )
    # tf-idf = tf * idf – term frequency – inverse document frequency

# Icelandic stopwords
with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    stopwords_is = []
    for line in stopwords_file:
        stopwords_is.append(line.strip())

# Creating list of punctuation
punct_list = list(punctuation)
# adding Icelandic quotation marks and other punctuation
punct_list.extend(("„", "“", "…", "«"))

# set of all words (lemmas) after extracting stopwords
vocabulary = set()

word_idf = defaultdict(lambda: 0)

# Fetching the document to be worked on
with open("output/lemmatized_clean.txt") as corp_file:
    corpus_list = []
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            corpus_list.append((list(line.strip().split())))

# Fetching the gold corpus from a local directory and counting the tokens and documents
file_paths = os.listdir("corpus/MIM-GOLD_0.9/")

# +1 is the input document
document_count = 2

total_words = []
for path in file_paths:
    # file path from the Gold standard, such as "mbl.txt"
    with open("corpus/MIM-GOLD_0.9/" + path) as g_file:
    
        lines = g_file.readlines()
        for line in lines:
            if line.strip():
                lemma = (line.split()[2])
                if lemma not in stopwords_is and lemma not in punct_list and not re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", lemma):
                    total_words.append(lemma)
    for word in total_words:
        word_idf[word] += 1


# Returns a list where stopwords, punctuation and digits have been removed
def exclude_stoptokens(corpus_file):
    temp_list = []
    for line in corpus_file:
        # some lines may contain fewer items, we don't want them
        if len(line) > 2:
            if line[2] not in stopwords_is and line[2] not in punct_list and not re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", line[2]):
                temp_list.append(line[2])
    return(temp_list)

# excluding all stopwords
working_words = exclude_stoptokens(corpus_list)


# adding the working words to the total list of tokens we want to look at
total_words.extend(working_words)


#print(total_words)

# Filling vocabulary set
vocabulary.update(working_words)
vocabulary.update(total_words)

vocabulary = list(vocabulary)
vocabulary_size = len(vocabulary)
print("VOCABULARY SIZE: " + str(vocabulary_size))

word_index = {w: idx for idx, w in enumerate(vocabulary)}

for word in working_words:
    word_idf[word] += 1
# Calculate idf for all words in the vocabulary
for word in vocabulary:
#    print("word_idf variables:")
#    print("float(1 + word_idf[word]): " + str(float(1 + word_idf[word])))
#    print(word + " word_idf[word]: " + str(math.log(document_count)))
    word_idf[word] = math.log(document_count / float(1 + word_idf[word]))
    #print(word)


print(word_idf["landssamband"])

# 
print(float(working_words.count("landssamband")) / len(working_words))

 
def word_tf(word, document):
    print("Word_tf: " + str(float(document.count(word)) / len(document)))
    return float(document.count(word)) / len(document)
 
def tf_idf(word, document):
 
    if word not in word_index:
        print("not in word_index:" + word)
        return .0

    print("tf_idf: " + str(word_tf(word, document)))
    print("word_idf: " + str(word_idf[word]))
    print("word_idf[word_index[word]]" + str(word_idf[word_index[word]]))
    return word_tf(word, document) * word_idf[word_index[word]]

# testing tf idf function
print(tf_idf("landssamband", working_words))
