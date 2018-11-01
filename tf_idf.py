
from string import punctuation
import re


# Icelandic stopwords
with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    stopwords_is = []
    for line in stopwords_file:
        stopwords_is.append(line.strip())

# Creating list of punctuation 
punct_list = list(punctuation)
# adding Icelandic quotation marks to punctuation list
punct_list.extend(("„", "“", "…"))

# Fetching the document to be worked on
with open("output/lemmatized_clean.txt") as corp_file:
    corpus_list = []
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            corpus_list.append((list(line.strip().split())))

# Fetching the gold corpus and adding the working document to it
with open("corpus/Gullstadall_all.txt") as gold_file:
    gold_list = []
    lines = gold_file.readlines()
    for line in lines:
        if line.strip():
            gold_list.append((list(line.strip().split())))

# adding all elements of the working file to the end of the Gold corpus file
gold_list.extend(corpus_list)

# Returns a list where stopwords, punctuation and digits have been removed
def exclude_stoptokens(corpus):
    temp_list = []
    new_list = []
    for line in corpus:
        # some lines only contain two items, we don't want them
        if len(line) == 3:
            if line[2] not in stopwords_is and line[2] not in punct_list:
                temp_list.append(line[2])
    for word in temp_list:
        match = re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", word)
        if not match:
            new_list.append(word)
    return(new_list)

# total number of tokens in working file
tok_count_working = len(corpus_list)

# total number of tokens in working file
tok_count_gold = len(gold_list)

working_words = exclude_stoptokens(corpus_list)
#gold_words = exclude_stoptokens(gold_list)
print(working_words)
# Get vocabulary
vocabulary = set()
#vocabulary.update(gold_words)
 
vocabulary = list(vocabulary)
word_index = {w: idx for idx, w in enumerate(vocabulary)}
 
VOCABULARY_SIZE = len(vocabulary)
 
print(VOCABULARY_SIZE) 

