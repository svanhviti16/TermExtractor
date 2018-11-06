import sys, re, os
from operator import itemgetter
from string import punctuation

try:
    file_path = sys.argv[1]
except IndexError:
    print("Usage: " + os.path.basename(__file__) + " <filename.txt>")
    sys.exit(1)

# checks word for stopwords, punctuation, numbers and length (don't want words shorter than 5 chars)
def isValid(word):
    if len(word) > 4 and word not in stopwords_is and word not in punct_list and not re.match(r"[0-9]+|[0-9]+\/[0-9]+|[0-9]+\.|[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+\.", word):
        return True


# will hold a list of tuples containing the corpus data
working_words = []
# words to search in, excluding stopwords
working_no_stoptokens = []
# the list of possible termlist candidates
candidates = []

# Icelandic stopwords
with open("stopwords/stopwords_is_extra.txt", "r") as stopwords_file:
    stopwords_is = []
    for line in stopwords_file:
        stopwords_is.append(line.strip())

# Creating list of punctuation
punct_list = list(punctuation)
# adding Icelandic quotation marks and other punctuation
punct_list.extend(("„", "“", "…", "«"))

# examining the tag of the token, which in the case of nouns starts with 'n'
noun_any_case = re.compile(r"^n...??$") 
# nouns in the genetive are marked with 'e'
noun_genetive = re.compile(r"^n..e??$")
# adjectives
adjective_any_case = re.compile(r"^l...??")

# Fetching the document to be worked on
with open(file_path) as corp_file:
    lines = corp_file.readlines()
    for line in lines:
        if line.strip():
            if len(line.split()) is 3:
                # get tuples with all the info
                lemma = line.split()[2]
                working_words.append(tuple(line.split()))
                if isValid(lemma):
                    working_no_stoptokens.append(tuple(line.split()))
                    
# indexing the tuples
for idx, (token, tag, lemma) in enumerate(working_words):
    # looking for nouns
    if re.match(noun_any_case, tag):
        if(idx + 1 < len(lemma)):
            # looking for a noun followed by a noun in the genetive (ex. Bændasamtök Íslands)
            if re.match(noun_genetive, working_words[idx+1][1]):
                # checking one further for another genetive 
                if(idx + 2 < len(working_words)):
                    if re.match(noun_genetive, working_words[idx+2][1]):
                        candidates.append(" ".join((working_words[idx][2], working_words[idx+1][0], working_words[idx+2][0])))
                else: 
                    candidates.append(" ".join((working_words[idx][2], working_words[idx+1][0])))
        else:
            candidates.append(working_words[idx][2])
    # looking for ADJ + NOUN phrases
    if re.match(adjective_any_case, tag):
        # TODO: check if same case as ADJ
        if re.match(noun_genetive, working_words[idx+1][1]):
            candidates.append(" ".join((working_words[idx][0], working_words[idx+1][0])))


def percentage(word):
    return (candidates.count(word) / len(candidates) * 100)

percentage_candidates = []
for word in candidates:
    percentage_candidates.append((word, percentage(word)))

percentage_candidates.sort(key=itemgetter(1), reverse=True)
new_list = [ seq[0] for seq in percentage_candidates ]

new_set = set()
new_set.update(new_list)
for term in new_set:
    print(term)


