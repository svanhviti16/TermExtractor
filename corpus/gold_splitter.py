import os, sys

# Splits the GOLD corpus into roughly 200 files of about 5000 words each.
# For use in the tf-idf approach

lines_per_file = 5000
smaller = None
with open('Gull_lemmatized.txt') as GOLD:
    for lineno, line in enumerate(GOLD):
        if lineno % lines_per_file == 0:
            if smaller:
                smaller.close()
            small_filename = 'GOLD_split/GOLD_{}.txt'.format(lineno)
            smaller = open(small_filename, "w")
        smaller.write(line)
    if smaller:
        smaller.close()


