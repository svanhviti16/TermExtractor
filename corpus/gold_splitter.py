import os, sys

# Splits the GOLD corpus into roughly 200 files of about 5000 words each.
# For use in the tf-idf approach

lines_per_file = 5000
smaller = None
# The input is a single file with the whole Gold corpus
with open('Gull_lemmatized.txt') as GOLD:
    for lineno, line in enumerate(GOLD):
        if lineno % lines_per_file == 0:
            if smaller:
                smaller.close()
            # constructing file names
            small_filename = 'GOLD_split/GOLD_{}.txt'.format(lineno)
            smaller = open(small_filename, "w")
        # getting rid of newlines
        if line.strip():
            smaller.write(line)
    if smaller:
        smaller.close()


