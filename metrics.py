from nltk.metrics import *
import sys, os

# Calculates the precision, recall and f-measure of a given term list of the highest ranking terms
# reference file is a hand-annotated termlist given as the second command line argument
# Two reference files exist in the termlists_for_metrics folder: bunadarlog_TERMLIST.txt and buvorulog_TERMLIST.txt

try:
    test_path = sys.argv[1]
    reference_path = sys.argv[2]
except IndexError:
    print("Usage: " + os.path.basename(__file__) + " <testfile.txt> <referencefile.txt>")
    sys.exit(1)

# the f_measure function takes in two sets
test = set()
reference = set()

with open(test_path) as test_file:
    for term in test_file:
        test.add(term)

with open(reference_path) as reference_file:
    for term in reference_file:
        reference.add(term)

print("File to test: " + test_path)
print("Precision: " + str(precision(reference, test)))
print("Recall: " + str(recall(reference, test)))
print("F-measure: " + str(f_measure(reference, test, alpha=0.5)))

